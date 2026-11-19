#ifndef ENZO_PHOTOELECTRIC_RADIATION_FIELD_H
#define ENZO_PHOTOELECTRIC_RADIATION_FIELD_H

// The same band-integrated Habing convention used by AEOS PE heating.
const double AEOSHabingFlux = 1.59e-3; // erg cm^-2 s^-1
float NormalizedDustToGasRatio(const float &Z);

inline float PhotoelectricDustAttenuation(int model, float Z, float nH, float dx)
{
  if (model == 0) return 1.0;
  if (model != 1)
    ENZO_FAIL("PhotoelectricHeatingDustModel must be either 0 or 1");
  return exp(-1.33e-21 * NormalizedDustToGasRatio(Z) * max(dx,0.0) * nH);
}

// fuv is the unattenuated, summed AEOS FUVRate field in code flux units.
// Only for RadiativeTransferOpticallyThinFUV: ray fields have other semantics.
// Proper units from GetUnits already account for cosmological expansion.
inline void FillPhotoelectricGrackleISRF(
    int size, float *isrf, const float *fuv, const float *density,
    const float *metal, const float *HI, const float *HII, const float *HM,
    const float *H2I, const float *H2II, int multispecies, int dust_model,
    double density_units, double velocity_units, double length_units,
    double time_units, double cell_width, double hydrogen_mass)
{
  const double flux_units = density_units * velocity_units * velocity_units *
                            length_units / time_units;
  for (int i=0; i<size; i++) {
    if (fuv[i] < 0 || !isfinite(fuv[i]))
      ENZO_FAIL("AEOS FUVRate must be finite and nonnegative for Grackle ISRF");
    // Ghost/vacuum cells may have no material; no dust attenuation there.
    float Z = density[i] > 0 ? metal[i]/density[i] : 0;
    float nH = HI[i] + HII[i];
    if (multispecies > 1) nH += HM[i] + H2I[i] + H2II[i];
    nH *= density_units / hydrogen_mass;
    isrf[i] = fuv[i] * flux_units / AEOSHabingFlux *
      PhotoelectricDustAttenuation(dust_model, Z, nH, cell_width*length_units);
  }
}
#endif
