"""Run after compiling parameters.cpp against the actual selected library."""
import subprocess, sys
exe = sys.argv[1]
for args, expected in [(['0','1','0'],0), (['0','2','0'],0),
                       (['-1','2','0'],2), (['1','1','0'],2),
                       (['2','1','0'],2), (['0','1','1'],2),
                       (['3','1','0'],2)]:
    result = subprocess.run([exe]+args, capture_output=True, text=True)
    assert result.returncode == expected, (args,result.stdout,result.stderr)
print('Seven compatibility cases passed:', exe)
