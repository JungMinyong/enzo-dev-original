# Batch 12: commits 551–577

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-551"></a>
## 551 — `3d9df1815` — 2025-07-11

Merge pull request #24 from cindytsai/fix

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#544](batch-11.md#commit-544).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

<a id="commit-552"></a>
## 552 — `d31817555` — 2025-07-11

Merge pull request #209 from data-exp-lab/libyt

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#233](batch-05.md#commit-233), [#234](batch-05.md#commit-234), [#235](batch-05.md#commit-235), [#236](batch-05.md#commit-236), [#237](batch-05.md#commit-237), [#238](batch-05.md#commit-238), [#239](batch-05.md#commit-239), [#240](batch-05.md#commit-240), [#241](batch-05.md#commit-241), [#242](batch-05.md#commit-242), [#243](batch-05.md#commit-243), [#244](batch-05.md#commit-244), [#245](batch-05.md#commit-245), [#246](batch-05.md#commit-246), [#247](batch-05.md#commit-247), [#248](batch-05.md#commit-248), [#249](batch-05.md#commit-249), [#250](batch-05.md#commit-250), [#251](batch-06.md#commit-251), [#252](batch-06.md#commit-252), [#253](batch-06.md#commit-253), [#254](batch-06.md#commit-254), [#255](batch-06.md#commit-255), [#258](batch-06.md#commit-258), [#259](batch-06.md#commit-259), [#260](batch-06.md#commit-260), [#261](batch-06.md#commit-261), [#262](batch-06.md#commit-262), [#263](batch-06.md#commit-263), [#264](batch-06.md#commit-264), [#265](batch-06.md#commit-265), [#266](batch-06.md#commit-266), [#267](batch-06.md#commit-267), [#268](batch-06.md#commit-268), [#269](batch-06.md#commit-269), [#270](batch-06.md#commit-270), [#271](batch-06.md#commit-271), [#272](batch-06.md#commit-272), [#273](batch-06.md#commit-273), [#274](batch-06.md#commit-274), [#275](batch-06.md#commit-275), [#276](batch-06.md#commit-276), [#277](batch-06.md#commit-277), [#278](batch-06.md#commit-278), [#279](batch-06.md#commit-279), [#280](batch-06.md#commit-280), [#281](batch-06.md#commit-281), [#282](batch-06.md#commit-282), [#283](batch-06.md#commit-283), [#284](batch-06.md#commit-284), [#285](batch-06.md#commit-285), [#286](batch-06.md#commit-286), [#287](batch-06.md#commit-287), [#288](batch-06.md#commit-288), [#289](batch-06.md#commit-289), [#290](batch-06.md#commit-290), [#291](batch-06.md#commit-291), [#292](batch-06.md#commit-292), [#293](batch-06.md#commit-293), [#294](batch-06.md#commit-294), [#295](batch-06.md#commit-295), [#296](batch-06.md#commit-296), [#297](batch-06.md#commit-297), [#298](batch-06.md#commit-298), [#299](batch-06.md#commit-299), [#300](batch-06.md#commit-300), [#301](batch-07.md#commit-301), [#302](batch-07.md#commit-302), [#303](batch-07.md#commit-303), [#304](batch-07.md#commit-304), [#305](batch-07.md#commit-305), [#306](batch-07.md#commit-306), [#307](batch-07.md#commit-307), [#308](batch-07.md#commit-308), [#309](batch-07.md#commit-309), [#310](batch-07.md#commit-310), [#311](batch-07.md#commit-311), [#312](batch-07.md#commit-312), [#313](batch-07.md#commit-313), [#314](batch-07.md#commit-314), [#315](batch-07.md#commit-315), [#316](batch-07.md#commit-316), [#317](batch-07.md#commit-317), [#318](batch-07.md#commit-318), [#319](batch-07.md#commit-319), [#320](batch-07.md#commit-320), [#321](batch-07.md#commit-321), [#322](batch-07.md#commit-322), [#323](batch-07.md#commit-323), [#324](batch-07.md#commit-324), [#325](batch-07.md#commit-325), [#326](batch-07.md#commit-326), [#327](batch-07.md#commit-327), [#328](batch-07.md#commit-328), [#329](batch-07.md#commit-329), [#330](batch-07.md#commit-330), [#331](batch-07.md#commit-331), [#332](batch-07.md#commit-332), [#391](batch-08.md#commit-391), [#392](batch-08.md#commit-392), [#393](batch-08.md#commit-393), [#394](batch-08.md#commit-394), [#395](batch-08.md#commit-395), [#396](batch-08.md#commit-396), [#397](batch-08.md#commit-397), [#398](batch-08.md#commit-398), [#399](batch-08.md#commit-399), [#400](batch-08.md#commit-400), [#401](batch-09.md#commit-401), [#402](batch-09.md#commit-402), [#403](batch-09.md#commit-403), [#404](batch-09.md#commit-404), [#443](batch-09.md#commit-443), [#444](batch-09.md#commit-444), [#445](batch-09.md#commit-445), [#446](batch-09.md#commit-446), [#447](batch-09.md#commit-447), [#448](batch-09.md#commit-448), [#449](batch-09.md#commit-449), [#450](batch-09.md#commit-450), [#451](batch-10.md#commit-451), [#452](batch-10.md#commit-452), [#453](batch-10.md#commit-453), [#454](batch-10.md#commit-454), [#455](batch-10.md#commit-455), [#456](batch-10.md#commit-456), [#457](batch-10.md#commit-457), [#458](batch-10.md#commit-458), [#459](batch-10.md#commit-459), [#460](batch-10.md#commit-460), [#461](batch-10.md#commit-461), [#462](batch-10.md#commit-462), [#463](batch-10.md#commit-463), [#464](batch-10.md#commit-464), [#465](batch-10.md#commit-465), [#466](batch-10.md#commit-466), [#467](batch-10.md#commit-467), [#468](batch-10.md#commit-468), [#469](batch-10.md#commit-469), [#470](batch-10.md#commit-470), [#471](batch-10.md#commit-471), [#472](batch-10.md#commit-472), [#473](batch-10.md#commit-473), [#474](batch-10.md#commit-474), [#475](batch-10.md#commit-475), [#476](batch-10.md#commit-476), [#477](batch-10.md#commit-477), [#478](batch-10.md#commit-478), [#479](batch-10.md#commit-479), [#480](batch-10.md#commit-480), [#481](batch-10.md#commit-481), [#482](batch-10.md#commit-482), [#483](batch-10.md#commit-483), [#484](batch-10.md#commit-484), [#485](batch-10.md#commit-485), [#486](batch-10.md#commit-486), [#487](batch-10.md#commit-487), [#488](batch-10.md#commit-488), [#489](batch-10.md#commit-489), [#490](batch-10.md#commit-490), [#491](batch-10.md#commit-491), [#492](batch-10.md#commit-492), [#493](batch-10.md#commit-493), [#494](batch-10.md#commit-494), [#495](batch-10.md#commit-495), [#496](batch-10.md#commit-496), [#497](batch-10.md#commit-497), [#498](batch-10.md#commit-498), [#499](batch-10.md#commit-499), [#500](batch-10.md#commit-500), [#501](batch-11.md#commit-501), [#502](batch-11.md#commit-502), [#503](batch-11.md#commit-503), [#523](batch-11.md#commit-523), [#524](batch-11.md#commit-524), [#525](batch-11.md#commit-525), [#526](batch-11.md#commit-526), [#527](batch-11.md#commit-527), [#528](batch-11.md#commit-528), [#529](batch-11.md#commit-529), [#530](batch-11.md#commit-530), [#531](batch-11.md#commit-531), [#532](batch-11.md#commit-532), [#533](batch-11.md#commit-533), [#534](batch-11.md#commit-534), [#535](batch-11.md#commit-535), [#536](batch-11.md#commit-536), [#537](batch-11.md#commit-537), [#538](batch-11.md#commit-538), [#539](batch-11.md#commit-539), [#540](batch-11.md#commit-540), [#541](batch-11.md#commit-541), [#542](batch-11.md#commit-542), [#543](batch-11.md#commit-543), [#544](batch-11.md#commit-544), [#549](batch-11.md#commit-549), [#550](batch-11.md#commit-550), [#551](batch-12.md#commit-551).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/reference/MakeOptions.rst`, `doc/manual/source/user_guide/AnalyzingWithYT.rst`, `doc/manual/source/user_guide/ControllingDataOutput.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `doc/manual/source/user_guide/building_enzo.rst`, `doc/manual/source/user_guide/index.rst`, `src/enzo/ActiveParticle.h`, `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/CallInSitulibyt.C`, `src/enzo/CheckForLibytCall.C`, `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/create_libyt_mapping.py`, `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

<a id="commit-553"></a>
## 553 — `838b41153` — 2025-08-23

Merge remote-tracking branch 'enzo-dev/main' into fix

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#549](batch-11.md#commit-549), [#550](batch-11.md#commit-550), [#551](batch-12.md#commit-551), [#552](batch-12.md#commit-552).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

<a id="commit-554"></a>
## 554 — `8e6c0dbb7` — 2025-08-23

Accidentally make it io for test it. Change it back.

**Categories:** 3.

Restores ordinary libyt particle type name DarkMatter after experimental io naming. Required metadata consistency with the selected frontend; review population naming before exporting Aeos stars.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -228,7 +228,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-555"></a>
## 555 — `b43a4fd97` — 2025-08-23

Update doc about time-based libyt call enzo param

**Categories:** 4.

Documents dtLibytCall and TimeLastLibytCall. Explicitly note this cadence can constrain simulation timesteps via #548.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/user_guide/ControllingDataOutput.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -3897,6 +3897,17 @@ libyt In Situ Python Analysis`; `@@ -116,6 +116,8 @@ CycleLastDataDump. (So if you change CycleSkipDataDump from 0 to 10`; `@@ -109,14 +109,19 @@ General`.

<a id="commit-556"></a>
## 556 — `560f32117` — 2025-08-23

Update libyt dependency.

**Categories:** 4.

Updates documented libyt dependency requirements. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -21,7 +21,7 @@ We can compile libyt using different options based on our used cases, so tha`.

<a id="commit-557"></a>
## 557 — `a89aeb79b` — 2025-08-23

Merge pull request #25 from cindytsai/fix

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#545](batch-11.md#commit-545), [#546](batch-11.md#commit-546), [#547](batch-11.md#commit-547), [#548](batch-11.md#commit-548), [#552](batch-12.md#commit-552), [#553](batch-12.md#commit-553), [#554](batch-12.md#commit-554), [#555](batch-12.md#commit-555), [#556](batch-12.md#commit-556).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/InitializeNew.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/user_guide/ControllingDataOutput.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/CheckForLibytCall.C`, `src/enzo/EvolveHierarchy.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeNew.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

<a id="commit-558"></a>
## 558 — `1599f74ab` — 2025-08-23

precision-32/64 and particles-32/64 can compile

**Categories:** 3,2.

Makes generated metadata exports respect baryon and particle FLOAT widths. Required for libyt precision variants, but upstream generated variables/types do not cover Aeos additions; regenerate and validate.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface_finderfunctions.inc`.

**Patch locations:** `@@ -4,6 +4,12 @@`; `@@ -44,8 +50,8 @@ YT_SET_USERPARAM_INTEGER("MaximumGravityRefinementLevel", 1, &MaximumGravityRefi`; `@@ -63,8 +69,8 @@ YT_SET_USERPARAM_INTEGER("MinimumSubgridEdge", 1, &MinimumSubgridEdge);`; `@@ -86,28 +92,28 @@ for (i = 0; i < MAX_NUMBER_OF_BARYON_FIELDS; i++){`; `@@ -135,8 +141,8 @@ YT_SET_USERPARAM_INTEGER("RadiativeCoolingModel", 1, &RadiativeCoolingModel);`; additional hunks in the same patch.

<a id="commit-559"></a>
## 559 — `47c082a7a` — 2025-08-23

precision-32/64 and particles-32/64 can compile

**Categories:** 3.

Updates non-generated libyt metadata exports for particle precision as well as baryon precision. Companion ABI fix for #558.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -26,6 +26,12 @@`; `@@ -112,12 +118,12 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`; `@@ -126,9 +132,9 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`; `@@ -151,8 +157,8 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`.

<a id="commit-560"></a>
## 560 — `59ab5fa36` — 2025-08-23

Merge pull request #26 from cindytsai/fix

**Categories:** 2,3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#558](batch-12.md#commit-558), [#559](batch-12.md#commit-559).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`.

<a id="commit-561"></a>
## 561 — `01e25b8c0` — 2025-08-23

Fix cannot compile without using libyt.

**Categories:** 3.

Guards time-based libyt timestep and initialization blocks with USE_LIBYT, restoring feature-disabled builds. Required if adopting #546-548; no issue if the feature is absent.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/InitializeNew.C`.

**Files:** `src/enzo/EvolveHierarchy.C`, `src/enzo/InitializeNew.C`.

**Patch locations:** `@@ -420,12 +420,14 @@ int EvolveHierarchy(HierarchyEntry &TopGrid, TopGridData &MetaData,`; `@@ -881,9 +881,11 @@ int InitializeNew(char *filename, HierarchyEntry &TopGrid,`.

<a id="commit-562"></a>
## 562 — `a1346e1bf` — 2025-08-23

Merge pull request #27 from cindytsai/fix

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#561](batch-12.md#commit-561).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/InitializeNew.C`.

**Files:** `src/enzo/EvolveHierarchy.C`, `src/enzo/InitializeNew.C`.

<a id="commit-563"></a>
## 563 — `7ed1dbc22` — 2025-08-27

rename grid_unit_length to cell_width

**Categories:** 4.

Renames local grid_unit_length to cell_width without changing particle-volume multiplication. Conditional readability cleanup only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -52,12 +52,12 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -126,7 +126,7 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-564"></a>
## 564 — `18812cdde` — 2025-08-27

Merge pull request #249 from data-exp-lab/libyt

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#545](batch-11.md#commit-545), [#546](batch-11.md#commit-546), [#547](batch-11.md#commit-547), [#548](batch-11.md#commit-548), [#553](batch-12.md#commit-553), [#554](batch-12.md#commit-554), [#555](batch-12.md#commit-555), [#556](batch-12.md#commit-556), [#557](batch-12.md#commit-557), [#558](batch-12.md#commit-558), [#559](batch-12.md#commit-559), [#560](batch-12.md#commit-560), [#561](batch-12.md#commit-561), [#562](batch-12.md#commit-562), [#563](batch-12.md#commit-563).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/InitializeNew.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/user_guide/ControllingDataOutput.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/CheckForLibytCall.C`, `src/enzo/EvolveHierarchy.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/InitializeNew.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

<a id="commit-565"></a>
## 565 — `8af7bd31b` — 2026-08-07

Migrate Enzo build system to modern CMake

**Categories:** 2,4.

Introduces CMake source lists/options/dependency discovery plus assorted source compatibility changes. Upstream source lists omit Aeos IndividualStar, deterministic-SN and backend-profile interfaces; default MAX_BARYONS=30 is inadequate for typical Aeos tracer sets. Plan a separate build migration with explicit feature/source/precision parity; do not cherry-pick as-is.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/Grid_ComputeDomainBoundaryMassFlux.C`, `src/enzo/Star_ComputePhotonRates.C`.

**Files:** `.gitignore`, `CMakeLists.txt`, `Makefile`, `cmake/AutoShowConfig.cmake`, `cmake/EnzoOptions.cmake`, `cmake/FindDependencies.cmake`, `cmake/FindGrackle.cmake`, `cmake/FindHYPRE.cmake`, `src/CMakeLists.txt`, `src/P-GroupFinder/CMakeLists.txt`, `src/P-GroupFinder/find_subgroups.c`, `src/P-GroupFinder/sources.cmake`, `src/anyl/CMakeLists.txt`, `src/anyl/sources.cmake`, `src/enzo/CMakeLists.txt`, `src/enzo/Grid_ComputeDomainBoundaryMassFlux.C`, `src/enzo/PopIIIRotationModel.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/sources.cmake`, `src/enzohop/CMakeLists.txt`, `src/enzohop/enzohop.C`, `src/enzohop/slice.h`, `src/enzohop/sources.cmake`, `src/inits/CMakeLists.txt`, `src/inits/sources.cmake`, `src/lcaperf/CMakeLists.txt`, `src/ring/CMakeLists.txt`, `src/ring/sources.cmake`.

**Patch locations:** `@@ -10,8 +10,9 @@ syntax: glob`; `@@ -0,0 +1,34 @@`; `@@ -0,0 +1,38 @@`; `@@ -0,0 +1,82 @@`; `@@ -0,0 +1,218 @@`; additional hunks in the same patch.

<a id="commit-566"></a>
## 566 — `f0101f15f` — 2026-08-07

Fix compiler warnings and main return types across tools

**Categories:** 3,4.

Corrects main return types and HDF5 hsize_t narrowing; also suppresses a one-based utility indexing warning, adds global warning suppressions and creates output directories. Split useful portable C/C++ repairs from CMake-specific choices; suppressions do not fix underlying type/format errors.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `CMakeLists.txt`, `src/P-GroupFinder/properties.c`, `src/enzo/ActiveParticle.h`, `src/lcaperf/jb-attribute.C`, `src/lcaperf/jb-columns.C`, `src/lcaperf/jb-counter.C`, `src/lcaperf/jb-delete.C`, `src/lcaperf/jb-derive.C`, `src/lcaperf/jb-global.C`, `src/lcaperf/jb-header.C`, `src/lcaperf/jb-merge.C`, `src/lcaperf/jb-print.C`, `src/lcaperf/jb-promote.C`, `src/lcaperf/jb-region.C`, `src/lcaperf/jb-rename.C`.

**Patch locations:** `@@ -10,6 +10,8 @@ list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")`; `@@ -21,6 +23,10 @@ if (CMAKE_Fortran_COMPILER_ID STREQUAL "GNU")`; `@@ -86,7 +86,10 @@ void get_properties(struct particle_data *p, int len, float *pcm, float *pmtot,`; `@@ -614,7 +614,7 @@ namespace ActiveParticleHelpers {`; `@@ -17,7 +17,7 @@`; additional hunks in the same patch.

<a id="commit-567"></a>
## 567 — `47a6fd04e` — 2026-08-07

Set bounded parallel build level using nproc/nprocs or default to 4 cores

**Categories:** 4.

Bounds the CMake wrapper parallel job count to detected CPUs with fallback four. Optional infrastructure; detected CPUs can still exceed a shared login node's allocated resources, so honor explicit job limits.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `Makefile`.

**Patch locations:** `@@ -1,6 +1,7 @@`; `@@ -8,31 +9,31 @@ all: build`.

<a id="commit-568"></a>
## 568 — `35fb2d051` — 2026-08-07

Migrate documentation, CI workflows, and purge legacy Makefile build system

**Categories:** 2,4.

Deletes legacy Makefiles, machine files and configure while migrating CI/docs/runner to CMake. Direct conflict with Aeos backend/LW make options and local machine configuration. Defer deletion until CMake reproduces all custom build profiles and source lists.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/Make.mach.ncsa-bluewaters-gnu`, `src/enzo/Make.mach.tacc-stampede-intel`, `src/enzo/Makefile`.

**Files:** `.circleci/config.yml`, `README.md`, `configure`, `doc/manual/source/faq/index.rst`, `doc/manual/source/reference/CMakeOptions.rst`, `doc/manual/source/reference/LegacyMakeOptions.rst`, `doc/manual/source/reference/MakeOptions.rst`, `doc/manual/source/reference/index.rst`, `doc/manual/source/user_guide/bootcamp.rst`, `doc/manual/source/user_guide/building_enzo.rst`, `run/test_runner.py`, `src/Makefile`, `src/P-GroupFinder/Make.config.objects`, `src/P-GroupFinder/Makefile`, `src/anyl/Make.config.objects`, `src/anyl/Makefile`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.arizona`, `src/enzo/Make.mach.conda`, `src/enzo/Make.mach.cuda`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.gordon`, `src/enzo/Make.mach.gtech-pace`, `src/enzo/Make.mach.hits-magny`, `src/enzo/Make.mach.hotfoot-condor`, `src/enzo/Make.mach.kolob`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.nasa-aitken-rome`, `src/enzo/Make.mach.nasa-discover`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/Make.mach.ncsa-bluedrop`, `src/enzo/Make.mach.ncsa-bluewaters-gnu`, `src/enzo/Make.mach.ncsa-cobalt`, `src/enzo/Make.mach.nics-kraken`, `src/enzo/Make.mach.nics-kraken-gnu`, `src/enzo/Make.mach.nics-kraken-gnu-yt`, `src/enzo/Make.mach.nics-nautilus`, `src/enzo/Make.mach.orange`, `src/enzo/Make.mach.ornl-jaguar-pgi`, `src/enzo/Make.mach.scinet`, `src/enzo/Make.mach.scinet-niagara`, `src/enzo/Make.mach.sdsc-comet`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/Make.mach.sunnyvale`, `src/enzo/Make.mach.tacc-stampede-gnu`, `src/enzo/Make.mach.tacc-stampede-intel`, `src/enzo/Make.mach.tigercpu`, `src/enzo/Make.mach.trestles`, `src/enzo/Make.mach.triton`, `src/enzo/Make.mach.triton-gnu`, `src/enzo/Make.mach.triton-intel`, `src/enzo/Make.mach.ubuntu`, `src/enzo/Make.mach.unknown`, `src/enzo/Make.settings.allphysics`, `src/enzo/Make.settings.test-suite`, `src/enzo/Makefile`, `src/enzohop/Make.config.objects`, `src/enzohop/Makefile`, `src/inits/Make.config.objects`, `src/inits/Makefile`, `src/inits/Makefile.harkness`, `src/inits/Makefile32`, `src/lcaperf/Makefile`, `src/ring/Make.config.objects`, `src/ring/Makefile`.

**Patch locations:** `@@ -28,7 +28,7 @@ commands:`; `@@ -114,13 +114,9 @@ commands:`; `@@ -132,49 +128,25 @@ commands:`; `@@ -236,7 +208,7 @@ jobs:`; `@@ -267,7 +239,7 @@ jobs:`; additional hunks in the same patch.

<a id="commit-569"></a>
## 569 — `26b57191d` — 2026-08-08

Fixing malformed table in CMake options doc page

**Categories:** 3.

Repairs CMake option documentation table formatting. Conditional documentation build fix only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/reference/CMakeOptions.rst`.

**Patch locations:** `@@ -80,14 +80,14 @@ Option                  Default      Description`.

<a id="commit-570"></a>
## 570 — `1acb4f054` — 2026-08-08

Configure Grackle and HYPRE search paths for CircleCI

**Categories:** 4.

Updates CMake Grackle/HYPRE discovery and CI prefix paths/dependencies. Adapt explicit dependency prefixes for legacy/main/newchem; dependency discovery alone must not choose the wrong physics backend.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `cmake/FindGrackle.cmake`, `cmake/FindHYPRE.cmake`.

**Patch locations:** `@@ -8,6 +8,9 @@ commands:`; `@@ -34,14 +37,7 @@ commands:`; `@@ -114,7 +110,7 @@ commands:`; `@@ -135,17 +131,17 @@ commands:`; `@@ -183,6 +179,7 @@ jobs:`; additional hunks in the same patch.

<a id="commit-571"></a>
## 571 — `6c6472dd7` — 2026-08-11

Fix Grackle precision handling and build issues across compile configurations

**Categories:** 3,2.

Adds GrackleFieldBuffer conversions when Enzo field and gr_float widths differ, with copy-back for evolved fields, cooling-time/rate outputs and RT inputs. Current Aeos passes raw pointers. Port helper plus all affected wrappers together while preserving custom dust/LW/RT/backend logic; also contains analysis/C include type repairs and CI cache churn. Require cross-precision chemistry/energy checks before trusting a compile-only pass.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_ComputeCoolingTime.C`, `src/enzo/Grid_GrackleWrapper.C`.

**Files:** `.circleci/config.yml`, `src/anyl/AnalyzeCluster.C`, `src/enzo/Grid_ComputeCoolingTime.C`, `src/enzo/Grid_GrackleCustomCoolRate.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/preincludes.h`, `src/enzo/smooth_deposit_c.c`.

**Patch locations:** `@@ -168,13 +168,13 @@ jobs:`; `@@ -220,13 +220,13 @@ jobs:`; `@@ -78,9 +78,9 @@ int CommunicationSumValues(FLOAT *values, int number);`; `@@ -1276,9 +1276,9 @@ void my_exit(int status)`; `@@ -271,32 +271,41 @@ int grid::ComputeCoolingTime(float *cooling_time, int CoolingTimeOnly)`; additional hunks in the same patch.

<a id="commit-572"></a>
## 572 — `08ff4c237` — 2026-10-19

Fix CMake option names, CI matrix, build type, and transfer/MPI-off builds

**Categories:** 3,4,2.

Repairs CMake option spellings/default build type, source selection for transfer/MPI-off builds, generated version/config writes and CI matrix. Necessary corrections if migrating, but custom Aeos options/source groups must be integrated separately.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `CMakeLists.txt`, `cmake/AutoShowConfig.cmake`, `cmake/EnzoOptions.cmake`, `cmake/GenerateVersion.cmake`, `cmake/WriteIfDifferent.cmake`, `src/CMakeLists.txt`, `src/enzo/CMakeLists.txt`, `src/enzo/sources.cmake`.

**Patch locations:** `@@ -110,7 +110,7 @@ commands:`; `@@ -124,25 +124,26 @@ commands:`; `@@ -3,6 +3,11 @@ cmake_minimum_required(VERSION 3.20)`; `@@ -2,45 +2,23 @@`; `@@ -64,7 +42,8 @@ void auto_show_config(FILE *fp) {`; additional hunks in the same patch.

<a id="commit-573"></a>
## 573 — `595cf7700` — 2026-10-19

CI: build legacy tags with Makefiles, and disable hypre in the no-MPI build

**Categories:** 3.

CI builds older gold-standard tags with legacy Make and disables MPI-dependent HYPRE in serial builds. Required historical-baseline compatibility if adopting new CMake CI; infrastructure only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -110,8 +110,14 @@ commands:`; `@@ -141,7 +147,8 @@ commands:`.

<a id="commit-574"></a>
## 574 — `928fc1205` — 2026-10-19

docs: update dead ipython intersphinx URL

**Categories:** 4.

Updates the dead IPython intersphinx URL in the newer Sphinx mapping. Documentation only; prerequisite context differs from Aeos.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/conf.py`.

**Patch locations:** `@@ -220,7 +220,7 @@ man_pages = [`.

<a id="commit-575"></a>
## 575 — `45f4c64b9` — 2026-10-20

Merge pull request #254 from jwise77/cmake

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#565](batch-12.md#commit-565), [#566](batch-12.md#commit-566), [#567](batch-12.md#commit-567), [#568](batch-12.md#commit-568), [#569](batch-12.md#commit-569), [#570](batch-12.md#commit-570), [#571](batch-12.md#commit-571), [#572](batch-12.md#commit-572), [#573](batch-12.md#commit-573), [#574](batch-12.md#commit-574).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/Grid_ComputeCoolingTime.C`, `src/enzo/Grid_ComputeDomainBoundaryMassFlux.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/Make.mach.ncsa-bluewaters-gnu`, `src/enzo/Make.mach.tacc-stampede-intel`, `src/enzo/Makefile`, `src/enzo/Star_ComputePhotonRates.C`.

**Files:** `.circleci/config.yml`, `.gitignore`, `CMakeLists.txt`, `Makefile`, `README.md`, `cmake/AutoShowConfig.cmake`, `cmake/EnzoOptions.cmake`, `cmake/FindDependencies.cmake`, `cmake/FindGrackle.cmake`, `cmake/FindHYPRE.cmake`, `cmake/GenerateVersion.cmake`, `cmake/WriteIfDifferent.cmake`, `configure`, `doc/manual/source/conf.py`, `doc/manual/source/faq/index.rst`, `doc/manual/source/reference/CMakeOptions.rst`, `doc/manual/source/reference/LegacyMakeOptions.rst`, `doc/manual/source/reference/MakeOptions.rst`, `doc/manual/source/reference/index.rst`, `doc/manual/source/user_guide/bootcamp.rst`, `doc/manual/source/user_guide/building_enzo.rst`, `run/test_runner.py`, `src/CMakeLists.txt`, `src/Makefile`, `src/P-GroupFinder/CMakeLists.txt`, `src/P-GroupFinder/Make.config.objects`, `src/P-GroupFinder/Makefile`, `src/P-GroupFinder/find_subgroups.c`, `src/P-GroupFinder/properties.c`, `src/P-GroupFinder/sources.cmake`, `src/anyl/AnalyzeCluster.C`, `src/anyl/CMakeLists.txt`, `src/anyl/Make.config.objects`, `src/anyl/Makefile`, `src/anyl/sources.cmake`, `src/enzo/ActiveParticle.h`, `src/enzo/CMakeLists.txt`, `src/enzo/Grid_ComputeCoolingTime.C`, `src/enzo/Grid_ComputeDomainBoundaryMassFlux.C`, `src/enzo/Grid_GrackleCustomCoolRate.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.arizona`, `src/enzo/Make.mach.conda`, `src/enzo/Make.mach.cuda`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.gordon`, `src/enzo/Make.mach.gtech-pace`, `src/enzo/Make.mach.hits-magny`, `src/enzo/Make.mach.hotfoot-condor`, `src/enzo/Make.mach.kolob`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.nasa-aitken-rome`, `src/enzo/Make.mach.nasa-discover`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/Make.mach.ncsa-bluedrop`, `src/enzo/Make.mach.ncsa-bluewaters-gnu`, `src/enzo/Make.mach.ncsa-cobalt`, `src/enzo/Make.mach.nics-kraken`, `src/enzo/Make.mach.nics-kraken-gnu`, `src/enzo/Make.mach.nics-kraken-gnu-yt`, `src/enzo/Make.mach.nics-nautilus`, `src/enzo/Make.mach.orange`, `src/enzo/Make.mach.ornl-jaguar-pgi`, `src/enzo/Make.mach.scinet`, `src/enzo/Make.mach.scinet-niagara`, `src/enzo/Make.mach.sdsc-comet`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/Make.mach.sunnyvale`, `src/enzo/Make.mach.tacc-stampede-gnu`, `src/enzo/Make.mach.tacc-stampede-intel`, `src/enzo/Make.mach.tigercpu`, `src/enzo/Make.mach.trestles`, `src/enzo/Make.mach.triton`, `src/enzo/Make.mach.triton-gnu`, `src/enzo/Make.mach.triton-intel`, `src/enzo/Make.mach.ubuntu`, `src/enzo/Make.mach.unknown`, `src/enzo/Make.settings.allphysics`, `src/enzo/Make.settings.test-suite`, `src/enzo/Makefile`, `src/enzo/PopIIIRotationModel.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/preincludes.h`, `src/enzo/smooth_deposit_c.c`, `src/enzo/sources.cmake`, `src/enzohop/CMakeLists.txt`, `src/enzohop/Make.config.objects`, `src/enzohop/Makefile`, `src/enzohop/enzohop.C`, `src/enzohop/slice.h`, `src/enzohop/sources.cmake`, `src/inits/CMakeLists.txt`, `src/inits/Make.config.objects`, `src/inits/Makefile`, `src/inits/Makefile.harkness`, `src/inits/Makefile32`, `src/inits/sources.cmake`, `src/lcaperf/CMakeLists.txt`, `src/lcaperf/Makefile`, `src/lcaperf/jb-attribute.C`, `src/lcaperf/jb-columns.C`, `src/lcaperf/jb-counter.C`, `src/lcaperf/jb-delete.C`, `src/lcaperf/jb-derive.C`, `src/lcaperf/jb-global.C`, `src/lcaperf/jb-header.C`, `src/lcaperf/jb-merge.C`, `src/lcaperf/jb-print.C`, `src/lcaperf/jb-promote.C`, `src/lcaperf/jb-region.C`, `src/lcaperf/jb-rename.C`, `src/ring/CMakeLists.txt`, `src/ring/Make.config.objects`, `src/ring/Makefile`, `src/ring/sources.cmake`.

<a id="commit-576"></a>
## 576 — `5ed618ce9` — 2026-10-26

Fixing FluxCorrection = 2 undo index and density creation

**Categories:** 3,2.

Confirmed in Aeos: right-face sibling rollback iterates ffield but subtracts flux arrays indexed by field, mixing corrections across variables. Fix that indexing. Separately, upstream floors nonpositive color fields instead of rolling back the entire cell; that changes conservation/positivity behavior and must be adapted for Aeos species/element fields, measured separately from the unambiguous index repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_CorrectForRefinedFluxes.C`.

**Files:** `src/enzo/Grid_CorrectForRefinedFluxes.C`.

**Patch locations:** `@@ -82,6 +82,8 @@ int grid::CorrectForRefinedFluxes(fluxes *InitialFluxes,`; `@@ -542,12 +544,23 @@ int grid::CorrectForRefinedFluxes(fluxes *InitialFluxes,`; `@@ -641,8 +654,8 @@ int grid::CorrectForRefinedFluxes(fluxes *InitialFluxes,`.

<a id="commit-577"></a>
## 577 — `7409c9a3e` — 2026-10-29

Merge pull request #257 from aqua-hl/fix-fc2-undo

**Categories:** 2,3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#576](batch-12.md#commit-576).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_CorrectForRefinedFluxes.C`.

**Files:** `src/enzo/Grid_CorrectForRefinedFluxes.C`.
