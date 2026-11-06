extern "C" {
#include <grackle.h>
}
#include <cstdio>
#include <cstdlib>
#include <stdexcept>
#define ENZO_FAIL(message) throw std::runtime_error(message)
#define ROOT_PROCESSOR 0
int MyProcessorNumber = 0;
int GrackleLWBackgroundModel, H2FormationOnDust, MultiSpecies = 2;
#include "GrackleParameters.h"
int main(int argc, char **argv) {
  if (argc != 4 && argc != 5) return 3;
  chemistry_data chemistry;
  set_default_chemistry_parameters(&chemistry);
  grackle_data->dust_chemistry = atoi(argv[1]);
  H2FormationOnDust = atoi(argv[2]);
  GrackleLWBackgroundModel = atoi(argv[3]);
  try { ConfigureGrackleParameters(); }
  catch (const std::runtime_error &e) { fprintf(stderr, "%s\n", e.what()); return 2; }
  if (argc == 5) {
    grackle_data->use_grackle = 1;
    grackle_data->primordial_chemistry = 2;
    grackle_data->metal_cooling = 1;
    grackle_data->photoelectric_heating = 0;
    grackle_data->grackle_data_file = argv[4];
    code_units units = {};
    units.a_units = units.a_value = 1.0;
    units.density_units = 1.67e-24;
    units.length_units = 3.0857e18;
    units.time_units = 3.1557e11;
    units.velocity_units = units.length_units / units.time_units;
    if (!initialize_chemistry_data(&units)) return 4;
    const int n = grackle_data->NumberOfTemperatureBins;
    if (n < 2 || !grackle_rates.k1 || !grackle_rates.k2) return 5;
    if (grackle_rates.k1[0] < 0 || grackle_rates.k1[n-1] < 0 ||
        grackle_rates.k2[0] < 0 || grackle_rates.k2[n-1] < 0) return 5;
    free_chemistry_data();
  }
  return 0;
}
