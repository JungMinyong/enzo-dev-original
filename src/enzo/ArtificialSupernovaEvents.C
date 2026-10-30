#include "ArtificialSupernovaTable.h"
#include <cstdlib>
#include <cstring>
#include <limits.h>
#ifdef USE_MPI
#include "mpi.h"
#endif
#include "ErrorExceptions.h"
#include "macros_and_parameters.h"
#include "typedefs.h"
#include "global_data.h"
#include "StarParticleData.h"
#include "phys_constants.h"
#include "ArtificialSupernovaEvents.h"

int GetUnits(float *, float *, float *, float *, float *, FLOAT);

namespace {
std::vector<artificial_sn::Event> events;
std::vector<FLOAT> event_times;
}

int InitializeArtificialSupernovaEvents(FLOAT time)
{
  events.clear();
  event_times.clear();
  if (IndividualStarICSupernovaEventFile == NULL) return SUCCESS;
  if (ComovingCoordinates || IndividualStarICSupernovaInjectionMethod != 1)
    ENZO_FAIL("SN event files require noncomoving coordinates and injection method 1.");

  // Only root reads the file. All ranks receive the identical event table.
  char path[PATH_MAX] = {0};
  char fingerprint[17] = {0};
  Eint32 count = 0;
  if (MyProcessorNumber == ROOT_PROCESSOR) {
    if (realpath(IndividualStarICSupernovaEventFile, path) == NULL)
      ENZO_FAIL("Cannot resolve IndividualStarICSupernovaEventFile.");
    try {
      artificial_sn::Table table = artificial_sn::read(path);
      events.swap(table.events);
      strcpy(fingerprint, table.fingerprint.c_str());
      count = events.size();
    } catch (const std::exception &error) {
      fprintf(stderr, "Artificial SN file %s: %s\n", path, error.what());
      ENZO_FAIL("Invalid artificial SN event file.");
    }
  }
#ifdef USE_MPI
  MPI_Bcast(path, PATH_MAX, MPI_CHAR, ROOT_PROCESSOR, MPI_COMM_WORLD);
  MPI_Bcast(fingerprint, 17, MPI_CHAR, ROOT_PROCESSOR, MPI_COMM_WORLD);
  MPI_Bcast(&count, 1, MPI_INT, ROOT_PROCESSOR, MPI_COMM_WORLD);
#endif
  if (IndividualStarICSupernovaEventFingerprint[0] &&
      strcmp(IndividualStarICSupernovaEventFingerprint, fingerprint))
    ENZO_FAIL("Artificial SN file changed since the checkpoint was written.");
  strcpy(IndividualStarICSupernovaEventFingerprint, fingerprint);
  IndividualStarICSupernovaEventFile = new char[strlen(path)+1];
  strcpy(IndividualStarICSupernovaEventFile, path);
  events.resize(count);
  std::vector<double> packed(4*count);
  if (MyProcessorNumber == ROOT_PROCESSOR)
    for (int n = 0; n < count; ++n) {
      packed[4*n] = events[n].time_myr;
      for (int d = 0; d < 3; ++d) packed[4*n+1+d] = events[n].position[d];
    }
#ifdef USE_MPI
  MPI_Bcast(&packed[0], 4*count, MPI_DOUBLE, ROOT_PROCESSOR, MPI_COMM_WORLD);
#endif
  float density, length, temperature, time_units, velocity;
  if (GetUnits(&density, &length, &temperature, &time_units, &velocity, time) == FAIL)
    ENZO_FAIL("Cannot get units for artificial SN event times.");
  if (!(time_units > 0))
    ENZO_FAIL("Artificial SN events require positive TimeUnits.");
  for (int n = 0; n < count; ++n) {
    events[n].time_myr = packed[4*n];
    for (int d = 0; d < 3; ++d) {
      events[n].position[d] = packed[4*n+1+d];
      if (events[n].position[d] < DomainLeftEdge[d] ||
          events[n].position[d] >= DomainRightEdge[d])
        ENZO_FAIL("Artificial SN position is outside the simulation domain.");
    }
    event_times.push_back(events[n].time_myr * Myr_s / time_units);
    if (!std::isfinite(static_cast<double>(event_times.back())) ||
        event_times.back() <= 0)
      ENZO_FAIL("Artificial SN time cannot be represented in code units.");
  }
  int next = IndividualStarICSupernovaNextEvent;
  // Checkpoint InitialTime uses GOUTSYM (14 significant digits in this build).
  // A checkpoint written at an event can round slightly below its exact time.
  FLOAT time_roundoff = PFLOAT_EPSILON * fabs(time);
  if (next < 0 || next > count ||
      (next > 0 && event_times[next-1] - time > time_roundoff) ||
      (next < count && event_times[next] <= time))
    ENZO_FAIL("SN event cursor is inconsistent with InitialTime; next event must be in the future.");

  int action = -1;
  for (int i = 0; i < MAX_TIME_ACTIONS; ++i)
    if (TimeActionType[i] == 3) {
      if (action >= 0) ENZO_FAIL("SN event file permits only one type-3 time action.");
      action = i;
    }
  if (action < 0)
    for (int i = 0; i < MAX_TIME_ACTIONS; ++i)
      if (TimeActionType[i] <= 0) { action = i; break; }
  if (action < 0) ENZO_FAIL("No free time-action slot for artificial SN events.");
  TimeActionType[action] = 3;
  TimeActionTime[action] = next < count ? event_times[next] : -1;
  TimeActionParameter[action] = 0;
  TimeActionRedshift[action] = -1;
  if (MyProcessorNumber == ROOT_PROCESSOR)
    printf("ArtificialSN: loaded %d events; next=%"ISYM"; fingerprint=%s; "
           "event file overrides the random SN rate and position settings.\n",
           count, next, fingerprint);
  return SUCCESS;
}

void ArtificialSupernovaPosition(float position[3], FLOAT actual_time)
{
  int next = IndividualStarICSupernovaNextEvent;
  if (next < 0 || next >= events.size())
    ENZO_FAIL("Artificial SN event cursor is out of range.");
  for (int d = 0; d < 3; ++d) position[d] = events[next].position[d];
  if (MyProcessorNumber == ROOT_PROCESSOR)
    printf("ArtificialSN: event=%"ISYM" time_Myr=%.17g code_time=%.17g "
           "actual_code_time=%.17g position=%.17g %.17g %.17g\n",
           next, events[next].time_myr, static_cast<double>(event_times[next]),
           static_cast<double>(actual_time),
           static_cast<double>(position[0]), static_cast<double>(position[1]),
           static_cast<double>(position[2]));
}

void AdvanceArtificialSupernovaEvent(int action)
{
  ++IndividualStarICSupernovaNextEvent;
  int next = IndividualStarICSupernovaNextEvent;
  TimeActionTime[action] = next < events.size() ? event_times[next] : -1;
}
