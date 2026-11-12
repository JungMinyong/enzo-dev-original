# Aeos v2 documentation

Development notes for the `aeos-v2` branch. The existing `doc/` directory retains
its upstream documentation.

- [Grackle compatibility and physics choices](grackle.md)
- [Deterministic artificial supernova events](artificial-supernova-events.md)
- [Initial integration validation and known limitations](validation.md)
- [SNIa model 2 timing correction](snia-timing.md)
- [Stellar-property and yield interpolation boundaries](interpolation-boundaries.md)
- [SNIa rate-table interpolation correction](snia-rate-interpolation.md)
- [SNIa cumulative-probability initialization](snia-dtd-integration.md)
- [Second review of custom-physics issues](physics-review.md)
- [PopIII yield provenance and mass-closure evidence](popiii-yield-evidence.md)
- [Enzo main commit review and adoption recommendations](upstream-review/README.md)
- [Upstream changes that can affect h277 and the isolated dwarf](upstream-review/h277-isolated-impact.md)
- [Adopted upstream fixes and their provenance](upstream-fixes-20261112.md)

Add future physics audits, correction decisions, and validation summaries here.
Keep runnable regression tests in `tests/` and simulation outputs outside the
source repository.
