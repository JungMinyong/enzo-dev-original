#ifndef ENZO_GRACKLE_PARAMETERS_H
#define ENZO_GRACKLE_PARAMETERS_H
#ifdef USE_GRACKLE
inline void ConfigureGrackleParameters() {
  const int dust_model = grackle_data->dust_chemistry;
  if (dust_model != 0 && dust_model != 1 && dust_model != 5)
    ENZO_FAIL("Supported dust_chemistry values are 0, 1 (standard), and 5 (corrected Remy-Ruyer).");
  if (H2FormationOnDust < 0 || H2FormationOnDust > 2)
    ENZO_FAIL("Unsupported H2FormationOnDust value.");
  if (H2FormationOnDust == 2 && dust_model != 5)
    ENZO_FAIL("Replace legacy H2FormationOnDust=2 with dust_chemistry=5 and omit the obsolete H2 switch.");
  if (GrackleLWBackgroundModel != 0)
    ENZO_FAIL("Only LWbackground_model=0 is supported; analytic LW models 1/2 are unsupported.");
  grackle_data->h2_on_dust = H2FormationOnDust > 0 ? 1 : 0;
  H2FormationOnDust = (dust_model > 0 && MultiSpecies > 1) || H2FormationOnDust > 0;
  if (MyProcessorNumber == ROOT_PROCESSOR) {
    grackle_version v = get_grackle_version();
    fprintf(stdout, "Grackle version=%s branch=%s revision=%s; dust_chemistry=%d; LW model=0\n",
            v.version, v.branch, v.revision, dust_model);
  }
}
#endif
#endif
