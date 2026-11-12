# Batch 10: commits 451–500

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-451"></a>
## 451 — `bd429e37b` — 2024-02-21

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#447](batch-09.md#commit-447), [#448](batch-09.md#commit-448), [#449](batch-09.md#commit-449), [#450](batch-09.md#commit-450).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

<a id="commit-452"></a>
## 452 — `92912156f` — 2024-02-21

Specify the options are for libyt only.

**Categories:** 4.

Clarifies that listed modes are libyt compile options. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -15,7 +15,8 @@ Below are links to the build and runtime requirements, which must be installed.`.

<a id="commit-453"></a>
## 453 — `0a6104c1e` — 2024-02-21

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Documents script override and parallel/serial interpreter startup. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -48,7 +48,7 @@ How it Works`.

<a id="commit-454"></a>
## 454 — `25b6c6889` — 2024-02-21

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#453](batch-10.md#commit-453).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

<a id="commit-455"></a>
## 455 — `071e388bd` — 2024-02-21

Reloading script used cases.

**Categories:** 4.

Documents file-based script reload use during batch HPC jobs. Optional analysis workflow.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -182,8 +182,12 @@ Reloading Script`.

<a id="commit-456"></a>
## 456 — `4f834d857` — 2024-02-21

Add more stuff to doing in situ analysis.

**Categories:** 4.

Adds mpi4py requirements and synchronized parallel Python examples. Documentation only; MPI collective ordering matters if enabled.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -32,6 +32,8 @@ Please follow the instructions in libyt documents:`; `@@ -46,6 +48,8 @@ Please follow the instructions in libyt documents:`; `@@ -292,4 +296,33 @@ This is something libyt will update and improve in the future.`.

<a id="commit-457"></a>
## 457 — `023e356aa` — 2024-02-21

Make imported script name a global.

**Categories:** 4.

Adds libyt_script_name input/default/output and wires it into initialization. Optional public parameter, with fixed-buffer/lifetime handling to retain.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -43,9 +43,9 @@ int InitializeLibytByItself(long long argc, char *argv[])`; `@@ -1191,6 +1191,7 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`; `@@ -968,6 +968,10 @@ int SetDefaultGlobalValues(TopGridData &MetaData)`; `@@ -181,6 +181,7 @@ int WriteParameterFile(FILE *fptr, TopGridData &MetaData, char *name = NULL)`; `@@ -980,6 +980,7 @@ EXTERN PyObject *my_processor;`.

<a id="commit-458"></a>
## 458 — `16e11fc14` — 2024-02-21

Explicitly define global libyt_script_name.

**Categories:** 3.

Makes libyt_script_name external declaration/storage size match at the isolated-header ABI boundary. Conditional correctness fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -33,6 +33,7 @@`; `@@ -980,7 +980,7 @@ EXTERN PyObject *my_processor;`.

<a id="commit-459"></a>
## 459 — `1b8984e4a` — 2024-02-21

Update doc.

**Categories:** 4.

Documents parameter-based script naming instead of source editing. Optional interface documentation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -80,14 +80,14 @@ General`.

<a id="commit-460"></a>
## 460 — `710ea3f80` — 2024-02-22

Update libyt parameter in doc.

**Categories:** 1.

Adds libyt parameter documentation to the parameter reference. Clean patch; does not enable the feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`.

**Patch locations:** `@@ -136,6 +136,8 @@ common convention of 0 meaning false or off and 1 for true or on.`; `@@ -3872,6 +3874,24 @@ Other Internal Parameters`.

<a id="commit-461"></a>
## 461 — `591669745` — 2024-02-29

Add libyt-yes/no make option to doc.

**Categories:** 1.

Lists optional libyt make controls. Documentation-only clean patch.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/reference/MakeOptions.rst`.

**Patch locations:** `@@ -220,6 +220,7 @@ External libraries`.

<a id="commit-462"></a>
## 462 — `18b4fc8b1` — 2024-02-29

Add option libyt-interactive-yes/no.

**Categories:** 4.

Adds default-off interactive libyt build control and guarded prompt API call. Optional analysis behavior, not a physics fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Files:** `doc/manual/source/reference/MakeOptions.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Patch locations:** `@@ -211,18 +211,19 @@ Algorithmic settings`; `@@ -338,12 +338,14 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -418,19 +418,25 @@`; `@@ -25,6 +25,7 @@`; `@@ -179,6 +180,15 @@`; additional hunks in the same patch.

<a id="commit-463"></a>
## 463 — `b9435d6f8` — 2024-02-29

Add option libyt-reload-yes/no.

**Categories:** 4.

Adds libyt script-reload build control and guarded API call. Requires matching libyt build capabilities.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Files:** `doc/manual/source/reference/MakeOptions.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Patch locations:** `@@ -222,6 +222,7 @@ External libraries`; `@@ -347,12 +347,14 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -437,6 +437,10 @@`; `@@ -26,6 +26,7 @@`; `@@ -181,7 +182,7 @@`; additional hunks in the same patch.

<a id="commit-464"></a>
## 464 — `22f93f917` — 2024-02-29

Add option libyt-jupyter-yes/no.

**Categories:** 4.

Adds libyt Jupyter build control and guarded kernel call. Optional analysis integration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Files:** `doc/manual/source/reference/MakeOptions.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Patch locations:** `@@ -223,6 +223,7 @@ External libraries`; `@@ -356,12 +356,14 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -441,6 +441,10 @@`; `@@ -27,6 +27,7 @@`; `@@ -199,6 +200,15 @@`; additional hunks in the same patch.

<a id="commit-465"></a>
## 465 — `6e1259276` — 2024-02-29

Update doc.

**Categories:** 4.

Updates documentation to use explicit analysis build controls. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -140,16 +140,18 @@ Interactive Python Prompt`; `@@ -170,18 +172,20 @@ Reloading Script`; `@@ -214,16 +218,18 @@ Jupyter Notebook / JupyterLab UI`; `@@ -243,8 +249,7 @@ Jupyter Notebook / JupyterLab UI`; `@@ -256,9 +261,17 @@ or to turn it off,`.

<a id="commit-466"></a>
## 466 — `4f11d9231` — 2024-03-01

Missing space in if.

**Categories:** 4.

Changes indentation of Make error target declarations; evaluate parsing of the whole final configuration rather than assume indentation is an algorithm defect.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`.

**Files:** `src/enzo/Make.config.assemble`.

**Patch locations:** `@@ -456,8 +456,8 @@`.

<a id="commit-467"></a>
## 467 — `0efa63078` — 2024-03-07

Move NumberOfLibyt* param inside USE_LIBYT clause.

**Categories:** 3.

Moves libyt counters inside USE_LIBYT declarations. Conditional feature-disabled build hygiene.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

**Patch locations:** `@@ -984,10 +984,10 @@ EXTERN char libyt_script_name[512];`.

<a id="commit-468"></a>
## 468 — `91eba5cd1` — 2024-03-07

Define libyt macros inside ifdef USE_LIBYT

**Categories:** 3.

Guards libyt dtype macros by USE_LIBYT. Required optional-dependency build separation when adopting the feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/macros_and_parameters.h`.

**Patch locations:** `@@ -342,8 +342,10 @@ typedef long long int   HDF5_hid_t;`; `@@ -352,8 +354,10 @@ typedef long long int   HDF5_hid_t;`.

<a id="commit-469"></a>
## 469 — `84ee4630f` — 2024-03-07

Remove advertising CallInSitulibyt can be called anywhere.

**Categories:** 4.

Removes the unsupported claim that in-situ callbacks can run anywhere. Useful MPI/synchronization constraint; no executable change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -89,14 +89,6 @@ General`.

<a id="commit-470"></a>
## 470 — `9c7612672` — 2024-05-16

Try generating Temperature / Cooling_Time in enzo and pass to libyt as inline field.

**Categories:** 4.

Exports Enzo-derived temperature/cooling-time arrays through libyt. New analysis fields; preserve Aeos chemistry/backend calculations and buffer ownership. Later commits fix allocation cleanup and units.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -170,6 +170,8 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -277,7 +279,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -285,6 +287,21 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -371,6 +388,10 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -78,10 +78,26 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; additional hunks in the same patch.

<a id="commit-471"></a>
## 471 — `946698579` — 2024-05-16

typo.

**Categories:** 3.

Fixes malformed std::vector<void*> declaration introduced in #470. Conditional compilation repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

**Patch locations:** `@@ -984,7 +984,7 @@ EXTERN PyObject *my_processor;`.

<a id="commit-472"></a>
## 472 — `01c13a2e7` — 2024-05-16

typo

**Categories:** 3.

Uses the actual ComputeCoolingTime method name for generated analysis field. Conditional compilation repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -87,7 +87,7 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-473"></a>
## 473 — `bbce99e83` — 2024-05-16

typo

**Categories:** 3.

Corrects vector push_back spelling. Conditional compilation repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -89,8 +89,8 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-474"></a>
## 474 — `8bba70c53` — 2024-05-16

typo.

**Categories:** 3.

Parenthesizes the cast before dereferencing libyt parameter pointer. Conditional compilation repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -92,8 +92,8 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-475"></a>
## 475 — `565d2bb1c` — 2024-05-16

forgot to clear all pointer once freed.

**Categories:** 3.

Clears generated-array pointer list after freeing its entries to avoid stale pointers/double deletion on later analysis calls. Essential if derived-field export is ported.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -391,6 +391,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-476"></a>
## 476 — `08614271c` — 2024-05-16

The Cooling_Time field unit computed from `ComputeCoolingTime` is code_time.

**Categories:** 3.

Labels exported cooling time with code_time units. Required analysis dimensional correctness; does not modify the cooling solver itself.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -297,6 +297,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-477"></a>
## 477 — `3c3fd4211` — 2024-05-16

Change Gamma to gamma, since yt reads ds.gamma.

**Categories:** 3.

Exports gamma under the name expected by yt, avoiding analysis EOS metadata mismatch. Conditional on libyt export.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface_finderfunctions.inc`.

**Patch locations:** `@@ -33,7 +33,7 @@ YT_SET_USERPARAM_INTEGER("ProblemType", 1, &ProblemType);`.

<a id="commit-478"></a>
## 478 — `bd635953e` — 2024-05-16

Follow how New_Grid_WriteGrid output grid.

**Categories:** 3.

Checks derived-field computation success and converts cooling time consistently with normal grid output. Required analysis consistency; preserve Aeos backend-specific failure/units behavior.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -17,6 +17,7 @@`; `@@ -29,6 +30,8 @@`; `@@ -86,17 +89,21 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-479"></a>
## 479 — `4bb7c6a3f` — 2024-05-20

Fix velocity units.

**Categories:** 3.

Initializes velocity_unit instead of leaving it unset while assigning an unrelated magnetic field. Required libyt metadata fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -149,7 +149,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-480"></a>
## 480 — `4488ffa17` — 2024-05-20

Fix magnetic_unit.

**Categories:** 3.

Sets magnetic unit to sqrt(4*pi*rho_unit)*velocity_unit. Required dimensional metadata for Enzo magnetic fields in libyt.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -150,6 +150,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-481"></a>
## 481 — `8ea327267` — 2024-05-20

Fix periodicity.

**Categories:** 4.

First attempt replaces hard-coded periodicity with Enzo boundary enum values. Still incorrect as Boolean metadata; use #498's equality-to-periodic correction.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -151,9 +151,9 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-482"></a>
## 482 — `a631777a0` — 2024-05-20

typo.

**Categories:** 3.

Adds required physical/constants include for magnetic-unit computation. Conditional compilation repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -18,6 +18,7 @@`.

<a id="commit-483"></a>
## 483 — `6a3769e96` — 2024-05-22

try to fix it through adding new method.

**Categories:** 4.

Adds active-particle attribute-name discovery to libyt and registration callbacks. New optional ActiveParticle API requiring compatible custom particle handlers.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticle.h`, `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -462,6 +462,18 @@ namespace ActiveParticleHelpers {`; `@@ -687,6 +699,7 @@ public:`; `@@ -709,6 +722,7 @@ public:`; `@@ -754,6 +768,7 @@ public:`; `@@ -793,6 +808,7 @@ ActiveParticleType_info *register_ptype(std::string name)`; additional hunks in the same patch.

<a id="commit-484"></a>
## 484 — `39f735085` — 2024-05-22

Make sure the lifetime of attribute name exist througout the entire in situ.

**Categories:** 3.

Retains attribute-name strings through the full analysis call instead of exposing pointers into temporary vectors. Essential lifetime correction if active-particle export is adopted.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -181,11 +181,16 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -242,11 +247,8 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-485"></a>
## 485 — `305c53232` — 2024-05-27

Map hdf5 type to yt_dtype (have error when compiling)

**Categories:** 4.

Adds HDF5-attribute type discovery and initial mapping to libyt. Intermediate switch implementation is not compilable for runtime HDF5 type IDs; use #486.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticle.h`, `src/enzo/CallInSitulibyt.C`, `src/enzo/ParticleAttributeHandler.h`.

**Patch locations:** `@@ -462,6 +462,17 @@ namespace ActiveParticleHelpers {`; `@@ -699,6 +710,7 @@ public:`; `@@ -722,6 +734,7 @@ public:`; `@@ -768,6 +781,7 @@ public:`; `@@ -808,6 +822,7 @@ ActiveParticleType_info *register_ptype(std::string name)`; additional hunks in the same patch.

<a id="commit-486"></a>
## 486 — `c73ead2a1` — 2024-05-27

Using if-else instead of switch, can compile and run.

**Categories:** 3.

Uses if/else HDF5 dtype comparisons instead of switch cases requiring compile-time constants. Conditional active-particle exporter compilation fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -45,17 +45,16 @@ void ExportParameterFile(TopGridData *MetaData, FLOAT CurrentTime, FLOAT OldTime`.

<a id="commit-487"></a>
## 487 — `9bc581b85` — 2024-05-27

Remove commented out USE_LIBYT.

**Categories:** 4.

Removes commented-out libyt additions from particle attribute handlers. Reverse check succeeds because Aeos matches the preaddition state; not evidence that active-particle export is already integrated.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ParticleAttributeHandler.h`.

**Patch locations:** `@@ -22,9 +22,6 @@`; `@@ -37,9 +34,6 @@ class ParticleAttributeHandler`; `@@ -66,33 +60,21 @@ class Handler : public ParticleAttributeHandler`; `@@ -136,33 +118,21 @@ class ArrayHandler : public ParticleAttributeHandler`.

<a id="commit-488"></a>
## 488 — `91af69667` — 2024-05-27

Load active particle count.

**Categories:** 4.

Exports per-enabled-type active-particle counts to libyt. New analysis capability; requires matching attribute buffers.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -123,5 +123,14 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-489"></a>
## 489 — `7ee892643` — 2024-05-29

Rename GetParticleAttributes to GetParticleAttributeNames.

**Categories:** 4.

Renames the attribute-name accessor to distinguish it from value export. Optional API cleanup, with all registrations/callers updated together.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticle.h`, `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -473,7 +473,7 @@ namespace ActiveParticleHelpers {`; `@@ -711,7 +711,7 @@ public:`; `@@ -735,7 +735,7 @@ public:`; `@@ -782,7 +782,7 @@ public:`; `@@ -823,7 +823,7 @@ ActiveParticleType_info *register_ptype(std::string name)`; additional hunks in the same patch.

<a id="commit-490"></a>
## 490 — `e82b0f528` — 2024-05-29

Fill in particle buffer, and ignore multi-dimensional array for now

**Categories:** 4.

Adds packed active-particle values to libyt; multidimensional attributes intentionally excluded. New analysis capability with later pointer/type corrections; not complete at this snapshot.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticle.h`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -473,6 +473,44 @@ namespace ActiveParticleHelpers {`; `@@ -711,6 +749,8 @@ public:`; `@@ -735,6 +775,7 @@ public:`; `@@ -782,6 +823,9 @@ public:`; `@@ -823,6 +867,7 @@ ActiveParticleType_info *register_ptype(std::string name)`; additional hunks in the same patch.

<a id="commit-491"></a>
## 491 — `07f52d9c5` — 2024-05-29

Typo.

**Categories:** 3.

Fixes missing semicolon and function-pointer declaration comma in new active-particle export API. Conditional compilation repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticle.h`.

**Patch locations:** `@@ -508,7 +508,7 @@ namespace ActiveParticleHelpers {`; `@@ -750,7 +750,7 @@ public:`.

<a id="commit-492"></a>
## 492 — `5380a5023` — 2024-06-06

Get attribute value and pass to libyt. (The attributes read in libyt are not correct)

**Categories:** 4.

Connects active-particle data buffers to the grid adapter but still exposes wrong buffer position; use with #493, not alone.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -133,24 +133,26 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-493"></a>
## 493 — `202be4157` — 2024-06-11

Pass in the correct pointer for libyt.

**Categories:** 3.

Preserves buffer start before GetAttribute advances the pointer, and exports the saved address. Required active-particle data/lifetime correctness.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticle.h`.

**Patch locations:** `@@ -496,6 +496,7 @@ namespace ActiveParticleHelpers {`; `@@ -504,7 +505,7 @@ namespace ActiveParticleHelpers {`.

<a id="commit-494"></a>
## 494 — `224839154` — 2024-06-11

This should match to YT_LONGLONG

**Categories:** 3.

Matches the long-long metadata macro to YT_LONGLONG. Conditional integer-width mapping correctness.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/macros_and_parameters.h`.

**Patch locations:** `@@ -355,7 +355,7 @@ typedef long long int   HDF5_hid_t;`.

<a id="commit-495"></a>
## 495 — `cded6587a` — 2024-06-13

Update link and version requirement.

**Categories:** 4.

Updates libyt dependency links and version requirements. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -36,17 +36,17 @@ Please follow the instructions in libyt documents:`.

<a id="commit-496"></a>
## 496 — `0b99fd51a` — 2024-06-13

Clarify one-sided mpi sm,pt2pt settings.

**Categories:** 4.

Clarifies one-sided OpenMPI transport environment setting. Documentation only; site-specific runtime tuning.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -295,7 +295,7 @@ Please add OMPI_MCA_osc=sm,pt2pt before mpirun, for example:`.

<a id="commit-497"></a>
## 497 — `ca7999663` — 2024-06-13

Remove TODOs, and rename libyt_generated_derived_field to *_data.

**Categories:** 4.

Renames derived-field allocation tracking to general generated-data tracking and removes TODOs. Preserve ownership and one-delete-per-buffer behavior if adapting.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -186,9 +186,10 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -436,10 +437,10 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -93,14 +93,14 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -130,7 +130,7 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -149,9 +149,8 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; additional hunks in the same patch.

<a id="commit-498"></a>
## 498 — `4e8f2ecd5` — 2024-09-30

Fix periodicity

**Categories:** 3.

Converts boundary enum to Boolean via equality with periodic. Fixes #481, where nonzero outflow/inflow enums otherwise look periodic to analysis.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -166,9 +166,9 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-499"></a>
## 499 — `cc6538bee` — 2024-09-30

Distinguish multi-dim particle attributes by element_size / size of hdf5type

**Categories:** 3.

Detects unsupported vector attributes through element_size/H5Tget_size rather than hard-coded SmartStar attribute names. Conditional generic exporter correctness; multidimensional data remain unsupported.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticle.h`.

**Patch locations:** `@@ -487,9 +487,11 @@ namespace ActiveParticleHelpers {`.

<a id="commit-500"></a>
## 500 — `7a356f389` — 2024-10-01

Update libyt/yt_libyt/jupyter_libyt version requirement.

**Categories:** 4.

Updates libyt and Python-side dependency version requirements. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -18,7 +18,7 @@ We can compile libyt using different options based on our used cases, so tha`; `@@ -36,9 +36,9 @@ Please follow the instructions in libyt documents:`.
