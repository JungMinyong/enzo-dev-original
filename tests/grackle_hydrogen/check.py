#!/usr/bin/env python3
"""Exercise Enzo's production parameter reader against an installed Grackle.

Usage: python3 tests/grackle_hydrogen/check.py GRACKLE_PREFIX CLOUDY_TABLE
Only the unit/expansion providers are replaced; Grackle defaults,
initialization, and Enzo parameter mapping are the production implementations.
"""
from pathlib import Path
import argparse
import os
import subprocess
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("grackle_prefix", type=Path)
parser.add_argument("cloudy_table", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[2]
src = root / "src/enzo"
prefix = args.grackle_prefix.resolve()
table = args.cloudy_table.resolve()
if not table.is_file():
    parser.error("Cloudy table does not exist: " + str(table))
libdir = prefix / "lib64"
if not libdir.is_dir():
    libdir = prefix / "lib"

harness = r"""
#include "preincludes.h"
#include <cstdlib>
#include "macros_and_parameters.h"
#include "typedefs.h"
#define DEFINE_STORAGE
#include "global_data.h"
#include "CosmologyParameters.h"

int GrackleSetDefaultParameters(FILE*);
int GrackleReadParameters(FILE*, FLOAT);
int GetUnits(float*d, float*l, float*t, float*time, float*v,
             double*m, FLOAT) {
  *d=1.67e-24; *l=3.0857e18; *t=1; *time=3.1557e11;
  *v=*l / *time; *m=*d * *l * *l * *l;
  return SUCCESS;
}
int CosmologyComputeExpansionFactor(FLOAT, FLOAT*a, FLOAT*dadt) {
  *a=1; *dadt=0; return SUCCESS;
}
int main(int argc, char**argv) {
  if(argc!=5) return 2;
  int mode=atoi(argv[1]), comoving=atoi(argv[2]);
  MyProcessorNumber=0; GrackleLWBackgroundModel=0;
  ComovingCoordinates=comoving; InitialRedshift=70; FinalRedshift=0;
  FILE* input=tmpfile();
  if(!input) return 3;
  fprintf(input, "use_grackle = 1\nUVbackground = 0\n"
          "grackle_data_file = %s\ndust_chemistry = 0\n",argv[4]);
  fflush(input);
  if(GrackleSetDefaultParameters(input)!=SUCCESS) return 4;
  MultiSpecies=mode; MetalCooling=0; RadiativeTransfer=0;
  double expected=(mode==0)?0.715768377353088514:0.76;
  if(atoi(argv[3])) {
    // Fully tabulated chemistry permits only its fixed Cloudy abundance.
    if(mode!=0) expected=0.72;
    CoolData.HydrogenFractionByMass=expected;
  }
  if(GrackleReadParameters(input,0)!=SUCCESS) return 5;
  fclose(input);
  if(fabs(grackle_data->HydrogenFractionByMass-expected)>1e-12 ||
     fabs(CoolData.HydrogenFractionByMass-expected)>1e-12) {
    fprintf(stderr,"mode=%d comoving=%d explicit=%s: "
            "Enzo=%.17g Grackle=%.17g expected=%.17g\n",
            mode,comoving,argv[3],CoolData.HydrogenFractionByMass,
            grackle_data->HydrogenFractionByMass,expected);
    return 1;
  }
  return free_chemistry_data()?0:6;
}
"""

with tempfile.TemporaryDirectory(prefix="aeos-hydrogen-") as temp:
    temp = Path(temp)
    cpp = temp / "check.cpp"
    cpp.write_text(harness)
    binary = temp / "check"
    subprocess.run(
        [os.environ.get("CXX", "c++"), "-std=c++11", "-O0", "-g",
         "-DUSE_GRACKLE", "-DCONFIG_BFLOAT_8", "-DCONFIG_PFLOAT_8",
         "-DCONFIG_PINT_8", "-DSMALL_INTS", "-D__max_baryons=60",
         "-D__max_particle_attr=30", "-I" + str(src),
         "-I" + str(prefix / "include"), str(cpp),
         str(src / "GrackleReadParameters.C"), "-L" + str(libdir),
         "-Wl,-rpath," + str(libdir), "-lgrackle", "-o", str(binary)],
        check=True)
    failures = []
    for mode in (0, 2):
        for comoving in (0, 1):
            for explicit in (0, 1):
                result = subprocess.run(
                    [str(binary), str(mode), str(comoving), str(explicit),
                     str(table)], capture_output=True, text=True)
                if result.returncode:
                    failures.append(result.stdout + result.stderr)
    if failures:
        raise SystemExit("".join(failures))
print("PASS: 8 production-reader cases: tabulated/molecular chemistry, "
      "proper/comoving units and default/explicit hydrogen fractions")
