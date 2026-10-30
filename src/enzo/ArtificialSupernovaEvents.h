#ifndef ARTIFICIAL_SUPERNOVA_EVENTS_H
#define ARTIFICIAL_SUPERNOVA_EVENTS_H
// Include after Enzo's type definitions.
int InitializeArtificialSupernovaEvents(FLOAT time);
void ArtificialSupernovaPosition(float position[3], FLOAT actual_time);
void AdvanceArtificialSupernovaEvent(int action);
#endif
