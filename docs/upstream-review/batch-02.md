# Batch 02: commits 051–100

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-051"></a>
## 051 — `aeea391f4` — 2021-10-19

lengthed timeout to 20m in circleci

**Categories:** 4.

CI no-output timeout only; infrastructure tuning, with prerequisites from earlier CI restructuring.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -97,6 +97,7 @@ commands:`.

<a id="commit-052"></a>
## 052 — `2b20d1c9e` — 2021-10-25

Merge pull request #181 from gregbryan/circleci-longer-timeout

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#051](batch-02.md#commit-051).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-053"></a>
## 053 — `0c2cc48bf` — 2022-02-22

Removing amr_cosmology from push suite because it is taking too long.

**Categories:** 4.

Removes AMR cosmology from push/quick suites to reduce duration. No physics change, but reduces coverage; retain a scheduled full suite if adopting.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`.

**Patch locations:** `@@ -10,6 +10,6 @@ cosmology_simulation = True`.

<a id="commit-054"></a>
## 054 — `b0d485029` — 2022-02-22

Removing RayleighTaylor_CT_Suppressed from push suite because it is taking too long.

**Categories:** 4.

Removes suppressed Rayleigh-Taylor MHD from push suite. Optional CI policy, not a correctness fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`.

**Patch locations:** `@@ -7,5 +7,5 @@ gravity = False`.

<a id="commit-055"></a>
## 055 — `2a293850f` — 2022-02-22

Setting circleci cache to look for push_suite directory since file doesn't seem to exist

**Categories:** 3.

CI skip marker is a directory: -e instead of -f and corrected directory path prevent unnecessary reruns. Relevant only to this CI design.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -101,7 +101,7 @@ commands:`; `@@ -209,7 +209,7 @@ jobs:`.

<a id="commit-056"></a>
## 056 — `c301b998f` — 2022-02-22

Decreasing the number of compile configurations tested so as not to exceed circleci testing limit

**Categories:** 4.

Shrinks the compile matrix to meet CI limits, reducing precision coverage. Optional policy; do not mistake it for improved solver compatibility.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -126,7 +126,7 @@ commands:`; `@@ -141,8 +141,8 @@ commands:`.

<a id="commit-057"></a>
## 057 — `6c377633f` — 2022-02-23

Merge pull request #185 from gregbryan/shrink-push-suite

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`.

<a id="commit-058"></a>
## 058 — `9172a79a2` — 2019-10-02

turning cooling/heating back on in the midplane

**Categories:** 4.

Despite its message, the patch adds z-face extrapolation boundary code, not a cooling switch. Optional new boundary physics; requires the later enum/interface sequence and is not a stand-alone fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`.

**Patch locations:** `@@ -18,7 +18,7 @@`; `@@ -55,8 +55,8 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -667,6 +667,21 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -773,6 +788,20 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`.

<a id="commit-059"></a>
## 059 — `7c1256a6d` — 2019-10-07

adding new external boundary type

**Categories:** 4.

Adds extrapolating boundary cases on x/y faces and boundary enum 6. Optional method; superseded by hydrostatic naming and behavior changes in #61/#67.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/typedefs.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/typedefs.h`.

**Patch locations:** `@@ -284,7 +284,8 @@ Initialization Parameters`; `@@ -240,6 +240,22 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -346,6 +362,20 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -454,6 +484,21 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -561,6 +606,20 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; additional hunks in the same patch.

<a id="commit-060"></a>
## 060 — `5377f8dc2` — 2019-10-07

removing unused variable

**Categories:** 4.

Removes an unused boundary variable introduced earlier; dependency cleanup only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`.

**Patch locations:** `@@ -55,7 +55,7 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`.

<a id="commit-061"></a>
## 061 — `0b0df3ea4` — 2019-10-08

Changing naming convention and adding documentation

**Categories:** 4,2.

Renames extrapolate to hydrostatic and changes numeric boundary codes: 5 becomes hydrostatic and undefined becomes 6. Parameter/restart semantics require explicit migration; never adopt as a mere rename.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/typedefs.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/typedefs.h`.

**Patch locations:** `@@ -284,13 +284,19 @@ Initialization Parameters`; `@@ -238,9 +238,7 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -255,7 +253,8 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -360,9 +359,7 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -376,6 +373,8 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; additional hunks in the same patch.

<a id="commit-062"></a>
## 062 — `e28320f46` — 2019-11-04

adding hydrostatic boundary to OOC_BOUNDARY

**Categories:** 4.

Adds hydrostatic boundary handling to the OOC path. Optional new boundary method; requires enum and later algorithm corrections as a coherent feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`.

**Patch locations:** `@@ -200,6 +200,21 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -320,6 +335,20 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -442,6 +471,21 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -563,6 +607,20 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -686,6 +744,21 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; additional hunks in the same patch.

<a id="commit-063"></a>
## 063 — `c2b57fd3b` — 2019-11-04

Merge https://github.com/enzo-project/enzo-dev into boundary

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** none; incoming history is already in the Aeos ancestry.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.linux-gnu`.

**Files:** `.circleci/config.yml`, `LICENSE`, `README`, `README.md`, `doc/manual/source/conf.py`, `doc/manual/source/developer_guide/EnzoTestSuite.rst`, `doc/manual/source/index.rst`, `doc/manual/source/physics/adaptive_mesh.rst`, `doc/manual/source/physics/gravity.rst`, `doc/manual/source/physics/hydro_methods.rst`, `doc/manual/source/physics/index.rst`, `doc/manual/source/reference/EnzoInternalUnits.rst`, `doc/manual/source/reference/EnzoPrimaryReferences.rst`, `doc/manual/source/reference/MakeOptions.rst`, `doc/manual/source/testproblems/index.rst`, `doc/manual/source/user_guide/CUDAEnzo.rst`, `doc/manual/source/user_guide/RunTestProblem.rst`, `doc/manual/source/user_guide/bootcamp.rst`, `doc/manual/source/user_guide/index.rst`, `method-paper-joss-2019/paper.md`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0000_Slice_x_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0000_Slice_y_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0000_Slice_z_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0010_Slice_x_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0010_Slice_y_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0010_Slice_z_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0070_Slice_x_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0070_Slice_y_density.png`, `run/Hydro/Hydro-3D/CollapseTestNonCosmological/frames/DD0070_Slice_z_density.png`, `run/test_runner.py`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.cuda`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.ubuntu`.

<a id="commit-064"></a>
## 064 — `e03622fb1` — 2019-11-04

merging with enzo-dev tip

**Categories:** 1.

Deletes unused legacy lcaperf typedefs/comments; clean patch, no solver operation changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/lcaperf.h`.

**Patch locations:** `@@ -37,26 +37,9 @@`.

<a id="commit-065"></a>
## 065 — `0b03aa089` — 2020-05-20

Merge remote-tracking branch 'origin/master' into boundary

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** none; incoming history is already in the Aeos ancestry.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/OutputFromEvolveLevel.C`.

**Files:** `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/OutputFromEvolveLevel.C`.

<a id="commit-066"></a>
## 066 — `9676570b9` — 2020-05-20

Merge remote-tracking branch 'upstream/master' into boundary

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#001](batch-01.md#commit-001), [#002](batch-01.md#commit-002), [#003](batch-01.md#commit-003), [#004](batch-01.md#commit-004), [#005](batch-01.md#commit-005), [#006](batch-01.md#commit-006), [#007](batch-01.md#commit-007), [#008](batch-01.md#commit-008), [#009](batch-01.md#commit-009).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/CommunicationCollectParticles.C`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_CollectStars.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_TransferSubgridStars.C`, `src/enzo/Make.config.objects`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleFindAll.C`, `src/enzo/StarRoutines.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/macros_and_parameters.h`, `src/enzo/pop3_maker.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `README.md`, `doc/manual/source/parameters/index.rst`, `src/enzo/CommunicationCollectParticles.C`, `src/enzo/CommunicationTransferSubgridParticles.C`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_CollectStars.C`, `src/enzo/Grid_CommunicationSendStars.C`, `src/enzo/Grid_CommunicationTransferStarsOpt.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/Grid_TransferSubgridStars.C`, `src/enzo/Grid_ZeusSolver.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.sdsc-comet`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleFindAll.C`, `src/enzo/StarRoutines.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/macros_and_parameters.h`, `src/enzo/pop3_maker.F`, `src/enzo/typedefs.h`.

<a id="commit-067"></a>
## 067 — `561b3b17f` — 2020-05-25

updating hydrostatic boundary to use average quantities near boundary

**Categories:** 4,2.

Changes hydrostatic ghost cells to face-averaged linear/quadratic extrapolation, normal velocity/B zeroing and tangential field copying, with positivity/NaN fallback. This is a boundary prescription, not a universal bug fix; port only if explicitly desired. The added DensField argument is removed in #68.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`.

**Patch locations:** `@@ -50,13 +50,13 @@ int READ_BV(float         *bv_buffer, int field, int dim, int face, int slabsize`; `@@ -166,7 +166,19 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -201,19 +213,28 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -225,10 +246,22 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; `@@ -254,19 +287,28 @@ int ExternalBoundary::SetExternalBoundary(int FieldRank, int GridDims[],`; additional hunks in the same patch.

<a id="commit-068"></a>
## 068 — `078578c37` — 2020-06-22

Fixing mismatch in routine arguments

**Categories:** 3.

Removes the unused DensField argument that mismatched callers. Reverse check succeeds against Aeos because its signature already lacks that argument; no missing standalone repair.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`.

**Patch locations:** `@@ -50,7 +50,7 @@ int READ_BV(float         *bv_buffer, int field, int dim, int face, int slabsize`.

<a id="commit-069"></a>
## 069 — `cad5e3fa5` — 2022-02-23

Merge pull request #121 from ibutsky/boundary

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068).

**Aeos-modified paths since common ancestor:** `src/enzo/typedefs.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/lcaperf.h`, `src/enzo/typedefs.h`.

<a id="commit-070"></a>
## 070 — `f78da8ef8` — 2020-09-01

Create Make.mach.tigercpu

**Categories:** 4.

Adds Princeton Tiger CPU compiler/dependency settings; site-specific and later superseded by CMake.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.tigercpu`.

**Patch locations:** `@@ -0,0 +1,146 @@`.

<a id="commit-071"></a>
## 071 — `5a77a6fbc` — 2022-02-23

Merge pull request #157 from HerculesJack/patch-1

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#070](batch-02.md#commit-070).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.tigercpu`.

<a id="commit-072"></a>
## 072 — `ea4ba316f` — 2021-03-26

Modified momentum check in single SN star formation algorithm to use the momentum modified by the previous check (to prevent energy excess) rather than the original momentum.

**Categories:** 3.

The second momentum cap must test already-limited pcell rather than original p_sn. Otherwise it can undo an earlier energy-limiting decision. Clean patch applies; relevant to star_maker_ssn, not automatically to Aeos individual-star feedback.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/star_maker_ssn.F`.

**Files:** `src/enzo/star_maker_ssn.F`.

**Patch locations:** `@@ -856,7 +856,7 @@ c                         from the SNe`.

<a id="commit-073"></a>
## 073 — `4e909d514` — 2021-04-12

Merge remote-tracking branch 'origin-enzo/master' into ssn-fix

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#036](batch-01.md#commit-036), [#037](batch-01.md#commit-037), [#038](batch-01.md#commit-038), [#039](batch-01.md#commit-039), [#040](batch-01.md#commit-040), [#041](batch-01.md#commit-041), [#042](batch-01.md#commit-042), [#043](batch-01.md#commit-043).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `.circleci/config.yml`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/uuid.C`.

<a id="commit-074"></a>
## 074 — `59f0e6d7f` — 2021-05-11

Added Single Supernovae feedback star formation method to calculation of number of feedback cells (since it also uses this parameter).

**Categories:** 3,2.

Includes SINGLE_SUPERNOVA when deriving feedback stencil cell count. Adapt the condition: the historical patch has OR/AND precedence that applies the trailing guard differently to NORMAL/UNIGRID. Use ((normal || unigrid || single) && guard), preserving Aeos methods.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`.

**Files:** `src/enzo/ReadParameterFile.C`.

**Patch locations:** `@@ -1805,7 +1805,8 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`.

<a id="commit-075"></a>
## 075 — `c38428aec` — 2022-02-23

Merge pull request #168 from gregbryan/ssn-fix

**Categories:** 2,3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074).

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/star_maker_ssn.F`.

**Files:** `src/enzo/ReadParameterFile.C`, `src/enzo/star_maker_ssn.F`.

<a id="commit-076"></a>
## 076 — `c911d5eb5` — 2021-04-12

Fix HDF5 include path

**Categories:** 4.

Corrects generic GNU HDF5 include directory to prefix/include. Resolve against the actual local machine file rather than replacing local dependency paths.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.linux-gnu`.

**Files:** `src/enzo/Make.mach.linux-gnu`.

**Patch locations:** `@@ -94,7 +94,7 @@ MACH_OPT_AGGRESSIVE  = -O3 -g`.

<a id="commit-077"></a>
## 077 — `e477ecba3` — 2022-02-23

Merge pull request #171 from michaelkuhn/hdf5-include

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#076](batch-02.md#commit-076).

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.linux-gnu`.

**Files:** `src/enzo/Make.mach.linux-gnu`.

<a id="commit-078"></a>
## 078 — `92122b849` — 2020-07-09

Fixing mixed precision issues

**Categories:** 3.

MassUnits is passed through a double interface and must remain double even when FLOAT selects another precision. Clean patch applies; duplicate development patch #116 has the same effect. Preserve newchem backend handling.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`.

**Files:** `src/enzo/GrackleReadParameters.C`.

**Patch locations:** `@@ -218,7 +218,8 @@ int GrackleReadParameters(FILE *fptr, FLOAT InitTime)`.

<a id="commit-079"></a>
## 079 — `8a0c3365c` — 2021-04-14

Removing unnecessary DebugField that caused a I/O crash

**Categories:** 3.

Removes an unallocated DebugField from CollapseMHD3D initialization that can crash output. Clean patch applies; relevant only to that initializer.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`.

**Patch locations:** `@@ -124,8 +124,6 @@ int grid::CollapseMHD3DInitializeGrid(int n_sphere,`.

<a id="commit-080"></a>
## 080 — `03cfddfd3` — 2022-02-23

Merge pull request #172 from jwise77/mhd-io-fix

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079).

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`.

**Files:** `src/enzo/GrackleReadParameters.C`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`.

<a id="commit-081"></a>
## 081 — `40f144cd3` — 2019-08-24

Adding ThermalInstability problem type

**Categories:** 4.

Adds ThermalInstability initializer and tests. Withdrawn by #100/#102 before upstream integration; do not port an abandoned intermediate feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`.

**Files:** `run/Hydro/Hydro-3D/ThermalInstability/ThermalInstability.enzo`, `run/Hydro/Hydro-3D/ThermalInstability/white_noise_generator.py`, `src/enzo/Grid.h`, `src/enzo/Grid_ThermalInstabilityInitializeGrid.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ThermalInstabilityInitialize.C`.

**Patch locations:** `@@ -0,0 +1,84 @@`; `@@ -0,0 +1,86 @@`; `@@ -2096,6 +2096,12 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -0,0 +1,352 @@`; `@@ -155,6 +155,8 @@ int ShearingBox2DInitialize(FILE *fptr, FILE *Outfptr, HierarchyEntry &TopGrid,`; additional hunks in the same patch.

<a id="commit-082"></a>
## 082 — `f0a77bfe9` — 2019-08-27

adding cosmic ray second fluid; tested SOD shocktube

**Categories:** 4,2.

Large optional CR two-fluid/MHD transport expansion: anisotropic diffusion, streaming, CR pressure in wave speeds and stellar CR feedback interfaces. Touches Aeos evolution, star handler and Riemann methods. Adopt only as a separately validated new-physics project; default-off does not certify every edited path equivalent.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/CosmologySimulationInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_InitializeUniformGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.config.objects`, `src/enzo/ProblemType_AgoraRestart.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CosmologySimulationInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_InitializeUniformGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.config.objects`, `src/enzo/ProblemType_AgoraRestart.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_MHD3DTestInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/star_maker2.F`.

**Patch locations:** `@@ -35,6 +35,10 @@ int CRShockTubesInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -52,7 +56,10 @@ int CRShockTubesInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -104,6 +111,24 @@ int CRShockTubesInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -131,7 +156,10 @@ int CRShockTubesInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -175,7 +203,10 @@ int CRShockTubesInitialize(FILE *fptr, FILE *Outfptr,`; additional hunks in the same patch.

<a id="commit-083"></a>
## 083 — `722d4032e` — 2019-10-12

Adding CR energy total energy calculations

**Categories:** 4,2.

Intermediate attempt to include CR energy in total energy across cooling, interpolation and flux routines. Reversed by #84; do not cherry-pick this transient energy convention.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`.

**Files:** `src/enzo/Grid_ComputePressure.C`, `src/enzo/Grid_ConductHeat.C`, `src/enzo/Grid_CopyZonesFromGrid.C`, `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`, `src/enzo/Grid_RestoreEnergyConsistency.C`, `src/enzo/Grid_SolveRadiativeCooling.C`, `src/enzo/Grid_SolveRateAndCoolEquations.C`, `src/enzo/Make.mach.CCA-hardy`.

**Patch locations:** `@@ -127,6 +127,9 @@ int grid::ComputePressure(FLOAT time, float *pressure,`; `@@ -141,6 +144,9 @@ int grid::ComputePressure(FLOAT time, float *pressure,`; `@@ -205,6 +211,8 @@ int grid::ComputePressure(FLOAT time, float *pressure,`; `@@ -219,6 +227,8 @@ int grid::ComputePressure(FLOAT time, float *pressure,`; `@@ -40,7 +40,7 @@ int grid::ConductHeat(){`; additional hunks in the same patch.

<a id="commit-084"></a>
## 084 — `9eeb7414e` — 2019-11-14

removing cosmic rays from total energy

**Categories:** 4,2.

Removes the CR contribution from gas total energy introduced in #83 and adjusts MHD flux/source terms. Treat the final CR energy contract as one feature, not two independent science fixes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`.

**Files:** `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_ComputePressure.C`, `src/enzo/Grid_ConductHeat.C`, `src/enzo/Grid_CopyZonesFromGrid.C`, `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`, `src/enzo/Grid_RestoreEnergyConsistency.C`, `src/enzo/Grid_SolveRadiativeCooling.C`, `src/enzo/Grid_SolveRateAndCoolEquations.C`, `src/enzo/hydro_rk/Grid_MHD3DTestInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`.

**Patch locations:** `@@ -92,7 +92,7 @@ int grid::CRShockTubesInitializeGrid(   float x0,`; `@@ -110,7 +110,7 @@ int grid::CRShockTubesInitializeGrid(   float x0,`; `@@ -205,7 +205,7 @@ int grid::CRShockTubesInitializeGrid(   float x0,   float x1,`; `@@ -223,7 +223,7 @@ int grid::CRShockTubesInitializeGrid(   float x0,   float x1,`; `@@ -242,7 +242,7 @@ int grid::CRShockTubesInitializeGrid(   float x0,   float x1,`; additional hunks in the same patch.

<a id="commit-085"></a>
## 085 — `02361a0d2` — 2019-12-05

reverting back to traditional CR only on this branch

**Categories:** 4.

CR transport initializer plumbing and solver timestep/source adjustments; belongs to the optional CR feature and relies on #86/#87.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`.

**Patch locations:** `@@ -1951,6 +1951,13 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -282,7 +282,6 @@ int grid::ComputeAnisotropicCRDiffusion(){`; `@@ -71,14 +71,12 @@ int grid::ComputeCRDiffusionTimeStep (float &dt) {`; `@@ -446,7 +446,6 @@ float grid::ComputeTimeStep()`; `@@ -570,6 +569,8 @@ float grid::ComputeTimeStep()`; additional hunks in the same patch.

<a id="commit-086"></a>
## 086 — `583dd89dc` — 2019-12-05

missed a couple of files

**Categories:** 4.

Adds the CR transport test initializer (problem 251) including explicit parameter parsing; optional verification fixture requiring grid implementation and registration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CRTransportTestInitialize.C`.

**Patch locations:** `@@ -0,0 +1,221 @@`.

<a id="commit-087"></a>
## 087 — `4f76af419` — 2019-12-05

adding another missed file

**Categories:** 4.

Adds grid-level CR diffusion/streaming test states; optional initializer, not an isolated-disk model change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_CRTransportTestInitialize.C`.

**Patch locations:** `@@ -0,0 +1,152 @@`.

<a id="commit-088"></a>
## 088 — `a712a028a` — 2019-12-05

streaming working; need to clean

**Categories:** 4,2.

Rewrites anisotropic diffusion and streaming fluxes, timestep stability parameters and CR source terms. Numerical model development conditional on the new CR feature; require directional diffusion/streaming tests before use.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`.

**Patch locations:** `@@ -47,12 +47,11 @@ int grid::ComputeAnisotropicCRDiffusion(){`; `@@ -62,14 +61,16 @@ int grid::ComputeAnisotropicCRDiffusion(){`; `@@ -81,7 +82,7 @@ int grid::ComputeAnisotropicCRDiffusion(){`; `@@ -94,222 +95,148 @@ int grid::ComputeAnisotropicCRDiffusion(){`; `@@ -43,8 +43,8 @@ int grid::ComputeCRStreaming(){`; additional hunks in the same patch.

<a id="commit-089"></a>
## 089 — `dac9d3ca9` — 2019-12-05

cleaning up CR streaming

**Categories:** 4.

Removes alternate CR flux buffers/debug calculations and changes CR defaults within the development branch. Take final parameter conventions, not intermediate tuning.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/SetDefaultGlobalValues.C`.

**Files:** `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/SetDefaultGlobalValues.C`.

**Patch locations:** `@@ -42,11 +42,10 @@ int grid::ComputeCRStreaming(){`; `@@ -56,14 +55,10 @@ int grid::ComputeCRStreaming(){`; `@@ -83,8 +78,7 @@ int grid::ComputeCRStreaming(){`; `@@ -92,44 +86,24 @@ int grid::ComputeCRStreaming(){`; `@@ -139,8 +113,6 @@ int grid::ComputeCRStreaming(){`; additional hunks in the same patch.

<a id="commit-090"></a>
## 090 — `386c71a05` — 2019-12-05

redefining CR streaming stability factor

**Categories:** 4.

Temporarily redefines the streaming smoothing scale from relative gradients to an absolute denominator. Superseded by #94; do not port this intermediate numerical convention.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/SetDefaultGlobalValues.C`.

**Files:** `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/SetDefaultGlobalValues.C`.

**Patch locations:** `@@ -78,7 +78,6 @@ int grid::ComputeCRStreaming(){`; `@@ -97,12 +96,12 @@ int grid::ComputeCRStreaming(){`; `@@ -38,7 +38,7 @@ int grid::ComputeCRStreamingTimeStep (float &dt) {`; `@@ -71,8 +71,8 @@ int grid::ComputeCRStreamingTimeStep (float &dt) {`; `@@ -474,8 +474,8 @@ int SetDefaultGlobalValues(TopGridData &MetaData)`.

<a id="commit-091"></a>
## 091 — `6cb8c1245` — 2019-12-06

Merge branch 'cosmic_rays_trad' of https://github.com/ibutsky/enzo-dev-cr into cosmic_rays

**Categories:** 2,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090).

**Aeos-modified paths since common ancestor:** `src/enzo/CosmologySimulationInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_InitializeUniformGrid.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ProblemType_AgoraRestart.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `run/Hydro/Hydro-3D/ThermalInstability/ThermalInstability.enzo`, `run/Hydro/Hydro-3D/ThermalInstability/white_noise_generator.py`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/CosmologySimulationInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputePressure.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_ConductHeat.C`, `src/enzo/Grid_CopyZonesFromGrid.C`, `src/enzo/Grid_CorrectForRefinedFluxes.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_InitializeUniformGrid.C`, `src/enzo/Grid_ProjectSolutionToParentGrid.C`, `src/enzo/Grid_RestoreEnergyConsistency.C`, `src/enzo/Grid_SolveRadiativeCooling.C`, `src/enzo/Grid_SolveRateAndCoolEquations.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Grid_ThermalInstabilityInitializeGrid.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.CCA-hardy`, `src/enzo/ProblemType_AgoraRestart.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/ThermalInstabilityInitialize.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_MHD3DTestInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/star_maker2.F`.

<a id="commit-092"></a>
## 092 — `d730d0592` — 2019-12-06

fixing streaming test ICs

**Categories:** 3.

Clamps the CR streaming test's triangular initial energy to nonnegative values. Required for that added fixture, not a defect reachable in the fiducial disk initializer.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_CRTransportTestInitialize.C`.

**Patch locations:** `@@ -122,7 +122,8 @@ int grid::CRTransportTestInitializeGrid(int test_type, float center,`.

<a id="commit-093"></a>
## 093 — `57dfa1bd4` — 2019-12-09

fixing Anisotropic diffusion indices, adding documentation

**Categories:** 3.

Corrects anisotropic CR diffusion indices and restores magnetic energy to shock-tube gas energy, plus CR documentation. Required if adopting #82; no standalone anisotropic path exists in current Aeos.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`.

**Patch locations:** `@@ -3376,18 +3376,39 @@ For details on the cosmic ray solver in Enzo see :ref:cosmic_rays.`; `@@ -6,10 +6,13 @@ Cosmic Ray Two-Fluid Model`; `@@ -24,15 +27,17 @@ these options. But most important are:`; `@@ -92,7 +92,7 @@ int grid::CRShockTubesInitializeGrid(   float x0,`; `@@ -110,7 +110,7 @@ int grid::CRShockTubesInitializeGrid(   float x0,`; additional hunks in the same patch.

<a id="commit-094"></a>
## 094 — `ed9c0ca8b` — 2019-12-09

cleaning up streaming and switching definition of streaming factor back

**Categories:** 4.

Restores cell/energy-dependent streaming regularization and builds a bottleneck density test. Model/parameter choice within optional CR functionality.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/SetDefaultGlobalValues.C`.

**Files:** `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/SetDefaultGlobalValues.C`.

**Patch locations:** `@@ -59,7 +59,7 @@ int grid::CRTransportTestInitializeGrid(int test_type, float center,`; `@@ -90,6 +90,7 @@ int grid::CRTransportTestInitializeGrid(int test_type, float center,`; `@@ -120,13 +121,23 @@ int grid::CRTransportTestInitializeGrid(int test_type, float center,`; `@@ -43,8 +43,8 @@ int grid::ComputeCRStreaming(){`; `@@ -71,12 +71,22 @@ int grid::ComputeCRStreaming(){`; additional hunks in the same patch.

<a id="commit-095"></a>
## 095 — `1da139f17` — 2019-12-09

bottleneck test mostly working

**Categories:** 4.

Refines bottleneck ICs, magnetic-energy normalization and test-specific CR boundary injection. Temporary hard-coded evolution behavior is removed later; do not adopt this snapshot alone.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`.

**Patch locations:** `@@ -131,9 +131,9 @@ int grid::CRTransportTestInitializeGrid(int test_type, float center,`; `@@ -154,7 +154,7 @@ int grid::CRTransportTestInitializeGrid(int test_type, float center,`; `@@ -112,7 +112,6 @@ int grid::ComputeCRStreaming(){`; `@@ -145,6 +144,17 @@ int grid::ComputeCRStreaming(){`; `@@ -287,7 +287,7 @@ int grid::UpdateMHDPrim(float **dU, float c1, float c2)`.

<a id="commit-096"></a>
## 096 — `34fe53b09` — 2019-12-07

cleaning up mhd source terms for CR heating and advection

**Categories:** 4,2.

Moves CR pressure work/heating and energy flux terms into their intended MHD paths. Required coherent CR subsystem integration, not a proven defect in the existing CR-disabled Aeos disk.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`.

**Patch locations:** `@@ -69,7 +69,7 @@ int grid::MHDSourceTerms(float **dU, float min_coeff)`; `@@ -89,29 +89,21 @@ int grid::MHDSourceTerms(float **dU, float min_coeff)`; `@@ -126,33 +118,40 @@ int grid::MHDSourceTerms(float **dU, float min_coeff)`; `@@ -93,7 +93,7 @@ int llf_mhd(float **FluxLine, float **priml, float **primr, float **prim, int Ac`; `@@ -168,7 +168,7 @@ int llf_mhd(float **FluxLine, float **priml, float **primr, float **prim, int Ac`.

<a id="commit-097"></a>
## 097 — `173712dd8` — 2019-12-07

adding CR expansion terms for all solvers

**Categories:** 3.

Extends cosmological CR adiabatic expansion beyond Zeus and avoids repeated application per spatial component in expand_terms. Conditional bug fix for comoving CR-enabled runs; clean patch applies.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/expand_terms.F`.

**Patch locations:** `@@ -140,15 +140,17 @@ int grid::ComovingExpansionTerms()`; `@@ -86,12 +86,16 @@ c`.

<a id="commit-098"></a>
## 098 — `fc809e3d6` — 2019-12-09

Merge branch 'cosmic_rays_trad' of https://github.com/ibutsky/enzo-dev-cr into cosmic_rays_trad

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/expand_terms.F`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`.

<a id="commit-099"></a>
## 099 — `73e3bdc6a` — 2019-12-10

Merge branch 'cosmic_rays_trad' of https://github.com/ibutsky/enzo-dev-cr into cosmic_rays

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098).

**Aeos-modified paths since common ancestor:** `src/enzo/SetDefaultGlobalValues.C`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/expand_terms.F`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`.

<a id="commit-100"></a>
## 100 — `cc7a01bd0` — 2019-12-10

remvoing Thermal instability problem from this branch

**Categories:** 4.

Removes abandoned ThermalInstability implementation and special MHD test additions; integrate the final feature set rather than replaying add/remove churn.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_ThermalInstabilityInitializeGrid.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ThermalInstabilityInitialize.C`, `src/enzo/hydro_rk/Grid_MHD3DTestInitializeGrid.C`.

**Patch locations:** `@@ -2115,12 +2115,6 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -1,352 +0,0 @@`; `@@ -157,8 +157,6 @@ int ShearingBox2DInitialize(FILE *fptr, FILE *Outfptr, HierarchyEntry &TopGrid,`; `@@ -736,10 +734,6 @@ int InitializeNew(char *filename, HierarchyEntry &TopGrid,`; `@@ -653,7 +653,6 @@ OBJS_CONFIG_LIB = \`; additional hunks in the same patch.
