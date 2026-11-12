# Findings and recommended adoption order

Baseline and category definitions: [review index](README.md). Every recommendation refers to the frozen `aeos-v2` source, not an earlier Emerick checkout. **A commit called a bug fix is not automatically a required or scientifically safe Aeos change.** The ledger covers all upstream-only history; runtime verification of ports remains future work.

The [h277/isolated run-impact follow-up](h277-isolated-impact.md) narrows these general priorities using actual parameters and outputs. It confirms the flux defect is reachable in both configurations, observes a stale hydrogen-fraction sentinel in newchem, and excludes generic formation and imposed-wind boundary fixes from the current individual-star/no-wind runs.

## First corrections to prepare

| Order | Upstream entry | Current Aeos evidence | Recommended decision |
| --- | --- | --- | --- |
| 1 | [#576: flux rollback](batch-12.md#commit-576) | `Grid_CorrectForRefinedFluxes.C:629–637` iterates `ffield` but subtracts `RightFluxes[field]` / `LeftFluxes[field]` | Category 3+2: fix the incorrect index in an isolated patch. Evaluate upstream's tracer-floor policy separately. |
| 2 | [#515: initialized hydrogen fraction](batch-11.md#commit-515) | `GrackleReadParameters.C:250` initializes chemistry but never copies the resulting fraction back into `CoolData` | Category 3: synchronize after successful initialization for each supported backend. |
| 3 | [#78](batch-02.md#commit-078), [duplicate #116](batch-03.md#commit-116): MassUnits type | `GrackleReadParameters.C:29` declares a `double*` argument but line 230 groups MassUnits with macro-dependent `float` | Category 3: keep MassUnits explicitly double. Current precision-64 aliases float to double, masking the mismatch; precision-32 exposes it. |
| 4 | [#42: missing metal field](batch-01.md#commit-042), [resolution #44](batch-01.md#commit-044) | `Grid_GrackleWrapper.C:159–164` silently disables a global cooling switch and assigns metal index zero | Category 3+2: fail explicitly for an invalid cooling/field configuration, preserving backend-specific contracts. |
| 5 | [#379: formation tracer scaling](batch-08.md#commit-379), superseding [#372](batch-08.md#commit-372) | `Grid_AddFeedbackSphere.C:901–927` overwrites gas density, then scales only two tracer channels with `factor` | Category 3+2: preserve each relevant abundance using the actual density ratio. Extend to Aeos elemental/source tracers, not just upstream's seven colors. Confirm this formation path is exercised by the selected stellar type. |
| 6 | [#434: external particle boundary](batch-09.md#commit-434) | `GalaxySimulationInitialize.C` builds constant exterior fluid boundaries without the corresponding particle boundary initializer | Category 3: initialize particle boundary state consistently. Direct patch check passes; check fresh start and restart. |

The #434 site is inside `GalaxySimulationRPSWind>0`. With the current isolated run's wind disabled, ordinary initialization already calls the particle-boundary initializer; this is not a missing boundary initialization in that run. Similarly, #379's generic formation feedback is bypassed by `INDIVIDUAL_STAR`. For #515, modern Grackle's undefined default also requires synchronization in non-equilibrium chemistry: the checked newchem disk saves `CoolData.HydrogenFractionByMass=-99999` while Grackle reports 0.76. The isolated IC uses a separate valid fraction, so the mismatch alone does not establish an evolved-disk abundance error.

These are source-level correctness recommendations. None establishes the magnitude of its effect on the previous isolated-disk comparison. For example, #78 may be invisible in the currently selected precision, and #379 is relevant only when that feedback path runs.

### Flux correction: split the two changes

The rollback loop should subtract the correction for each variable `ffield`; using the current failing variable `field` for every subtraction mixes unrelated gas/energy/tracer fluxes. This error is directly visible in current Aeos and is the strongest straightforward numerical repair in the final upstream history.

The same commit instead floors nonpositive non-gas density fields with `min_color = 1e-5*tiny_number`, retaining gas/momentum corrections. Aeos explicitly includes `FieldTypeIsSpeciesDensity` in its old rollback condition and carries many extra elemental fields. Replacing the condition verbatim can alter species handling and conservation. Review the field predicates, define what happens to each species/color family, and measure mass/species closure before adopting that policy. A clean result from an unrelated hydro test would not validate custom tracer handling.

### Grackle: preserve the Aeos compatibility profiles

[#571](batch-12.md#commit-571) introduces `GrackleFieldBuffer` to convert between Enzo baryon precision and `gr_float`. It affects chemistry evolution, cooling-time output, custom cooling-rate calls and radiation inputs. Current Aeos passes raw field pointers (`Grid_GrackleWrapper.C:237` and following). A mismatch can fail compilation; casts that conceal the mismatch can produce incorrect data interpretation. The correct response is a consistent conversion/copy-back contract, or an explicit supported-precision restriction, not pointer casting.

Port this independently of CMake. Preserve custom backend dispatch, radiation-field units, dust compatibility and legacy-LW compile guards. Verify that modified species/internal energy are copied back, temporary radiation conversions are reversed correctly, and an input-only conversion is not accidentally written over evolved state. The current local build override selects precision 64, 60 baryon fields, backend `newchem`, and legacy LW disabled; other profiles need their own validation.

[#514](batch-11.md#commit-514) restores a metal-density cap at 90% of gas density. This is a useful guard after Grackle removed its historical cap, but it does not repair a nonconservative enrichment update. `MetalPointer` can reference a persistent single metal field or a temporary sum of multiple fields. The same loop therefore has different persistent side effects in those cases. Define consistent behavior for total metals and elemental tracers before porting, and report any amount clipped. Do not use the cap to hide a mass-budget defect.

## Conditional repairs

| Upstream entries | Relevant configuration | Decision |
| --- | --- | --- |
| [#72](batch-02.md#commit-072), [#74](batch-02.md#commit-074) | `star_maker_ssn`, SINGLE_SUPERNOVA feedback | Adopt the already-limited momentum check and correct stencil count when that algorithm is used. Repair Boolean grouping in #74 rather than copy its OR/AND precedence. These are not automatically Aeos individual-star/artificial-SN paths. |
| [#230](batch-05.md#commit-230) | MagneticFieldResetter | Remove old magnetic energy for every reset/clear and add replacement energy consistently. Existing code updates energy only in one density/dual-energy branch; changing B without matching total energy changes inferred thermal energy. |
| [#165](batch-04.md#commit-165) | `UseHydro=0` with legacy hydro solvers | Extend the disable guard consistently; inspect both RK stages and custom evolution hooks. |
| [#79](batch-02.md#commit-079) | CollapseMHD3D initializer/output | Remove the unallocated DebugField entry. Does not affect other initializers. |
| [#371](batch-08.md#commit-371), [#374–376](batch-08.md#commit-374) | Enabling gravity/potential fields on restart | Adapt readers, parent/child gravity boundaries and field metadata together; exercise parallel ownership. |
| [#21–22](batch-01.md#commit-021) | ActiveParticle radiation sources | Use subsidiary-aware source deletion with TRANSFER guards. Aeos's ordinary star radiation cleanup is already repaired. |
| [#366](batch-08.md#commit-366) | C++11 diagnostics | Adapt string-literal/macro separation without changing format argument types. Do not rely on warning suppression in #566 as a repair. |

Bugs introduced and then repaired inside optional CR, libyt, PopIII-rotation or CGM development are marked category 3 **conditional on adopting those features**. They are not 116 missing defects in the currently configured Aeos disk.

## Changes that need a physical-model decision

### Galaxy/CGM initialization and external gravity

The [#210–229](batch-05.md#commit-210) import changes disk/halo initial conditions, equilibrium-chemistry setup, external gravity, mean molecular weight handling and star_maker2 selection/efficiency controls. It also contains accidental file copies subsequently reverted. Aeos has a different galaxy initializer, custom element/source fields and individual stellar feedback. Porting the whole PR would change the problem being simulated and discard custom behavior.

The [#345–358](batch-07.md#commit-345) follow-up restores force-balance helpers, reintroduces NFW/Burkert selection and repairs units/types. [#348](batch-07.md#commit-348) fixes a missing inverse-radius-squared factor in the **new upstream NFW expression**. Current Aeos's `Grid_ComputeAccelerationFieldExternal.C:431–437` instead uses a Burkert term with its own `1/r^2` already present. This upstream NFW defect is not evidence that the Aeos Burkert halo is missing that factor. [#351](batch-08.md#commit-351) fixes a cgs/code-radius mismatch in the new halo helper; apply only if that helper is adopted.

The [#504/#505](batch-11.md#commit-504) boundary changes repair internal-energy/species updates for galaxy inflows, but additionally set inflow metallicity to **0.1 solar** and prescribe ionization fractions. They also retain `if (BoundaryRank == 1)` for the x-velocity kinetic term, so x kinetic energy is omitted from that new sum in 2D/3D. Port the correctness principle, correct the component sum and preserve explicitly chosen Aeos composition; do not copy this pair as a purely mechanical fix. No inflow composition change is authorized by this review.

### Cooling, shielding and stellar radiation

- [#368/#369](batch-08.md#commit-368) add native `RadiationShield=3`, the WG/Haiman 2019 fit. This is an optional shielding model, not a Grackle change and not Emerick `LWbackground_model` support.
- [#521](batch-11.md#commit-521) changes native H2 Doppler mass from atomic H to molecular H2 and halves the uncapped column-length expression. The latter needs further derivation: the code sums one-sided negative density differences, not a central difference. Writing `min(L/2,Lmax)` differs from multiplying the final capped column by one half. For `L >= 2*Lmax`, upstream leaves the capped length unchanged. Check the `dom*H2I` mass-to-molecule convention, Sobolev estimator and maximum-length convention separately. The Doppler-mass correction is well motivated; the entire patch is not certified by its bug-fix title.
- [#333–343](batch-07.md#commit-333) add rotating/nonrotating PopIII photon models and a radiating-star fixture. These intentionally change stellar radiation and overlap custom Aeos photon bins/rates. The early test problem ID 251 is later changed to 252 to avoid the CR test collision.
- Neither the upstream Enzo history nor a successful merge determines the correctness of Emerick's Rémy-Ruyer dust normalization. Retain the separate dust/custom-physics review and backend decisions.

### Star formation and new transport methods

[#405–407](batch-09.md#commit-405) extend once-per-root-step formation and change which levels are eligible. This alters temporal sampling and relies on each star maker excluding covered cells. Retain Aeos cadence until a deliberate change and refinement/timestep convergence comparison are specified.

The CR series ([#82 onward](batch-02.md#commit-082)) adds anisotropic transport, streaming, pressure work/heating and feedback interfaces across common solver paths. Several intermediate energy definitions are reversed. The FDM series ([batch 4](batch-04.md)) changes wave damping, particle sampling and even replaces a point-source potential with a rotating tidal expression. These are optional physical/numerical models; evaluate final integrated behavior in dedicated problems before introducing them.

## Maintenance worth adopting as coherent projects

**Modern build system:** [#565–575](batch-12.md#commit-565) introduces CMake and removes the Make infrastructure. Upstream source lists do not register Aeos `IndividualStar*`/deterministic-event objects, and options do not implement `CONFIG_GRACKLE_BACKEND` or `CONFIG_GRACKLE_LEGACY_LW`. Upstream CMake's default 30 baryon fields also does not reproduce the current local 60-field override. Porting only the source lists or deleting Make configuration first would break this branch. Prepare source/option/dependency parity, then validate backend and precision combinations before retiring the old build path. Split source-level precision fixes out of the migration when useful.

**Tests and CI:** yt4 migration, test multiprocessing and toolchain improvements are advisable. Historical image/cache churn and temporary yt forks need not be replayed. Removing expensive tests or updating a gold-standard tag is a coverage/baseline decision, not evidence of improved physics. Retain legacy/main/newchem comparisons and explain changed answers.

**libyt:** most later history develops optional in-situ analysis. Final adapters include essential repairs for ghost zones, dimensions, units, data types and buffer lifetimes. Generate metadata mappings from Aeos declarations; upstream's generated file cannot represent all custom fields. Unsupported particle/vector attributes remain a consideration. [#548](batch-11.md#commit-548) constrains evolution timesteps to analysis times, so enabling time-cadenced analysis can change numerical evolution even when analysis only reads arrays. It is not automatically physics-neutral when enabled.

**Safe immediate maintenance:** the category-1 ordinary entries are documentation/template updates and small behavior-preserving cleanups with passing patch checks. Their presence in this category authorizes no automatic change of runtime parameter files.

## Rejected or already satisfied bug hypotheses

- [#34](batch-01.md#commit-034), titled HDF5 reference fix, does **not demonstrate a broken reference buffer** with the installed HDF5 1.8.23 header: `hdset_reg_ref_t` is already an unsigned-byte array (`H5Rpublic.h:105`). Wrapping it in `[1]` and changing `&reference` to `reference` preserves the initial buffer address/size through the void-pointer API. Category 1, not a confirmed missing bug.
- Radiation expiry and ordinary-star source-list cleanup are already present: [#17–20](batch-01.md#commit-017); #20 is the exact patch-ID match. Extracting a shared helper in #24 remains optional.
- The `j` particle-transfer index and zero-local-star guard in [#3](batch-01.md#commit-003) already exist, with different persistent-buffer handling. [#46](batch-01.md#commit-046)'s shrink/reset policy is not a demonstrated requirement for the current implementation.
- [#111](batch-03.md#commit-111)'s hydro pointer field count and [#144](batch-03.md#commit-144)'s numeric timing min/max return type already match current Aeos.
- [#408](batch-09.md#commit-408)'s suspicious factors of eight are already commented out in current Aeos `Grid_NestedCosmologySimulationInitializeGrid.C:1690–1699`. Searching text without reading the comment would incorrectly report an active cosmological mass bug.
- Reverse patch checks for deleted optional headers/initializers can pass simply because those files are absent. These are not additional incorporated physics fixes.

## Acceptance checks for future implementation

No new simulation tests were run for this report. Use small deterministic checks before the existing three-backend galaxy comparison:

| Proposed port | Minimum meaningful check |
| --- | --- |
| Flux rollback indexing | Force right-face sibling rollback with deliberately different density/energy/tracer fluxes; restore each variable by its own flux. |
| Tracer-floor policy | Independent positivity and total/elemental mass budgets across AMR boundaries, with multiple Aeos tracers and both rollback sides. |
| Grackle fraction/precision | Initialize all supported backends; assert Enzo/Grackle hydrogen fractions agree; evolve a small chemical state across matching and mismatching field precisions and compare energy/species/cooling time. |
| Missing-metal-field guard | Invalid metal-cooling configuration errors before solving; valid single/summed-metal configurations preserve behavior. |
| Formation tracer scaling | Change density by a known factor while carrying distinct positive abundances; each retained mass fraction remains unchanged, without cross-channel copying. |
| Particle/fluid boundaries | Fresh start and restart; particle escape behavior plus inflow energy closure for velocity on each axis, dual energy on/off, and species levels 0–3. |
| Magnetic reset | High/low density, initial nonzero B, repeated calls, dual energy on/off; preserve intended thermal energy and reset amplitude units. |
| Native H2 shielding | Analytical molecular number and Doppler width checks; test uncapped, transition and capped columns before selecting a model. |
| CMake/libyt | Compile profile/precision/MPI/TRANSFER matrix, custom object inclusion and field capacity; compare exported data with normal grid output; match timesteps in evolution comparisons. |

After focused tests pass, repeat deterministic artificial-SN comparisons with identical event files, physics parameters, backend tables, timesteps where appropriate and run endpoints. A fixed SN event file removes one source of stochastic mismatch; it does not make different numerical/physical models equivalent.
