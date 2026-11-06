#ifndef ENZO_GRACKLE_COMPATIBILITY_H
#define ENZO_GRACKLE_COMPATIBILITY_H
#ifdef USE_GRACKLE
#if (defined(ENZO_GRACKLE_main) + defined(ENZO_GRACKLE_newchem) + defined(ENZO_GRACKLE_emerick)) != 1
#error "Select make grackle-backend-main, grackle-backend-newchem, or grackle-backend-emerick"
#endif
#include <type_traits>
#include <utility>
template<class T> struct GrackleHasMetalChemistry {
  template<class U> static auto check(int) -> decltype(std::declval<U>().metal_chemistry, std::true_type());
  template<class> static std::false_type check(...);
  static const bool value = decltype(check<T>(0))::value;
};
#ifdef ENZO_GRACKLE_newchem
static_assert(GrackleHasMetalChemistry<chemistry_data>::value, "newchem profile requires newchem headers");
#else
static_assert(!GrackleHasMetalChemistry<chemistry_data>::value, "main/emerick profile cannot use newchem headers");
#endif
template<class T> struct GrackleHasLegacyLW {
  template<class U> static auto check(int) -> decltype(std::declval<U>().LWbackground_model, std::true_type());
  template<class> static std::false_type check(...);
  static const bool value = decltype(check<T>(0))::value;
};
#ifdef ENZO_GRACKLE_emerick
static_assert(GrackleHasLegacyLW<chemistry_data>::value, "emerick profile requires legacy headers");
#endif
#include <vector>
inline void GracklePhotonRateTable(const char* name, std::vector<double>& values) {
  const int n = grackle_data->NumberOfTemperatureBins;
  if (n < 2) ENZO_FAIL("Grackle rate interpolation requires at least two bins.");
  values.resize(n);
#ifdef ENZO_GRACKLE_newchem
  const auto id = grunstable_ratequery_id(&grackle_rates, name);
  int64_t ndim = 0, length = 0;
  if (grunstable_ratequery_prop(&grackle_rates, id, GRUNSTABLE_QPROP_NDIM, &ndim) != GR_SUCCESS || ndim != 1 ||
      grunstable_ratequery_prop(&grackle_rates, id, GRUNSTABLE_QPROP_SHAPE, &length) != GR_SUCCESS || length != n ||
      grunstable_ratequery_get_f64(&grackle_rates, id, values.data()) != GR_SUCCESS)
    ENZO_FAIL("Cannot query Grackle photon-timestep rate table.");
#else
  const double* source = name[1] == '1' ? grackle_rates.k1 : grackle_rates.k2;
  for (int i=0; i<n; i++) values[i] = source[i];
#endif
}
inline void ConfigureGrackleCompatibility() {
  const int dust_model = grackle_data->dust_chemistry;
  const bool remy_ruyer = dust_model == 4 || dust_model == 5;
  if (dust_model == 2)
    ENZO_FAIL("dust_chemistry=2 requires Chiaki species fields, which this Enzo adapter does not integrate.");
  if (dust_model != 0 && dust_model != 1 && !remy_ruyer)
    ENZO_FAIL("Supported dust_chemistry values are 0, 1, 4 (historical Remy-Ruyer), and 5 (corrected Remy-Ruyer).");
  if (H2FormationOnDust < 0 || H2FormationOnDust > 2)
    ENZO_FAIL("Unsupported H2FormationOnDust value.");
  if (H2FormationOnDust == 2 && !remy_ruyer)
    ENZO_FAIL("Replace legacy H2FormationOnDust=2 with dust_chemistry=4 (historical) or 5 (corrected), and omit the obsolete H2 switch.");
  if (GrackleLWBackgroundModel != 0)
    ENZO_FAIL("Only LWbackground_model=0 is supported; analytic LW models 1/2 are unsupported.");
#ifdef ENZO_GRACKLE_emerick
  grackle_data->LWbackground_model = 0;
#endif
#ifdef ENZO_GRACKLE_newchem
  if (H2FormationOnDust > 0 && (grackle_data->dust_chemistry < 1 || MultiSpecies < 2))
    ENZO_FAIL("newchem H2 formation on dust requires dust_chemistry>0 and MultiSpecies>1.");
  grackle_data->h2_on_dust = 0;
#else
  grackle_data->h2_on_dust = H2FormationOnDust > 0 ? 1 : 0;
#endif
  // Serialize an unambiguous resolved switch; newchem's internal field stays zero.
  H2FormationOnDust = (grackle_data->dust_chemistry > 0 && MultiSpecies > 1) || H2FormationOnDust > 0;
  if (MyProcessorNumber == ROOT_PROCESSOR) {
#ifdef ENZO_GRACKLE_newchem
    const char* backend = "newchem";
#elif defined(ENZO_GRACKLE_emerick)
    const char* backend = "emerick";
#else
    const char* backend = "main";
#endif
    fprintf(stdout, "Enzo Grackle backend=%s\n", backend);
#ifdef ENZO_GRACKLE_emerick
    fprintf(stdout, "Legacy Grackle; dust_chemistry=%d; LW model=%d; h2_on_dust before initialization=%d\n", dust_model, GrackleLWBackgroundModel, grackle_data->h2_on_dust);
#else
    grackle_version v = get_grackle_version();
    fprintf(stdout, "Grackle version=%s branch=%s revision=%s; dust_chemistry=%d; LW model=%d; internal h2_on_dust=%d\n", v.version, v.branch, v.revision, dust_model, GrackleLWBackgroundModel, grackle_data->h2_on_dust);
#endif
  }
}
#endif
#endif
