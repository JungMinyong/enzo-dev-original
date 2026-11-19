#!/usr/bin/env python3
"""Compare scalar and per-cell ISRF in real Grackle cooling/chemistry APIs.
Usage: python3 check_grackle.py GRACKLE_PREFIX CLOUDY_TABLE
"""
from pathlib import Path
import subprocess,tempfile,sys,itertools,math,os
r=Path(__file__).resolve().parent;prefix=Path(sys.argv[1]).resolve();table=str(Path(sys.argv[2]).resolve())
libdir=next(p for p in [prefix/'lib',prefix/'lib64'] if list(p.glob('libgrackle*.so')))
cells=list(itertools.product([100,3000,10000,1e6],[.01,1,100],[0,.00198596855345912,1.7],[9.24056296e-6,3.91427027e-4]))
text=''.join(f'{t} {n} .001 {g} {d}\n' for t,n,g,d in cells)
with tempfile.TemporaryDirectory(prefix='aeos-isrf-grackle-') as tmp:
 exe=Path(tmp)/'cell'
 subprocess.run([os.environ.get('CC','gcc'),'-std=c99','-I'+str(prefix/'include'),str(r/'grackle_cell.c'),'-L'+str(libdir),'-Wl,-rpath,'+str(libdir),'-lgrackle','-lm','-o',str(exe)],check=True)
 for units in ['0','-3','3']:
  outputs=[]
  for field in ['0','1']:
   p=subprocess.run([str(exe),table,units,field],input=text,text=True,capture_output=True,check=True,cwd=tmp)
   outputs.append([[float(x) for x in line.split()[1:]] for line in p.stdout.splitlines() if line.startswith('RESULT')])
  assert len(outputs[0])==len(cells) and len(outputs[1])==len(cells)
  for a,b in zip(*outputs):
   assert all(math.isfinite(x) and math.isfinite(y) and math.isclose(x,y,rel_tol=1e-12,abs_tol=1e-290) for x,y in zip(a,b)),(a,b)
 print('PASS',len(cells)*3,'scalar/field comparisons, including chemistry updates and scalar=999 override')
