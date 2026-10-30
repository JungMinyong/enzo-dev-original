# Aeos-v2 Grackle integration

Baseline: Aeos `72ee7320821cdc5fdfba3737438309698525701e`. This branch adds compatibility plumbing; it does not implement a new dust law in Grackle.

## Build

Choose the installation paths in your machine file, then:

```sh
make grackle-yes
make grackle-backend-newchem  # alternatives: main, emerick
make grackle-legacy-lw-no    # yes requires a library exposing LWbackground_model
make show-config
make -j8
```

The backend must match the headers AND linked library. C++ header checks reject a main/newchem profile mismatch; enabling legacy LW compiles a reference to its required member. These checks cannot prove provenance of arbitrary ABI-compatible libraries. Use matching prefixes and inspect the runtime library path. The executable logs Grackle version/branch/revision and resolved options.

A build fingerprint includes compiler flags, includes, library flags and the two new configuration options; changing it rebuilds objects. Perform a clean rebuild if replacing a library or headers in place. Build distinct backends in separate build copies. Intel-compiled Enzo requires its own Fortran runtime libraries independently of Grackle. The local happiness2 configuration now places `-lifcore -lifport` in machine libraries.

## Runtime physics choices

`LWbackground_model` is Enzo-owned and defaults to 0. With legacy LW disabled, only 0 is accepted; tabulated LW, constant intensity, and sawtooth controls remain available. Values 1/2 require a supporting library and the legacy build option.

`GrackleDustAbundanceModel`:

| Value | Meaning | Available here |
| --- | --- | --- |
| 0 | Standard library metallicity scaling | main/newchem/emerick |
| 1 | Physical-ratio Remy-Ruyer | Reserved for a future Grackle extension |
| 2 | Emerick legacy-normalization Remy-Ruyer | emerick; future extension |

A future library extension must define `GRACKLE_HAS_DUST_ABUNDANCE_MODEL` and expose `chemistry_data.dust_abundance_model` with these meanings. Until then main/newchem reject 1/2. Custom abundance requires `dust_chemistry=1` and no explicit dust field. This work does not add Chiaki species fields to Enzo or implement the physical-ratio prescription.

Old `H2FormationOnDust=2` without an explicit abundance choice is rejected. Explicit model 0 is an intentional physics change from Emerick's broken power law. In main, Enzo uses the supported H2 switch. In newchem, the internal deprecated switch stays zero and dust chemistry plus the molecular network enable formation. An explicit H2-off request conflicting with enabled molecular dust chemistry is rejected; omit the old switch to accept the automatic behavior. Resolved choices are serialized for restarts.

Enzo's external photoelectric heating is unchanged. Selecting standard Grackle dust does not make the photoelectric prescription linear; that separate physics choice must be considered when interpreting runs.

## Other compatibility fixes

- Correct double parsing for `local_dust_to_gas_ratio`.
- Zero-initialize every optional Grackle field and require metal density when metal cooling is enabled. Existing species-field validation remains active.
- Photon timesteps query k1/k2 through newchem's experimental public rate API; main/emerick use their exposed tables. Validate table dimensions before copying.
- Correct one-based interpolation indices to zero-based Grackle table offsets, including the upper endpoint. This also corrects the previous main/emerick access, which could read beyond the array.

## Tests and limits

`tests/grackle_compatibility/parameters.cpp` and `check.py` check standard selection, explicit migration, rejection paths, and optionally rate-table loading. Compile against the actual installation, for example:

```sh
c++ -std=c++11 -DUSE_GRACKLE -DENZO_GRACKLE_newchem -DENZO_GRACKLE_LW_no \
  -Isrc/enzo -I"$GRACKLE_PREFIX/include" tests/grackle_compatibility/parameters.cpp \
  -L"$GRACKLE_PREFIX/lib64" -Wl,-rpath,"$GRACKLE_PREFIX/lib64" -lgrackle -o /tmp/aeos-grackle-check
python3 tests/grackle_compatibility/check.py /tmp/aeos-grackle-check
/tmp/aeos-grackle-check 0 1 0 /absolute/path/CloudyData_HM2012_highz_shielded.h5
```

Full build and smoke-test results are recorded separately. Standard-dust startup tests establish integration, not reproduction of the paper's Remy-Ruyer model. The normalization issue and H-/H2+ stellar radiation integration remain separate scientific follow-ups. No library sources or production input decks are modified by this branch.
