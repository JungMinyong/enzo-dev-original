# Batch 06: commits 251–300

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-251"></a>
## 251 — `2443d3c95` — 2023-04-20

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Nonempty merge resolution adds the interactive-mode header to CallInSitulibyt. This header is later removed in #308; do not replay obsolete resolution independently.

**Merge inspection:** combined diff 485 bytes; remerge diff 662 bytes. Positive results are discussed above.

**Constituents in inventory:** [#250](batch-05.md#commit-250).

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/create_libyt_mapping.py`, `src/enzo/global_data.h`.

<a id="commit-252"></a>
## 252 — `3b25ec1cc` — 2023-04-21

Initialize interface before enzo includes

**Categories:** 4.

Isolates libyt initialization from Enzo macro-modified integer headers; optional ABI boundary arrangement, later refined for precision variants.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/enzo.C`.

**Patch locations:** `@@ -16,8 +16,28 @@`; `@@ -38,18 +58,9 @@ int ExposeDataHierarchy(TopGridData *MetaData, HierarchyEntry *Grid,`; `@@ -57,12 +68,12 @@ int InitializeLibytInterface(int argc, char *argv[])`; `@@ -60,7 +60,8 @@ int InitializePythonInterface(int argc, char **argv);`; `@@ -792,8 +793,8 @@ Eint32 MAIN_NAME(Eint32 argc, char *argv[])`.

<a id="commit-253"></a>
## 253 — `5b4bd5e83` — 2023-04-21

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Nonempty merge resolution retains isolated libyt initialization and opaque parameter pointers. Review with #252/#260; not independent new physics.

**Merge inspection:** combined diff 1122 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#252](batch-06.md#commit-252).

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/enzo.C`.

<a id="commit-254"></a>
## 254 — `fb8b53644` — 2023-04-21

Auto stash before merge of "libyt" and "data-exp-lab/libyt"

**Categories:** 4.

Adds blank lines/include-area formatting in libyt call file despite auto-stash subject; no scientific change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -12,8 +12,11 @@`.

<a id="commit-255"></a>
## 255 — `769691fe3` — 2023-04-21

Update parameter setting

**Categories:** 3.

Generated libyt mappings skip null string entries and update user-parameter access. Required null-safety fix if this optional exporter is adopted.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/create_libyt_mapping.py`.

**Patch locations:** `@@ -68,7 +68,7 @@ int InitializeLibytInterface()`; `@@ -62,15 +62,17 @@ def handle_char(var):`; `@@ -97,7 +99,7 @@ def handle_variable(var):`.

<a id="commit-256"></a>
## 256 — `2bb0db0c8` — 2023-04-18

Make all declarations on their own line

**Categories:** 2,4.

Splits global variable declarations onto separate lines for the mapper. Intended behavior-neutral refactor, but overlaps Aeos global_data.h; preserve all custom declarations and exact types.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

**Patch locations:** `@@ -114,7 +114,8 @@ EXTERN hydro_method HydroMethod;`; `@@ -239,7 +240,8 @@ EXTERN int NumberOfBufferZones;`; `@@ -247,19 +249,20 @@ EXTERN float GridVelocity[MAX_DIMENSION];`; `@@ -273,7 +276,8 @@ EXTERN FLOAT MultiRefineRegionStaggeredRefinement[MAX_STATIC_REGIONS];`; `@@ -285,8 +289,8 @@ EXTERN float PointSourceGravityCoreRadius;`; additional hunks in the same patch.

<a id="commit-257"></a>
## 257 — `acd119556` — 2023-04-21

Merge pull request #203 from data-exp-lab/single_line_defs

**Categories:** 2,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#256](batch-06.md#commit-256).

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

<a id="commit-258"></a>
## 258 — `34a2da2f8` — 2023-04-21

Merge branch 'main' of github.com:enzo-project/enzo-dev into libyt

**Categories:** 2,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#256](batch-06.md#commit-256), [#257](batch-06.md#commit-257).

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

<a id="commit-259"></a>
## 259 — `ed361e113` — 2023-04-21

Update finder functions

**Categories:** 3.

Regenerates libyt mappings with null checks and updated global declarations. Conditional exporter safety; upstream generated file is not complete for Aeos custom fields.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface_finderfunctions.inc`.

**Patch locations:** `@@ -55,18 +55,22 @@ yt_set_UserParameterDouble("DomainRightEdge", MAX_DIMENSION, DomainRightEdge);`; `@@ -190,11 +194,13 @@ yt_set_UserParameterDouble("ZEUSQuadraticArtificialViscosity", 1, &ZEUSQuadratic`; `@@ -203,7 +209,8 @@ yt_set_UserParameterLongLong("UseCoolingRefineRegion", 1, &UseCoolingRefineRegio`; `@@ -287,6 +294,7 @@ yt_set_UserParameterDouble("TimeActionRedshift", MAX_TIME_ACTIONS, TimeActionRed`; `@@ -304,18 +312,21 @@ yt_set_UserParameterLongLong("SimpleConstantBoundary", 1, &SimpleConstantBoundar`; additional hunks in the same patch.

<a id="commit-260"></a>
## 260 — `350614602` — 2023-04-21

Move everything into the single libyt interface call

**Categories:** 4.

Consolidates libyt startup into one interface call with argc/argv. Adopt coherent final lifecycle, not intermediate startup combinations.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/enzo.C`.

**Patch locations:** `@@ -58,9 +58,10 @@ int ExposeDataHierarchy(TopGridData *MetaData, HierarchyEntry *Grid,`; `@@ -60,8 +60,7 @@ int InitializePythonInterface(int argc, char **argv);`; `@@ -793,8 +792,7 @@ Eint32 MAIN_NAME(Eint32 argc, char *argv[])`.

<a id="commit-261"></a>
## 261 — `b1c804a02` — 2023-04-21

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#255](batch-06.md#commit-255), [#256](batch-06.md#commit-256), [#257](batch-06.md#commit-257), [#258](batch-06.md#commit-258), [#259](batch-06.md#commit-259), [#260](batch-06.md#commit-260).

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/create_libyt_mapping.py`, `src/enzo/enzo.C`, `src/enzo/global_data.h`.

<a id="commit-262"></a>
## 262 — `7d48aea6a` — 2023-04-24

First pass at grid::ConvertToLibyt

**Categories:** 4.

Adds grid-to-libyt adapter and Grid declaration. New optional API; later fixes active dimensions, ranks, particle pointers and lifetimes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Make.config.objects`, `src/enzo/global_data.h`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/Make.config.objects`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -49,6 +49,10 @@ struct HierarchyEntry;`; `@@ -2837,6 +2841,9 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -0,0 +1,76 @@`; `@@ -63,7 +63,68 @@ int InitializeLibytInterface(int argc, char *argv[])`; `@@ -440,6 +440,7 @@ OBJS_CONFIG_LIB = \`; additional hunks in the same patch.

<a id="commit-263"></a>
## 263 — `8faa3906c` — 2023-04-24

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#262](batch-06.md#commit-262).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Make.config.objects`, `src/enzo/global_data.h`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/Make.config.objects`, `src/enzo/global_data.h`.

<a id="commit-264"></a>
## 264 — `752ba4c60` — 2023-04-25

Refer to NumberOfGhostZones parameter

**Categories:** 3.

Exports NumberOfGhostZones instead of hard-coded three. Required metadata correctness if libyt is enabled with nonstandard ghost zones.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -98,17 +98,13 @@ int InitializeLibytInterface(int argc, char *argv[])`.

<a id="commit-265"></a>
## 265 — `31b779466` — 2023-04-25

Fix dtype setting

**Categories:** 3.

Fixes bytes-versus-bits dtype detection using precision-specific EYT_FLOAT macros. Required if libyt is ported; test all supported field/particle precision combinations.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/macros_and_parameters.h`.

**Patch locations:** `@@ -96,7 +96,7 @@ int InitializeLibytInterface(int argc, char *argv[])`; `@@ -245,6 +245,9 @@ typedef long long int   HDF5_hid_t;`; `@@ -262,6 +265,9 @@ typedef long long int   HDF5_hid_t;`; `@@ -279,6 +285,9 @@ typedef long long int   HDF5_hid_t;`; `@@ -296,6 +305,9 @@ typedef long long int   HDF5_hid_t;`; additional hunks in the same patch.

<a id="commit-266"></a>
## 266 — `b44ade855` — 2023-04-25

minor changes

**Categories:** 4.

Adds local-grid counts, metadata and parameter cleanup to evolving libyt integration. Conditional analysis infrastructure.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -69,8 +69,8 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -79,10 +79,16 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -150,8 +156,10 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -66,6 +66,12 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-267"></a>
## 267 — `205d69561` — 2023-04-25

Continue with libyt calls

**Categories:** 4.

Builds libyt field registration and grid hierarchy and corrects processor ownership access. Incomplete interface stage; use final validated integration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -50,6 +50,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -80,15 +81,12 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -157,10 +155,102 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -42,7 +42,7 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -65,62 +65,6 @@ int InitializeLibytInterface(int argc, char *argv[])`.

<a id="commit-268"></a>
## 268 — `8ce98745f` — 2023-04-25

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#264](batch-06.md#commit-264), [#265](batch-06.md#commit-265), [#266](batch-06.md#commit-266), [#267](batch-06.md#commit-267).

**Aeos-modified paths since common ancestor:** `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/macros_and_parameters.h`.

<a id="commit-269"></a>
## 269 — `265165866` — 2023-04-25

Starting to move back to idiomatic enzoisms

**Categories:** 4.

Moves grid conversion toward Enzo interfaces and pointer/reference conventions. Requires companion hierarchy changes; not an independent solver fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -227,32 +227,30 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -30,7 +30,7 @@`; `@@ -40,20 +40,26 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -75,7 +81,7 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-270"></a>
## 270 — `c668a6c27` — 2023-04-25

draft libyt hierarchy

**Categories:** 4.

Introduces recursive hierarchy exposure to libyt. Optional traversal API; later changes fix IDs, dimensions and ranks.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExposeHierarchyToLibyt.C`.

**Patch locations:** `@@ -0,0 +1,74 @@`.

<a id="commit-271"></a>
## 271 — `e8e90428b` — 2023-04-25

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#269](batch-06.md#commit-269), [#270](batch-06.md#commit-270).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

<a id="commit-272"></a>
## 272 — `00f523e5f` — 2023-04-25

Almost done with enzo-specific code

**Categories:** 4.

Connects hierarchy exporter and libyt parameter flow; optional feature scaffolding with later corrections.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`.

**Patch locations:** `@@ -36,8 +36,9 @@ int  GetUnits(float *DensityUnits, float *LengthUnits,`; `@@ -240,13 +241,18 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -47,7 +47,7 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`.

<a id="commit-273"></a>
## 273 — `050dfa699` — 2023-04-25

Adding to make config objects

**Categories:** 4.

Registers hierarchy exporter in object list and aligns Grid method declaration; conditional build plumbing.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Make.config.objects`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Make.config.objects`.

**Patch locations:** `@@ -2842,7 +2842,7 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -189,6 +189,7 @@ OBJS_CONFIG_LIB = \`.

<a id="commit-274"></a>
## 274 — `24a731242` — 2023-04-25

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#272](batch-06.md#commit-272), [#273](batch-06.md#commit-273).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Make.config.objects`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid.h`, `src/enzo/Make.config.objects`.

<a id="commit-275"></a>
## 275 — `95642fff4` — 2023-04-25

Call libyt API yt_set_Parameters.

**Categories:** 3.

Calls yt_set_Parameters before using the libyt hierarchy. Required API lifecycle fix for the new feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -166,6 +166,11 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-276"></a>
## 276 — `430909f25` — 2023-04-25

Need libyt.h to compile and typo when calling Grid::ConvertToLibyt

**Categories:** 3.

Corrects ConvertToLibyt call signature and required header; compilation repair conditional on libyt integration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExposeHierarchyToLibyt.C`.

**Patch locations:** `@@ -11,6 +11,9 @@`; `@@ -46,8 +49,8 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`.

<a id="commit-277"></a>
## 277 — `63fc793ea` — 2023-04-26

Originally I was trying to match the include in data_exp_lab.

**Categories:** 4.

Updates libyt header path spelling in adapter files. Superseded by installed public header conventions.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -12,7 +12,7 @@`; `@@ -18,7 +18,7 @@`.

<a id="commit-278"></a>
## 278 — `ca12e2d61` — 2023-04-26

Bug, params initialize through malloc, no guarantee that pointer is valid.

**Categories:** 3.

Initializes fig_basename in malloc-allocated libyt parameters, avoiding an uninitialized string pointer. Required feature safety.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -111,6 +111,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-279"></a>
## 279 — `78c179947` — 2023-04-26

Recursion only has 8 inputs, compile success.

**Categories:** 3.

Removes extra argument from recursive hierarchy exporter calls. Conditional compilation/interface repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExposeHierarchyToLibyt.C`.

**Patch locations:** `@@ -57,7 +57,7 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`; `@@ -66,7 +66,7 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`.

<a id="commit-280"></a>
## 280 — `9b59ee834` — 2023-04-26

Add TODO list and includes whole libyt workflow.

**Categories:** 4.

Completes commit/analysis/free API calls and replaces the interactive stub in EvolveLevel. Optional feature; final call scheduling changes later.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -167,11 +167,20 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -234,6 +243,10 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -263,6 +276,27 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -257,8 +257,10 @@ void my_exit(int status);`; `@@ -847,7 +849,8 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; additional hunks in the same patch.

<a id="commit-281"></a>
## 281 — `897d6ebf9` — 2023-04-26

Add more comments.

**Categories:** 4.

Adds libyt comments and removes an unused temporary name buffer; maintenance only within optional feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -177,9 +177,10 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-282"></a>
## 282 — `68ab3d198` — 2023-04-26

Align how conda env includes libyt header.

**Categories:** 4.

Changes libyt includes and adds temporary grid debug output. Not suitable as a final snapshot; #285 removes the logging.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -13,8 +13,8 @@`; `@@ -13,8 +13,8 @@`; `@@ -12,7 +12,7 @@`; `@@ -18,7 +18,7 @@`; `@@ -62,6 +62,17 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; additional hunks in the same patch.

<a id="commit-283"></a>
## 283 — `7867cfa02` — 2023-04-26

Bug, this is due to we allocate params through malloc.

**Categories:** 3.

Initializes num_par_types before passing malloc-allocated libyt parameters. Required feature safety before particle support exists.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -170,6 +170,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-284"></a>
## 284 — `41702555b` — 2023-04-26

Merge branch 'libyt' into libyt-PR

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#283](batch-06.md#commit-283).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

<a id="commit-285"></a>
## 285 — `d2faef392` — 2023-05-02

Update the comments and remove printing some debug stuff.

**Categories:** 4.

Removes temporary grid debug prints and refreshes comments. Conditional cleanup, no solver change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -177,9 +177,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -62,17 +62,6 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-286"></a>
## 286 — `515d0270c` — 2023-05-03

Remove Make.mach.libyt

**Categories:** 4.

Deletes a developer-specific libyt machine file. Do not infer that locally needed configurations must be removed.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.libyt`.

**Patch locations:** `@@ -1,116 +0,0 @@`.

<a id="commit-287"></a>
## 287 — `511e770a6` — 2023-04-26

Fix compilation issues

**Categories:** 3.

Corrects hierarchy recursion and Grid conversion reference/pointer access to compile. Conditional interface repair; use with merge resolution #288.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`.

**Files:** `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -12,6 +12,7 @@`; `@@ -46,7 +47,7 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`; `@@ -54,7 +55,7 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`; `@@ -63,7 +64,7 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`; `@@ -2842,7 +2842,7 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; additional hunks in the same patch.

<a id="commit-288"></a>
## 288 — `55bdd56d3` — 2023-05-03

Merge branch 'libyt' into libyt-PR

**Categories:** 3.

Nonempty merge resolution reconciles libyt Grid adapter headers and reference-member access. Conditional compile fix; no independent scientific model change.

**Merge inspection:** combined diff 1859 bytes; remerge diff 1790 bytes. Positive results are discussed above.

**Constituents in inventory:** [#287](batch-06.md#commit-287).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`.

**Files:** `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ConvertToLibyt.C`.

<a id="commit-289"></a>
## 289 — `eceff2c02` — 2023-05-03

Merge pull request #1 from cindytsai/libyt-PR

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#242](batch-05.md#commit-242), [#245](batch-05.md#commit-245), [#247](batch-05.md#commit-247), [#248](batch-05.md#commit-248), [#249](batch-05.md#commit-249), [#251](batch-06.md#commit-251), [#253](batch-06.md#commit-253), [#254](batch-06.md#commit-254), [#261](batch-06.md#commit-261), [#263](batch-06.md#commit-263), [#268](batch-06.md#commit-268), [#271](batch-06.md#commit-271), [#274](batch-06.md#commit-274), [#275](batch-06.md#commit-275), [#276](batch-06.md#commit-276), [#277](batch-06.md#commit-277), [#278](batch-06.md#commit-278), [#279](batch-06.md#commit-279), [#280](batch-06.md#commit-280), [#281](batch-06.md#commit-281), [#282](batch-06.md#commit-282), [#283](batch-06.md#commit-283), [#284](batch-06.md#commit-284), [#285](batch-06.md#commit-285), [#286](batch-06.md#commit-286), [#288](batch-06.md#commit-288).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/EvolveLevel.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

<a id="commit-290"></a>
## 290 — `02c472f4b` — 2023-05-04

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#282](batch-06.md#commit-282), [#284](batch-06.md#commit-284), [#285](batch-06.md#commit-285), [#286](batch-06.md#commit-286), [#287](batch-06.md#commit-287), [#288](batch-06.md#commit-288), [#289](batch-06.md#commit-289).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/Make.mach.libyt`.

<a id="commit-291"></a>
## 291 — `80b5d384f` — 2023-05-04

Set index_offset = 1.

**Categories:** 3.

Sets libyt index_offset=1 to match exported grid IDs. Required analysis hierarchy consistency for this implementation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -156,6 +156,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-292"></a>
## 292 — `844451c80` — 2023-05-04

Merge pull request #2 from cindytsai/libyt-PR

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#290](batch-06.md#commit-290), [#291](batch-06.md#commit-291).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

<a id="commit-293"></a>
## 293 — `71e518d9c` — 2023-05-04

Add hydro method

**Categories:** 4.

Adds HydroMethod to libyt metadata mapping. Required for analysis interpretation but does not change chosen simulation hydro solver.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/create_libyt_mapping.py`.

**Patch locations:** `@@ -18,6 +18,7 @@ yt_set_UserParameterLongLong("CheckpointRestart", 1, &CheckpointRestart);`; `@@ -15,6 +15,7 @@ libyt_functions = {`.

<a id="commit-294"></a>
## 294 — `21450dcbe` — 2023-05-04

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#292](batch-06.md#commit-292), [#293](batch-06.md#commit-293).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/create_libyt_mapping.py`.

<a id="commit-295"></a>
## 295 — `63cdc70c1` — 2023-05-04

Remove debug stuff at initialization stage, fix typo while merging.

**Categories:** 3.

Fixes a merged GridInfoArray argument, metadata types and analysis timing labels; also removes debugging initialization. Conditional libyt correctness.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/EvolveLevel.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`.

**Patch locations:** `@@ -848,10 +848,10 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; `@@ -51,7 +51,7 @@ int ExposeHierarchyToLibyt(TopGridData *MetaData, HierarchyEntry *Grid,`; `@@ -13,8 +13,8 @@`; `@@ -30,7 +30,7 @@ int InitializeLibytByItself(long long argc, char *argv[])`; `@@ -64,17 +64,7 @@ int InitializeLibytInterface(int argc, char *argv[])`; additional hunks in the same patch.

<a id="commit-296"></a>
## 296 — `bdd13a8f4` — 2023-05-04

Match how data_exp_lab include libyt header

**Categories:** 4.

Aligns installed libyt header spelling; optional integration cleanup.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -13,8 +13,8 @@`.

<a id="commit-297"></a>
## 297 — `64da0432d` — 2023-05-04

Accidentally changed libyt log to debug mode, change it back

**Categories:** 4.

Returns libyt verbosity to INFO from temporary DEBUG. No evolution physics change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -30,7 +30,7 @@ int InitializeLibytByItself(long long argc, char *argv[])`.

<a id="commit-298"></a>
## 298 — `297e81247` — 2023-05-04

Make counter starts at 0.

**Categories:** 3.

Initializes libyt output counter to zero and documents script/check_data choices. Required initialized state for deterministic analysis naming.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -31,8 +31,9 @@ int InitializeLibytByItself(long long argc, char *argv[])`.

<a id="commit-299"></a>
## 299 — `a3f531a88` — 2023-05-05

Merge pull request #3 from cindytsai/libyt-PR

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#294](batch-06.md#commit-294), [#295](batch-06.md#commit-295), [#296](batch-06.md#commit-296), [#297](batch-06.md#commit-297), [#298](batch-06.md#commit-298).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/EvolveLevel.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`.

<a id="commit-300"></a>
## 300 — `089cf729a` — 2023-05-05

Merge branch 'libyt-PR' into libyt

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#296](batch-06.md#commit-296), [#297](batch-06.md#commit-297), [#298](batch-06.md#commit-298).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`.
