# Validation of the initial aeos-v2 integration

Subsequent artificial-SN event-file implementation and replay tests are
documented in [artificial-supernova-events.md](artificial-supernova-events.md).

## Versions and artifacts

- Enzo baseline: `72ee7320821cdc5fdfba3737438309698525701e`, with the aeos-v2 working-tree changes.
- Main Grackle: `01261db0cefc69d8d5558e76a671b0c1f6e48271`.
- Newchem: `6700d14c2cbfda0cfba7a693c38dcd3065d43019`.
- Both Grackle libraries built with GCC toolset 13; Enzo built with the Intel21 compiler/MPI/HDF5 modules, 64-bit precision, photons and individual-star physics enabled.
- Runtime version reports have branch/revision `N/A`; the commits above identify the inspected source builds.
- Main Enzo build copy: `/home/wispedia/AA/isolated/grackle-compatibility/aeos-v2-main`.
- Newchem Enzo: `/home/wispedia/enzo/EnzoAeos-v2/bin/enzo`.
- Logs, input decks, tables and outputs: `/home/wispedia/AA/isolated/grackle-compatibility/v2-tests` (including `build-logs`).

## Results

| Check | Main | Newchem |
| --- | --- | --- |
| Full compile and link | Pass | Pass |
| Seven parameter acceptance/rejection checks | Pass | Pass |
| High-z table initialization and k1/k2 rate-table query, including endpoint access | Pass | Pass |
| Reduced isolated-galaxy startup to cycle 2 | Pass | Pass |
| Restart from cycle 2 to cycle 3 | Pass | Pass |
| Finite floating-point output datasets in galaxy startup/restart | 208 checked, none nonfinite | 208 checked, none nonfinite |
| Broad cooling grid | **Fails numerical validation** | **Fails numerical validation** |

Wrong main/newchem header selection and unsupported legacy-LW compilation are rejected. The compatibility header compiles with Grackle disabled; a full no-Grackle executable was not built. The legacy Emerick profile was implemented but not built or run in this validation.

The isolated smoke decks derive from the exported run3-fiducial input, explicitly selecting standard dust model 0 and H2 formation enabled. They use a 16^3 root grid, no refinement, and two startup cycles followed by one restart cycle. This is a low-cost integration test; it does not resolve the galaxy, validate stellar-feedback evolution, or reproduce the paper's Remy-Ruyer dust model. Original production inputs are unchanged.

The broad cooling test derives from CoolingTest_Grackle with a 3x3x5 density/metallicity/temperature grid, a nine-species network, dust model 0, and the high-z table. Both executables exit successfully, but both emit chemistry subcycle-limit warnings and produce 30 NaNs each in GasEnergy and TotalEnergy in DD0001. Successful exit is therefore not counted as a pass. The cause and acceptable numerical agreement remain unresolved; do not use this test to claim equivalence or production readiness.

An initial restart attempt used a renamed parameter file without matching hierarchy files and failed. Retesting with the original checkpoint basename and only the generated test StopCycle changed passed for both libraries.

## Build observations

The local machine file needed Intel Fortran runtime libraries independently of the Grackle link flags. Both builds still emit ignored dependency-generation Error 127 messages from the existing make setup. New compatibility-header dependencies and the configuration fingerprint are explicit, but repair of the legacy dependency generator remains a build-system follow-up.

No new Grackle physics was implemented, no source was pushed, and the original aeos checkout was retained. Remy-Ruyer support in newchem, normalization validation, molecular radiation coupling, and production-scale comparisons remain outstanding.

A comparison of the reduced galaxy cycle-3 outputs gives max absolute differences normalized by the main field's maximum magnitude: density 2.51e-8, HI density 2.28e-4, H2 density 3.90e-3, and gas energy 1.08e-5. These are descriptive differences for this smoke test, not an established scientific tolerance or per-cell relative errors.

## Subsequent deterministic comparison

The Emerick profile was later compiled successfully after accommodating its
older version-reporting API. The three deterministic-feedback cases reached
5 Myr with matched event records and finite saved fields. See
[the event-file validation](artificial-supernova-events.md#tests).
This baseline does not fix the separately identified stellar interpolation,
Type Ia timing, or Pop III yield-table issues.
