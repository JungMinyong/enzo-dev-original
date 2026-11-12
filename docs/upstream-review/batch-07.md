# Batch 07: commits 301–350

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-301"></a>
## 301 — `a8ac9f295` — 2023-05-06

Find the bug, grid_dimension defined in libyt is active dimension

**Categories:** 3.

Exports active grid dimensions rather than allocated dimensions including ghosts. Essential hierarchy/data-interpretation fix if libyt is enabled.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -51,7 +51,7 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-302"></a>
## 302 — `cf382d8b8` — 2023-05-06

Merge pull request #4 from cindytsai/libyt-PR

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#300](batch-06.md#commit-300), [#301](batch-07.md#commit-301).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

<a id="commit-303"></a>
## 303 — `a4aa3773c` — 2023-05-09

Use particle array pointers

**Categories:** 4.

Adds ordinary particle array export and dtype macros to libyt. New analysis capability; incomplete until #305 and later unit/type fixes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/macros_and_parameters.h`.

**Patch locations:** `@@ -171,7 +171,51 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -213,7 +257,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -58,9 +58,6 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -85,5 +82,20 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -211,6 +211,7 @@ typedef long long int   HDF5_hid_t;`; additional hunks in the same patch.

<a id="commit-304"></a>
## 304 — `1af7b7d5c` — 2023-05-09

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#299](batch-06.md#commit-299), [#302](batch-07.md#commit-302), [#303](batch-07.md#commit-303).

**Aeos-modified paths since common ancestor:** `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/macros_and_parameters.h`.

<a id="commit-305"></a>
## 305 — `8928eced3` — 2023-05-09

Fix bug

**Categories:** 3.

Registers particle type/attributes before yt_set_Parameters and corrects particle pointers. Required companion fix for #303.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -168,10 +168,17 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -217,11 +224,6 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -288,10 +290,6 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -83,19 +83,22 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-306"></a>
## 306 — `9a693d365` — 2023-05-09

Merge pull request #5 from cindytsai/libyt

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#304](batch-07.md#commit-304), [#305](batch-07.md#commit-305).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

<a id="commit-307"></a>
## 307 — `d5c2d3b8a` — 2023-05-10

Make libyt header to libyt.h, so that it is easier to install.

**Categories:** 4.

Normalizes all adapters to installed libyt.h. Optional dependency integration cleanup.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -13,8 +13,8 @@`; `@@ -13,8 +13,8 @@`; `@@ -12,10 +12,10 @@`; `@@ -18,7 +18,7 @@`; `@@ -13,8 +13,8 @@`.

<a id="commit-308"></a>
## 308 — `e8ca554f6` — 2023-05-10

Remove libyt_interactive_mode.h header and initialize the doc.

**Categories:** 4.

Removes obsolete interactive header and begins analysis documentation. Adopt final installed API include conventions.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/supplementary_info/PythonInSituAnalysis.rst`, `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/CallInSitulibyt.C`, `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -0,0 +1,24 @@`; `@@ -14,7 +14,6 @@`; `@@ -14,7 +14,6 @@`; `@@ -14,7 +14,6 @@`.

<a id="commit-309"></a>
## 309 — `485ff9468` — 2023-05-10

Merge pull request #6 from cindytsai/libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#307](batch-07.md#commit-307), [#308](batch-07.md#commit-308).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/supplementary_info/PythonInSituAnalysis.rst`, `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface.C`.

<a id="commit-310"></a>
## 310 — `c7d5744a6` — 2023-05-10

To make libyt work both in normal mode and interactive mode.

**Categories:** 4.

Makes unsupported interactive mode diagnostic nonfatal, supporting normal-mode libyt use. Deliberate analysis error-policy change; review desired failure behavior.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -330,7 +330,8 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-311"></a>
## 311 — `9cedc5e3d` — 2023-05-10

Merge pull request #7 from cindytsai/libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#310](batch-07.md#commit-310).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

<a id="commit-312"></a>
## 312 — `1cd9a4fc8` — 2023-05-25

Start writing doc for libyt.

**Categories:** 4.

Moves initial libyt documentation from supplementary information into the user guide. Requires the optional feature; no executable patch.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/supplementary_info/PythonInSituAnalysis.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -1,24 +0,0 @@`; `@@ -0,0 +1,50 @@`.

<a id="commit-313"></a>
## 313 — `fdf3de9fe` — 2023-05-25

Add how it works.

**Categories:** 4.

Explains libyt lifecycle, borrowed simulation arrays and cleanup. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -17,12 +17,16 @@ Please follow the links to install the requirements.`.

<a id="commit-314"></a>
## 314 — `fd2361ef9` — 2023-05-25

Add links.

**Categories:** 4.

Adds libyt API/workflow links. Documentation only; use final links after later URL migrations.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -17,6 +17,9 @@ Please follow the links to install the requirements.`; `@@ -28,9 +31,6 @@ After in situ analysis is done, libyt frees resources allocated for itself,`.

<a id="commit-315"></a>
## 315 — `a6050e2dc` — 2023-05-25

Update how to configure and how to compile.

**Categories:** 4.

Expands compile/configure documentation and removes a temporary analysis function call. No new physical model; final analysis script contract must be explicit.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -10,10 +10,12 @@ Requirements`; `@@ -33,14 +35,77 @@ At the end, when the simulation is shutting down, Enzo calls FinalizeLibytInte`; `@@ -324,8 +324,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-316"></a>
## 316 — `f50d0af8f` — 2023-05-26

Finished writing the doc

**Categories:** 4.

Completes script placement, compilation and MPI launch instructions for libyt. Optional feature documentation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -40,7 +40,7 @@ Some settings are hard-coded inside Enzo, you can customize it to your own needs`; `@@ -60,6 +60,8 @@ Just put them right after the comments TODO: yt_run_Function and yt_run_Functi`; `@@ -105,15 +107,24 @@ This includes libyt header, links to the library, and adds library search pa`.

<a id="commit-317"></a>
## 317 — `43400fc47` — 2023-05-26

They should be in the same line.

**Categories:** 4.

Joins the libyt/embedded-Python incompatibility warning onto one paragraph. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -86,8 +86,7 @@ or to turn it off,`.

<a id="commit-318"></a>
## 318 — `fe39cf820` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Edits introductory libyt explanation. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -2,7 +2,8 @@`.

<a id="commit-319"></a>
## 319 — `18f0f7292` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Clarifies that in-situ analysis avoids output to disk before analysis. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -4,7 +4,7 @@ In Situ Python Analysis`.

<a id="commit-320"></a>
## 320 — `0c6a4d40d` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Uses HTTPS yt link and clearer wording. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -5,7 +5,7 @@ In Situ Python Analysis`.

<a id="commit-321"></a>
## 321 — `86622aeaf` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Clarifies dependency installation instructions. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -9,7 +9,8 @@ Here, we use yt <https://yt-project.org>_ as an analysis platform.`.

<a id="commit-322"></a>
## 322 — `cebdea7fa` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Formats libyt requirements list/hyperlinks. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -16,7 +16,7 @@ Below are links to the build and runtime requirements, which must be installed.`.

<a id="commit-323"></a>
## 323 — `d99d73a64` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Clarifies that Enzo pauses for analysis after a computation cycle. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -26,7 +26,7 @@ You can find how libyt works more in detail here <https://calab-ntu.github.`.

<a id="commit-324"></a>
## 324 — `c47607cdc` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Clarifies ownership of metadata export to libyt. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -28,7 +28,7 @@ At initialization stage, libyt imports inline Python script inline.py an`.

<a id="commit-325"></a>
## 325 — `1aa12aaca` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Names the CallInSitulibyt workflow more clearly. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -27,7 +27,7 @@ You can find how libyt works more in detail here <https://calab-ntu.github.`.

<a id="commit-326"></a>
## 326 — `4679721e8` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Documents borrowed array pointers and potential yt copies. Useful lifetime/memory caveat if enabling analysis; no solver change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -29,7 +29,7 @@ At initialization stage, libyt imports inline Python script inline.py an`.

<a id="commit-327"></a>
## 327 — `696d0e7ef` — 2023-05-26

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Corrects grammar of libyt data wrapping explanation. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -30,7 +30,7 @@ When Enzo finishes its computation in a cycle, the whole simulation pauses and s`.

<a id="commit-328"></a>
## 328 — `ee9e504f8` — 2023-05-26

Merge pull request #8 from cindytsai/libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#312](batch-07.md#commit-312), [#313](batch-07.md#commit-313), [#314](batch-07.md#commit-314), [#315](batch-07.md#commit-315), [#316](batch-07.md#commit-316), [#317](batch-07.md#commit-317), [#318](batch-07.md#commit-318), [#319](batch-07.md#commit-319), [#320](batch-07.md#commit-320), [#321](batch-07.md#commit-321), [#322](batch-07.md#commit-322), [#323](batch-07.md#commit-323), [#324](batch-07.md#commit-324), [#325](batch-07.md#commit-325), [#326](batch-07.md#commit-326), [#327](batch-07.md#commit-327).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/supplementary_info/PythonInSituAnalysis.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`.

<a id="commit-329"></a>
## 329 — `3039d58f2` — 2023-06-15

Update libyt doc.

**Categories:** 4.

Updates libyt documentation URLs and notes EvolveLevel invocation. That scheduling description is superseded by #541.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -12,17 +12,17 @@ Requirements`; `@@ -53,10 +53,10 @@ Please use const char*, or else, you have to make sure the lifetime of this`; `@@ -69,7 +69,7 @@ You have to compile libyt in interactive mode.`; `@@ -127,5 +127,5 @@ This is something libyt will update and improve in the future.`.

<a id="commit-330"></a>
## 330 — `68d6625e8` — 2023-06-15

Make sure libyt-no can compile.

**Categories:** 3.

Adds missing USE_LIBYT guards so builds without the optional dependency compile. Required if porting libyt source registration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`.

**Patch locations:** `@@ -29,6 +29,7 @@`; `@@ -42,6 +43,8 @@ void ExposeGridHierarchy(int NumberOfGrids);`; `@@ -15,7 +15,6 @@`.

<a id="commit-331"></a>
## 331 — `986a885e3` — 2023-06-15

Make integers-32 or 64 compilable in precision-64.

**Categories:** 3,2.

Updates metadata exporter types and startup arguments for 32/64-bit integer builds. Aeos custom globals make blind use of the generated mapping unsafe; regenerate type-correct mappings and test the ABI matrix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/enzo.C`.

**Patch locations:** `@@ -20,6 +20,19 @@`; `@@ -76,7 +89,7 @@ int FinalizeLibytInterface()`; `@@ -98,25 +111,25 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`; `@@ -130,22 +143,24 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`; `@@ -1,59 +1,71 @@`; additional hunks in the same patch.

<a id="commit-332"></a>
## 332 — `7173f2d36` — 2023-06-16

Merge pull request #9 from cindytsai/libyt

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#329](batch-07.md#commit-329), [#330](batch-07.md#commit-330), [#331](batch-07.md#commit-331).

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/ExposeHierarchyToLibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/enzo.C`.

<a id="commit-333"></a>
## 333 — `99a77d5d8` — 2021-09-17

Adding PopIII_Rotating parameter

**Categories:** 4.

Adds default-off PopIII_Rotating parameter, subsequently renamed PopIIIRotating. New radiative stellar model selection, not a bug correction.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -1368,6 +1368,9 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`; `@@ -1050,5 +1050,8 @@ int SetDefaultGlobalValues(TopGridData &MetaData)`; `@@ -1274,6 +1274,9 @@ int WriteParameterFile(FILE *fptr, TopGridData &MetaData, char *name = NULL)`; `@@ -1205,4 +1205,7 @@ EXTERN float MagneticSupernovaRadius;`.

<a id="commit-334"></a>
## 334 — `24c706396` — 2021-10-01

Making Test Star Particle a radiating P3 star.

**Categories:** 2,4.

Adds rotating/nonrotating PopIII luminosity tables and initially rewrites the existing test-star initializer. Conflicts with Aeos photon-rate/stellar interfaces; preserve its individual-star model. Initializer split follows in #335.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Star.h`, `src/enzo/Star_ComputePhotonRates.C`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_TestStarParticleInitializeGrid.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/PopIIIRotationModel.C`, `src/enzo/Star.h`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/TestStarParticleInitialize.C`.

**Patch locations:** `@@ -2070,7 +2070,18 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -14,6 +14,7 @@`; `@@ -29,27 +30,144 @@ int GetUnits(float *DensityUnits, float *LengthUnits,`; `@@ -70,12 +188,22 @@ int grid::TestStarParticleInitializeGrid(float TestStarParticleStarMass,`; `@@ -83,8 +211,7 @@ int grid::TestStarParticleInitializeGrid(float TestStarParticleStarMass,`; additional hunks in the same patch.

<a id="commit-335"></a>
## 335 — `232bff73e` — 2022-07-21

Separating TestStarParticle and TestRadiatingStarParticle. New test added.

**Categories:** 2,4.

Separates radiating-star and ordinary test initializers and registers a new problem. Resolve Aeos problem IDs, stellar types and Grid interfaces before porting.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`, `src/enzo/Grid_TestStarParticleInitializeGrid.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/TestRadiatingStarParticleInitialize.C`, `src/enzo/TestStarParticleInitialize.C`.

**Patch locations:** `@@ -2068,6 +2068,12 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -0,0 +1,393 @@`; `@@ -14,7 +14,6 @@`; `@@ -30,144 +29,26 @@ int GetUnits(float *DensityUnits, float *LengthUnits,`; `@@ -188,22 +69,12 @@ int grid::TestStarParticleInitializeGrid(float TestStarParticleStarMass,`; additional hunks in the same patch.

<a id="commit-336"></a>
## 336 — `28dec0bae` — 2022-07-21

Adding param file for new test.

**Categories:** 4.

Adds an opt-in radiating-star test input. Its initial problem ID 251 collides with the CR transport test; #341 changes it to 252. Do not use this intermediate input alone.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzo`.

**Patch locations:** `@@ -0,0 +1,92 @@`.

<a id="commit-337"></a>
## 337 — `f389a8cd4` — 2022-07-25

Merge branch 'main' into RotatingPopIII

**Categories:** 4.

Nonempty merge resolution combines FDM object entries with the PopIII rotation object. Build-list integration only; preserve all Aeos stellar objects.

**Merge inspection:** combined diff 657 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#046](batch-01.md#commit-046), [#047](batch-01.md#commit-047), [#048](batch-01.md#commit-048), [#049](batch-01.md#commit-049), [#050](batch-01.md#commit-050), [#051](batch-02.md#commit-051), [#052](batch-02.md#commit-052), [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056), [#057](batch-02.md#commit-057), [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068), [#069](batch-02.md#commit-069), [#070](batch-02.md#commit-070), [#071](batch-02.md#commit-071), [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074), [#075](batch-02.md#commit-075), [#076](batch-02.md#commit-076), [#077](batch-02.md#commit-077), [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079), [#080](batch-02.md#commit-080), [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114), [#115](batch-03.md#commit-115), [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131), [#132](batch-03.md#commit-132), [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134), [#135](batch-03.md#commit-135), [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141), [#142](batch-03.md#commit-142), [#143](batch-03.md#commit-143), [#144](batch-03.md#commit-144), [#145](batch-03.md#commit-145), [#146](batch-03.md#commit-146), [#147](batch-03.md#commit-147), [#148](batch-03.md#commit-148), [#149](batch-03.md#commit-149), [#150](batch-03.md#commit-150), [#151](batch-04.md#commit-151), [#152](batch-04.md#commit-152), [#153](batch-04.md#commit-153), [#154](batch-04.md#commit-154), [#155](batch-04.md#commit-155), [#156](batch-04.md#commit-156), [#157](batch-04.md#commit-157), [#158](batch-04.md#commit-158), [#159](batch-04.md#commit-159), [#160](batch-04.md#commit-160), [#161](batch-04.md#commit-161), [#162](batch-04.md#commit-162), [#163](batch-04.md#commit-163), [#164](batch-04.md#commit-164), [#165](batch-04.md#commit-165), [#166](batch-04.md#commit-166), [#167](batch-04.md#commit-167), [#168](batch-04.md#commit-168), [#169](batch-04.md#commit-169), [#170](batch-04.md#commit-170), [#171](batch-04.md#commit-171), [#172](batch-04.md#commit-172), [#173](batch-04.md#commit-173), [#174](batch-04.md#commit-174), [#175](batch-04.md#commit-175), [#176](batch-04.md#commit-176), [#177](batch-04.md#commit-177), [#178](batch-04.md#commit-178), [#179](batch-04.md#commit-179), [#180](batch-04.md#commit-180), [#181](batch-04.md#commit-181), [#182](batch-04.md#commit-182), [#183](batch-04.md#commit-183), [#184](batch-04.md#commit-184), [#185](batch-04.md#commit-185), [#186](batch-04.md#commit-186), [#187](batch-04.md#commit-187), [#188](batch-04.md#commit-188), [#189](batch-04.md#commit-189), [#190](batch-04.md#commit-190), [#191](batch-04.md#commit-191), [#192](batch-04.md#commit-192), [#193](batch-04.md#commit-193), [#194](batch-04.md#commit-194), [#195](batch-04.md#commit-195), [#196](batch-04.md#commit-196), [#197](batch-04.md#commit-197), [#198](batch-04.md#commit-198), [#199](batch-04.md#commit-199), [#200](batch-04.md#commit-200).

**Aeos-modified paths since common ancestor:** `src/enzo/EnzoTiming.h`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleFindAll.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EnzoTiming.h`, `src/enzo/EvolveLevel.C`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/FDMCollapse.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_ParallelFDMCollapseInitialize.C`, `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeLocal.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.nasa-aitken-rome`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/Make.mach.scinet-niagara`, `src/enzo/Make.mach.tigercpu`, `src/enzo/ParallelFDMCollapseInitialize.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleFindAll.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/lcaperf.h`, `src/enzo/star_maker2.F`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

<a id="commit-338"></a>
## 338 — `e7b547c6e` — 2022-07-25

Making requested changes.

**Categories:** 2,4.

Renames PopIII rotation parameter, updates photon model selection and radiating-star fixture. Intentional new spectra/luminosities; requires explicit science choice and Aeos photon-bin reconciliation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `doc/manual/source/parameters/index.rst`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzo`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzotest`, `src/enzo/Grid.h`, `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/TestRadiatingStarParticleInitialize.C`, `src/enzo/WriteParameterFile.C`.

**Patch locations:** `@@ -2338,6 +2338,12 @@ The parameters below are considered in StarParticleCreation method 3.`; `@@ -6,7 +6,7 @@`; `@@ -0,0 +1,2 @@`; `@@ -2101,12 +2101,12 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -1,6 +1,6 @@`; additional hunks in the same patch.

<a id="commit-339"></a>
## 339 — `56acb9b11` — 2022-07-25

Fixing parameter name

**Categories:** 3.

Fixes remaining global parameter name to match PopIIIRotating. Conditional interface/compilation correction.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

**Patch locations:** `@@ -1219,6 +1219,6 @@ EXTERN float MagneticSupernovaDuration;`.

<a id="commit-340"></a>
## 340 — `444dbe2d0` — 2022-07-25

Fixing an else if statement.

**Categories:** 3.

Limits the rotation branch to model values 1/2 rather than a broad else. Required conditional branch correctness if adding this model.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Star_ComputePhotonRates.C`.

**Files:** `src/enzo/Star_ComputePhotonRates.C`.

**Patch locations:** `@@ -79,7 +79,7 @@ int Star::ComputePhotonRates(const float TimeUnits, int &nbins, float E[], doubl`.

<a id="commit-341"></a>
## 341 — `221ab20f5` — 2022-07-29

Fixing radiating star particle to run on multiple cores and compile with photon-no.

**Categories:** 3,2.

Repairs multi-rank radiating-star initialization and photon-disabled compilation, relocates declarations and changes problem ID to 252. Adapt to Aeos star creation/radiation interfaces; do not overwrite them.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/Star_ComputePhotonRates.C`.

**Files:** `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzo`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzotest`, `src/enzo/Grid.h`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/TestRadiatingStarParticleInitialize.C`.

**Patch locations:** `@@ -3,18 +3,20 @@`; `@@ -44,8 +46,12 @@ Gamma = 1.6666667`; `@@ -55,16 +61,14 @@ RadiativeTransferAdaptiveTimestep       = 1`; `@@ -74,6 +78,7 @@ RadiativeCooling  =  0`; `@@ -81,12 +86,13 @@ RadiativeCooling  =  0`; additional hunks in the same patch.

<a id="commit-342"></a>
## 342 — `8e7cac45b` — 2023-05-15

Update src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C

**Categories:** 4.

Replaces rounded solar mass with shared SolarMass in the new radiating-star fixture; small normalization change conditional on that fixture.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`.

**Patch locations:** `@@ -254,7 +254,7 @@ if (MultiSpecies) {`.

<a id="commit-343"></a>
## 343 — `c60970f36` — 2023-05-15

Addressing comments made by Greg Bryan.

**Categories:** 3.

Clarifies problem-specific mass assignment in FindNewStarParticles and photon-rate initialization. Conditional fix for new fixture/rotation branches; preserve Aeos custom final-mass rules.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Star_ComputePhotonRates.C`.

**Files:** `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Star_ComputePhotonRates.C`.

**Patch locations:** `@@ -64,11 +64,13 @@ int grid::FindNewStarParticles(int level)`; `@@ -45,7 +45,9 @@ int Star::ComputePhotonRates(const float TimeUnits, int &nbins, float E[], doubl`.

<a id="commit-344"></a>
## 344 — `31cb28c61` — 2023-05-08

Removing intersphinx from docs Not supported after sphinx v7.0

**Categories:** 4.

Removes obsolete intersphinx config during Sphinx migration; superseded by corrected mapping syntax in #383. Documentation infrastructure only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/conf.py`.

**Patch locations:** `@@ -26,8 +26,7 @@ import sys, os`; `@@ -218,12 +217,3 @@ man_pages = [`.

<a id="commit-345"></a>
## 345 — `4e9aef12c` — 2022-11-16

All that code I deleted was from Tonnesen & Bryan 09

**Categories:** 2,4.

Restores Tonnesen/Bryan force-balance integration and disk pressure/rotation helpers removed during galaxy/CGM import. Aeos retains its own disk setup; this is restoration of upstream feature behavior, not proof of a missing Aeos calculation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -65,7 +65,6 @@ double bilinear_interp(double x, double y,`; `@@ -103,6 +102,13 @@ double DiskGravityCircularVelocity(FLOAT rsph, FLOAT rcyl, FLOAT z);`; `@@ -138,6 +144,7 @@ double halo_mod_g_of_r(FLOAT r);`; `@@ -284,8 +291,8 @@ int grid::GalaxySimulationInitializeGrid(double DiskRadius,`; `@@ -404,7 +411,7 @@ int grid::GalaxySimulationInitializeGrid(double DiskRadius,`; additional hunks in the same patch.

<a id="commit-346"></a>
## 346 — `403fdc286` — 2022-11-18

Changing names to allow NFW and Burkert profile options

**Categories:** 4.

Generalizes force-balance helper naming/signature for NFW and Burkert choices. Prerequisite-dependent optional interface refactor.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -103,7 +103,8 @@ double DiskGravityStellarAccel(FLOAT rcyl, FLOAT z);`; `@@ -1821,8 +1822,7 @@ double findZicm(FLOAT r, struct CGMdata& CGM_data){`; `@@ -1966,9 +1966,9 @@ float DiskPotentialCircularVelocity(FLOAT cellwidth, FLOAT z, FLOAT density, FLO`; `@@ -2141,7 +2141,7 @@ void polint(double xa[],double ya[],int n,double x,double *y,double *dy)`.

<a id="commit-347"></a>
## 347 — `aac605135` — 2022-11-18

Re-integrated Burkert potential

**Categories:** 2,4.

Reintroduces Burkert alongside NFW through explicit switches and profile parameters. Aeos already has customized external gravity; do not replace its potential or defaults with this independently developed interface.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -1308,7 +1308,9 @@ added to the acceleration field for the baryons and particles.`; `@@ -1332,11 +1334,27 @@ added to the acceleration field for the baryons and particles.`; `@@ -4902,15 +4920,18 @@ Isolated Galaxy Evolution (31)`; `@@ -285,7 +285,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -355,7 +355,7 @@ int grid::ComputeAccelerationFieldExternal()`; additional hunks in the same patch.

<a id="commit-348"></a>
## 348 — `8fdbd5d31` — 2022-11-18

Bug in NFW accel, Better switching between DM pot

**Categories:** 3,2.

Fixes an omitted 1/r^2 in the new upstream NFW acceleration, while also adding pressure-balance selection and restructuring halo routines. Split the mathematical correction from feature changes. Aeos DiskGravity currently implements its own Burkert expression, so this exact NFW defect is not automatically present there.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -4967,18 +4967,20 @@ Isolated Galaxy Evolution (31)`; `@@ -109,6 +109,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -149,6 +150,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -228,6 +230,8 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -330,7 +334,8 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; additional hunks in the same patch.

<a id="commit-349"></a>
## 349 — `f345c2d02` — 2022-11-18

Line limit tweak in Fortran

**Categories:** 3.

Splits long fixed-form Fortran expression for the new star_maker2 self-gravity criterion to avoid truncation. Conditional build/numerical correctness following #214.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/star_maker2.F`.

**Patch locations:** `@@ -202,7 +202,8 @@ c`.

<a id="commit-350"></a>
## 350 — `ab2dbfb23` — 2022-11-21

Better name for pressure balance param

**Categories:** 4.

Renames DiskThermalPressure to DiskPressureBalance throughout reader/callers. Intentional new parameter convention; migrate inputs if adopting this upstream feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -109,7 +109,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -150,7 +150,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -230,8 +230,8 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -335,7 +335,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -414,7 +414,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; additional hunks in the same patch.
