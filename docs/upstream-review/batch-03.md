# Batch 03: commits 101–150

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-101"></a>
## 101 — `1e82e557f` — 2019-12-10

removing test-specific hard coding

**Categories:** 3.

Removes a hard-coded velocity reset for CR test problem 251. Necessary cleanup if the intermediate CR solver is ported; current disk does not select that problem.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`.

**Patch locations:** `@@ -246,13 +246,6 @@ int grid::UpdateMHDPrim(float **dU, float c1, float c2)`.

<a id="commit-102"></a>
## 102 — `cc4a1766a` — 2019-12-10

removing thermal instability from this branch

**Categories:** 4.

Deletes test inputs for the withdrawn ThermalInstability feature. Reverse check means those files happen to exist in Aeos; deletion is not automatically desirable for the fork.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/Hydro/Hydro-3D/ThermalInstability/ThermalInstability.enzo`, `run/Hydro/Hydro-3D/ThermalInstability/white_noise_generator.py`.

**Patch locations:** `@@ -1,84 +0,0 @@`; `@@ -1,86 +0,0 @@`.

<a id="commit-103"></a>
## 103 — `6cd89cc09` — 2019-12-10

fixing definition of StreamingStabilityFactor in documentation

**Categories:** 4.

Documents the final relative streaming regularization scale and removes stale timestep calculation. Requires final CR model and recalibration, not blind reuse of old parameter values.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`.

**Patch locations:** `@@ -3396,8 +3396,8 @@ For details on the cosmic ray solver in Enzo see :ref:cosmic_rays.`; `@@ -72,7 +72,6 @@ int grid::ComputeCRStreamingTimeStep (float &dt) {`.

<a id="commit-104"></a>
## 104 — `293d0595b` — 2019-12-10

removing minor changes that are irrelevant

**Categories:** 4.

Removes unrelated CR development edits, including experimental AGORA CR setup, and restores solver field counts/indices for dual-energy choices. Use final integrated CR diff; do not replay experimental changes individually.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/CosmologySimulationInitialize.C`, `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`, `src/enzo/ProblemType_AgoraRestart.C`, `src/enzo/ReadParameterFile.C`.

**Files:** `src/enzo/CosmologySimulationInitialize.C`, `src/enzo/Grid_ComputePressure.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_ConductHeat.C`, `src/enzo/Grid_CopyZonesFromGrid.C`, `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`, `src/enzo/Grid_RestoreEnergyConsistency.C`, `src/enzo/Grid_SolveRadiativeCooling.C`, `src/enzo/Grid_SolveRateAndCoolEquations.C`, `src/enzo/ProblemType_AgoraRestart.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/hydro_rk/Grid_MHD3DTestInitializeGrid.C`.

**Patch locations:** `@@ -729,7 +729,7 @@ int CosmologySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -127,7 +127,6 @@ int grid::ComputePressure(FLOAT time, float *pressure,`; `@@ -142,7 +141,6 @@ int grid::ComputePressure(FLOAT time, float *pressure,`; `@@ -446,6 +446,8 @@ float grid::ComputeTimeStep()`; `@@ -114,7 +114,6 @@ int grid::ConductHeat(){`; additional hunks in the same patch.

<a id="commit-105"></a>
## 105 — `793d72216` — 2020-01-07

Merge https://github.com/enzo-project/enzo-dev into cosmic_rays

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** none; incoming history is already in the Aeos ancestry.

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/pop3_maker.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/pop3_maker.F`, `src/enzo/typedefs.h`.

<a id="commit-106"></a>
## 106 — `3a1965f2d` — 2020-06-22

Merge https://github.com/enzo-project/enzo-dev into cosmic_rays

**Categories:** 1,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#001](batch-01.md#commit-001), [#002](batch-01.md#commit-002), [#003](batch-01.md#commit-003), [#004](batch-01.md#commit-004), [#005](batch-01.md#commit-005), [#006](batch-01.md#commit-006), [#007](batch-01.md#commit-007), [#008](batch-01.md#commit-008), [#009](batch-01.md#commit-009), [#010](batch-01.md#commit-010), [#011](batch-01.md#commit-011), [#012](batch-01.md#commit-012), [#013](batch-01.md#commit-013), [#014](batch-01.md#commit-014), [#015](batch-01.md#commit-015), [#016](batch-01.md#commit-016).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/CommunicationCollectParticles.C`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_CollectStars.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_TransferSubgridStars.C`, `src/enzo/Make.config.objects`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/Star.h`, `src/enzo/StarParticleFindAll.C`, `src/enzo/StarRoutines.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/macros_and_parameters.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `README.md`, `doc/manual/Makefile`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/user_guide/RunTestProblem.rst`, `doc/manual/source/user_guide/SampleParameterFiles.rst`, `doc/manual/source/user_guide/index.rst`, `doc/manual/source/user_guide/samples/SG64-L2.conf`, `doc/manual/source/user_guide/samples/wise2014_zoomin_update.enzo`, `src/enzo/CommunicationCollectParticles.C`, `src/enzo/CommunicationTransferSubgridParticles.C`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_CollectStars.C`, `src/enzo/Grid_CommunicationSendStars.C`, `src/enzo/Grid_CommunicationTransferStarsOpt.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/Grid_TransferSubgridStars.C`, `src/enzo/Grid_ZeusSolver.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.sdsc-comet`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/Star.h`, `src/enzo/StarParticleFindAll.C`, `src/enzo/StarRoutines.C`, `src/enzo/StochasticForcing_Init.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/macros_and_parameters.h`.

<a id="commit-107"></a>
## 107 — `c7407db37` — 2020-08-06

Merge branch 'master' into cosmic_rays

**Categories:** 1,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#017](batch-01.md#commit-017), [#018](batch-01.md#commit-018), [#019](batch-01.md#commit-019), [#020](batch-01.md#commit-020), [#021](batch-01.md#commit-021), [#022](batch-01.md#commit-022), [#023](batch-01.md#commit-023), [#024](batch-01.md#commit-024), [#025](batch-01.md#commit-025).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolvePhotons.C`, `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/ActiveParticleInitialize.C`, `src/enzo/DeleteRadiationSource.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/StarParticleRadTransfer.C`.

<a id="commit-108"></a>
## 108 — `a1aacc7dd` — 2020-08-06

Fixing documentation and minor optimization for PR

**Categories:** 4.

CR documentation and common inverse-sqrt optimization; renames the cosmological CR field index to avoid collision with solver iCR. Also removes a personal machine file. Keep optional model adoption separate from this cleanup.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/ReadParameterFile.C`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Make.mach.CCA-hardy`, `src/enzo/ReadParameterFile.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`.

**Patch locations:** `@@ -3386,8 +3386,8 @@ For details on the cosmic ray solver in Enzo see :ref:cosmic_rays.`; `@@ -3397,11 +3397,11 @@ For details on the cosmic ray solver in Enzo see :ref:cosmic_rays.`; `@@ -10,7 +10,7 @@ Bryan 2014 <http://adsabs.harvard.edu/abs/2014MNRAS.437.3312S>_ .`; `@@ -23,15 +23,15 @@ star formation. See :ref:cosmic_ray_two_fluid_model_parameters for information`; `@@ -5,6 +5,7 @@`; additional hunks in the same patch.

<a id="commit-109"></a>
## 109 — `8f196da92` — 2021-09-14

Applying minor suggestions/typo fixes from review

**Categories:** 3.

Fixes the newly introduced CR shock-tube CenterBy parameter typo; accompanying wording/debug corrections. Conditional on porting that initializer.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`.

**Patch locations:** `@@ -3399,8 +3399,8 @@ For details on the cosmic ray solver in Enzo see :ref:cosmic_rays.`; `@@ -121,7 +121,7 @@ int CRShockTubesInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -107,7 +107,7 @@ int CRTransportTestInitialize(FILE *fptr, FILE *Outfptr,`.

<a id="commit-110"></a>
## 110 — `41ec16085` — 2022-03-16

Add suggested comment

**Categories:** 4.

Comment explains that super-Alfvenic streaming factor does not multiply gas heating; no executable change and requires new CR source block.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`.

**Patch locations:** `@@ -146,6 +146,7 @@ int grid::MHDSourceTerms(float **dU, float min_coeff)`.

<a id="commit-111"></a>
## 111 — `23f932f52` — 2022-04-15

Restored incorrectly deleted line

**Categories:** 3.

Restores hydro field count initialization in ReturnOldHydroRKPointers. Reverse check succeeds: already present in Aeos.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`.

**Patch locations:** `@@ -44,6 +44,7 @@ int grid::ReturnOldHydroRKPointers(float **Prim, bool ReturnMassFractions)`.

<a id="commit-112"></a>
## 112 — `bba4a17a1` — 2022-04-15

Added suggested if statement

**Categories:** 3.

Guards CR internal-energy source updates with DualEnergyFormalism to avoid touching an absent energy component. Required if adopting new CR heating support.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`.

**Patch locations:** `@@ -151,7 +151,8 @@ int grid::MHDSourceTerms(float **dU, float min_coeff)`.

<a id="commit-113"></a>
## 113 — `5ae4d9b6f` — 2022-04-27

Push test suite (sans Hypre tests) passes

**Categories:** 4.

Reverts the temporary named-energy-index changes in uniform initialization to upstream field-order assumptions. Not an independent science improvement; prefer preserving Aeos field layout.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_InitializeUniformGrid.C`.

**Files:** `src/enzo/Grid_InitializeUniformGrid.C`.

**Patch locations:** `@@ -34,7 +34,7 @@ int grid::InitializeUniformGrid(float UniformDensity,`; `@@ -47,15 +47,15 @@ int grid::InitializeUniformGrid(float UniformDensity,`; `@@ -193,7 +193,7 @@ int grid::InitializeUniformGrid(float UniformDensity,`; `@@ -207,17 +207,16 @@ int grid::InitializeUniformGrid(float UniformDensity,`.

<a id="commit-114"></a>
## 114 — `aceb1cf1d` — 2022-04-27

Merge pull request #132 from ibutsky/cosmic_rays

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/star_maker2.F`.

<a id="commit-115"></a>
## 115 — `c84aec8e9` — 2022-06-29

Merge remote-tracking branch 'main/main' into fix_StarParticleFindAll

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#047](batch-01.md#commit-047), [#048](batch-01.md#commit-048), [#049](batch-01.md#commit-049), [#050](batch-01.md#commit-050), [#051](batch-02.md#commit-051), [#052](batch-02.md#commit-052), [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056), [#057](batch-02.md#commit-057), [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068), [#069](batch-02.md#commit-069), [#070](batch-02.md#commit-070), [#071](batch-02.md#commit-071), [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074), [#075](batch-02.md#commit-075), [#076](batch-02.md#commit-076), [#077](batch-02.md#commit-077), [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079), [#080](batch-02.md#commit-080), [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`, `run/test_runner.py`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.tigercpu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/lcaperf.h`, `src/enzo/star_maker2.F`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

<a id="commit-116"></a>
## 116 — `b83339118` — 2020-07-09

Fixing mixed precision issues

**Categories:** 3.

Same mixed-precision MassUnits correction as #78 on another history path; incorporate once only. Clean patch applies.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`.

**Files:** `src/enzo/GrackleReadParameters.C`.

**Patch locations:** `@@ -218,7 +218,8 @@ int GrackleReadParameters(FILE *fptr, FLOAT InitTime)`.

<a id="commit-117"></a>
## 117 — `ec054a0ef` — 2021-01-02

Merge branch 'master' of https://github.com/enzo-project/enzo-dev into main

**Categories:** 1,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#010](batch-01.md#commit-010), [#011](batch-01.md#commit-011), [#012](batch-01.md#commit-012), [#013](batch-01.md#commit-013), [#014](batch-01.md#commit-014), [#015](batch-01.md#commit-015), [#016](batch-01.md#commit-016), [#017](batch-01.md#commit-017), [#018](batch-01.md#commit-018), [#019](batch-01.md#commit-019), [#020](batch-01.md#commit-020), [#021](batch-01.md#commit-021), [#022](batch-01.md#commit-022), [#023](batch-01.md#commit-023), [#024](batch-01.md#commit-024), [#025](batch-01.md#commit-025), [#026](batch-01.md#commit-026), [#027](batch-01.md#commit-027), [#028](batch-01.md#commit-028), [#029](batch-01.md#commit-029), [#030](batch-01.md#commit-030).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolvePhotons.C`, `src/enzo/StarParticleRadTransfer.C`.

**Files:** `.circleci/config.yml`, `.gitignore`, `doc/manual/Makefile`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/reference/NestedGridParticles.rst`, `doc/manual/source/supplementary_info/EmbeddedPython.rst`, `doc/manual/source/user_guide/RunTestProblem.rst`, `doc/manual/source/user_guide/SampleParameterFiles.rst`, `doc/manual/source/user_guide/index.rst`, `doc/manual/source/user_guide/samples/SG64-L2.conf`, `doc/manual/source/user_guide/samples/wise2014_zoomin_update.enzo`, `src/enzo/ActiveParticleInitialize.C`, `src/enzo/DeleteRadiationSource.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/StochasticForcing_Init.C`, `src/enzo/python_bridge/problemtype_handler.pyx`.

<a id="commit-118"></a>
## 118 — `3c2dcd0b3` — 2021-02-26

Merge remote-tracking branch 'main/master' into main

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#034](batch-01.md#commit-034), [#035](batch-01.md#commit-035).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_CreateParticleTypeGrouping.C`.

<a id="commit-119"></a>
## 119 — `8b84c0f4a` — 2021-04-14

Merge remote-tracking branch 'main/master' into main

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#031](batch-01.md#commit-031), [#032](batch-01.md#commit-032), [#033](batch-01.md#commit-033), [#036](batch-01.md#commit-036), [#037](batch-01.md#commit-037), [#038](batch-01.md#commit-038), [#039](batch-01.md#commit-039), [#040](batch-01.md#commit-040), [#041](batch-01.md#commit-041), [#042](batch-01.md#commit-042), [#043](batch-01.md#commit-043), [#044](batch-01.md#commit-044), [#045](batch-01.md#commit-045).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `.circleci/config.yml`, `src/enzo/Grid_CalculateSmartStarAccretionRate.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/uuid.C`.

<a id="commit-120"></a>
## 120 — `361808a2b` — 2022-02-18

Merge remote-tracking branch 'main/main' into main

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#047](batch-01.md#commit-047), [#048](batch-01.md#commit-048), [#049](batch-01.md#commit-049), [#050](batch-01.md#commit-050), [#051](batch-02.md#commit-051), [#052](batch-02.md#commit-052).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/test_runner.py`.

<a id="commit-121"></a>
## 121 — `9ca1d6e22` — 2022-06-09

Merge remote-tracking branch 'main/main' into main

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056), [#057](batch-02.md#commit-057), [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068), [#069](batch-02.md#commit-069), [#070](batch-02.md#commit-070), [#071](batch-02.md#commit-071), [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074), [#075](batch-02.md#commit-075), [#076](batch-02.md#commit-076), [#077](batch-02.md#commit-077), [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079), [#080](batch-02.md#commit-080), [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.tigercpu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/lcaperf.h`, `src/enzo/star_maker2.F`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

<a id="commit-122"></a>
## 122 — `398c5d6fd` — 2022-07-01

Several changes to make the test suite compatible with yt-4.x

**Categories:** 4.

Begins yt4 answer-test migration: typed fields, new dataset API, CI dependencies and runner. Adopt as coherent tooling update; source evolution physics unaffected.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

**Patch locations:** `@@ -30,8 +30,7 @@ commands:`; `@@ -108,7 +107,7 @@ commands:`; `@@ -135,7 +134,7 @@ commands:`; `@@ -151,19 +150,19 @@ commands:`; `@@ -180,6 +179,7 @@ jobs:`; additional hunks in the same patch.

<a id="commit-123"></a>
## 123 — `6a8f3f4b4` — 2022-07-01

Updating to first gold standard with yt-4.x

**Categories:** 4.

Rebaselines CI answer data for the yt4 transition; require provenance of answer changes rather than treating a gold-standard update as a physics validation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -205,16 +205,16 @@ jobs:`.

<a id="commit-124"></a>
## 124 — `0923b43e1` — 2022-07-01

More changes for yt-4.x comptability

**Categories:** 4.

Updates yt field/dataset access across cosmological and hydro tests; also fixes a 1D pancake input dimension list. Test fixtures only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

**Patch locations:** `@@ -29,7 +29,7 @@ def test_standard():`; `@@ -6,7 +6,7 @@`; `@@ -29,7 +29,7 @@ def test_almost_standard():`; `@@ -3,8 +3,7 @@ import yt`; `@@ -3,8 +3,7 @@ import yt`; additional hunks in the same patch.

<a id="commit-125"></a>
## 125 — `6e9b961ca` — 2022-07-01

More yt-4.x fixes

**Categories:** 4.

Updates yt halo catalogs, particle field names and data containers. Required companion for the test-toolchain migration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

**Patch locations:** `@@ -29,7 +29,7 @@ def test_hmf():`; `@@ -68,12 +68,12 @@ def test_max_density_halo_quantities():`; `@@ -114,7 +114,7 @@ def test_dark_matter_mass():`; `@@ -144,8 +144,8 @@ def test_individual_baryon_mass():`; `@@ -175,8 +175,8 @@ def test_total_baryon_mass():`; additional hunks in the same patch.

<a id="commit-126"></a>
## 126 — `7d017a747` — 2022-07-02

Fixing more field name tuples in test scripts

**Categories:** 4.

Converts hydro shock tests to typed gas fields (density, specific thermal energy, pressure). May change analysis field conventions, not simulation methods.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`.

**Patch locations:** `@@ -8,7 +8,10 @@ import os`; `@@ -8,7 +8,12 @@ import os`; `@@ -8,7 +8,12 @@ import os`; `@@ -8,7 +8,10 @@ import os`; `@@ -8,7 +8,12 @@ import os`; additional hunks in the same patch.

<a id="commit-127"></a>
## 127 — `1994354f5` — 2022-07-02

All tests pass with yt4!

**Categories:** 3.

Adds missing list commas to two Toro test scripts introduced during migration. Necessary test syntax repair if adopting #126.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`.

**Patch locations:** `@@ -10,7 +10,7 @@ _data_file = 'DD0001/data0001'`; `@@ -10,7 +10,7 @@ _data_file = 'DD0001/data0001'`.

<a id="commit-128"></a>
## 128 — `8bbbc278e` — 2022-07-02

Many changes to bring tests up to date with yt-4.x

**Categories:** 4.

Completes broad yt4/Python test modernization and runner imports. Adopt final coherent versions and verify that Aeos-specific analyses still map custom fields correctly.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

**Patch locations:** `@@ -1,4 +1,4 @@`; `@@ -1,4 +1,4 @@`; `@@ -1,4 +1,4 @@`; `@@ -1,4 +1,4 @@`; `@@ -3,7 +3,6 @@`; additional hunks in the same patch.

<a id="commit-129"></a>
## 129 — `ac3f9b60d` — 2022-07-02

Last few fixes for yt-4.x testing compat

**Categories:** 3.

Corrects yt profile tuple indexing in AMR cosmology tests. Conditional test API fix following yt4 migration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`.

**Patch locations:** `@@ -227,14 +227,14 @@ def test_phase():`; `@@ -253,7 +253,7 @@ def test_phase():`; `@@ -227,14 +227,14 @@ def test_phase():`; `@@ -253,7 +253,7 @@ def test_phase():`.

<a id="commit-130"></a>
## 130 — `dbfb5c8ee` — 2022-07-02

Use updated answer testing fork (jwise77) until next yt point release

**Categories:** 4.

Temporary forked-yt answer-testing dependency and CI cache changes; superseded by #140. Do not pin to the historical development fork.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -30,7 +30,15 @@ commands:`; `@@ -188,13 +196,13 @@ jobs:`; `@@ -205,7 +213,7 @@ jobs:`; `@@ -214,7 +222,7 @@ jobs:`; `@@ -236,13 +244,13 @@ jobs:`.

<a id="commit-131"></a>
## 131 — `39262f4fe` — 2022-07-03

Introducing concurrent sims for the test_runner with multiprocessing

**Categories:** 4.

Adds multiprocessing --jrun control for independent test simulations and adjusts CI launch settings. Useful test-throughput feature; control aggregate MPI/process resources.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/test_runner.py`.

**Patch locations:** `@@ -24,7 +24,7 @@ commands:`; `@@ -117,7 +117,7 @@ commands:`; `@@ -13,6 +13,7 @@ import sys`; `@@ -267,11 +268,13 @@ class EnzoTestCollection(object):`; `@@ -294,8 +297,8 @@ class EnzoTestCollection(object):`; additional hunks in the same patch.

<a id="commit-132"></a>
## 132 — `05e6b2cbe` — 2022-07-10

Merge branch 'fix-test-suite' into fix_StarParticleFindAll

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

<a id="commit-133"></a>
## 133 — `a6707c304` — 2022-07-13

Fetching tags from PR issuing repo in CI

**Categories:** 4.

CI fetches PR repository tags to find test baselines. Infrastructure only; superseded by guarded PR repository handling in #134.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -11,8 +11,10 @@ commands:`.

<a id="commit-134"></a>
## 134 — `e115b9751` — 2022-07-13

Minor update

**Categories:** 4.

Guards fork tag fetching on CircleCI PR variables. Adopt with the final CI workflow and intentional trusted tag provenance.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -14,7 +14,9 @@ commands:`.

<a id="commit-135"></a>
## 135 — `a3dc5bfba` — 2022-07-13

Merge branch 'fix-test-suite' into fix_StarParticleFindAll

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-136"></a>
## 136 — `9a72ad3c3` — 2022-07-14

Update run/Hydro/Hydro-3D/RotatingSphere/profile_script.py

**Categories:** 4.

Removes unused os import from the rotating-sphere analysis after test migration. No simulation changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`.

**Patch locations:** `@@ -4,7 +4,6 @@ import matplotlib as mpl`.

<a id="commit-137"></a>
## 137 — `15a7a9749` — 2022-07-14

Update run/Hydro/Hydro-3D/RotatingSphere/profile_script.py

**Categories:** 4.

Removes unused numpy import from the same analysis; dependent cleanup only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`.

**Patch locations:** `@@ -4,7 +4,6 @@ import matplotlib as mpl`.

<a id="commit-138"></a>
## 138 — `3366ec2fb` — 2022-07-14

Update run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py

**Categories:** 4.

Removes unused os import from rotor answer test; dependent cleanup only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`.

**Patch locations:** `@@ -2,7 +2,6 @@`.

<a id="commit-139"></a>
## 139 — `c81625451` — 2022-07-14

Update run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py

**Categories:** 4.

Removes unused os import from CT Orszag-Tang AMR test; dependent cleanup only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

**Patch locations:** `@@ -2,7 +2,6 @@`.

<a id="commit-140"></a>
## 140 — `9d218106a` — 2022-07-14

Change yt version from jwise77 to yt-project repo

**Categories:** 4.

Switches the temporary yt fork back to yt-project and removes a test import. Use a reproducible supported yt version rather than blindly following a moving branch.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`.

**Patch locations:** `@@ -35,11 +35,11 @@ commands:`; `@@ -2,7 +2,6 @@`.

<a id="commit-141"></a>
## 141 — `a01a390c9` — 2022-07-14

Merge pull request #190 from jwise77/fix-test-suite

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131), [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134), [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

<a id="commit-142"></a>
## 142 — `4252ec1f7` — 2022-07-14

Merge remote-tracking branch 'upstream/main' into fix_StarParticleFindAll

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

<a id="commit-143"></a>
## 143 — `98b635e18` — 2022-07-14

Merge pull request #176 from setsuna0402/fix_StarParticleFindAll

**Categories:** 2,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#046](batch-01.md#commit-046), [#115](batch-03.md#commit-115), [#132](batch-03.md#commit-132), [#135](batch-03.md#commit-135), [#142](batch-03.md#commit-142).

**Aeos-modified paths since common ancestor:** `src/enzo/StarParticleFindAll.C`.

**Files:** `src/enzo/StarParticleFindAll.C`.

<a id="commit-144"></a>
## 144 — `3d8ff999f` — 2022-06-09

[BUGFIX] min/max timing are now properly calculated and reported

**Categories:** 3.

Timing min/max templates return T instead of bool, preventing numerical timing extrema collapsing to Boolean values. Reverse check succeeds: already fixed in Aeos.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EnzoTiming.h`.

**Files:** `src/enzo/EnzoTiming.h`.

**Patch locations:** `@@ -30,12 +30,12 @@`.

<a id="commit-145"></a>
## 145 — `57fbecefd` — 2022-07-10

Merge branch 'fix-test-suite' into enzo-timing-minmax

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

<a id="commit-146"></a>
## 146 — `49f0eacde` — 2022-07-14

Merge remote-tracking branch 'upstream/main' into enzo-timing-minmax

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134), [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

<a id="commit-147"></a>
## 147 — `0667dc088` — 2022-07-14

Merge pull request #189 from jwise77/enzo-timing-minmax

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#144](batch-03.md#commit-144), [#145](batch-03.md#commit-145), [#146](batch-03.md#commit-146).

**Aeos-modified paths since common ancestor:** `src/enzo/EnzoTiming.h`.

**Files:** `src/enzo/EnzoTiming.h`.

<a id="commit-148"></a>
## 148 — `28829f014` — 2021-06-03

Create Make.mach.nasa-aitken-rome

**Categories:** 4.

Adds NASA Aitken Rome machine configuration; opt-in infrastructure and later replaced by CMake.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.nasa-aitken-rome`.

**Patch locations:** `@@ -0,0 +1,134 @@`.

<a id="commit-149"></a>
## 149 — `467460ca5` — 2021-06-03

Update Make.mach.nasa-pleiades

**Categories:** 4.

Updates NASA Pleiades compiler/MPI modules and library paths only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.nasa-pleiades`.

**Files:** `src/enzo/Make.mach.nasa-pleiades`.

**Patch locations:** `@@ -4,8 +4,8 @@`; `@@ -21,7 +21,10 @@`; `@@ -31,8 +34,8 @@ MACH_FILE  = Make.mach.nasa-pleiades`; `@@ -44,10 +47,10 @@ MACHINE_NOTES = "MACHINE_NOTES for Pleiades at NASA: \`; `@@ -107,7 +110,8 @@ MACH_LDFLAGS  =`.

<a id="commit-150"></a>
## 150 — `0ef244ef6` — 2022-06-29

Update src/enzo/Make.mach.nasa-aitken-rome

**Categories:** 4.

Adds AVX2 optimization flags to Aitken Rome. Site-specific numerical reproducibility must be checked when compiler optimization changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.nasa-aitken-rome`.

**Patch locations:** `@@ -97,10 +97,10 @@ MACH_LDFLAGS  =`.
