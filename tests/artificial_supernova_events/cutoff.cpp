// Compile the production event implementation with controlled units and globals.
#include <cassert>
#include <cstdio>
#include <stdexcept>
#define DEFINE_STORAGE
#include "../../src/enzo/ArtificialSupernovaTable.h"
#include "../../src/enzo/ErrorExceptions.h"
#include "../../src/enzo/macros_and_parameters.h"
#undef ENZO_FAIL
#define ENZO_FAIL(message) throw std::runtime_error(message)
#include "../../src/enzo/ArtificialSupernovaEvents.C"

int GetUnits(float *d, float *l, float *t, float *u, float *v, FLOAT) {
  *d = *l = *t = *v = 1; *u = 3.15576e13; return SUCCESS;
}

void setup(char *path, double delay, double first = -1, int next = 0,
           double now = 0) {
  IndividualStarICSupernovaEventFile = path;
  IndividualStarICSupernovaStopAfterFirstStarMyr = delay;
  IndividualStarICSupernovaFirstStarTime = first;
  IndividualStarICSupernovaNextEvent = next;
  IndividualStarICSupernovaEventFingerprint[0] = 0;
  IndividualStarICSupernovaInjectionMethod = 1;
  ComovingCoordinates = 0;
  for (int i=0;i<3;++i) { DomainLeftEdge[i]=0; DomainRightEdge[i]=1; }
  for (int i=0;i<MAX_TIME_ACTIONS;++i) {
    TimeActionType[i]=0; TimeActionTime[i]=-1;
  }
  assert(InitializeArtificialSupernovaEvents(now)==SUCCESS);
}
int main(int argc, char **argv) {
#ifdef USE_MPI
  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&MyProcessorNumber);
  MPI_Comm_size(MPI_COMM_WORLD,&NumberOfProcessors);
#else
  MyProcessorNumber=0; NumberOfProcessors=1;
#endif
  assert(argc==2);
  setup(argv[1],5);
  const double scale=myr_in_code_units;
  UpdateArtificialSupernovaCutoff(0);
  assert(IndividualStarICSupernovaFirstStarTime==-1);
  // Nonstellar particles do not start the clock.
  RecordArtificialSupernovaFirstStar(1,0);
  UpdateArtificialSupernovaCutoff(0);
  assert(IndividualStarICSupernovaFirstStarTime==-1);
  // Earliest birth is on the last rank, with multiple types/signs represented.
  RecordArtificialSupernovaFirstStar(-11,MyProcessorNumber==NumberOfProcessors-1 ? 0 : scale);
  RecordArtificialSupernovaFirstStar(15,2*scale);
  UpdateArtificialSupernovaCutoff(2*scale);
  assert(IndividualStarICSupernovaFirstStarTime==0);
  assert(TimeActionTime[0]==event_times[0]);
  assert(!suppressed(0)); assert(suppressed(1)); // event exactly at cutoff excluded
  AdvanceArtificialSupernovaEvent(0);
  assert(TimeActionTime[0]==-1 && IndividualStarICSupernovaNextEvent==1);
  // A checkpoint after shutdown retains an unconsumed event in the past.
  setup(argv[1],5,0,1,100*scale);
  assert(TimeActionTime[0]==-1);
  // Birth and cutoff survive the full-precision checkpoint representation.
  char saved[100]; snprintf(saved,sizeof(saved),"%.21Lg",static_cast<long double>(3*scale));
  setup(argv[1],3,strtod(saved,0),1,4*scale);
  assert(!suppressed(1) && suppressed(2));
  AdvanceArtificialSupernovaEvent(0);
  assert(TimeActionTime[0]==-1);
  // Uninterrupted and checkpointed executions consume the same prefix.
  setup(argv[1],6);
  std::vector<int> continuous;
  continuous.push_back(IndividualStarICSupernovaNextEvent);
  AdvanceArtificialSupernovaEvent(0); // 2.5 Myr, before stars
  RecordArtificialSupernovaFirstStar(11,5*scale);
  UpdateArtificialSupernovaCutoff(5*scale);
  continuous.push_back(IndividualStarICSupernovaNextEvent);
  AdvanceArtificialSupernovaEvent(0); // 5 Myr
  const double saved_first=IndividualStarICSupernovaFirstStarTime;
  const int saved_next=IndividualStarICSupernovaNextEvent;
  while (TimeActionTime[0]>0) {
    continuous.push_back(IndividualStarICSupernovaNextEvent);
    AdvanceArtificialSupernovaEvent(0);
  }
  setup(argv[1],6,saved_first,saved_next,5*scale);
  std::vector<int> restarted;
  restarted.push_back(0); restarted.push_back(1);
  while (TimeActionTime[0]>0) {
    restarted.push_back(IndividualStarICSupernovaNextEvent);
    AdvanceArtificialSupernovaEvent(0);
  }
  assert(continuous==restarted && continuous.size()==4);
  setup(argv[1],25,5*scale,2,5*scale);
  assert(!suppressed(10) && suppressed(11)); // exactly 30 Myr, nonunit conversion
  setup(argv[1],6);
  RecordArtificialSupernovaFirstStar(14,0); UpdateArtificialSupernovaCutoff(0);
  assert(!suppressed(1) && suppressed(2)); // cutoff between events
  setup(argv[1],0);
  RecordArtificialSupernovaFirstStar(11,0); UpdateArtificialSupernovaCutoff(0);
  assert(TimeActionTime[0]==-1);
  setup(argv[1],-1);
  RecordArtificialSupernovaFirstStar(11,0); UpdateArtificialSupernovaCutoff(0);
  assert(IndividualStarICSupernovaFirstStarTime==-1);
  assert(!suppressed(59));
  for (int i=0;i<60;++i) AdvanceArtificialSupernovaEvent(0);
  assert(TimeActionTime[0]==-1 && IndividualStarICSupernovaNextEvent==60);
  setup(argv[1],25,-1,60,151*scale); // exhausted, no stars, valid restart
  assert(TimeActionTime[0]==-1);
  bool rejected=false;
  try { setup(argv[1],5,-1,1,100*scale); }
  catch (const std::runtime_error&) { rejected=true; }
  assert(rejected); // a stale cursor without saved cutoff still fails
  rejected=false;
  try { setup(argv[1],-2); }
  catch (const std::runtime_error&) { rejected=true; }
  assert(rejected);
  rejected=false;
  try { setup(argv[1],25,2*scale,0,scale); }
  catch (const std::runtime_error&) { rejected=true; }
  assert(rejected);
  if (MyProcessorNumber==0) puts("PASS production cutoff: non-root birth, boundaries, restart, disabled, exhaustion");
#ifdef USE_MPI
  MPI_Finalize();
#endif
}
