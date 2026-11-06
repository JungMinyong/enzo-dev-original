"""Run after compiling parameters.cpp against the actual selected library."""
import argparse
import subprocess
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("exe")
options = parser.parse_args()
custom = 0  # Enzo forwards these modes; support is determined by the library.
cases = [(['0','0','0'],0), (['1','1','0'],0), (['1','2','0'],2),
         (['4','1','0'],custom), (['5','1','0'],custom),
         (['4','2','0'],custom), (['5','2','0'],custom),
         (['2','1','0'],2), (['3','1','0'],2), (['-1','1','0'],2),
         (['6','1','0'],2), (['1','1','1'],2), (['1','1','2'],2),
         (['1','1','-1'],2), (['1','3','0'],2)]
for args, expected in cases:
    result = subprocess.run([options.exe]+args, capture_output=True, text=True)
    assert result.returncode == expected, (args,result.stdout,result.stderr)
print(f'{len(cases)} compatibility cases passed:', options.exe)
