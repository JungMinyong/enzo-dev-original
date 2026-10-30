#ifndef ENZO_GRACKLE_COMPATIBILITY_H
#define ENZO_GRACKLE_COMPATIBILITY_H
#ifdef USE_GRACKLE
#if (defined(ENZO_GRACKLE_main) + defined(ENZO_GRACKLE_newchem) + defined(ENZO_GRACKLE_emerick)) != 1
#error "Select make grackle-backend-main, grackle-backend-newchem, or grackle-backend-emerick"
#endif
#if !defined(ENZO_GRACKLE_LW_yes) && !defined(ENZO_GRACKLE_LW_no)
#error "Select make grackle-legacy-lw-no or grackle-legacy-lw-yes"
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
  if (grackle_data->dust_chemistry < 0 || grackle_data->dust_chemistry > 1)
    ENZO_FAIL("This Enzo adapter supports dust_chemistry=0/1 only; Chiaki species fields are not integrated.");
  if (GrackleDustAbundanceModel == -1) {
    if (H2FormationOnDust == 2)
      ENZO_FAIL("Legacy H2FormationOnDust=2 requires explicit GrackleDustAbundanceModel: 0 standard, 1 physical Remy-Ruyer, 2 legacy Remy-Ruyer.");
    GrackleDustAbundanceModel = 0;
  }
  if (GrackleDustAbundanceModel < 0 || GrackleDustAbundanceModel > 2)
    ENZO_FAIL("GrackleDustAbundanceModel must be 0, 1, or 2.");
  if (H2FormationOnDust < 0 || H2FormationOnDust > 2)
    ENZO_FAIL("Unsupported H2FormationOnDust value.");
  if (GrackleLWBackgroundModel < 0 || GrackleLWBackgroundModel > 2)
    ENZO_FAIL("LWbackground_model must be 0, 1, or 2.");
#ifdef ENZO_GRACKLE_LW_yes
  grackle_data->LWbackground_model = GrackleLWBackgroundModel;
#else
  if (GrackleLWBackgroundModel != 0)
    ENZO_FAIL("Analytic LW model requires a supporting Grackle library and make grackle-legacy-lw-yes; table LW remains available.");
#endif
  if (GrackleDustAbundanceModel && (grackle_data->dust_chemistry != 1 || grackle_data->use_dust_density_field))
    ENZO_FAIL("Custom dust abundance requires dust_chemistry=1 and use_dust_density_field=0.");
#ifdef GRACKLE_HAS_DUST_ABUNDANCE_MODEL
  grackle_data->dust_abundance_model = GrackleDustAbundanceModel;
#elif defined(ENZO_GRACKLE_emerick)
  if (GrackleDustAbundanceModel == 1)
    ENZO_FAIL("Emerick supports legacy normalization only (model 2).");
#else
  if (GrackleDustAbundanceModel != 0)
    ENZO_FAIL("This Grackle library lacks Remy-Ruyer support. Model 0 explicitly selects standard dust physics.");
#endif
#ifdef ENZO_GRACKLE_newchem
  if (H2FormationOnDust > 0 && (grackle_data->dust_chemistry < 1 || MultiSpecies < 2))
    ENZO_FAIL("newchem H2 formation on dust requires dust_chemistry>0 and MultiSpecies>1.");
  grackle_data->h2_on_dust = 0;
#else
  grackle_data->h2_on_dust = H2FormationOnDust > 0 ? 1 : 0;
#ifdef ENZO_GRACKLE_emerick
  if (GrackleDustAbundanceModel == 2) grackle_data->h2_on_dust = 2;
#endif
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
    fprintf(stdout, "Legacy Grackle; dust abundance=%d; LW model=%d; internal h2_on_dust=%d\n", GrackleDustAbundanceModel, GrackleLWBackgroundModel, grackle_data->h2_on_dust);
#else
    grackle_version v = get_grackle_version();
    fprintf(stdout, "Grackle version=%s branch=%s revision=%s; dust abundance=%d; LW model=%d; internal h2_on_dust=%d\n", v.version, v.branch, v.revision, GrackleDustAbundanceModel, GrackleLWBackgroundModel, grackle_data->h2_on_dust);
#endif
  }
}
#endif
#endif
