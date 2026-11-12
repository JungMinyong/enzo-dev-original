# Second review of the Emerick/Aeos physics findings

Historical audit: the findings below describe the baseline on the review date.
Subsequent SNIa timing and interpolation repairs are documented in
[snia-timing.md](snia-timing.md), [interpolation-boundaries.md](interpolation-boundaries.md),
[snia-rate-interpolation.md](snia-rate-interpolation.md), and
[snia-dtd-integration.md](snia-dtd-integration.md). The later
[PopIII evidence](popiii-yield-evidence.md) identifies the source yield model.

Reviewed 2026-10-31 against aeos-v2 baseline `0dbaa4beae8f1e411a6dd99680b9650d5960791b`. No production physics, executable, yield table, or run input was changed. The original PBS jobs were cancelled in a subsequent task; the old audit's statement that they remained queued is historical, not current status.

This review checks the previous findings against callers and reruns focused tests. It does not establish that every issue arose in a particular author's branch or affected the published simulations. The tested functions are inherited custom stellar routines, not changes introduced by the new deterministic artificial-SN feature.

## Decisions after re-review

| Finding | Updated assessment | Priority |
| --- | --- | --- |
| SNIa model 2 adds birth epoch to a stored duration | **Confirmed by actual assignment method and downstream trigger** | High |
| Exact upper stellar-property/yield endpoint reads past table | **Reproduced again; callers admit the endpoint** | High |
| Ruiter table has duplicate 2 Gyr knots | **New reproduction: exact 2 Gyr returns NaN** | High, shared interpolation/rate cleanup |
| PopIII total mass disagrees with species ejecta | **Confirmed file/consumer mismatch; correction still needs physical provenance** | High for PopIII applications |
| DTD first-bin integration inconsistency | Confirmed implementation inconsistency; small total-probability effect in the tested configuration | Secondary |
| Negative-age SNIa rate returns 1 | Confirmed invalid-input behavior; normal-run reachability unproven | Defensive correction |
| SNIa channel marking loses zero-valued tags | Reproduced, but isolated initializer supplies positive tiny tracers | Conditional |

## 1. SNIa lifetime convention: the earlier finding stands

`IndividualStarProperties.C:124` processes negative WD particle types in `grid::IndividualStarSetWDLifetime`. For model 2 it obtains a delay in years, described in the code as measured from main-sequence birth, converts it to code time, **adds the birth epoch**, and stores it in particle attribute 1.

The caller chain does not cancel this addition:

- `Star_HitEndpoint.C` changes the individual-star type to negative WD after AGB feedback, preserving the original birth time.
- `Grid_StarParticleHandler.C:2078` invokes the lifetime assignment.
- `StarRoutines.C:121,167` reads attributes 0 and 1 as `BirthTime` and `LifeTime`.
- `Star_SetFeedbackFlag.C:128` triggers WD supernova feedback only after `Time > BirthTime + LifeTime`.

The actual assignment method was exercised again in a controlled one-particle fixture. Only unit lookup, the sampled delay, and channel-rate/RNG inputs were mocked. For a 100 Myr sampled delay:

| Birth [Myr] | Stored duration [Myr] | Trigger endpoint [Myr] | Expected birth + delay |
| ---: | ---: | ---: | ---: |
| 0 | 100 | 100 | 100 |
| 83 | 183 | 266 | 183 |

Shifting birth and WD-formation epochs by 83 Myr shifts the predicted endpoint by 166 Myr. This is a time-translation error, independent of the stochastic delay realization.

A separate causality fixture places WD formation at 100 Myr and forces a sampled age of 1 Myr: the stored endpoint is already in the past. The existing guard compares years with a code-unit timestep and does not enforce a future endpoint relative to WD formation. A repair therefore needs a documented policy for sampled delays shorter than the progenitor lifetime (for example rejection/resampling versus clipping); the correct physical choice is not settled by this software test. Merely deleting the extra birth-time addition is not a complete repair.

This confirms faulty timing logic, not a measured count of missing SNe Ia in any galaxy run.

## 2. Interpolation endpoints: genuine caller-visible defects

Both the generic stellar interpolator and the yield-position routine accept equality with the last axis value. `search_lower_bound` returns the index of that last value. Their subsequent `i+1` read is outside the axis.

Re-running with unoptimized extracted routines and Valgrind reproduces:

- Interior query 2.5 on `[1,2,3]`: interval 1, weight 0.5, no invalid read.
- Query 3: invalid read one element past the allocation.
- Yield lookup at maximum mass: invalid read followed by abort, despite extrapolation being enabled.

`IndividualStarGetSETablePosition` directly forwards mass and metallicity to the interpolation helper; it does not clamp maximum values inward. The yield extrapolation clamp only handles strict out-of-range values. Thus these are not artifacts of calling helpers in a way their callers forbid. The frequency of exact-endpoint queries in real evolution remains unmeasured.

For a one-point metallicity axis, context matters: the PopIII lookup ignores the returned metallicity interval and its interpolator is mass-only. Do not call that particular path broken simply because `Nz=1`, nor apply a blanket `n-2` clamp to every generic search call. Separate element search from interval selection.

## 3. SNIa table duplicates and endpoint behavior

The Ruiter table in `IndividualStarProperties.C:396` includes **two consecutive times equal to 2.0 Gyr**, with repeated rates. Evaluating the actual routine at `2e9` yr returns **NaN** because its selected interpolation interval has zero width. The function should return the finite tabulated rate at that age.

At 14 Gyr, the first optimized test printed a plausible endpoint value and Valgrind did not flag it. The unoptimized re-review now reports use of uninitialized values even though the printed rate remains plausible. The final-index `i+1` access is therefore not exonerated by a numerically plausible return value. These differences illustrate why successful output alone is not a bounds check.

The regular 2000-bin DTD initialization remains finite in the tested configuration. It does not necessarily query exactly 2 Gyr or exactly the final knot because its ages are generated by logarithmic floating-point arithmetic. We have reproduced unsafe boundary behavior, not demonstrated NaNs in every initialized DTD.

## 4. PopIII table: more evidence, still a model-contract decision

The current `IndividualStarYields-Mix0.1.h5` was checked again across **all rows**, using every available species rather than only the tracked subset:

| Group | Rows | `Mtot` equals progenitor mass | `Mtot` equals sum of species |
| --- | ---: | ---: | ---: |
| AGB | 80 | 0 | 80 |
| SN | 117 | 0 | 117 |
| Wind | 117 | 0 | 117 |
| SN+Wind | 117 | 0 | 117 |
| PopIII | 134 | 120 | 14 |

Every group's `Metal_Mtot` agrees with the sum of its metal species at the tested tolerance. In PopIII, the 120 core-collapse rows use progenitor mass in the first column; the 14 pair-instability rows agree with species ejecta. At 70 Msun the first column is 70, while summed species are about 34.80575 Msun.

`StellarYields_Initialize.C:736` copies the first column to `Mtot`. `IndividualStarSetPopIIISupernovaProperties` then uses its interpolation as ejecta mass. The current TypeII bounds are 10–100 Msun, so the 70 Msun example is not excluded by those bounds.

A previous workspace investigation independently describes the same pattern:
`/home/wispedia/AA/isolated/runs/run3-abyss-noFEWBODY/build/source/documentation/campaign-72h/2026-09-07-popiii-yield-table-investigation.md`.
Its statement that the upstream generating pipeline was unavailable is evidence about that investigation, not proof that no generator exists anywhere today. No original generator was located in the paths searched during this review.

The observations favor a progenitor/remnant-inclusive column being consumed as ejecta in the core-collapse block. They do not authorize an automatic replacement with the species sum without tracing the table source and intended remnant treatment. The initial disk is enriched; actual PopIII event exposure in the comparison runs has not been established.

## 5. Secondary checks and conditional findings

**DTD initialization.** `t_prev=0` conflicts with the first tabulated age of 1e6 yr, and `data[0]` starts as a rate rather than a cumulative probability. Relative to integration beginning at 1e6 yr, the first CDF bin is 2.76956e-5 instead of 1.32156e-7; maximum absolute CDF discrepancy is 2.75635e-5. The terminal fraction remains 0.1508. If the intended support begins at zero instead, the probability from zero to 1 Myr must be represented consistently in the first bin. The lower-bound convention should be decided before repair; this is not a factor-of-hundreds error in total SNIa probability.

**Negative ages.** The rate routine still returns 1 at -1 yr: it sets the logarithmic rate to zero and exponentiates it. That contradicts the code's intended zero-rate handling. Normal DTD generation samples positive ages, so this has lower demonstrated exposure.

**Channel tagging.** Model 2 records a channel by multiplying a tracer abundance by -1; `DetermineSNIaType` searches for a value strictly below zero. A selected channel 3 with initial abundance 0 becomes negative zero and is recovered as default channel 0. Starting from 1e-20 recovers channel 3 correctly. The star-maker copies tracer values without a local positivity floor, but `Grid_GalaxySimulationInitializeGrid.C:765–770` initializes these source tracers to positive tiny values. Therefore this is a fragile encoding and a reproduced zero-input defect, not a demonstrated channel error for the initialized fiducial disk.

**Passes rechecked.** Kroupa's analytic-CDF comparison still passes (maximum absolute error 0.001972, tolerance 0.005). PopII mass closure and the tested LW unit/suppression contracts still pass. These are narrow checks, not full physics validation.

## Test artifacts and proposed repair order

Raw fixtures/results: `/home/wispedia/AA/isolated/physics-audit/review/`.

- `boundary.cpp`, `boundary-results.json`, and individual Valgrind logs.
- `wd-review.cpp`, `wd-review.txt`: timing, causality, and channel round-trip fixtures.
- `yield-provenance-check.json`: current-file all-row checks.
- Earlier extraction scripts and numerical references remain in the parent audit directory.

Rebuild fixtures with `g++ -O0 -g boundary.cpp -o boundary` and `g++ -O0 wd-review.cpp -o wd-review`; run boundary cases under `valgrind --error-exitcode=99 --leak-check=no`.

Recommended separate fixes, each with regression tests:

1. Endpoint-safe interpolation and duplicate-time handling, including actual table-axis tests.
2. SNIa lifetime/epoch/unit consistency, with a chosen pre-WD-delay policy and a real stellar-lifecycle test.
3. DTD integration and invalid-input handling; replace channel encoding if a robust restart-compatible representation is chosen.
4. PopIII table correction only after confirming the mass convention and remnant budget.

No fix or commit was made as part of this review. This report is a local documentation update pending the user's next instruction.
