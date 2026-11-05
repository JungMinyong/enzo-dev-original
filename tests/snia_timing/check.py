#!/usr/bin/env python3
"""Exercise the actual WD assignment and feedback branch with controlled draws.

Run: python3 tests/snia_timing/check.py
Only external units, DTD sampling, channel rates and RNG are stubbed.
"""
from pathlib import Path
import os
import subprocess
import tempfile

root = Path(__file__).resolve().parents[2]
source = (root / "src/enzo/IndividualStarProperties.C").read_text()
start = source.index("int grid::IndividualStarSetWDLifetime(void){")
end = source.index("int WDExplosionTime(float &WD_lifetime){", start)
assignment = source[start:end]
feedback = (root / "src/enzo/Star_SetFeedbackFlag.C").read_text()
start = feedback.index("  case IndividualStarWD:")
end = feedback.index("  case IndividualStarRemnant:", start)
wd_feedback = feedback[start:end]

prefix = r"""
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define float double
#define SUCCESS 1
#define FAIL 0
#define ABS std::abs
#define ENZO_FAIL(...) abort()
#define PARTICLE_TYPE_INDIVIDUAL_STAR_WD 12
using unsigned_long_int = unsigned long;
const int IndividualStarWD = 12, INDIVIDUAL_STAR_SNIA = 9;
int MyProcessorNumber=0, IndividualStarSNIaModel=2, ComovingCoordinates=0;
int StellarYieldsNumberOfSpecies=15, IndividualStarTrackAGBMetalDensity=0;
int IndividualStarPopIIIFormation=0, IndividualStarPopIIISeparateYields=0;
int IndividualStarTrackWindDensity=0;
double HubbleConstantNow=.701, yr_s=3.1556952e7, Myr_s=3.1556952e13;
double unit_time=Myr_s, chosen_delay=1.e8;
int chosen_result=1, draws=0;
int GetUnits(double*a,double*b,double*c,double*d,double*e,double) {
  *a=*b=*c=*e=1; *d=unit_time; return SUCCESS;
}
int WDExplosionTime(double& delay) {
  ++draws; delay=chosen_delay; return chosen_result;
}
int SetWDLifetime(double&,double,double,double,double) { return FAIL; }
double Ruiter_SNIa_DTD(double,int) { return 1; }
unsigned_long_int mt_random() { return 50000; }
struct grid {
  int ProcessorNumber=0, NumberOfParticles=1;
  int ParticleType[1]={-12};
  double Time=0, dtFixed=.01, ParticleAttribute[40][1]={{0}};
  int IndividualStarSetWDLifetime();
};
struct Star {
  int type=12, FeedbackFlag=0;
  double BirthTime, LifeTime, Mass=1;
  void check(double Time) {
    switch (std::abs(type)) {
"""
suffix = r"""
    }
  }
};
void require(bool ok, const char* message) {
  if (!ok) { std::fprintf(stderr, "FAIL: %s\n", message); std::exit(1); }
}
void scenario(double birth, double wd, double delay, double units,
              double expected_lifetime, double probe, bool fires) {
  unit_time=units; chosen_delay=delay; chosen_result=1;
  const double scale=Myr_s/units;
  grid g; g.Time=wd*scale; g.dtFixed=.01*scale;
  g.ParticleAttribute[0][0]=birth*scale;
  // Positive tracers avoid the unrelated zero-valued channel-tag issue.
  for (int i=4;i<40;++i) g.ParticleAttribute[i][0]=1.e-20;
  require(g.IndividualStarSetWDLifetime()==SUCCESS, "assignment succeeds");
  require(std::abs(g.ParticleAttribute[1][0]/scale-expected_lifetime)<1.e-8,
          "stored lifetime is sampled age in code units");
  Star star; star.BirthTime=birth*scale;
  star.LifeTime=g.ParticleAttribute[1][0]; star.type=g.ParticleType[0];
  star.check(probe*scale);
  require((star.FeedbackFlag==INDIVIDUAL_STAR_SNIA)==fires,
          "WD feedback timing");
  star.type=-IndividualStarWD; star.FeedbackFlag=0;
  star.check(probe*scale);
  require(star.FeedbackFlag==0, "uninitialized WD cannot trigger feedback");
  // The assignment guard must preserve an already assigned/restarted WD.
  int old_draws=draws;
  double saved_lifetime=g.ParticleAttribute[1][0];
  g.IndividualStarSetWDLifetime();
  require(draws==old_draws && g.ParticleAttribute[1][0]==saved_lifetime,
          "assigned WD is not resampled");
}
int main() {
  scenario(0,47,1.e8,Myr_s,100,100.01,true);
  scenario(83,130,1.e8,Myr_s,100,182.99,false);
  scenario(83,130,1.e8,Myr_s,100,183.01,true);
  scenario(83,130,3.e7,Myr_s,30,130,true);
  scenario(0,100,1.e6,Myr_s,1,100,true);
  scenario(83,130,4.7e7,Myr_s,47,130.01,true);
  scenario(83,130,1.e8,yr_s,100,183.01,true);
  scenario(83,130,3.e7,yr_s,30,130,true);
  scenario(83,130,3.e7,1.,30,130,true);
  // No-event draws must remain non-exploding throughout the DTD horizon.
  unit_time=Myr_s; chosen_delay=1.4e13; chosen_result=0;
  grid g; g.Time=130; g.ParticleAttribute[0][0]=83;
  g.IndividualStarSetWDLifetime();
  Star star; star.BirthTime=83; star.LifeTime=g.ParticleAttribute[1][0];
  star.check(83+14000);
  require(star.FeedbackFlag==0, "non-event remains inactive at 14 Gyr");
  std::puts("PASS: future/early/equal delays, shifted birth, units, "
            "non-events and assigned-WD persistence");
}
"""
with tempfile.TemporaryDirectory(prefix="aeos-snia-") as temp:
    temp = Path(temp)
    cpp = temp / "check.cpp"
    cpp.write_text(prefix + wd_feedback + suffix + "\n" + assignment)
    binary = temp / "check"
    subprocess.run(
        [os.environ.get("CXX", "c++"), "-std=c++11", "-O0", "-g",
         str(cpp), "-o", str(binary)], check=True)
    subprocess.run([str(binary)], check=True)
