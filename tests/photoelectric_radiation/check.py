#!/usr/bin/env python3
"""Compile production ISRF/PE routines and parameter guards; test physical limits."""
from pathlib import Path
import subprocess,tempfile,os
r=Path(__file__).resolve().parents[2];s=r/'src/enzo'
text=(s/'StarParticleOpticallyThinRadiation.C').read_text()
functions=text[text.index('float NormalizedDustToGasRatio('):text.index('void grid::ComputeBackgroundFUV(')]
read=(s/'GrackleReadParameters.C').read_text();guard=read[read.index('  // AEOS owns PE heating'):read.index('  if ( grackle_data->use_dust_density_field')]
rt=(s/'RadiativeTransferReadParameters.C').read_text()
rtguard=rt[rt.index('  // This flag is only initialized'):rt.index('  // Set some radiative transfer grackle parameters.')]
code=r'''
#include <cmath>
#include <cstdio>
#include <stdexcept>
#include <algorithm>
using std::isfinite;
#ifdef ENZO_TEST_DOUBLE
#define float double
#endif
#define max(A,B) ((A)>(B)?(A):(B))
#define POW pow
#define ENZO_FAIL(x) throw std::runtime_error(x)
#include "PhotoelectricRadiationField.h"
int PhotoelectricHeatingDustModel=1;
float PhotoelectricHeatingDustModelEfficiency=.05;
struct Chemistry {int use_grackle,photoelectric_heating,use_volumetric_heating_rate,use_isrf_field;};
Chemistry chemistry={1,0,1,0}, *grackle_data=&chemistry;
int IndividualStarFUVHeating=1,RadiativeTransfer=1,RadiativeTransferOpticallyThinFUV=1,MultiSpecies=2;
int MyProcessorNumber=1;
#define ROOT_PROCESSOR 0
'''+functions+'\nvoid configure(){\n'+guard+'\n}\nvoid validate_transport(){\n'+rtguard+'\n}\n'+r'''
void close(double a,double b){if(!std::isfinite(a)||std::abs(a-b)>2.e-6*std::max(std::abs(b),1.e-30)) {std::fprintf(stderr,"%g != %g\n",a,b);throw std::runtime_error("mismatch");}}
int main(){
 int cases=0;
 const double mh=1.67262171e-24;
 for(int model=0;model<=1;model++) for(double ru : {1.e-27,1.e-24,1.e-21})
 for(double lu : {1.e18,1.e21}) for(double G : {0.,.00198596855345912,1.7})
 for(float z : {0.f,.00054f,.014f}) for(float molecular : {0.f,1.f}) {
  const double vu=1.e5,tu=lu/vu,dx=5*3.0856775814913673e18,nh=10;
  const double fu=ru*vu*vu*lu/tu;
  float rho=nh*mh/.76/ru, metal=rho*z, hi=nh*mh/ru*(1-molecular), hii=0,hm=0,h2=nh*mh/ru*molecular,h2ii=0;
  float fuv=G*1.59e-3/fu,out=-1;
  PhotoelectricHeatingDustModel=model;
  FillPhotoelectricGrackleISRF(1,&out,&fuv,&rho,&metal,&hi,&hii,&hm,&h2,&h2ii,2,model,ru,vu,lu,tu,dx/lu,mh);
  double x=z>0?log10(z/.014):0;
  double D=z==0?0:pow(10.,x<=-.73?-.68+3.08*x:-2.21+x)/.006616595;
  double attenuation=model?exp(-1.33e-21*D*dx*nh):1;
  close(out,G*attenuation);
  float pe=ComputeHeatingRateFromDustModel(nh,0,z,G*1.59e-3,dx);
  close(pe,1.3e-24*nh*.05*out*(model?D:z/.02));
  cases++;
 }
 // Direct and tree source sums share one cell attenuation, applied exactly once.
 float rho=1,metal=.014,hi=.76,zero=0,out[3],fuv[]={.001,.002,.003};
 float densities[]={rho,rho,rho},metals[]={metal,metal,metal},HI[]={hi,hi,hi},zeros[]={0,0,0};
 FillPhotoelectricGrackleISRF(3,out,fuv,densities,metals,HI,zeros,zeros,zeros,zeros,2,1,1.e-24,1.e5,1.e18,1.e13,1,mh);
 close(out[0]+out[1],out[2]);
 fuv[0]=-1; bool rejected=false;
 try{FillPhotoelectricGrackleISRF(1,out,fuv,&rho,&metal,&hi,&zero,&zero,&zero,&zero,2,1,1.e-24,1.e5,1.e18,1.e13,1,mh);}catch(const std::runtime_error&){rejected=true;}
 if(!rejected)return 1;
 // Old input and restart settings converge to the same resolved configuration.
 configure();if(chemistry.use_isrf_field!=1)return 2;configure();
 validate_transport();RadiativeTransferOpticallyThinFUV=0;rejected=false;
 try{validate_transport();}catch(const std::runtime_error&){rejected=true;}
 if(!rejected)return 7;RadiativeTransferOpticallyThinFUV=1;
 int *invalid[]={&RadiativeTransfer,&MultiSpecies,&chemistry.use_volumetric_heating_rate};
 for(int *p:invalid){int old=*p;*p=0;rejected=false;try{configure();}catch(const std::runtime_error&){rejected=true;}*p=old;if(!rejected)return 3;}
 chemistry.photoelectric_heating=1;rejected=false;try{configure();}catch(const std::runtime_error&){rejected=true;}if(!rejected)return 4;
 chemistry.photoelectric_heating=0;IndividualStarFUVHeating=0;rejected=false;try{configure();}catch(const std::runtime_error&){rejected=true;}if(!rejected)return 5;
 chemistry.use_isrf_field=0;configure();if(chemistry.use_isrf_field!=0)return 6;
 std::printf("PASS %d radiation/PE cases, source addition, invalid flux and configuration guards\n",cases);
}
'''
# std::max is hidden by Enzo's macro; use fmax in the test comparator.
code=code.replace('std::max(std::abs(b),1.e-30)','std::fmax(std::abs(b),1.e-30)')
with tempfile.TemporaryDirectory(prefix='aeos-isrf-') as d:
 p=Path(d)/'check.cpp';p.write_text(code);exe=Path(d)/'check'
 for flags in [[],['-DENZO_TEST_DOUBLE']]:
  subprocess.run([os.environ.get('CXX','g++'),'-std=c++11',*flags,'-I'+str(s),str(p),'-o',str(exe)],check=True)
  subprocess.run([str(exe)],check=True)
# Both solver and diagnostic API must consume the field, and restart must save it.
for name in ['Grid_GrackleWrapper.C','Grid_ComputeCoolingTime.C']:
 t=(s/name).read_text();assert 'FillPhotoelectricGrackleISRF(' in t and 'my_fields.isrf_habing = isrf;' in t and 'delete [] isrf;' in t
assert 'use_isrf_field' in (s/'GrackleWriteParameters.C').read_text()
