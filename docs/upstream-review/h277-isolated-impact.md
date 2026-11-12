# Upstream commits that can affect h277 and the isolated dwarf

Reviewed 2026-10-31 against the frozen branches in [the upstream review](README.md). This follow-up filters the 577-commit review through the actual run parameters, build records, current Aeos callers, and selected saved outputs. It distinguishes an enabled code path from proof that a particular event occurred.

**The strongest missing numerical correction for both runs is `5ed618ce9a` (#576), specifically its flux-rollback index repair.** Its separate tracer-floor policy can also change both runs, but needs an explicit conservation/positivity decision. `b35de34341` (#515) addresses an observed newchem integration defect: Enzo retains an undefined hydrogen fraction while Grackle initializes it to 0.76. Most other upstream correctness fixes are already present or concern algorithms these runs do not use.

No source, executable, input parameter, table, running process, or branch was changed. No new galaxy evolution was run. The output checks below are read-only.

## Run configurations and provenance

“h277” means `/home/wispedia/AA/ufds/h277/run1`. “Isolated” includes the original run3 fiducial and the three deterministic comparisons; these have different dust choices and executable histories and must not be treated as one identical physics configuration.

| Setting | h277 | Isolated dwarf |
| --- | --- | --- |
| Inputs checked | `parameter_file.txt`, `DD0000/DD0000`, `DD0125/DD0125` | `runs/run3-fiducial/input.enzo`; the three `DD0011` restart inputs under the recorded login launch |
| Problem / coordinates | `ProblemType=30`, comoving | `ProblemType=31`, fixed physical coordinates |
| Hydro / cooling | PPM (`HydroMethod=0`), dual energy, `use_grackle=1` | Same |
| AMR flux correction | `FluxCorrection=2` | `FluxCorrection=2` |
| Chemistry / metal fields | `MultiSpecies=2`, `MultiMetals=2`, `MetalCooling=1` | Same |
| Formation / feedback bits | `32768 / 32768`: `INDIVIDUAL_STAR` | Same |
| Once per root-step formation | `StarFormationOncePerRootGridTimeStep=0` | Same |
| Gas boundaries | Periodic | Outflow |
| Particle boundary | Periodic (`ParticleBoundaryType=3`) | Also periodic in the saved inputs; gas outflow does not select particle outflow |
| Imposed galaxy wind | `GalaxySimulationRPSWind=0` | `GalaxySimulationRPSWind=0` |
| Gravity | Self-gravity, cosmological DM; `PartitionNestedGrids=1` | Self-gravity plus analytic Burkert halo |
| Other gates | `UseHydro=1`, `ResetMagneticField=0`, `CRModel=0` | Same |
| Stellar radiation | `PopIIIRadiationModel=1`, custom Aeos individual-star radiation | Same retained model |
| Build precision | Enzo and legacy Grackle both 64 | Recorded comparison builds and Grackle libraries: 64 |

The saved h277 build records, including `DD0000.configure` and `DD0125.configure`, identify Aeos revision `b1b85185e64873c1b1b83d23fbed03b4043b866a`. The current review baseline is `0dbaa4beae8f1e411a6dd99680b9650d5960791b`. Their `Grid_CorrectForRefinedFluxes.C` and `StarParticleFinalize.C` have identical Git content, so the relevant flux defect and individual-star dispatch are also present at the recorded h277 revision. Build records alone do not prove that a binary contained no uncommitted edits.

The deterministic continuation was inspected at:

`/home/wispedia/AA/isolated/runs/deterministic-150Myr/login-20261031-023139-1239130/`

Its launcher resumes each case from 5 Myr with `StopTime=150`, using 16 ranks per case. Its newchem build record names `aeos-v2` but revision `72ee732...`, predating the commits that recorded the compatibility work; therefore the saved build revision alone is not a complete source manifest. The saved runtime parameters and Grackle output are direct evidence of the settings actually used.

## Changes with a reachable effect

| Upstream commit | h277 with legacy Grackle | Isolated with legacy Grackle | Isolated / future h277 with main or newchem | Decision |
| --- | --- | --- | --- | --- |
| [#576 `5ed618ce9a`](batch-12.md#commit-576), rollback index | Enabled path; effect if right-face sibling rollback occurs | Same | Same | Highest-priority numerical repair; measure event frequency and conservation |
| Same commit, tracer flooring | Changes treatment of nonpositive species/colors if encountered | Same | Same | Separate model/numerical-policy decision; do not bundle with the index repair |
| [#515 `b35de34341`](batch-11.md#commit-515), initialized hydrogen fraction | Saved Enzo and Grackle values already agree at 0.76 | Legacy values agree | **Observed Enzo/Grackle mismatch in newchem**; fresh cosmological initialization directly consumes the stale Enzo value | Repair synchronization; distinguish metadata consistency from demonstrated disk evolution changes |
| [#514 `439fa3eb6f`](batch-11.md#commit-514), metal-density cap | Legacy library already caps its supplied metal array | Same | Missing wrapper cap can change chemistry and persistent metal density if `rho_Z/rho > 0.9` | Conditional; no such cells in checked endpoint outputs; do not use clipping to conceal an enrichment defect |
| [#42 `0f89eb892d`](batch-01.md#commit-042), plus [resolution #44](batch-01.md#commit-044) | Valid metal fields are present | Same | Same | Fail-fast protection for an invalid configuration; no intended change to these valid runs |

### 1. Flux rollback: a direct numerical error

`src/enzo/Grid_CorrectForRefinedFluxes.C:629–640` loops over the previously corrected fields as `ffield` but subtracts the failing field's flux using `field`:

```cpp
BaryonField[ffield][FieldIndex + Offset]
  -= (InitialFluxes->RightFluxes[field][dim][FluxIndex]
      - RefinedFluxes->LeftFluxes[field][dim][RefinedFluxIndex]);
```

Both flux-array indices must be `ffield`. With distinct corrections of 0.2 and 0.01 for two fields, the old loop subtracts 0.01 from both when the second field fails, leaving an unwanted 0.19 correction in the first field. This is an algebraic illustration of the error, not a measured error in a galaxy cell.

The trigger requires Cartesian AMR correction at a sibling interface, on its right side, with a corrected density-like quantity becoming nonpositive. Both runs enable the relevant correction and have many chemical and elemental tracers. Gas density, chemical composition, metal transport, and subsequent cooling/feedback can therefore diverge after the trigger. With radiative cooling enabled, this routine excludes total/internal energy from direct flux correction; an energy change in these runs would be downstream, rather than evidence that the loop directly corrected their energy fields.

The same upstream commit also replaces whole-cell rollback on nonpositive color densities with an individual tiny floor. That can retain gas and momentum corrections which Aeos currently discards. It can alter metal conservation and species ratios even if the incorrect-index branch never runs. Preserve Aeos's full species/element/source-field definitions when evaluating it.

**Established:** the defect is present and the configuration allows it. **Not established:** how many times it occurred, the resulting mass error, or its effect on either star-formation history. Existing logs are not an event counter. Do not claim that every h277 result is wrong, or that a correction is guaranteed to produce a large change.

### 2. Hydrogen fraction: observed newchem inconsistency

`GrackleReadParameters.C:85` copies Grackle's *default* hydrogen fraction into `CoolData`; line 202 sends it back before initialization. `initialize_chemistry_data` is called at line 250, and the initialized value is never copied back.

Modern main/newchem initially use a negative sentinel. For `primordial_chemistry=2`, initialization replaces an unspecified negative value with 0.76. This defect is therefore **not limited to fully tabulated chemistry** (`MultiSpecies=0`).

| Saved case | Enzo restart `HydrogenFractionByMass` | Grackle `HydrogenFractionByMass` |
| --- | ---: | ---: |
| h277, DD0000 and DD0125 | 0.76 | 0.76 in the run's `GRACKLE_INFO` |
| Isolated emerick, 5 Myr restart | 0.76 | 0.76 |
| Isolated emerick-standard, 5 Myr restart | 0.76 | 0.76 |
| Isolated newchem, initial DD0000 and 5 Myr restart | **−99999** | **0.76** |
| Isolated newchem, final DD0301 at 150 Myr | **−99999** | **0.76** |

The initial newchem DD0000 evidence is in `grackle-compatibility/deterministic-comparison/newchem/DD0000/DD0000`; the 5–150 Myr evidence is in the login continuation. The stale value survives through the saved endpoint.

For a **fresh h277-style initialization with modern Grackle**, `Grid_NestedCosmologySimulationInitializeGrid.C:651–676` uses `CoolData.HydrogenFractionByMass` to construct H/He species. This gives a direct route from the sentinel to invalid initial species if the input does not explicitly supply a valid fraction. Grackle initialization precedes the problem initializer through `ReadParameterFile`, so the upstream copy-back fixes that route. The recorded legacy h277 uses a valid fraction and is not evidence of this failure.

For the **current isolated initializer**, `Grid_GalaxySimulationInitializeGrid.C:423` uses `TestProblemData.HydrogenFractionByMass`, whose default is 0.76, independently of the stale `CoolData` member. Chemistry evolution and cooling-time calculation use Grackle's initialized data, and individual-star feedback bypasses the generic feedback routine that reads `CoolData`. Thus the observed mismatch does **not** establish that the current disk's evolved H/He abundance or SN energetics used −99999. Correct it for interface consistency, restart metadata/analysis, and other consumers; do not attribute the existing disk differences to this defect without a before/after calculation.

An explicitly specified valid `HydrogenFractionByMass` avoids the sentinel for non-equilibrium chemistry, but the durable repair is the post-initialization synchronization in #515.

### 3. Metal cap: backend difference, conditional exposure

Current Aeos has no wrapper-level cap. The inspected legacy Grackle implements `metal = min(max(metal,tiny),0.9*d)` in `solve_rate_cool_g.F:1038–1039`. Main/newchem no longer supply that legacy guard; #514 restores the upper cap in Enzo.

The checked h277 and isolated hierarchy field lists contain `Metallicity` (type 20), with no `SNColour` (type 19). In those grids, Aeos passes the persistent metal-density array rather than a scratch sum. Applying a wrapper cap can therefore change stored metals as well as the cooling input. Cases that use a scratch sum need a separately defined conservation policy.

Read-only endpoint screening is recorded in [run-impact-evidence.json](run-impact-evidence.json). It reads gas and total metal density in every stored grid at the listed outputs, including covered coarse cells; it does not compute composite AMR masses. Endpoint absence cannot rule out an earlier transient, and legacy output may already have been clipped inside Grackle.

| Isolated case / last stored output checked | Time [Myr] | Maximum `rho_Z/rho` | Stored cells above 0.9 |
| --- | ---: | ---: | ---: |
| newchem DD0301 | 150 | 0.0005484461 | 0 |
| emerick DD0199 | 99.000001 | 0.001276882 | 0 |
| emerick-standard DD0194 | 96.500045 | 0.0008337220 | 0 |

These outputs have different times; this is a threshold-exposure check, not a matched-time backend comparison. A target of 150 Myr does not establish that every case reached it.

The h277 DD0125 screening covers all **3,030 stored grids / 83,635,640 stored active cells**, including covered coarse cells. At `z=8.4507494`, the maximum `rho_Z/rho` is **0.35117045**, with **zero** stored cells above 0.9 and no nonpositive gas densities or nonfinite ratios. This also gives no endpoint evidence for an active upper-cap correction, subject to the same historical-clipping limitation. The isolated outputs are fixed snapshots selected during this review, not a declaration that the other jobs had finished.

## Important fixes that do not currently change these runs

| Upstream change | Why it is not an active result change here |
| --- | --- |
| [#372 `00300b2be3`](batch-08.md#commit-372), superseded by [#379 `a94592e941`](batch-08.md#commit-379): metal scaling after formation | They repair the **generic** `Grid_AddFeedbackSphere` `FORMATION` branch. `StarParticleFinalize.C:103–119` dispatches these runs to `IndividualStarParticleAddFeedback` instead. Individual-star gas removal is another implementation. This fix does not establish correctness of that custom implementation. |
| [#72 `ea4ba316f8`](batch-02.md#commit-072), [#74 `59f0e6d7f2`](batch-02.md#commit-074): single-SN momentum/stencil | `SINGLE_SUPERNOVA` / `star_maker_ssn` is a different bit and algorithm from `INDIVIDUAL_STAR`. The deterministic artificial-SN driver also has a separate injection path. |
| [#434 `54193b832c`](batch-09.md#commit-434): galaxy particle boundaries | The missing call is **inside `GalaxySimulationRPSWind>0`**. The isolated inputs set this to zero, so `InitializeNew.C:789–847` prepares ordinary boundaries and already initializes the particle boundary. h277 does not use the galaxy initializer. |
| [#504 `da37013eb7`](batch-11.md#commit-504), [#505 `27e25c6a7f`](batch-11.md#commit-505): galaxy inflow energy/species | `SetGalaxySimulationBoundary` returns immediately when `GalaxySimulationRPSWind=0`. These changes do not repair ordinary outflow boundaries. They also prescribe a new inflow composition and retain an incomplete kinetic-energy sum, so are not safe wholesale fixes. |
| [#521 `becf37fd73`](batch-11.md#commit-521): native H₂ shielding | Both runs return from `Grid_MultiSpeciesHandler.C:34–40` after `GrackleWrapper`, bypassing the native solver. Grackle shielding requires its own review. |
| [#368 `5553977401`](batch-08.md#commit-368), [#369](batch-08.md#commit-369): native WG2019 shielding | Same dispatch exclusion; also an explicit new shielding option. Does not implement Emerick LW backgrounds in Grackle. |
| [#78 `92122b8491`](batch-02.md#commit-078), duplicate [#116 `b83339118a`](batch-03.md#commit-116): MassUnits type | Current recorded Enzo precision is 64, where `float` is macro-mapped to `double`; the mismatch is masked. Still worth fixing before supporting precision 32. |
| [#571 `6c6472dd76`](batch-12.md#commit-571): Grackle field conversion | Required for differing Enzo/Grackle field widths. These recorded builds match at 64. Its zero-copy matching-width path is not a new physical model. Preserve Aeos radiation/backends when porting. |
| [#165 `9c3eacf476`](batch-04.md#commit-165): `UseHydro` guard | Both runs set `UseHydro=1`. |
| [#230 `df16c63f64`](batch-05.md#commit-230): magnetic reset energy | `ResetMagneticField=0` and these are PPM hydro configurations. |
| [#371](batch-08.md#commit-371), [#374–376](batch-08.md#commit-374): enabling gravity/potential on restart | Self-gravity is enabled from startup. h277's `WritePotential=1` is also already enabled at DD0000, rather than newly added on restart. These commits matter if changing those controls across a restart. |
| [#405 `8357505ade`](batch-09.md#commit-405), [#406](batch-09.md#commit-406), [#407 `00a59a5d13`](batch-09.md#commit-407): root-step SF cadence | Their modified scheduling gates are `NORMAL_STAR`/`H2REG_STAR`; the runs use `INDIVIDUAL_STAR`, with root-step formation disabled. Do not extend them to Aeos without choosing a new sampling/timing model. |
| [#58–68](batch-02.md#commit-058): hydrostatic boundary development | These runs select periodic or outflow boundaries, not the new hydrostatic type. The final signature repair is already reflected in Aeos. |
| CR development, including [#97 `173712dd87`](batch-02.md#commit-097) | `CRModel=0`; comoving coordinates alone do not enable cosmic-ray expansion terms. |
| ActiveParticle radiation cleanup [#21–22](batch-01.md#commit-021) | Ordinary individual-star particles use another radiation-source path. The checked hierarchies report zero ActiveParticles. |
| FDM, CollapseMHD3D and stochastic-forcing test fixes | Different problem/solver/forcing paths; h277's nested cosmological initializer is not FDM particle sampling. |
| libyt development and timestep cap [#548 `cd68440e20`](batch-11.md#commit-548) | libyt is absent from these recorded builds. Adding timed libyt analysis later can alter integration timesteps and therefore results. |

### Cosmological particle masses: already repaired in the actual h277 path

[#408 `d13f0bb3a2`](batch-09.md#commit-408) removes the factor-of-eight heuristic from **`Grid_NestedCosmologySimulationInitializeGrid.C`**. Aeos already encloses those multipliers in a block comment at lines 1690–1699, including at the saved h277 source revision.

This distinction matters: `Grid_CosmologySimulationInitializeGrid.C` still contains active multipliers. h277 sets `PartitionNestedGrids=1`, so `InitializeNew.C:511–516` selects the **nested** initializer. The active text in the other initializer is not evidence that h277 used the multiplier. No new h277 mass change follows from applying #408's already-effective repair. Restarting also reads stored particle masses rather than reconstructing the original IC masses.

Ordinary-star radiation deletion [#17–20](batch-01.md#commit-017), the particle-gather safeguards in [#3](batch-01.md#commit-003), the old-hydro pointer initialization [#111](batch-03.md#commit-111), and numeric timing returns [#144](batch-03.md#commit-144) already have corresponding implementations in Aeos. Missing commit ancestry does not make them missing fixes. [#34](batch-01.md#commit-034)'s HDF5-reference rewrite does not demonstrate a scientific-data error in the existing array buffer.

## Changes that would intentionally define a different experiment

| Commit family | h277 | Isolated dwarf |
| --- | --- | --- |
| [#210–229](batch-05.md#commit-210), [#345–358](batch-07.md#commit-345): galaxy/CGM initialization and potentials | Galaxy initializer and analytic disk potential are unused | Replacing Aeos's initializer can change disk/ambient structure, chemistry/temperature setup, rotation, and gravity. Add a distinct mode if desired; do not call it a numerical correction to the same ICs. The upstream NFW inverse-square repair is not a missing inverse-square term in Aeos's existing Burkert force. |
| [#214 `e9d7589c4c`](batch-05.md#commit-214): Hopkins-style star_maker2 criteria | Different star maker | Different star maker; porting the criteria into individual-star formation would change the SF model |
| [#333–343](batch-07.md#commit-333): rotating/nonrotating PopIII radiation | Potentially significant if deliberately integrated into Aeos PopIII radiation | Conditional on forming PopIII stars; not required to run an enriched disk |
| [#565–575](batch-12.md#commit-565): CMake migration and compatibility | Build parity required | Build parity required |

The new upstream PopIII option is not a correction to the selected Aeos `PopIIIRadiationModel=1` Heger/Woosley fits. It uses a different stellar-type/model interface. Likewise, a CMake migration must preserve individual-star source files, deterministic artificial-SN objects, backend/LW controls, 60-field capacity, precision and numerical flags. A build that omits those features does not reproduce these experiments.

The reviewed Enzo commits do not by themselves fix or validate the separate Rémy-Ruyer dust prescription, Grackle cooling algorithms, or table LW rates. Changing Grackle backends remains a separate physics/numerics comparison.

## Recommended order and remaining evidence

1. Prepare the **index-only** #576 correction and a forced right-face sibling-rollback regression with distinct fluxes for gas and multiple tracers. Count rollback events and mass/species changes in short h277 and deterministic-disk segments.
2. Synchronize initialized hydrogen fraction using #515, with checks for legacy/main/newchem and both fresh starts and restarts. Verify a fresh nested cosmological IC and the independent isolated initializer; quantify the disk difference rather than presuming one.
3. Evaluate #576's tracer-floor policy in a separate patch with metal/element/charge conservation diagnostics. Identical SN event files do not control the resulting SF stochastic sequence once hydrodynamics diverges.
4. Keep #514 and the missing-metal-field guard as explicit interface/robustness work. Check pre-solver states and enrichment closure before interpreting a metal cap as a repair to physical metal production.
5. Keep the dormant fixes available for their triggering configurations. Native shielding, galaxy winds/CGM, rotating spectra, root-step SF and build migration each need separate scope and validation.

The independent [custom-physics audit](../physics-review.md) still matters: the SNIa lifetime convention, interpolation endpoints, and PopIII ejecta contract are in custom Aeos routines that these upstream patches do not repair. Both configurations enable SNIa model 2 and retain PopIII formation machinery; individual event exposure and the effect on each result still need measurement. This report identifies upstream adoption impact, not a clean bill of health for the remaining custom physics.
