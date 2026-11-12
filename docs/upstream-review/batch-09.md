# Batch 09: commits 401–450

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-401"></a>
## 401 — `0faff93fe` — 2024-02-17

Update interactive mode.

**Categories:** 4.

Expands interactive prompt instructions and cross references. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -57,7 +57,7 @@ This includes simulation information, like adaptive mesh grid hierarchy, paramet`; `@@ -94,24 +94,48 @@ General`; `@@ -148,7 +172,7 @@ This includes libyt header, links to the library, and adds library search pa`.

<a id="commit-402"></a>
## 402 — `caf614dd3` — 2024-02-17

Update reloading script.

**Categories:** 4.

Documents script reload and prompt behavior. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -130,12 +130,40 @@ Interactive Python Prompt`.

<a id="commit-403"></a>
## 403 — `cf5b4ca02` — 2024-02-17

Add Jupyter Notebook and change "you" to "we".

**Categories:** 4.

Adds Jupyter UI instructions and revises prose. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -11,7 +11,7 @@ Requirements`; `@@ -46,7 +46,7 @@ A brief description of each mode (option) is shown here. The options are mutuall`; `@@ -65,7 +65,7 @@ At the end, when the simulation is shutting down, Enzo calls FinalizeLibytInte`; `@@ -73,26 +73,26 @@ General`; `@@ -101,9 +101,9 @@ General`; additional hunks in the same patch.

<a id="commit-404"></a>
## 404 — `8aff9e4ba` — 2024-02-17

Add code snippet for reloading script and jupyter kernel.

**Categories:** 4.

Replaces unconditional interactive call with commented examples for interactive, reload and Jupyter modes. Changes optional analysis behavior; choose an explicit final mode when porting.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -329,12 +329,26 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-405"></a>
## 405 — `8357505ad` — 2023-08-30

Extend TopGrid star formation to NORMAL_STAR

**Categories:** 2,4.

Extends once-per-root-step formation to NORMAL_STAR and changes MakeStars scheduling/handler timestep. Alters temporal sampling of star formation; do not apply to Aeos individual-star scheduling without a separate science decision.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_StarParticleHandler.C`.

**Files:** `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_StarParticleHandler.C`.

**Patch locations:** `@@ -406,21 +406,21 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; `@@ -148,8 +148,8 @@ class grid`; `@@ -806,39 +806,55 @@ int grid::StarParticleHandler(HierarchyEntry* SubgridPointer, int level,`.

<a id="commit-406"></a>
## 406 — `d7bcfa566` — 2023-09-08

Updated if statement for RootGridSF

**Categories:** 3.

Includes NORMAL_STAR in the root-step scheduling condition introduced by #405. Conditional completeness fix for that optional timing model.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/EvolveLevel.C`.

**Patch locations:** `@@ -409,7 +409,7 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`.

<a id="commit-407"></a>
## 407 — `00a59a5d1` — 2023-09-11

Set MakeStars on all girds, not just at max refine

**Categories:** 3,2.

Sets formation eligibility on every level, relying on each maker to exclude covered cells. Prevents missing lower-level cells for root-step formation but requires validating Aeos per-cell refinement exclusion before adapting.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/EvolveLevel.C`.

**Patch locations:** `@@ -412,18 +412,17 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`.

<a id="commit-408"></a>
## 408 — `d13f0bb3a` — 2023-09-05

removed particle mass multiplier added for init ICs that can cause error with MUSIC ICs

**Categories:** 3.

Removes particle-count-based factors of eight in nested cosmological IC mass assignment, which can corrupt MUSIC masses. Inspection of Aeos lines 1690–1699 finds these factors already inside a block comment, so the operative repair is present through a different implementation. No new mass-normalization change is warranted; verify IC mass closure when modifying this reader.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`.

**Patch locations:** `@@ -1474,19 +1474,6 @@ int grid::NestedCosmologySimulationInitializeGrid(`.

<a id="commit-409"></a>
## 409 — `8dbf79698` — 2023-09-05

Merge pull request #220 from mihirskulkarni/main

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#408](batch-09.md#commit-408).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`.

<a id="commit-410"></a>
## 410 — `1e464bb56` — 2023-09-20

Merge branch 'main' into sf-top-grid-timestep

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#408](batch-09.md#commit-408), [#409](batch-09.md#commit-409).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`.

<a id="commit-411"></a>
## 411 — `a35ef3add` — 2023-09-20

Update CircleCI Python several versions for future proofing

**Categories:** 4.

Updates CI Python image. Subsequent compatibility experiments supersede this exact pin.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -189,7 +189,7 @@ commands:`; `@@ -237,7 +237,7 @@ jobs:`; `@@ -268,7 +268,7 @@ jobs:`.

<a id="commit-412"></a>
## 412 — `989aee2a3` — 2023-09-20

Fortran type flag

**Categories:** 4.

Temporary Ubuntu -finteger-4-integer-8 flags alter Fortran ABI, not just warnings. Superseded by #414; do not adopt independently across Aeos C++/Fortran interfaces.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.ubuntu`.

**Patch locations:** `@@ -60,8 +60,8 @@ MACH_DEFINES   = -DLINUX -DH5_USE_16_API`.

<a id="commit-413"></a>
## 413 — `302e58183` — 2023-09-20

Another Fortran flag

**Categories:** 4.

Adds argument-mismatch suppression to the temporary integer-promotion flags. Superseded; suppression does not prove ABI correctness.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.ubuntu`.

**Patch locations:** `@@ -60,8 +60,8 @@ MACH_DEFINES   = -DLINUX -DH5_USE_16_API`.

<a id="commit-414"></a>
## 414 — `59d9345f8` — 2023-09-25

Try alt Fortran flag

**Categories:** 4.

Replaces integer-promotion experiment with -std=legacy. Toolchain compatibility choice; retain Aeos explicit integer-width configuration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.ubuntu`.

**Patch locations:** `@@ -60,8 +60,8 @@ MACH_DEFINES   = -DLINUX -DH5_USE_16_API`.

<a id="commit-415"></a>
## 415 — `3bde0790b` — 2023-09-25

Save out.compile for build & test CI

**Categories:** 4.

Saves compile log in build/test CI job. Useful diagnostics only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -235,6 +235,9 @@ jobs:`.

<a id="commit-416"></a>
## 416 — `4d020920b` — 2023-10-10

update gold standard tag

**Categories:** 4.

Updates CI gold standard to v16; answer rebaseline needs explanation of changed results. It does not itself establish scientific correctness.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -217,16 +217,16 @@ jobs:`.

<a id="commit-417"></a>
## 417 — `20ea3b9c4` — 2023-12-07

Updated dep tag to reset CircleCI cache

**Categories:** 4.

Invalidates CI dependency cache. Historical infrastructure churn; use final cache/dependency policy.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -200,13 +200,13 @@ jobs:`; `@@ -251,13 +251,13 @@ jobs:`.

<a id="commit-418"></a>
## 418 — `69d9e7b19` — 2023-12-19

Downgrade Python image for nose compatibility

**Categories:** 4.

Downgrades one Python image for nose compatibility. Superseded by subsequent image/cache changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -189,7 +189,7 @@ commands:`.

<a id="commit-419"></a>
## 419 — `575c0ac47` — 2023-12-19

This image doesn't have python3??

**Categories:** 4.

Switches CI python3 invocations to python experimentally. Superseded; use interpreter from selected environment.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -29,7 +29,7 @@ commands:`; `@@ -76,7 +76,7 @@ commands:`.

<a id="commit-420"></a>
## 420 — `b77d994cf` — 2023-12-19

Missed some image names

**Categories:** 4.

Updates remaining CI image names. Infrastructure-only continuation of #418.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -240,7 +240,7 @@ jobs:`; `@@ -271,7 +271,7 @@ jobs:`.

<a id="commit-421"></a>
## 421 — `d526bd2ca` — 2023-12-19

Put the 3's back...

**Categories:** 4.

Reverts interpreter spelling experiments and introduces a venv invocation typo fixed next. Do not adopt alone.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -29,7 +29,7 @@ commands:`; `@@ -76,7 +76,7 @@ commands:`.

<a id="commit-422"></a>
## 422 — `aeeb8f3f5` — 2023-12-19

Back to fully downgraded python image

**Categories:** 3.

Restores missing -m in python3 -m venv. Conditional CI command repair only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -76,7 +76,7 @@ commands:`.

<a id="commit-423"></a>
## 423 — `cb7a56e10` — 2023-12-19

python3 -> python

**Categories:** 4.

Another temporary CI interpreter spelling change. Superseded by #424.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -29,7 +29,7 @@ commands:`.

<a id="commit-424"></a>
## 424 — `6a228a14b` — 2023-12-19

Settle on python 3.11.5 b/c it runs as far as using the nose package

**Categories:** 4.

Restores python3 and retries Python3.11 image. Superseded dependency experiment.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -29,7 +29,7 @@ commands:`; `@@ -189,7 +189,7 @@ commands:`; `@@ -240,7 +240,7 @@ jobs:`; `@@ -271,7 +271,7 @@ jobs:`.

<a id="commit-425"></a>
## 425 — `dc2e6a475` — 2023-12-19

nose3 can replace nose but not for Python 3.11

**Categories:** 4.

Moves CI to nose3 and older Python for legacy runner compatibility. Adopt a coherent tested tooling stack, not these experiments individually.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -34,7 +34,7 @@ commands:`; `@@ -189,7 +189,7 @@ commands:`; `@@ -240,7 +240,7 @@ jobs:`; `@@ -271,7 +271,7 @@ jobs:`.

<a id="commit-426"></a>
## 426 — `f95a749af` — 2023-12-20

Missing Python exe seems to be outdated cache again

**Categories:** 4.

Changes CI image/cache after environment executable failures. Infrastructure only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -189,7 +189,7 @@ commands:`; `@@ -200,13 +200,13 @@ jobs:`; `@@ -240,7 +240,7 @@ jobs:`; `@@ -251,13 +251,13 @@ jobs:`; `@@ -271,7 +271,7 @@ jobs:`.

<a id="commit-427"></a>
## 427 — `03a532b17` — 2023-12-21

Reset answer cache

**Categories:** 4.

Resets historical answer cache keys. No executable simulation change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -217,7 +217,7 @@ jobs:`; `@@ -226,7 +226,7 @@ jobs:`.

<a id="commit-428"></a>
## 428 — `8d55018e9` — 2024-01-05

gosh darn typos

**Categories:** 3.

Corrects answer-cache key typo in CI. Conditional workflow correctness only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -217,7 +217,7 @@ jobs:`.

<a id="commit-429"></a>
## 429 — `9733d8a7a` — 2024-01-05

try new answer cache name

**Categories:** 4.

Changes CI answer cache suffix. Obsolete historical cache invalidation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -217,7 +217,7 @@ jobs:`; `@@ -226,7 +226,7 @@ jobs:`.

<a id="commit-430"></a>
## 430 — `beffe2c30` — 2024-01-08

Update cache and tag

**Categories:** 4.

Changes CI answer cache suffix again. Obsolete historical cache invalidation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -217,7 +217,7 @@ jobs:`; `@@ -226,7 +226,7 @@ jobs:`.

<a id="commit-431"></a>
## 431 — `083f4dc80` — 2024-01-08

Update cache and tag

**Categories:** 4.

Changes CI answer cache suffix again; no simulation changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -217,7 +217,7 @@ jobs:`; `@@ -226,7 +226,7 @@ jobs:`.

<a id="commit-432"></a>
## 432 — `7b319eaee` — 2024-01-08

Have to update cache letter & tag at the same time

**Categories:** 4.

Remerge-diff chooses answer-cache v16a consistently. CI bookkeeping only; not a scientific correction.

**Merge inspection:** combined diff 0 bytes; remerge diff 841 bytes. Positive results are discussed above.

**Constituents in inventory:** [#431](batch-09.md#commit-431).

**Aeos-modified paths since common ancestor:** none.

**Files:** .

<a id="commit-433"></a>
## 433 — `11ccabadf` — 2024-01-09

Merge pull request #223 from clairekope/circleci-python

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#411](batch-09.md#commit-411), [#412](batch-09.md#commit-412), [#413](batch-09.md#commit-413), [#414](batch-09.md#commit-414), [#415](batch-09.md#commit-415), [#416](batch-09.md#commit-416), [#417](batch-09.md#commit-417), [#418](batch-09.md#commit-418), [#419](batch-09.md#commit-419), [#420](batch-09.md#commit-420), [#421](batch-09.md#commit-421), [#422](batch-09.md#commit-422), [#423](batch-09.md#commit-423), [#424](batch-09.md#commit-424), [#425](batch-09.md#commit-425), [#426](batch-09.md#commit-426), [#427](batch-09.md#commit-427), [#428](batch-09.md#commit-428), [#429](batch-09.md#commit-429), [#430](batch-09.md#commit-430), [#431](batch-09.md#commit-431), [#432](batch-09.md#commit-432).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `src/enzo/Make.mach.ubuntu`.

<a id="commit-434"></a>
## 434 — `54193b832` — 2023-08-15

Added small change to GalaxySimulation to initialize the particle boundary in the exterior boundary condition.

**Categories:** 3.

Initializes external particle boundaries in GalaxySimulation when constructing constant fluid boundaries. Clean patch applies; avoids undefined particle-boundary state. Verify fresh-start and restart particle escape behavior.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`.

**Files:** `src/enzo/GalaxySimulationInitialize.C`.

**Patch locations:** `@@ -494,6 +494,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`.

<a id="commit-435"></a>
## 435 — `8016fe9e4` — 2024-01-09

Merge pull request #217 from gregbryan/galsim-particle

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#434](batch-09.md#commit-434).

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`.

**Files:** `src/enzo/GalaxySimulationInitialize.C`.

<a id="commit-436"></a>
## 436 — `8ebd25f30` — 2024-01-11

Merge branch 'main' into sf-top-grid-timestep

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#411](batch-09.md#commit-411), [#412](batch-09.md#commit-412), [#413](batch-09.md#commit-413), [#414](batch-09.md#commit-414), [#415](batch-09.md#commit-415), [#416](batch-09.md#commit-416), [#417](batch-09.md#commit-417), [#418](batch-09.md#commit-418), [#419](batch-09.md#commit-419), [#420](batch-09.md#commit-420), [#421](batch-09.md#commit-421), [#422](batch-09.md#commit-422), [#423](batch-09.md#commit-423), [#424](batch-09.md#commit-424), [#425](batch-09.md#commit-425), [#426](batch-09.md#commit-426), [#427](batch-09.md#commit-427), [#428](batch-09.md#commit-428), [#429](batch-09.md#commit-429), [#430](batch-09.md#commit-430), [#431](batch-09.md#commit-431), [#432](batch-09.md#commit-432), [#433](batch-09.md#commit-433), [#434](batch-09.md#commit-434), [#435](batch-09.md#commit-435).

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`.

**Files:** `.circleci/config.yml`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Make.mach.ubuntu`.

<a id="commit-437"></a>
## 437 — `16128cdef` — 2024-01-23

Update docs

**Categories:** 4.

Documents once-per-root-grid-timestep formation support and limitations. Optional scheduling model, not a direction to change the Aeos individual-star cadence.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`.

**Patch locations:** `@@ -2266,6 +2266,12 @@ The parameters below are considered in StarParticleCreation method`; `@@ -2354,8 +2360,6 @@ The parameters below are considered in StarParticleCreation method 11.`; `@@ -441,10 +441,11 @@ applied, below which no star formation occurs.`.

<a id="commit-438"></a>
## 438 — `5b3fc383a` — 2024-01-25

Merge pull request #221 from clairekope/sf-top-grid-timestep

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#405](batch-09.md#commit-405), [#406](batch-09.md#commit-406), [#407](batch-09.md#commit-407), [#410](batch-09.md#commit-410), [#436](batch-09.md#commit-436), [#437](batch-09.md#commit-437).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_StarParticleHandler.C`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_StarParticleHandler.C`.

<a id="commit-439"></a>
## 439 — `22c9d3b7d` — 2023-06-29

Add correct, newer gen eq table script!

**Categories:** 3.

Corrects the optional equilibrium-table generator's pygrackle setup, density/temperature sampling and reader initialization. Required if porting the upstream equilibrium-IC workflow; it does not replace the simulation cooling data table.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `input/gen_equilibrium_table.py`, `src/enzo/ReadEquilibriumTable.C`.

**Patch locations:** `@@ -8,7 +8,7 @@`; `@@ -19,18 +19,22 @@ from pygrackle import \`; `@@ -40,8 +44,7 @@ chem.primordial_chemistry = 2`; `@@ -49,7 +52,7 @@ chem.use_volumetric_heating_rate = 0`; `@@ -60,22 +63,24 @@ chem.velocity_units = chem.a_units \`; additional hunks in the same patch.

<a id="commit-440"></a>
## 440 — `235794683` — 2024-01-11

Merge branch 'main' into correct_chem_generator

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#408](batch-09.md#commit-408), [#409](batch-09.md#commit-409), [#411](batch-09.md#commit-411), [#412](batch-09.md#commit-412), [#413](batch-09.md#commit-413), [#414](batch-09.md#commit-414), [#415](batch-09.md#commit-415), [#416](batch-09.md#commit-416), [#417](batch-09.md#commit-417), [#418](batch-09.md#commit-418), [#419](batch-09.md#commit-419), [#420](batch-09.md#commit-420), [#421](batch-09.md#commit-421), [#422](batch-09.md#commit-422), [#423](batch-09.md#commit-423), [#424](batch-09.md#commit-424), [#425](batch-09.md#commit-425), [#426](batch-09.md#commit-426), [#427](batch-09.md#commit-427), [#428](batch-09.md#commit-428), [#429](batch-09.md#commit-429), [#430](batch-09.md#commit-430), [#431](batch-09.md#commit-431), [#432](batch-09.md#commit-432), [#433](batch-09.md#commit-433), [#434](batch-09.md#commit-434), [#435](batch-09.md#commit-435).

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`.

**Files:** `.circleci/config.yml`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`, `src/enzo/Make.mach.ubuntu`.

<a id="commit-441"></a>
## 441 — `d3cb9bb96` — 2024-01-22

Add command line arguments to script

**Categories:** 4.

Adds command-line controls for equilibrium table size, metallicity and UV redshift. Useful reproducibility interface for the optional generator.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `input/gen_equilibrium_table.py`.

**Patch locations:** `@@ -26,14 +26,34 @@ from pygrackle.utilities.physical_constants import \`; `@@ -44,7 +64,7 @@ chem.primordial_chemistry = 2`; `@@ -67,8 +87,8 @@ fc = setup_fluid_container(chem,`.

<a id="commit-442"></a>
## 442 — `74412740d` — 2024-01-25

Merge pull request #215 from clairekope/correct_chem_generator

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#439](batch-09.md#commit-439), [#440](batch-09.md#commit-440), [#441](batch-09.md#commit-441).

**Aeos-modified paths since common ancestor:** none.

**Files:** `input/gen_equilibrium_table.py`, `src/enzo/ReadEquilibriumTable.C`.

<a id="commit-443"></a>
## 443 — `e5d4f973d` — 2024-02-17

Merge remote-tracking branch 'enzo-dev/main' into libyt

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#405](batch-09.md#commit-405), [#406](batch-09.md#commit-406), [#407](batch-09.md#commit-407), [#408](batch-09.md#commit-408), [#409](batch-09.md#commit-409), [#410](batch-09.md#commit-410), [#411](batch-09.md#commit-411), [#412](batch-09.md#commit-412), [#413](batch-09.md#commit-413), [#414](batch-09.md#commit-414), [#415](batch-09.md#commit-415), [#416](batch-09.md#commit-416), [#417](batch-09.md#commit-417), [#418](batch-09.md#commit-418), [#419](batch-09.md#commit-419), [#420](batch-09.md#commit-420), [#421](batch-09.md#commit-421), [#422](batch-09.md#commit-422), [#423](batch-09.md#commit-423), [#424](batch-09.md#commit-424), [#425](batch-09.md#commit-425), [#426](batch-09.md#commit-426), [#427](batch-09.md#commit-427), [#428](batch-09.md#commit-428), [#429](batch-09.md#commit-429), [#430](batch-09.md#commit-430), [#431](batch-09.md#commit-431), [#432](batch-09.md#commit-432), [#433](batch-09.md#commit-433), [#434](batch-09.md#commit-434), [#435](batch-09.md#commit-435), [#436](batch-09.md#commit-436), [#437](batch-09.md#commit-437), [#438](batch-09.md#commit-438), [#439](batch-09.md#commit-439), [#440](batch-09.md#commit-440), [#441](batch-09.md#commit-441), [#442](batch-09.md#commit-442).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `input/gen_equilibrium_table.py`, `src/enzo/EvolveLevel.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.mach.ubuntu`, `src/enzo/ReadEquilibriumTable.C`.

<a id="commit-444"></a>
## 444 — `db38bc074` — 2024-02-21

add link to libyt repo.

**Categories:** 4.

Adds libyt source-repository link. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -11,6 +11,8 @@ Requirements`.

<a id="commit-445"></a>
## 445 — `83440af9b` — 2024-02-21

Add code snippet for yt_run_Function/yt_run_FunctionArguments.

**Categories:** 4.

Adds commented libyt function-call examples and matching documentation. Optional user analysis code; no automatic physical evolution change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -96,14 +96,33 @@ General`; `@@ -121,11 +140,11 @@ Interactive Python Prompt`; `@@ -327,7 +327,16 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-446"></a>
## 446 — `5ce5da3bf` — 2024-02-21

Add libyt to build page.

**Categories:** 1.

Documents optional libyt dependency on the build page. Clean patch, no simulation change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/building_enzo.rst`.

**Patch locations:** `@@ -27,6 +27,8 @@ compiler, the following libraries are necessary:`.

<a id="commit-447"></a>
## 447 — `0c81d48c0` — 2023-06-19

Merge pull request #10 from cindytsai/libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#392](batch-08.md#commit-392), [#393](batch-08.md#commit-393), [#394](batch-08.md#commit-394), [#395](batch-08.md#commit-395).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `doc/manual/source/user_guide/index.rst`.

<a id="commit-448"></a>
## 448 — `54e7a4c12` — 2024-02-17

Merge pull request #11 from cindytsai/libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#396](batch-08.md#commit-396), [#397](batch-08.md#commit-397), [#398](batch-08.md#commit-398), [#399](batch-08.md#commit-399), [#400](batch-08.md#commit-400), [#401](batch-09.md#commit-401), [#402](batch-09.md#commit-402), [#403](batch-09.md#commit-403), [#404](batch-09.md#commit-404).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`.

<a id="commit-449"></a>
## 449 — `65439d8bd` — 2024-02-19

Merge pull request #12 from cindytsai/libyt

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#405](batch-09.md#commit-405), [#406](batch-09.md#commit-406), [#407](batch-09.md#commit-407), [#408](batch-09.md#commit-408), [#409](batch-09.md#commit-409), [#410](batch-09.md#commit-410), [#411](batch-09.md#commit-411), [#412](batch-09.md#commit-412), [#413](batch-09.md#commit-413), [#414](batch-09.md#commit-414), [#415](batch-09.md#commit-415), [#416](batch-09.md#commit-416), [#417](batch-09.md#commit-417), [#418](batch-09.md#commit-418), [#419](batch-09.md#commit-419), [#420](batch-09.md#commit-420), [#421](batch-09.md#commit-421), [#422](batch-09.md#commit-422), [#423](batch-09.md#commit-423), [#424](batch-09.md#commit-424), [#425](batch-09.md#commit-425), [#426](batch-09.md#commit-426), [#427](batch-09.md#commit-427), [#428](batch-09.md#commit-428), [#429](batch-09.md#commit-429), [#430](batch-09.md#commit-430), [#431](batch-09.md#commit-431), [#432](batch-09.md#commit-432), [#433](batch-09.md#commit-433), [#434](batch-09.md#commit-434), [#435](batch-09.md#commit-435), [#436](batch-09.md#commit-436), [#437](batch-09.md#commit-437), [#438](batch-09.md#commit-438), [#439](batch-09.md#commit-439), [#440](batch-09.md#commit-440), [#441](batch-09.md#commit-441), [#442](batch-09.md#commit-442), [#443](batch-09.md#commit-443).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `input/gen_equilibrium_table.py`, `src/enzo/EvolveLevel.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.mach.ubuntu`, `src/enzo/ReadEquilibriumTable.C`.

<a id="commit-450"></a>
## 450 — `20109a7fc` — 2024-02-21

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Updates libyt requirements wording/link formatting. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -27,7 +27,7 @@ A brief description of each mode (option) is shown here. The options are mutuall`.
