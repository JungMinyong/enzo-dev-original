# Batch 08: commits 351–400

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-351"></a>
## 351 — `028b0235a` — 2022-11-21

Unit error at disk/CGM boundary

**Categories:** 3.

Converts cgs spherical radius back to code units before HaloGasDensity at disk/CGM boundary. Required dimensional correction in the new force-balance helper; absent helper in current Aeos means conditional applicability.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -973,7 +973,7 @@ void DiskForceBalance(FLOAT cellwidth, FLOAT z, FLOAT density, struct CGMdata& C`; `@@ -984,6 +984,7 @@ void DiskForceBalance(FLOAT cellwidth, FLOAT z, FLOAT density, struct CGMdata& C`; `@@ -1047,22 +1048,23 @@ void DiskForceBalance(FLOAT cellwidth, FLOAT z, FLOAT density, struct CGMdata& C`.

<a id="commit-352"></a>
## 352 — `2af13a74a` — 2022-11-22

doc changes

**Categories:** 4.

Documents pressure balance and explicit dark matter profile switches. Optional galaxy initializer documentation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`.

**Patch locations:** `@@ -4905,7 +4905,8 @@ Isolated Galaxy Evolution (31)`; `@@ -4959,6 +4960,11 @@ Isolated Galaxy Evolution (31)`.

<a id="commit-353"></a>
## 353 — `324468252` — 2022-11-22

Expanse GNU machine file

**Categories:** 4.

Adds Expanse GNU machine file. Site-specific configuration, not simulation science.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.sdsc-expanse-gnu`.

**Patch locations:** `@@ -0,0 +1,127 @@`.

<a id="commit-354"></a>
## 354 — `07f73f808` — 2022-12-08

Updated machine file for Expanse; GCC 10

**Categories:** 4.

Updates Expanse compiler/MPI requirements and flags, including GCC10 support. Adopt only for the actual toolchain.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.sdsc-expanse-gnu`.

**Patch locations:** `@@ -13,11 +13,10 @@`; `@@ -63,8 +62,8 @@ MACH_DEFINES   = -DLINUX -DH5_USE_16_API`; `@@ -124,4 +123,4 @@ MACH_LIBS         = $(LOCAL_LIBS_HDF5) $(LOCAL_LIBS_MACH)`.

<a id="commit-355"></a>
## 355 — `21ddc3c74` — 2023-03-17

Density & temperature shouldn't be variable prec

**Categories:** 3.

Uses double density/temperature in DiskForceBalance to match its actual callers and avoid variable-FLOAT reference type mismatch. Conditional on new galaxy initializer.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -103,8 +103,8 @@ double DiskGravityStellarAccel(FLOAT rcyl, FLOAT z);`; `@@ -962,7 +962,7 @@ double findZicm(FLOAT r, struct CGMdata& CGM_data){`.

<a id="commit-356"></a>
## 356 — `1c9de56ac` — 2023-04-05

Attempt to save out.compile as CircleCI artifact

**Categories:** 4.

Stores compile log as CI artifact. Useful diagnostics only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -263,6 +263,9 @@ jobs:`.

<a id="commit-357"></a>
## 357 — `b2637e8fe` — 2023-04-05

Fix type double -> float

**Categories:** 3.

Matches extern rcyl to its FLOAT definition, avoiding a cross-translation-unit type mismatch under nondefault precision. Conditional on restored force-balance code.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -973,7 +973,7 @@ void DiskForceBalance(FLOAT cellwidth, FLOAT z, double density, struct CGMdata&`.

<a id="commit-358"></a>
## 358 — `0c370fb3d` — 2023-04-05

More missing FLOATs

**Categories:** 3.

Makes remaining force-balance globals/externs consistently FLOAT. Required type consistency for the optional upstream initializer; do not change Aeos types without inspecting its definitions.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -108,7 +108,7 @@ void DiskForceBalance(FLOAT cellwidth, FLOAT z, double density, struct CGMdata&`; `@@ -1134,13 +1134,13 @@ double PbulgeComp_general(double rvalue, double zint)`; `@@ -1169,13 +1169,13 @@ double PstellarComp_general(double rvalue, double zint)`; `@@ -1208,12 +1208,12 @@ double PDMComp_general(double rvalue, double zint){`.

<a id="commit-359"></a>
## 359 — `c7dfafca1` — 2023-05-02

Merge branch 'main' into ressurect_disk_funcs

**Categories:** 4.

Nonempty merge resolution splits gravity global declarations and retains new profile switches. Preserve Aeos custom globals rather than importing upstream header wholesale.

**Merge inspection:** combined diff 1333 bytes; remerge diff 1479 bytes. Positive results are discussed above.

**Constituents in inventory:** [#256](batch-06.md#commit-256), [#257](batch-06.md#commit-257).

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

<a id="commit-360"></a>
## 360 — `c31ba26c0` — 2023-05-03

Merge pull request #201 from clairekope/ressurect_disk_funcs

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#345](batch-07.md#commit-345), [#346](batch-07.md#commit-346), [#347](batch-07.md#commit-347), [#348](batch-07.md#commit-348), [#349](batch-07.md#commit-349), [#350](batch-07.md#commit-350), [#351](batch-08.md#commit-351), [#352](batch-08.md#commit-352), [#353](batch-08.md#commit-353), [#354](batch-08.md#commit-354), [#355](batch-08.md#commit-355), [#356](batch-08.md#commit-356), [#357](batch-08.md#commit-357), [#358](batch-08.md#commit-358), [#359](batch-08.md#commit-359).

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker2.F`.

<a id="commit-361"></a>
## 361 — `1d7f9525b` — 2023-03-15

Ignore personal machine file

**Categories:** 4.

Ignores a contributor's personal machine file. No executable behavior; unnecessary locally unless using that filename.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `.gitignore`.

**Files:** `.gitignore`.

**Patch locations:** `@@ -56,3 +56,5 @@ doc/manual/build`.

<a id="commit-362"></a>
## 362 — `50ee32030` — 2022-11-18

Line limit tweak in Fortran

**Categories:** 3.

Duplicate fixed-form line-wrap fix for star_maker2 self-gravity expression (#349). Incorporate once, conditional on that model.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/star_maker2.F`.

**Patch locations:** `@@ -202,7 +202,8 @@ c`.

<a id="commit-363"></a>
## 363 — `6c960f9b9` — 2023-03-27

Ignore test files

**Categories:** 4.

Ignores test-output directory. Repository hygiene only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `.gitignore`.

**Files:** `.gitignore`.

**Patch locations:** `@@ -58,3 +58,5 @@ doc/manual/source/_build`.

<a id="commit-364"></a>
## 364 — `bdede6af7` — 2023-05-03

Updated format to address deprication warning-as-error

**Categories:** 4.

Updates Sphinx string/configuration syntax and intersphinx keys. Take final configuration including #383 and #574; no solver effect.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/conf.py`.

**Patch locations:** `@@ -84,7 +84,7 @@ exclude_patterns = []`; `@@ -103,10 +103,10 @@ html_theme = 'theme-agogo-local'`; `@@ -123,7 +123,7 @@ html_theme_path = ["."]`; `@@ -153,10 +153,10 @@ html_last_updated_fmt = '%b %d, %Y'`; `@@ -164,7 +164,7 @@ html_last_updated_fmt = '%b %d, %Y'`; additional hunks in the same patch.

<a id="commit-365"></a>
## 365 — `b01a95187` — 2023-05-04

Merge pull request #207 from clairekope/sphinx-update

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#361](batch-08.md#commit-361), [#362](batch-08.md#commit-362), [#363](batch-08.md#commit-363), [#364](batch-08.md#commit-364).

**Aeos-modified paths since common ancestor:** `.gitignore`.

**Files:** `.gitignore`, `doc/manual/source/conf.py`.

<a id="commit-366"></a>
## 366 — `cc7ffa649` — 2023-04-26

Fix C++11 compile-errors

**Categories:** 3,2.

Inserts whitespace between format-string literals and macros for C++11 parsing in Grid/PhotonPackage diagnostics. Aeos has widespread matching custom format usage; adapt compatible syntax while preserving output argument types.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/PhotonPackage.h`.

**Files:** `src/enzo/Grid.h`, `src/enzo/PhotonPackage.h`.

**Patch locations:** `@@ -1127,7 +1127,7 @@ gradient force to gravitational force for one-zone collapse test. */`; `@@ -56,12 +56,12 @@ public:`.

<a id="commit-367"></a>
## 367 — `2ebd75a2c` — 2023-05-04

Merge pull request #204 from data-exp-lab/compile_errors

**Categories:** 2,3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#366](batch-08.md#commit-366).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/PhotonPackage.h`.

**Files:** `src/enzo/Grid.h`, `src/enzo/PhotonPackage.h`.

<a id="commit-368"></a>
## 368 — `555397740` — 2023-03-17

added Wolcott-Green+ 2019 self-shielding

**Categories:** 4.

Adds RadiationShield=3 Wolcott-Green/Haiman 2019 H2 fit to Enzo's native solve_rate_cool.F; existing modes remain selectable. It does not implement Grackle H2_self_shielding or Emerick LWbackground_model. Adopting mode 3 is an explicit science change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/solve_rate_cool.F`.

**Patch locations:** `@@ -969,7 +969,7 @@ c -------------------------------------------------------------------`; `@@ -1164,7 +1164,8 @@ c -------------------------------------------------------------------`; `@@ -1180,7 +1181,7 @@ c -------------------------------------------------------------------`; `@@ -1206,7 +1207,22 @@ c               endif`.

<a id="commit-369"></a>
## 369 — `e0a15ce37` — 2023-03-17

changed doc for RadiationShield for including fit from Wolcott-Green et al 2019

**Categories:** 1.

Documents the new native RadiationShield mode. Clean documentation patch; enabling that mode in inputs remains a separate physics choice.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`.

**Patch locations:** `@@ -2686,7 +2686,8 @@ Background Radiation Parameters`.

<a id="commit-370"></a>
## 370 — `7e45f9e70` — 2023-05-04

Merge pull request #202 from mihirskulkarni/master

**Categories:** 1,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#368](batch-08.md#commit-368), [#369](batch-08.md#commit-369).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/solve_rate_cool.F`.

<a id="commit-371"></a>
## 371 — `03c549a0e` — 2019-06-28

Putting collapse test analysis in debug1 and allowing restarts that turn SelfGravity on

**Categories:** 3,2.

Adds gravity parameter/field allocation when enabling gravity on restart and gates collapse-test analysis. Adapt Aeos restart readers as a coherent feature with #374-376; runtime physics changes only when explicitly enabling gravity.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/New_Grid_ReadGrid.C`.

**Files:** `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/New_Grid_ReadGrid.C`.

**Patch locations:** `@@ -42,7 +42,7 @@ int CallProblemSpecificRoutines(TopGridData * MetaData, HierarchyEntry *ThisGrid`; `@@ -225,6 +225,10 @@ int Group_ReadDataHierarchy(FILE *fptr, hid_t Hfile_id, HierarchyEntry *Grid,`; `@@ -65,6 +65,7 @@ int grid::Group_ReadGrid(FILE *fptr, int GridID, HDF5_hid_t file_id,`; `@@ -223,10 +224,18 @@ int grid::Group_ReadGrid(FILE *fptr, int GridID, HDF5_hid_t file_id,`.

<a id="commit-372"></a>
## 372 — `00300b2be` — 2019-07-15

Bugfix for metallicity after SF

**Categories:** 3.

Corrects metal density adjustment during stellar formation, but this intermediate version writes a common metallicity into two tracer channels. Prefer final per-channel ratio scaling in #379, extended to Aeos tracers.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_AddFeedbackSphere.C`.

**Patch locations:** `@@ -922,10 +922,10 @@ int grid::AddFeedbackSphere(Star *cstar, int level, float radius, float DensityU`.

<a id="commit-373"></a>
## 373 — `d0222bd82` — 2019-07-15

Use metallicity field and radiating particles in CollapseTest

**Categories:** 4,2.

Changes CollapseTest to use Metallicity rather than SNColour and permits generated stellar radiation sources there. Opt-in test-model semantics and custom radiation overlap; not a universal disk bug fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolvePhotons.C`, `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/EvolvePhotons.C`, `src/enzo/Grid_CollapseTestInitializeGrid.C`, `src/enzo/StarParticleRadTransfer.C`.

**Patch locations:** `@@ -265,13 +265,14 @@ int EvolvePhotons(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; `@@ -141,7 +141,7 @@ int grid::CollapseTestInitializeGrid(int NumberOfSpheres,`; `@@ -39,7 +39,7 @@ int StarParticleRadTransfer(LevelHierarchyEntry *LevelArray[], int level,`.

<a id="commit-374"></a>
## 374 — `7fde4c6ea` — 2020-05-18

Adding ability to restart with WritePotential or ComputePotential

**Categories:** 3,2.

Allocates missing potential fields/boundary slots when WritePotential/ComputePotential is enabled on restart. Must adapt both grouped/new readers and field metadata without changing Aeos tracer order.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ExternalBoundary.h`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/New_Grid_ReadGrid.C`.

**Files:** `src/enzo/ExternalBoundary.h`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/New_Grid_ReadGrid.C`.

**Patch locations:** `@@ -13,6 +13,7 @@`; `@@ -113,6 +114,11 @@ class ExternalBoundary`; `@@ -557,7 +557,25 @@ int grid::Group_ReadGrid(FILE *fptr, int GridID, HDF5_hid_t file_id,`; `@@ -463,6 +463,14 @@ int Group_ReadAllData(char *name, HierarchyEntry *TopGrid, TopGridData &MetaData`; `@@ -513,8 +521,7 @@ int Group_ReadAllData(char *name, HierarchyEntry *TopGrid, TopGridData &MetaData`; additional hunks in the same patch.

<a id="commit-375"></a>
## 375 — `34dfe0f15` — 2020-05-28

Restart with write/compute potential work now in parallel

**Categories:** 3,2.

Moves potential/Phi allocation outside processor-local data-read branch so parallel grid metadata remains consistent. Conditional restart correctness; integrate with #374 and preserve custom fields.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/New_Grid_ReadGrid.C`.

**Files:** `src/enzo/New_Grid_ReadGrid.C`.

**Patch locations:** `@@ -395,48 +395,39 @@ int grid::Group_ReadGrid(FILE *fptr, int GridID, HDF5_hid_t file_id,`; `@@ -456,11 +447,6 @@ int grid::Group_ReadGrid(FILE *fptr, int GridID, HDF5_hid_t file_id,`.

<a id="commit-376"></a>
## 376 — `2afd2c73a` — 2020-06-17

Cleaned up setting subgrid gravity boundaries

**Categories:** 3,2.

Uses periodic/top-grid gravity boundary for roots and SubGridIsolated for descendants when initializing restart gravity. Required hierarchy consistency when turning gravity on at restart.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/New_Grid_ReadGrid.C`.

**Files:** `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/New_Grid_ReadGrid.C`.

**Patch locations:** `@@ -226,8 +226,12 @@ int Group_ReadDataHierarchy(FILE *fptr, hid_t Hfile_id, HierarchyEntry *Grid,`; `@@ -65,7 +65,6 @@ int grid::Group_ReadGrid(FILE *fptr, int GridID, HDF5_hid_t file_id,`; `@@ -225,16 +224,9 @@ int grid::Group_ReadGrid(FILE *fptr, int GridID, HDF5_hid_t file_id,`.

<a id="commit-377"></a>
## 377 — `09a8f14fb` — 2022-07-10

Merge branch 'fix-test-suite' into potential-restarts

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#010](batch-01.md#commit-010), [#011](batch-01.md#commit-011), [#012](batch-01.md#commit-012), [#013](batch-01.md#commit-013), [#014](batch-01.md#commit-014), [#015](batch-01.md#commit-015), [#016](batch-01.md#commit-016), [#017](batch-01.md#commit-017), [#018](batch-01.md#commit-018), [#019](batch-01.md#commit-019), [#020](batch-01.md#commit-020), [#021](batch-01.md#commit-021), [#022](batch-01.md#commit-022), [#023](batch-01.md#commit-023), [#024](batch-01.md#commit-024), [#025](batch-01.md#commit-025), [#026](batch-01.md#commit-026), [#027](batch-01.md#commit-027), [#028](batch-01.md#commit-028), [#029](batch-01.md#commit-029), [#030](batch-01.md#commit-030), [#031](batch-01.md#commit-031), [#032](batch-01.md#commit-032), [#033](batch-01.md#commit-033), [#034](batch-01.md#commit-034), [#035](batch-01.md#commit-035), [#036](batch-01.md#commit-036), [#037](batch-01.md#commit-037), [#038](batch-01.md#commit-038), [#039](batch-01.md#commit-039), [#040](batch-01.md#commit-040), [#041](batch-01.md#commit-041), [#042](batch-01.md#commit-042), [#043](batch-01.md#commit-043), [#044](batch-01.md#commit-044), [#045](batch-01.md#commit-045), [#047](batch-01.md#commit-047), [#048](batch-01.md#commit-048), [#049](batch-01.md#commit-049), [#050](batch-01.md#commit-050), [#051](batch-02.md#commit-051), [#052](batch-02.md#commit-052), [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056), [#057](batch-02.md#commit-057), [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068), [#069](batch-02.md#commit-069), [#070](batch-02.md#commit-070), [#071](batch-02.md#commit-071), [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074), [#075](batch-02.md#commit-075), [#076](batch-02.md#commit-076), [#077](batch-02.md#commit-077), [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079), [#080](batch-02.md#commit-080), [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114), [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveLevel.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `doc/manual/Makefile`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `doc/manual/source/reference/NestedGridParticles.rst`, `doc/manual/source/supplementary_info/EmbeddedPython.rst`, `doc/manual/source/user_guide/RunTestProblem.rst`, `doc/manual/source/user_guide/SampleParameterFiles.rst`, `doc/manual/source/user_guide/index.rst`, `doc/manual/source/user_guide/samples/SG64-L2.conf`, `doc/manual/source/user_guide/samples/wise2014_zoomin_update.enzo`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`, `src/enzo/ActiveParticleInitialize.C`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/DeleteRadiationSource.C`, `src/enzo/EvolveLevel.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_CalculateSmartStarAccretionRate.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_CreateParticleTypeGrouping.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.tigercpu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/StochasticForcing_Init.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/lcaperf.h`, `src/enzo/python_bridge/problemtype_handler.pyx`, `src/enzo/star_maker2.F`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`, `src/enzo/uuid.C`.

<a id="commit-378"></a>
## 378 — `d3767f422` — 2022-07-14

Merge remote-tracking branch 'upstream/main' into potential-restarts

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134), [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

<a id="commit-379"></a>
## 379 — `a94592e94` — 2022-07-14

Addressing two things from PR review

**Categories:** 3,2.

Scales each existing metal/color density by rho_new/rho_old after formation, preserving each abundance independently. Aeos still has the earlier factor multiplication. Adapt the same rule to its full elemental/dust/source tracer set; upstream's seven-field list is incomplete for Aeos. Also changes collapse-test diagnostic guard.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/Grid_AddFeedbackSphere.C`.

**Patch locations:** `@@ -42,7 +42,7 @@ int CallProblemSpecificRoutines(TopGridData * MetaData, HierarchyEntry *ThisGrid`; `@@ -116,6 +116,10 @@ int grid::AddFeedbackSphere(Star *cstar, int level, float radius, float DensityU`; `@@ -838,7 +842,8 @@ int grid::AddFeedbackSphere(Star *cstar, int level, float radius, float DensityU`; `@@ -898,6 +903,9 @@ int grid::AddFeedbackSphere(Star *cstar, int level, float radius, float DensityU`; `@@ -921,10 +929,11 @@ int grid::AddFeedbackSphere(Star *cstar, int level, float radius, float DensityU`.

<a id="commit-380"></a>
## 380 — `b774741a4` — 2023-05-08

Merge pull request #151 from jwise77/potential-restarts

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#371](batch-08.md#commit-371), [#372](batch-08.md#commit-372), [#373](batch-08.md#commit-373), [#374](batch-08.md#commit-374), [#375](batch-08.md#commit-375), [#376](batch-08.md#commit-376), [#377](batch-08.md#commit-377), [#378](batch-08.md#commit-378), [#379](batch-08.md#commit-379).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/Grid_AddFeedbackSphere.C`, `src/enzo/Grid_CollapseTestInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/StarParticleRadTransfer.C`.

<a id="commit-381"></a>
## 381 — `a156ac8c7` — 2023-05-08

Merge branch 'main' into docs-intersphinx

**Categories:** 4.

Remerge-diff retains removal of obsolete intersphinx config; subsequent #383 restores valid syntax. Documentation build resolution only.

**Merge inspection:** combined diff 0 bytes; remerge diff 945 bytes. Positive results are discussed above.

**Constituents in inventory:** [#161](batch-04.md#commit-161), [#162](batch-04.md#commit-162), [#163](batch-04.md#commit-163), [#164](batch-04.md#commit-164), [#165](batch-04.md#commit-165), [#166](batch-04.md#commit-166), [#167](batch-04.md#commit-167), [#168](batch-04.md#commit-168), [#169](batch-04.md#commit-169), [#170](batch-04.md#commit-170), [#171](batch-04.md#commit-171), [#172](batch-04.md#commit-172), [#173](batch-04.md#commit-173), [#174](batch-04.md#commit-174), [#175](batch-04.md#commit-175), [#176](batch-04.md#commit-176), [#177](batch-04.md#commit-177), [#178](batch-04.md#commit-178), [#179](batch-04.md#commit-179), [#180](batch-04.md#commit-180), [#181](batch-04.md#commit-181), [#182](batch-04.md#commit-182), [#183](batch-04.md#commit-183), [#184](batch-04.md#commit-184), [#185](batch-04.md#commit-185), [#186](batch-04.md#commit-186), [#187](batch-04.md#commit-187), [#188](batch-04.md#commit-188), [#189](batch-04.md#commit-189), [#190](batch-04.md#commit-190), [#191](batch-04.md#commit-191), [#192](batch-04.md#commit-192), [#193](batch-04.md#commit-193), [#194](batch-04.md#commit-194), [#195](batch-04.md#commit-195), [#196](batch-04.md#commit-196), [#197](batch-04.md#commit-197), [#198](batch-04.md#commit-198), [#199](batch-04.md#commit-199), [#200](batch-04.md#commit-200), [#201](batch-05.md#commit-201), [#202](batch-05.md#commit-202), [#203](batch-05.md#commit-203), [#204](batch-05.md#commit-204), [#205](batch-05.md#commit-205), [#206](batch-05.md#commit-206), [#207](batch-05.md#commit-207), [#208](batch-05.md#commit-208), [#209](batch-05.md#commit-209), [#210](batch-05.md#commit-210), [#211](batch-05.md#commit-211), [#212](batch-05.md#commit-212), [#213](batch-05.md#commit-213), [#214](batch-05.md#commit-214), [#215](batch-05.md#commit-215), [#216](batch-05.md#commit-216), [#217](batch-05.md#commit-217), [#218](batch-05.md#commit-218), [#219](batch-05.md#commit-219), [#220](batch-05.md#commit-220), [#221](batch-05.md#commit-221), [#222](batch-05.md#commit-222), [#223](batch-05.md#commit-223), [#224](batch-05.md#commit-224), [#225](batch-05.md#commit-225), [#226](batch-05.md#commit-226), [#227](batch-05.md#commit-227), [#228](batch-05.md#commit-228), [#229](batch-05.md#commit-229), [#230](batch-05.md#commit-230), [#231](batch-05.md#commit-231), [#232](batch-05.md#commit-232), [#256](batch-06.md#commit-256), [#257](batch-06.md#commit-257), [#345](batch-07.md#commit-345), [#346](batch-07.md#commit-346), [#347](batch-07.md#commit-347), [#348](batch-07.md#commit-348), [#349](batch-07.md#commit-349), [#350](batch-07.md#commit-350), [#351](batch-08.md#commit-351), [#352](batch-08.md#commit-352), [#353](batch-08.md#commit-353), [#354](batch-08.md#commit-354), [#355](batch-08.md#commit-355), [#356](batch-08.md#commit-356), [#357](batch-08.md#commit-357), [#358](batch-08.md#commit-358), [#359](batch-08.md#commit-359), [#360](batch-08.md#commit-360), [#361](batch-08.md#commit-361), [#362](batch-08.md#commit-362), [#363](batch-08.md#commit-363), [#364](batch-08.md#commit-364), [#365](batch-08.md#commit-365), [#366](batch-08.md#commit-366), [#367](batch-08.md#commit-367), [#368](batch-08.md#commit-368), [#369](batch-08.md#commit-369), [#370](batch-08.md#commit-370), [#371](batch-08.md#commit-371), [#372](batch-08.md#commit-372), [#373](batch-08.md#commit-373), [#374](batch-08.md#commit-374), [#375](batch-08.md#commit-375), [#376](batch-08.md#commit-376), [#377](batch-08.md#commit-377), [#378](batch-08.md#commit-378), [#379](batch-08.md#commit-379), [#380](batch-08.md#commit-380).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/FindSuperSourceByPosition.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonPackage.h`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleData.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `README.md`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `input/gen_equilibrium_table.py`, `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/EquilibriumTable.h`, `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/FDMCollapse.C`, `src/enzo/FindSuperSourceByPosition.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddFeedbackSphere.C`, `src/enzo/Grid_CollapseTestInitializeGrid.C`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_ComputeTemperatureField.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_GrackleCustomCoolRate.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_MagneticFieldResetter.C`, `src/enzo/Grid_ParallelFDMCollapseInitialize.C`, `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/InitializeLocal.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.scinet-niagara`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/ParallelFDMCollapseInitialize.C`, `src/enzo/PhotonPackage.h`, `src/enzo/ReadEquilibriumTable.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/SetStellarFeedbackEfficiency.C`, `src/enzo/StarParticleData.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/solve_rate_cool.F`, `src/enzo/sse2neon.h`, `src/enzo/star_maker2.F`, `src/enzo/typedefs.h`.

<a id="commit-382"></a>
## 382 — `d4053b5c4` — 2023-05-09

Specifying an OS for RTDs to avoid an SSL issue with the newest urllib

**Categories:** 1.

Adds ReadTheDocs OS/Python build configuration; no simulation change. Historic version pin should be checked during any documentation deployment.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.readthedocs.yaml`.

**Patch locations:** `@@ -0,0 +1,7 @@`.

<a id="commit-383"></a>
## 383 — `f84d63289` — 2023-05-09

Reintroduce intersphinx with updated syntax

**Categories:** 4.

Restores intersphinx with supported mapping syntax after #344. Documentation compatibility, not a physics correction.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/conf.py`.

**Patch locations:** `@@ -26,7 +26,8 @@ import sys, os`; `@@ -217,3 +218,9 @@ man_pages = [`.

<a id="commit-384"></a>
## 384 — `15a8281bd` — 2023-05-09

Merge pull request #210 from jwise77/docs-intersphinx

**Categories:** 1,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#344](batch-07.md#commit-344), [#381](batch-08.md#commit-381), [#382](batch-08.md#commit-382), [#383](batch-08.md#commit-383).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.readthedocs.yaml`, `doc/manual/source/conf.py`.

<a id="commit-385"></a>
## 385 — `8d0861580` — 2023-04-26

Add a conda makefile

**Categories:** 4.

Adds generic conda machine file. Compare with #234 and retain one final platform definition; no scientific method change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.conda`.

**Patch locations:** `@@ -0,0 +1,116 @@`.

<a id="commit-386"></a>
## 386 — `fb292095f` — 2023-05-09

Merge pull request #205 from data-exp-lab/conda-makefile

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#385](batch-08.md#commit-385).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.conda`.

<a id="commit-387"></a>
## 387 — `70980a53c` — 2023-05-10

Update grackle branch name from master to main (in CI tests)

**Categories:** 3.

CI clones Grackle main instead of removed master branch. For Aeos, preserve explicit main/newchem/legacy backend coverage rather than testing only upstream main.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -60,7 +60,7 @@ commands:`.

<a id="commit-388"></a>
## 388 — `1831fe142` — 2023-05-11

Merge pull request #211 from mabruzzo/upstream-grackle-branch

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#387](batch-08.md#commit-387).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-389"></a>
## 389 — `993dd47bb` — 2023-05-15

Merge https://github.com/enzo-project/enzo-dev into RotatingPopIII

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#201](batch-05.md#commit-201), [#202](batch-05.md#commit-202), [#203](batch-05.md#commit-203), [#204](batch-05.md#commit-204), [#205](batch-05.md#commit-205), [#206](batch-05.md#commit-206), [#207](batch-05.md#commit-207), [#208](batch-05.md#commit-208), [#209](batch-05.md#commit-209), [#210](batch-05.md#commit-210), [#211](batch-05.md#commit-211), [#212](batch-05.md#commit-212), [#213](batch-05.md#commit-213), [#214](batch-05.md#commit-214), [#215](batch-05.md#commit-215), [#216](batch-05.md#commit-216), [#217](batch-05.md#commit-217), [#218](batch-05.md#commit-218), [#219](batch-05.md#commit-219), [#220](batch-05.md#commit-220), [#221](batch-05.md#commit-221), [#222](batch-05.md#commit-222), [#223](batch-05.md#commit-223), [#224](batch-05.md#commit-224), [#225](batch-05.md#commit-225), [#226](batch-05.md#commit-226), [#227](batch-05.md#commit-227), [#228](batch-05.md#commit-228), [#229](batch-05.md#commit-229), [#230](batch-05.md#commit-230), [#231](batch-05.md#commit-231), [#232](batch-05.md#commit-232), [#256](batch-06.md#commit-256), [#257](batch-06.md#commit-257), [#344](batch-07.md#commit-344), [#345](batch-07.md#commit-345), [#346](batch-07.md#commit-346), [#347](batch-07.md#commit-347), [#348](batch-07.md#commit-348), [#349](batch-07.md#commit-349), [#350](batch-07.md#commit-350), [#351](batch-08.md#commit-351), [#352](batch-08.md#commit-352), [#353](batch-08.md#commit-353), [#354](batch-08.md#commit-354), [#355](batch-08.md#commit-355), [#356](batch-08.md#commit-356), [#357](batch-08.md#commit-357), [#358](batch-08.md#commit-358), [#359](batch-08.md#commit-359), [#360](batch-08.md#commit-360), [#361](batch-08.md#commit-361), [#362](batch-08.md#commit-362), [#363](batch-08.md#commit-363), [#364](batch-08.md#commit-364), [#365](batch-08.md#commit-365), [#366](batch-08.md#commit-366), [#367](batch-08.md#commit-367), [#368](batch-08.md#commit-368), [#369](batch-08.md#commit-369), [#370](batch-08.md#commit-370), [#371](batch-08.md#commit-371), [#372](batch-08.md#commit-372), [#373](batch-08.md#commit-373), [#374](batch-08.md#commit-374), [#375](batch-08.md#commit-375), [#376](batch-08.md#commit-376), [#377](batch-08.md#commit-377), [#378](batch-08.md#commit-378), [#379](batch-08.md#commit-379), [#380](batch-08.md#commit-380), [#381](batch-08.md#commit-381), [#382](batch-08.md#commit-382), [#383](batch-08.md#commit-383), [#384](batch-08.md#commit-384), [#385](batch-08.md#commit-385), [#386](batch-08.md#commit-386), [#387](batch-08.md#commit-387), [#388](batch-08.md#commit-388).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/FindSuperSourceByPosition.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/Make.config.objects`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonPackage.h`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleData.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `.readthedocs.yaml`, `README.md`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `input/gen_equilibrium_table.py`, `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/EquilibriumTable.h`, `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/FindSuperSourceByPosition.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddFeedbackSphere.C`, `src/enzo/Grid_CollapseTestInitializeGrid.C`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_ComputeTemperatureField.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_GrackleCustomCoolRate.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_MagneticFieldResetter.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.conda`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonPackage.h`, `src/enzo/ReadEquilibriumTable.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/SetStellarFeedbackEfficiency.C`, `src/enzo/StarParticleData.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/solve_rate_cool.F`, `src/enzo/sse2neon.h`, `src/enzo/star_maker2.F`, `src/enzo/typedefs.h`.

<a id="commit-390"></a>
## 390 — `ca4a04c6d` — 2023-05-15

Merge pull request #195 from drenniks/RotatingPopIII

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#333](batch-07.md#commit-333), [#334](batch-07.md#commit-334), [#335](batch-07.md#commit-335), [#336](batch-07.md#commit-336), [#337](batch-07.md#commit-337), [#338](batch-07.md#commit-338), [#339](batch-07.md#commit-339), [#340](batch-07.md#commit-340), [#341](batch-07.md#commit-341), [#342](batch-07.md#commit-342), [#343](batch-07.md#commit-343), [#389](batch-08.md#commit-389).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzo`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzotest`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`, `src/enzo/Grid_TestStarParticleInitializeGrid.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/PopIIIRotationModel.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/TestRadiatingStarParticleInitialize.C`, `src/enzo/TestStarParticleInitialize.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

<a id="commit-391"></a>
## 391 — `7bffe1f97` — 2023-06-19

Merge branch 'main' into libyt

**Categories:** 4.

Remerge-diff resolves an add/add conda machine file conflict by retaining expanded installation instructions. No solver behavior change.

**Merge inspection:** combined diff 0 bytes; remerge diff 911 bytes. Positive results are discussed above.

**Constituents in inventory:** [#333](batch-07.md#commit-333), [#334](batch-07.md#commit-334), [#335](batch-07.md#commit-335), [#336](batch-07.md#commit-336), [#337](batch-07.md#commit-337), [#338](batch-07.md#commit-338), [#339](batch-07.md#commit-339), [#340](batch-07.md#commit-340), [#341](batch-07.md#commit-341), [#342](batch-07.md#commit-342), [#343](batch-07.md#commit-343), [#344](batch-07.md#commit-344), [#345](batch-07.md#commit-345), [#346](batch-07.md#commit-346), [#347](batch-07.md#commit-347), [#348](batch-07.md#commit-348), [#349](batch-07.md#commit-349), [#350](batch-07.md#commit-350), [#351](batch-08.md#commit-351), [#352](batch-08.md#commit-352), [#353](batch-08.md#commit-353), [#354](batch-08.md#commit-354), [#355](batch-08.md#commit-355), [#356](batch-08.md#commit-356), [#357](batch-08.md#commit-357), [#358](batch-08.md#commit-358), [#359](batch-08.md#commit-359), [#360](batch-08.md#commit-360), [#361](batch-08.md#commit-361), [#362](batch-08.md#commit-362), [#363](batch-08.md#commit-363), [#364](batch-08.md#commit-364), [#365](batch-08.md#commit-365), [#366](batch-08.md#commit-366), [#367](batch-08.md#commit-367), [#368](batch-08.md#commit-368), [#369](batch-08.md#commit-369), [#370](batch-08.md#commit-370), [#371](batch-08.md#commit-371), [#372](batch-08.md#commit-372), [#373](batch-08.md#commit-373), [#374](batch-08.md#commit-374), [#375](batch-08.md#commit-375), [#376](batch-08.md#commit-376), [#377](batch-08.md#commit-377), [#378](batch-08.md#commit-378), [#379](batch-08.md#commit-379), [#380](batch-08.md#commit-380), [#381](batch-08.md#commit-381), [#382](batch-08.md#commit-382), [#383](batch-08.md#commit-383), [#384](batch-08.md#commit-384), [#385](batch-08.md#commit-385), [#386](batch-08.md#commit-386), [#387](batch-08.md#commit-387), [#388](batch-08.md#commit-388), [#389](batch-08.md#commit-389), [#390](batch-08.md#commit-390).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/PhotonPackage.h`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `.readthedocs.yaml`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzo`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzotest`, `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddFeedbackSphere.C`, `src/enzo/Grid_CollapseTestInitializeGrid.C`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`, `src/enzo/Grid_TestStarParticleInitializeGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.conda`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/PhotonPackage.h`, `src/enzo/PopIIIRotationModel.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/TestRadiatingStarParticleInitialize.C`, `src/enzo/TestStarParticleInitialize.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/solve_rate_cool.F`, `src/enzo/star_maker2.F`.

<a id="commit-392"></a>
## 392 — `9798f00ae` — 2023-06-19

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#306](batch-07.md#commit-306), [#309](batch-07.md#commit-309), [#311](batch-07.md#commit-311), [#328](batch-07.md#commit-328), [#332](batch-07.md#commit-332), [#333](batch-07.md#commit-333), [#334](batch-07.md#commit-334), [#335](batch-07.md#commit-335), [#336](batch-07.md#commit-336), [#337](batch-07.md#commit-337), [#338](batch-07.md#commit-338), [#339](batch-07.md#commit-339), [#340](batch-07.md#commit-340), [#341](batch-07.md#commit-341), [#342](batch-07.md#commit-342), [#343](batch-07.md#commit-343), [#344](batch-07.md#commit-344), [#345](batch-07.md#commit-345), [#346](batch-07.md#commit-346), [#347](batch-07.md#commit-347), [#348](batch-07.md#commit-348), [#349](batch-07.md#commit-349), [#350](batch-07.md#commit-350), [#351](batch-08.md#commit-351), [#352](batch-08.md#commit-352), [#353](batch-08.md#commit-353), [#354](batch-08.md#commit-354), [#355](batch-08.md#commit-355), [#356](batch-08.md#commit-356), [#357](batch-08.md#commit-357), [#358](batch-08.md#commit-358), [#359](batch-08.md#commit-359), [#360](batch-08.md#commit-360), [#361](batch-08.md#commit-361), [#362](batch-08.md#commit-362), [#363](batch-08.md#commit-363), [#364](batch-08.md#commit-364), [#365](batch-08.md#commit-365), [#366](batch-08.md#commit-366), [#367](batch-08.md#commit-367), [#368](batch-08.md#commit-368), [#369](batch-08.md#commit-369), [#370](batch-08.md#commit-370), [#371](batch-08.md#commit-371), [#372](batch-08.md#commit-372), [#373](batch-08.md#commit-373), [#374](batch-08.md#commit-374), [#375](batch-08.md#commit-375), [#376](batch-08.md#commit-376), [#377](batch-08.md#commit-377), [#378](batch-08.md#commit-378), [#379](batch-08.md#commit-379), [#380](batch-08.md#commit-380), [#381](batch-08.md#commit-381), [#382](batch-08.md#commit-382), [#383](batch-08.md#commit-383), [#384](batch-08.md#commit-384), [#385](batch-08.md#commit-385), [#386](batch-08.md#commit-386), [#387](batch-08.md#commit-387), [#388](batch-08.md#commit-388), [#389](batch-08.md#commit-389), [#390](batch-08.md#commit-390), [#391](batch-08.md#commit-391).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/PhotonPackage.h`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `.readthedocs.yaml`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzo`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzotest`, `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddFeedbackSphere.C`, `src/enzo/Grid_CollapseTestInitializeGrid.C`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`, `src/enzo/Grid_TestStarParticleInitializeGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.conda`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/PhotonPackage.h`, `src/enzo/PopIIIRotationModel.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/TestRadiatingStarParticleInitialize.C`, `src/enzo/TestStarParticleInitialize.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/solve_rate_cool.F`, `src/enzo/star_maker2.F`.

<a id="commit-393"></a>
## 393 — `feb02be46` — 2023-06-19

Fix syntax error in doc

**Categories:** 4.

Fixes libyt RST syntax and user-guide registration. Requires the new analysis documentation tree.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `doc/manual/source/user_guide/index.rst`.

**Patch locations:** `@@ -5,7 +5,7 @@ In Situ Python Analysis`; `@@ -13,16 +13,22 @@ Requirements`; `@@ -40,6 +46,7 @@ How to Configure`; `@@ -51,12 +58,14 @@ If you really want to change the name, you can go to`; `@@ -65,11 +74,12 @@ Please make sure the functions you called are defined inside the script. Otherwi`; additional hunks in the same patch.

<a id="commit-394"></a>
## 394 — `e50742b1b` — 2023-06-19

Fix syntax error in lists' hyperlink.

**Categories:** 4.

Repairs libyt requirements hyperlink syntax and paragraph formatting. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -12,18 +12,23 @@ Requirements`; `@@ -43,7 +48,7 @@ At the end, when the simulation is shutting down, Enzo calls FinalizeLibytInte`; `@@ -61,7 +66,9 @@ Please use const char*, or else, you have to make sure the lifetime of this`; `@@ -98,7 +105,7 @@ or to turn it off,`; `@@ -137,5 +144,5 @@ This is something libyt will update and improve in the future.`.

<a id="commit-395"></a>
## 395 — `cbc3bde07` — 2023-06-19

Typo.

**Categories:** 4.

Corrects libyt usage typo. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -125,7 +125,7 @@ This includes libyt header, links to the library, and adds library search pa`.

<a id="commit-396"></a>
## 396 — `a0d846f42` — 2024-02-16

Update link

**Categories:** 4.

Migrates libyt API/installation URLs to ReadTheDocs. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -12,28 +12,28 @@ Requirements`; `@@ -72,27 +72,27 @@ Currently, it is called inside EvolveLevel function.`; `@@ -104,8 +104,7 @@ or to turn it off,`; `@@ -114,7 +113,7 @@ The option will look for the following variables in the machine-specific Makefil`; `@@ -141,6 +140,7 @@ Please add OMPI_MCA_osc=sm,pt2pt before mpirun, for example:`.

<a id="commit-397"></a>
## 397 — `15af636b5` — 2024-02-16

fix link

**Categories:** 4.

Fixes the remaining inline-analysis URL. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -144,5 +144,5 @@ This is something libyt will update and improve in the future.`.

<a id="commit-398"></a>
## 398 — `4dbbb6c69` — 2024-02-17

Update requirements.

**Categories:** 4.

Documents independent libyt interactive/reload/Jupyter requirements. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -11,25 +11,38 @@ Requirements`.

<a id="commit-399"></a>
## 399 — `70af63f54` — 2024-02-17

Update How it works.

**Categories:** 4.

Documents interactive analysis lifecycle and UI modes. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -33,7 +33,7 @@ A brief description of each mode (option) is shown here. The options are mutuall`; `@@ -55,6 +55,10 @@ The CallInSitulibyt function in src/enzo/CallInSitulibyt.C conducts this`.

<a id="commit-400"></a>
## 400 — `c281d2e2e` — 2024-02-17

Fix page layout

**Categories:** 4.

Organizes libyt configuration guidance and script naming. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -11,7 +11,7 @@ Requirements`; `@@ -67,43 +67,50 @@ How to Configure`.
