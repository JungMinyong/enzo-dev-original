#!/usr/bin/env python3
"""Compile actual interpolation routines; optionally check supplied table axes."""
import argparse
import os
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--stellar-table", type=Path)
parser.add_argument("--yield-table", type=Path)
parser.add_argument("--valgrind", action="store_true")
parser.add_argument("--source-ref", help="Read routines from a Git revision")
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


prefix = r"""
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#define float double
#define SUCCESS 1
#define FAIL 0
#define ISYM "d"
#define ESYM "g"
#define ENZO_FAIL(...) abort()
#define ENZO_VFAIL(...) abort()
int IndividualStarExtrapolateYields=0;
struct StellarYieldsDataType { double *M,*Z; int Nm,Nz; };
void require(bool ok, const char *message) {
  if (!ok) { std::fprintf(stderr,"FAIL: %s\n",message); std::exit(1); }
}
"""
parts = [
    ("SearchUtilities.C", "int search_lower_bound(float *arr"),
    ("IndividualStarProperties.C",
     "float LinearInterpolationCoefficient(const int &i,\n"),
    ("IndividualStarProperties.C",
     "int LinearInterpolationCoefficients(float &t, int &i,\n"),
    ("IndividualStarProperties.C",
     "int LinearInterpolationCoefficients(float &t, float &u, int &i, int &j,\n"),
    ("IndividualStarProperties.C",
     "int LinearInterpolationCoefficients(float &t, float &u, float &v, int &i, int &j, int &k,\n"),
    ("StellarYieldsRoutines.C",
     "int StellarYieldsGetYieldTablePosition(const StellarYieldsDataType & table,"),
]
body = r"""
void axis(std::vector<double> a) {
  require(a.size()>=2,"fixture has an interval");
  std::vector<double> queries=a;
  for (size_t k=1;k<a.size();k++) queries.push_back((a[k-1]+a[k])/2);
  queries.push_back(std::nextafter(a.back(),a.front()));
  for (double q: queries) {
    int i=-1; double t=-9;
    require(LinearInterpolationCoefficients(t,i,q,a.data(),a.size())==SUCCESS,
            "in-range stellar lookup");
    require(i>=0 && i<int(a.size())-1,"stellar interval stays inside axis");
    require(std::isfinite(t) && t>=0 && t<=1,"finite convex weight");
    require(std::abs((1-t)*a[i]+t*a[i+1]-q) <=
            1.e-12*std::max(1.,std::abs(q)),"linear reconstruction");
    if(q==a.back()) require(i==int(a.size())-2 && t==1,
                           "upper knot uses final interval with weight one");
  }
  int i; double t;
  require(LinearInterpolationCoefficients(t,i,
          std::nextafter(a.back(),INFINITY),a.data(),a.size())==FAIL,
          "above maximum remains out of range");
  require(LinearInterpolationCoefficients(t,i,
          std::nextafter(a.front(),-INFINITY),a.data(),a.size())==FAIL,
          "below minimum remains out of range");
}
void yields(std::vector<double> m,std::vector<double> z) {
  StellarYieldsDataType table={m.data(),z.data(),int(m.size()),int(z.size())};
  for(double mass: m) for(double metal: z) {
    int i=-1,j=-1;
    require(StellarYieldsGetYieldTablePosition(table,i,j,mass,metal,0)==SUCCESS,
            "yield knot lookup");
    require(i>=0 && i<table.Nm-1,"yield mass interval stays inside axis");
    require(m[i]<=mass && mass<=m[i+1],"yield interval brackets mass");
    if(z.size()==1) require(j==0,"single-metallicity PopIII position");
    else {
      require(j>=0 && j<table.Nz-1,"yield metallicity interval inside axis");
      require(z[j]<=metal && metal<=z[j+1],"yield interval brackets metallicity");
    }
  }
}
int main(int argc,char **argv) {
  if(!std::strcmp(argv[1],"stellar")) {
    axis({1,2,3}); axis({1,2});
    int i,j,k; double t,u,v;
    std::vector<double> a={1,2,3};
    require(LinearInterpolationCoefficients(t,u,i,j,3,3,a.data(),a.data(),3,3)
            ==SUCCESS && i==1 && j==1 && t==1 && u==1,"2D upper corner");
    require(LinearInterpolationCoefficients(t,u,v,i,j,k,3,3,3,
            a.data(),a.data(),a.data(),3,3,3)==SUCCESS &&
            i==1 && j==1 && k==1 && t==1 && u==1 && v==1,"3D upper corner");
    require(LinearInterpolationCoefficients(t,i,0,nullptr,0)==FAIL,
            "empty axis rejected before dereference");
    require(LinearInterpolationCoefficients(t,i,1,a.data(),1)==FAIL,
            "singleton linear axis rejected");
    REAL_STELLAR
  } else {
    yields({1,2,3},{.001,.02}); yields({1,2,3},{0});
    yields({1,2},{0,.02});
    std::vector<double> m={1,2,3}, z={.001,.02};
    StellarYieldsDataType table={m.data(),z.data(),3,2};
    int i,j;
    require(StellarYieldsGetYieldTablePosition(table,i,j,4,.01,1)==SUCCESS
            && i==1,"explicit upper mass extrapolation retained");
    require(StellarYieldsGetYieldTablePosition(table,i,j,.5,.01,1)==SUCCESS
            && i==0,"explicit lower mass extrapolation retained");
    require(StellarYieldsGetYieldTablePosition(table,i,j,3,0,0)==SUCCESS
            && j==0,"low metallicity floor retained");
    StellarYieldsDataType empty={nullptr,nullptr,0,0};
    require(StellarYieldsGetYieldTablePosition(empty,i,j,1,0,0)==FAIL,
            "empty yield axes rejected before dereference");
    table.Nm=1;
    require(StellarYieldsGetYieldTablePosition(table,i,j,1,.001,0)==FAIL,
            "single mass yield axis rejected");
    REAL_YIELDS
  }
  std::printf("PASS: %s interpolation boundaries\n",argv[1]);
}
"""


def vector(values):
    return "{" + ",".join(format(float(v), ".17g") for v in values) + "}"


stellar_cases, yield_cases = [], []
if args.stellar_table:
    import numpy as np
    table = np.loadtxt(args.stellar_table)
    for column in [0, 1]:
        stellar_cases.append("axis(" + vector(np.unique(table[:, column])) + ");")
if args.yield_table:
    import h5py
    with h5py.File(args.yield_table) as table:
        for name, group in table.items():
            m, z = group["M"][:], group["Z"][:]
            yield_cases.append(f"yields({vector(m)},{vector(z)});")
body = body.replace("REAL_STELLAR", "\n".join(stellar_cases))
body = body.replace("REAL_YIELDS", "\n".join(yield_cases))
with tempfile.TemporaryDirectory(prefix="aeos-interpolation-") as temp:
    temp = Path(temp)
    cpp = temp / "check.cpp"
    cpp.write_text(prefix + "\n".join(extract(*p) for p in parts) + body)
    binary = temp / "check"
    subprocess.run([os.environ.get("CXX", "c++"), "-std=c++11", "-O0", "-g",
                    str(cpp), "-o", str(binary)], check=True)
    prefix_command = (["valgrind", "--error-exitcode=99", "--leak-check=no"]
                      if args.valgrind else [])
    failed = False
    for case in ["stellar", "yield"]:
        result = subprocess.run(prefix_command + [str(binary), case])
        failed |= result.returncode != 0
    if failed:
        raise SystemExit(1)
print(f"Checked {len(stellar_cases)} stellar axes and "
      f"{len(yield_cases)} actual yield groups.")
