#!/usr/bin/env python3
"""Run the complete production flux-correction method on controlled faces.

Only the grid container/field lookup interface is reduced. Production field
predicates, conservative-field conversion and the entire correction method
are compiled, including flux indexing, rollback and energy reconstruction.
"""
from pathlib import Path
import os
import subprocess
import tempfile

root = Path(__file__).resolve().parents[2]
src = root / "src/enzo"


def function(filename, signature):
    text = (src / filename).read_text()
    return text[text.index(signature):]


prefix = r"""
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include "ErrorExceptions.h"
#include "macros_and_parameters.h"
#include "typedefs.h"
#define DEFINE_STORAGE
#include "global_data.h"
#include "Fluxes.h"
struct TopGridData {
  int LeftFaceBoundaryCondition[3] = {1,1,1};
  int RightFaceBoundaryCondition[3] = {1,1,1};
};
struct grid {
  int ProcessorNumber=0, NumberOfBaryonFields=11, GridRank=1;
  int GridDimension[3]={1,1,1}, GridStartIndex[3]={0,0,0};
  int GridEndIndex[3]={0,0,0};
  int FieldType[11]={Density,TotalEnergy,InternalEnergy,
                    Velocity1,Velocity2,Velocity3,
                    HIDensity,HIIDensity,Metallicity,FeDensity,MetalSNIaDensity};
  float *BaryonField[11], *CellLeftEdge[3], *CellWidth[3];
  int IdentifyPhysicalQuantities(int&d,int&g,int&v1,int&v2,int&v3,int&t,
                                int&b1,int&b2,int&b3) {
    d=0; t=1; g=2; v1=3; v2=4; v3=5; b1=b2=b3=0; return SUCCESS;
  }
  int CorrectForRefinedFluxes(fluxes*,fluxes*,fluxes*,int,TopGridData*);
};
"""

suffix = r"""
void require(bool ok, const char* message) {
  if (!ok) { std::fprintf(stderr,"FAIL: %s\n",message); std::exit(1); }
}
int main(int argc, char**argv) {
  require(argc==4, "arguments: face axis failing-field");
  int face=atoi(argv[1]), axis=atoi(argv[2]), failing=atoi(argv[3]);
  bool sibling=(face<2), right=(face%2==0);
  MyProcessorNumber=0; UseHydro=1; HydroMethod=0;
  RadiativeCooling=1; FluxCorrection=2; DualEnergyFormalism=1;
  UseMHD=0; Coordinate=Cartesian;
  grid g; g.GridRank=axis+1;
  g.GridDimension[axis]=8; g.GridStartIndex[axis]=1; g.GridEndIndex[axis]=6;
  for(int d=0; d<3; ++d) {
    DomainLeftEdge[d]=0; DomainRightEdge[d]=8;
    g.CellLeftEdge[d]=new float[8];
    g.CellWidth[d]=new float[8];
    for(int i=0;i<8;++i) {g.CellLeftEdge[d][i]=i; g.CellWidth[d][i]=1;}
  }
  const float original[11]={1,2.07,2,.1,.2,.3,.4,.1,.01,.002,.001};
  // Keep initial total energy consistent for each dimensionality.
  float energy=2;
  for(int d=0;d<g.GridRank;++d) energy+=0.5*original[3+d]*original[3+d];
  float before[11];
  for(int f=0;f<11;++f) {
    before[f]=(f==1)?energy:original[f];
    g.BaryonField[f]=new float[8];
    for(int i=0;i<8;++i) g.BaryonField[f][i]=before[f];
  }
  fluxes initial={}, refined={}, boundary={};
  for(int d=0;d<3;++d) {
    for(int f=0;f<11;++f) {
      initial.LeftFluxes[f][d]=new float[1]();
      initial.RightFluxes[f][d]=new float[1]();
      refined.LeftFluxes[f][d]=new float[1]();
      refined.RightFluxes[f][d]=new float[1]();
      boundary.LeftFluxes[f][d]=new float[1]();
      boundary.RightFluxes[f][d]=new float[1]();
    }
  }
  initial.LeftFluxStartGlobalIndex[axis][axis]=2;
  initial.LeftFluxEndGlobalIndex[axis][axis]=2;
  initial.RightFluxStartGlobalIndex[axis][axis]=4;
  initial.RightFluxEndGlobalIndex[axis][axis]=4;
  refined.LeftFluxStartGlobalIndex[axis][axis]=sibling?(right?5:-1):2;
  refined.LeftFluxEndGlobalIndex[axis][axis]=refined.LeftFluxStartGlobalIndex[axis][axis];
  refined.RightFluxStartGlobalIndex[axis][axis]=sibling?(right?6:1):4;
  refined.RightFluxEndGlobalIndex[axis][axis]=refined.RightFluxStartGlobalIndex[axis][axis];
  float change[11]={.2,0,0,0,0,0,.03,.04,.005,.001,.0005};
  if(failing>=0) change[failing]=-2*before[failing];
  for(int f=0;f<11;++f) {
    // Sibling right adds InitialRight-RefinedLeft. Child right uses its
    // negative; the left-face signs are the opposite.
    float value=change[f]*(right?1:-1)*(sibling?1:-1);
    if(right) initial.RightFluxes[f][axis][0]=value;
    else initial.LeftFluxes[f][axis][0]=value;
  }
  TopGridData metadata;
  require(g.CorrectForRefinedFluxes(&initial,&refined,&boundary,sibling,
                                  &metadata)==SUCCESS, "correction succeeds");
  int target=sibling?(right?4:2):(right?5:1);
  for(int i=0;i<8;++i) {
    for(int f=0;f<11;++f) {
      float expected=before[f];
      if(i==target && failing<0) {
        if(f==0 || f>=6) expected+=change[f];
        else if(f>=3 && f<=5) expected/=1.2;
        else if(f==1) {
          expected=2;
          for(int d=0;d<g.GridRank;++d)
            expected+=0.5*before[3+d]*before[3+d]/(1.2*1.2);
        }
      }
      if(std::abs(g.BaryonField[f][i]-expected)>1e-12) {
        std::fprintf(stderr,"face=%d axis=%d failing=%d cell=%d field=%d "
                     "got=%.17g expected=%.17g\n",face,axis,failing,i,f,
                     g.BaryonField[f][i],expected);
        return 1;
      }
    }
  }
  for(int d=0;d<3;++d) {
    delete[] g.CellLeftEdge[d]; delete[] g.CellWidth[d];
    for(int f=0;f<11;++f) {
      delete[] initial.LeftFluxes[f][d]; delete[] initial.RightFluxes[f][d];
      delete[] refined.LeftFluxes[f][d]; delete[] refined.RightFluxes[f][d];
      delete[] boundary.LeftFluxes[f][d]; delete[] boundary.RightFluxes[f][d];
    }
  }
  for(int f=0;f<11;++f) delete[] g.BaryonField[f];
}
"""

with tempfile.TemporaryDirectory(prefix="aeos-flux-") as temp:
    temp = Path(temp)
    cpp = temp / "check.cpp"
    cpp.write_text(
        prefix
        + function("MakeFieldConservative.C", "int MakeFieldConservative(")
        + function("Grid_CorrectForRefinedFluxes.C",
                   "int grid::CorrectForRefinedFluxes(")
        + suffix
    )
    binary = temp / "check"
    subprocess.run(
        [os.environ.get("CXX", "c++"), "-std=c++11", "-O0", "-g",
         "-DCONFIG_BFLOAT_8", "-DCONFIG_PFLOAT_8", "-DCONFIG_PINT_8",
         "-DSMALL_INTS", "-D__max_baryons=60", "-D__max_particle_attr=30",
         "-I" + str(src), str(cpp), "-o", str(binary)], check=True)
    failures = []
    for face in range(4):  # sibling right/left, child right/left
        for axis in range(3):
            for failing in [-1, 6, 8, 9, 10]:
                result = subprocess.run(
                    [str(binary), str(face), str(axis), str(failing)],
                    capture_output=True, text=True)
                if result.returncode:
                    failures.append(result.stderr)
    if failures:
        raise SystemExit("".join(failures))
print("PASS: 60 full-method cases: four faces, three axes, successful "
      "corrections and H/metal/Fe/SNIa rollback; fields and momentum preserved")
