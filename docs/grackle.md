# Aeos-v2 Grackle integration

Baseline: Aeos `72ee7320821cdc5fdfba3737438309698525701e`. This branch adds compatibility plumbing; it does not implement a new dust law in Grackle.

## Build

Choose the installation paths in your machine file, then:

```sh
make grackle-yes
make grackle-backend-newchem  # alternatives: main, emerick
make show-config
make -j8
```

The backend must match the headers AND linked library. C++ header checks reject a main/newchem profile mismatch; enabling legacy LW compiles a reference to its required member. These checks cannot prove provenance of arbitrary ABI-compatible libraries. Use matching prefixes and inspect the runtime library path. The executable logs Grackle version/branch/revision and resolved options.

A build fingerprint includes compiler flags, includes, library flags and the two new configuration options; changing it rebuilds objects. Perform a clean rebuild if replacing a library or headers in place. Build distinct backends in separate build copies. Intel-compiled Enzo requires its own Fortran runtime libraries independently of Grackle. The local happiness2 configuration now places `-lifcore -lifport` in machine libraries.

## Runtime physics choices

`LWbackground_model` is Enzo-owned and defaults to 0. Only 0 is accepted;
analytic models 1/2 are unsupported. Tabulated LW, constant intensity, and
sawtooth controls remain available. There is no legacy-LW build option.

`dust_chemistry` is the single dust-model selector:

| Value | Meaning | Available here |
| --- | --- | --- |
| 0 | No dust chemistry | main/newchem/emerick |
| 1 | Standard static dust | main/newchem/emerick |
| 2 | Chiaki evolution | Unsupported by this Enzo adapter; required species fields are not integrated |
| 3 | Reserved | Unsupported |
| 4 | Historical normalized Remy-Ruyer | Patched emerick |
| 5 | Corrected physical-ratio Remy-Ruyer | Patched emerick or Grackle aeos-v2 (main-based) |

Enzo passes modes 4/5 to Grackle without a compile-time capability check and
checks initialization for failure. Use a matching patched library: unmodified
libraries may silently interpret unknown positive values as standard dust.
Grackle aeos-v2 supports 5 and rejects 4. The patched Grackle-Emerick branch
supplies the corrected absolute empirical fit for 5 and retains the old
normalization error for reproducibility in 4. Explicit dust density takes
precedence over inferred abundance. This does not implement Chiaki evolution
in Enzo.

The separate `GrackleDustAbundanceModel` parameter was removed; old input
files containing it receive a migration error rather than silently changing
physics. Translate old abundance values 0/1/2 to `dust_chemistry=1/5/4`,
respectively (or retain 0 when dust was disabled), and remove the old parameter.

Old `H2FormationOnDust=2` without `dust_chemistry=4/5` is rejected. Prefer
omitting the obsolete H2 switch and letting dust chemistry enable formation.
In main, Enzo uses the supported H2 switch. In newchem, the internal deprecated
switch stays zero and dust chemistry plus the molecular network enable
formation. An explicit H2-off request conflicting with enabled molecular dust
chemistry is rejected. Resolved choices are serialized for restarts.

Enzo's external photoelectric heating is unchanged. Selecting standard Grackle dust does not make the photoelectric prescription linear; that separate physics choice must be considered when interpreting runs.

## Other compatibility fixes

- Correct double parsing for `local_dust_to_gas_ratio`.
- Zero-initialize every optional Grackle field and require metal density when metal cooling is enabled. Existing species-field validation remains active.
- Photon timesteps query k1/k2 through newchem's experimental public rate API; main/emerick use their exposed tables. Validate table dimensions before copying.
- Correct one-based interpolation indices to zero-based Grackle table offsets, including the upper endpoint. This also corrects the previous main/emerick access, which could read beyond the array.

## Tests and limits

`tests/grackle_compatibility/parameters.cpp` and `check.py` check standard selection, explicit migration, rejection paths, and optionally rate-table loading. Compile against the actual installation, for example:

```sh
c++ -std=c++11 -DUSE_GRACKLE -DENZO_GRACKLE_newchem \
  -Isrc/enzo -I"$GRACKLE_PREFIX/include" tests/grackle_compatibility/parameters.cpp \
  -L"$GRACKLE_PREFIX/lib64" -Wl,-rpath,"$GRACKLE_PREFIX/lib64" -lgrackle -o /tmp/aeos-grackle-check
python3 tests/grackle_compatibility/check.py /tmp/aeos-grackle-check
/tmp/aeos-grackle-check 1 1 0 /absolute/path/CloudyData_HM2012_highz_shielded.h5
```

The first fixture argument is `dust_chemistry`. The selection checks accept
4/5 independently of the backend; supply a data-file argument to test actual
library initialization and rejection. The legacy header requires wrapping
its C declarations in `extern "C"` (as the fixture does). Full build and
smoke-test results are recorded separately. Standard-dust startup tests
establish integration, not reproduction of the paper's Remy-Ruyer model.
The Grackle normalization fix has separate single-cell tests; the broader
cooling-grid NaNs and H-/H2+ stellar radiation integration remain separate
follow-ups. Production input decks are not modified.
