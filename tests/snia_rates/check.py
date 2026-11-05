#!/usr/bin/env python3
"""Check actual Ruiter rates against pre-fix tabulated values and intervals."""
import argparse
import bisect
import csv
import math
import os
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--valgrind", action="store_true")
parser.add_argument("--source-ref", help="Test routines from this Git revision")
parser.add_argument("--case", action="append",
                    choices=["knots", "endpoint", "interiors", "cdf"],
                    help="Run selected cases; default runs all, including known failures")
args = parser.parse_args()


def extract(filename, signature):
    path = "src/enzo/" + filename
    source = (subprocess.check_output(
        ["git", "show", f"{args.source_ref}:{path}"], cwd=root, text=True)
        if args.source_ref else (root / path).read_text())
    start = source.rindex(signature)
    opening = source.index("{", start)
    depth, end = 1, opening + 1
    while depth:
        depth += (source[end] == "{") - (source[end] == "}")
        end += 1
    return source[start:end]


# This fixture preserves all 46 original rows, including the duplicate.
with (Path(__file__).parent / "reference-knots.csv").open() as file:
    reader = csv.reader(file)
    next(reader)
    original = [list(map(float, row)) for row in reader]
knots = []
for row in original:
    if knots and row[0] == knots[-1][0]:
        assert row == knots[-1], "Only identical duplicate rows may be removed"
    else:
        knots.append(row)
assert len(original) == 46 and len(knots) == 45
ages = [row[0] for row in knots]


def expected(years, model):
    age = years / 1.e9
    index = max(0, min(bisect.bisect_right(ages, age) - 1, len(ages) - 2))
    left, right = knots[index], knots[index + 1]
    weight = (age - left[0]) / (right[0] - left[0])
    return 10 ** ((1 - weight) * left[model + 1] + weight * right[model + 1])


cases = {"knots": [], "endpoint": [], "interiors": []}
for model in range(5):
    # Keep the final endpoint separate so pre-fix failures are both observed.
    for row in knots[:-1]:
        year = row[0] * 1.e9
        for query in [year, math.nextafter(year, math.inf),
                      math.nextafter(year, -math.inf)]:
            if query >= 0:
                cases["knots"].append((model, query, expected(query, model)))
    for query in [14.e9, math.nextafter(14.e9, 0),
                  math.nextafter(14.e9, math.inf), 15.e9]:
        cases["endpoint"].append((model, query, expected(query, model)))
    for left, right in zip(ages, ages[1:]):
        for weight in [.25, .5, .75]:
            query = (left + weight * (right - left)) * 1.e9
            cases["interiors"].append((model, query, expected(query, model)))

prefix = r"""
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define float double
#define POW pow
#define SUCCESS 1
#define FAIL 0
#define ISYM "d"
#define IMF_TABLE_ENTRIES 2000
#define ENZO_FAIL(...) abort()
#define ENZO_VFAIL(...) abort()
double IndividualStarSNIaFraction=.1508;
"""
parts = [
    ("SearchUtilities.C", "int search_lower_bound(float *arr"),
    ("IndividualStarProperties.C",
     "float LinearInterpolationCoefficient(const int &i,\n"),
    ("IndividualStarProperties.C",
     "int LinearInterpolationCoefficients(float &t, int &i,\n"),
    ("IndividualStarProperties.C",
     "float Ruiter_SNIa_DTD(float time, const int model){"),
    ("StarParticleIndividual_IMFInitialize.C",
     "int InitializeDTD(float *& data){"),
]
main = r"""
int main(int argc,char **argv) {
  if (!std::strcmp(argv[1],"cdf")) {
    double *cdf;
    InitializeDTD(cdf);
    for(int i=0;i<IMF_TABLE_ENTRIES;i++)
      if(!std::isfinite(cdf[i]) || cdf[i]<0 || (i && cdf[i]<cdf[i-1]))
        return 1;
    if(std::abs(cdf[IMF_TABLE_ENTRIES-1]-.1508)>1.e-14) return 1;
    delete[] cdf;
  } else {
    int model, count=0;
    double years, reference;
    while(std::scanf("%d %lf %lf",&model,&years,&reference)==3) {
      double actual=Ruiter_SNIa_DTD(years,model);
      if(!std::isfinite(actual) || actual<=0 ||
          std::abs(actual/reference-1)>1.e-11) {
        std::fprintf(stderr,
          "FAIL: model=%d age=%.17g yr actual=%.17g expected=%.17g\n",
          model,years,actual,reference);
        return 1;
      }
      ++count;
    }
    std::printf("Checked %d rate queries\n",count);
  }
  std::printf("PASS: %s\n",argv[1]);
}
"""
with tempfile.TemporaryDirectory(prefix="aeos-snia-rates-") as temp:
    temp = Path(temp)
    cpp = temp / "check.cpp"
    cpp.write_text(prefix + "\n".join(extract(*p) for p in parts) + main)
    binary = temp / "check"
    subprocess.run([os.environ.get("CXX", "c++"), "-std=c++11", "-O0", "-g",
                    str(cpp), "-o", str(binary)], check=True)
    command = (["valgrind", "--error-exitcode=99", "--leak-check=no"]
               if args.valgrind else [])
    failed = False
    for name in args.case or [*cases, "cdf"]:
        data = "".join(f"{model} {year:.17g} {rate:.17g}\n"
                       for model, year, rate in cases.get(name, []))
        result = subprocess.run(command + [str(binary), name],
                                input=data, text=True)
        failed |= result.returncode != 0
    if failed:
        raise SystemExit(1)
