# Immediate upstream fixes for aeos-v2

Reviewed and ported on 2026-11-12. Enzo started at `f5a817b9e`;
`/home/wispedia/install/enzo-dev` was at `7409c9a3`. Grackle's working
branch is also `aeos-v2`, at `21f71a30`, based on main. Its local dust
changes are a separate workstream.

## Adoption decisions

| Upstream commit | Decision | Reason |
| --- | --- | --- |
| `5ed618ce9a31ce1ea21d5d60346b6990d807dc9c` | Port the rollback indices only | A right-hand sibling rollback subtracts the failing field's flux from previously corrected fields. Use each field's own flux instead. Both h277 and the isolated disk enable the relevant `FluxCorrection=2` path. |
| `b35de343417568fb9d89323053d17ed083a2d500` | Port the hydrogen-fraction synchronization | Modern Grackle resolves its negative default during initialization. Enzo must copy back the resolved abundance before initializers and restart output use it. |
| `439fa3eb6f0c3f869ff0ec6148e8673c86142350` | Defer the metal-density cap | The cap can change the persistent metal field when the metal fraction exceeds 0.9. Earlier endpoint screening found no such cells, which does not rule out transient exposure. Check enrichment closure and pre-solver states before choosing a clipping policy. |
| Other part of `5ed618ce9a` | Defer tracer flooring | Replacing whole-cell rollback with a floor on individual tracers changes gas, momentum and species corrections. This needs a separate conservation/positivity comparison with all Aeos elemental fields. |

The hydrogen fix is a direct `git cherry-pick -x` of the upstream commit,
recorded as `c8657fc94`, preserving its author, message and source patch.
Its tests and this report are recorded separately. This replaces the earlier
manual hydrogen port `e2ad6eb7e`.

The flux fix remains the unchanged Aeos-specific partial port `4a184506b`;
it does not include the upstream tracer-floor policy. The existing Aeos
rollback policy, field definitions, dust selectors and LW configuration are
retained.

The earlier [run-impact review](upstream-review/h277-isolated-impact.md)
provides the h277/isolated trigger analysis and output screening. It is a
historical review against an older Aeos baseline; the adoption status here
supersedes its statements that these two corrections are missing.

## Regression evidence

### Flux rollback

```sh
python3 tests/flux_correction/check.py
```

The test compiles the entire production `CorrectForRefinedFluxes` method,
its conservative-field conversion and real field predicates. Only the grid
container and field lookup interface are reduced. It exercises four faces
(left/right sibling and left/right child), all three axes, successful
corrections, and forced failures in H I, total metal, Fe and SNIa-source
densities. Gas/species densities, velocities and reconstructed total energy
are checked in all cells.

Before the port, 12 of 60 cases fail: every forced right-sibling rollback.
For example, a negative H I correction changes gas density from 1 to 2,
instead of restoring 1. The other 48 cases pass. After the port, all 60 pass.
Distinct gas and tracer fluxes make incorrect reuse of another field's flux
observable.

### Hydrogen fraction

Load the selected library's runtime dependencies, then run:

```sh
module load intel21/compiler-21 intel21/intelmpi-21 intel21/hdf5-1.10.5
python3 tests/grackle_hydrogen/check.py \
  /home/wispedia/AA/isolated/physics-audit/grackle-aeos-v2-dust/install \
  /home/wispedia/AA/isolated/CloudyData_HM2012_highz_shielded.h5
```

This compiles the production `GrackleReadParameters.C` with the actual Grackle
headers and shared library. Only the unit/expansion providers are replaced.
Eight cases combine molecular/tabulated chemistry, proper/comoving units
and default/explicit fractions. Fully tabulated chemistry uses its required
Cloudy fraction; molecular chemistry also checks an explicit fraction of 0.72.

Before the port, the four default-fraction cases leave Enzo at `-99999`,
while Grackle holds 0.76 (molecular) or 0.715768377353088514 (tabulated).
The four explicit-fraction controls pass. After the port, all eight pass.
The existing 15 Grackle compatibility cases and actual mode-5 initialization
with the high-redshift Cloudy table also pass.

This validates synchronization with the installed library, not every change
in the separate dirty Grackle working tree. The tested `lib64/libgrackle.so`
has SHA-256:

```text
e92da6062dc9e5b477a23b3449e2063fe360c7e714e133afa28be5485da8e455
```

## Build and scope

A clean `make -j8` compiled 1,237 objects and linked successfully in
`/tmp/aeos-immediate-fixes-20261112-m0i9ytv7/`. Its manifest, patch and
`build.log` record the tracked working state, including changes that preceded
these ports. The temporary build uses the existing happiness2 configuration,
64-bit baryon/particle precision, 32-bit integers, Grackle, photons,
individual stars, new yield tables and 60 baryon fields. The archive has no
Git metadata, so generated version output is unavailable; the manifest
supplies provenance. `makedepend` is absent and its optional commands emit
ignored warnings; every object was compiled from scratch.

A serial executable smoke test used a reduced `CoolingTest_Grackle`
problem (2 x 2 x 8 cells, molecular chemistry, dust mode 5 and a single
step to code time `1e-6`). With positive initial ion fractions, it exits
successfully, all 36 numeric datasets across initial/final outputs are finite,
and density fields are nonnegative. Both parameter outputs record
`HydrogenFractionByMass=0.76` and `dust_chemistry=5`. The input, outputs and log
are under `cooling-smoke-positive-ions/` in the validation directory.

The first smoke test retained the fixture's fully neutral defaults while
enabling molecular dust. Its initializer subtracts nonzero minor species
from an already fully neutral abundance, leaving tiny negative H II and
He III densities. Although the executable exits successfully, 16 cells later
have NaN gas/total energy and cooling time. That attempt is retained under
`cooling-smoke/`; it is not counted as a passing numerical test. The second
input supplies H I and He I fractions of 0.99998, He II of `1e-5`, HM and
H2 II of `1e-12`, and H2 I of `1e-6`. The fixture initialization/solver
handling of the first state remains a separate follow-up, not a source
change in these ports.

The flux test demonstrates a numerical error, not its frequency or integrated
effect in h277 or the isolated disk. The hydrogen fix protects fresh
cosmological species initialization and consistent restart metadata. The
isolated initializer has an independent hydrogen-fraction default, so a
large change to its evolved chemistry is not established by this mismatch.
No galaxy comparison or restart migration is part of these ports.

The dust-recombination normalization findings in the separate
`physics-audit/dust-validation-suite/REPORT.md` concern Grackle cooling,
not either of these Enzo commits. No Grackle source changes are made here.
