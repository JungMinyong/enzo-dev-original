#!/usr/bin/env python3
"""Compile the four actual PE conversion blocks; check nuclei/charge conservation.

Usage: python3 tests/photoelectric_density/check.py [--source-ref HEAD]
A pre-fix revision is expected to fail (negative control).
"""
import argparse
import os
from pathlib import Path
import re
import subprocess
import tempfile

root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-ref')
args = parser.parse_args()
names = ['StarParticleOpticallyThinRadiation.C', 'Grid_AddPeHeatingFromSources.C',
         'Grid_AddPeHeatingFromTree.C', 'Grid_FinalizeRadiationFields.C']
source = r'''
#include <cmath>
#include <cstdio>
const float mh=1.67262171e-24f, me=9.10938291e-28f;
const int HINum=0, HIINum=1, HMNum=2, H2INum=3, H2IINum=4,
          DeNum=5, ElectronNum=5;
struct Result { float h, e; };
'''
for i, name in enumerate(names):
    path = 'src/enzo/' + name
    text = (subprocess.check_output(['git', 'show', f'{args.source_ref}:{path}'],
                                   cwd=root, text=True)
            if args.source_ref else (root/path).read_text())
    block = re.search(r'n_H\s*=.*?n_e\s*=.*?;', text, re.S)
    if block is None:
        raise RuntimeError(f'Cannot locate density conversion in {name}')
    source += f'Result convert{i}(float **BaryonField, int MultiSpecies, float DensityUnits) {{\n'
    source += 'const int index=0; float n_H,n_e; float DensityConversion=DensityUnits/mh; (void)DensityConversion;\n'
    source += block.group().replace('this->', '') + '\nreturn {n_H,n_e};\n}\n'
source += r'''
int main() {
  Result (*functions[])(float**,int,float)={convert0,convert1,convert2,convert3};
  // Each row has the same total hydrogen mass. Electrons follow charge balance:
  // HII + H2II/2 - HM, in units of m_H per reference volume.
  const float cases[][6] = {
    {1,0,0,0,0,0}, {0,1,0,0,0,1}, {0,0,0,1,0,0},
    {0,0,0,0,1,.5}, {.2,.3,.1,.2,.2,.3},
    {.5,.5,0,0,0,.5}, {0,0,0,0,0,0}
  };
  const float units[]={1.e-27f,1.e-24f,1.e-21f};
  int checks=0, failures=0;
  for(int f=0;f<4;f++) for(float unit: units)
    for(int c=0;c<7;c++) for(int network: {1,2}) {
      float values[6], *fields[6];
      for(int j=0;j<6;j++){values[j]=cases[c][j]*1.e-24f/unit; fields[j]=values+j;}
      Result got=functions[f](fields,network,unit);
      double mass=network>1 ? (c==6 ? 0:1) : cases[c][0]+cases[c][1];
      double expected_h=mass*1.e-24/double(mh);
      double expected_e=cases[c][5]*1.e-24/double(mh);
      if(std::abs(got.h-expected_h)>3.e-6*std::fmax(expected_h,1.e-30) ||
         std::abs(got.e-expected_e)>3.e-6*std::fmax(expected_e,1.e-30)) {
        if(failures<8) std::fprintf(stderr,"path=%d case=%d network=%d units=%g: H=%g expected=%g e=%g expected=%g\n",f,c,network,unit,got.h,expected_h,got.e,expected_e);
        failures++;
      }
      checks++;
    }
  std::printf("%d conversion cases; %d failures\n",checks,failures);
  return failures ? 1:0;
}
'''
source = '#include <initializer_list>\n' + source
with tempfile.TemporaryDirectory(prefix='aeos-pe-density-') as directory:
    cpp = Path(directory)/'check.cpp'
    cpp.write_text(source)
    binary = Path(directory)/'check'
    subprocess.run([os.environ.get('CXX','g++'), '-std=c++11', '-Wall', '-Wextra',
                    str(cpp), '-o', str(binary)], check=True)
    subprocess.run([str(binary)], check=True)
