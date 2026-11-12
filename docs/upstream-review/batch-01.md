# Batch 01: commits 001–050

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-001"></a>
## 001 — `642c2aaad` — 2019-10-25

Merge branch 'master' into sp-memfix

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** none; incoming history is already in the Aeos ancestry.

**Aeos-modified paths since common ancestor:** none.

**Files:** .

<a id="commit-002"></a>
## 002 — `9ecce3bbd` — 2020-03-26

Merge branch 'master' into sp-memfix

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** none; incoming history is already in the Aeos ancestry.

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/OutputFromEvolveLevel.C`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `.circleci/config.yml`, `.gitignore`, `README.md`, `doc/manual/source/parameters/index.rst`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/Grid_ZeusSolver.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/OutputFromEvolveLevel.C`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`.

<a id="commit-003"></a>
## 003 — `6148ab327` — 2020-03-26

Two Bugfixes from recent star particle memfix update

**Categories:** 3.

Both fixes already exist in Aeos: CommunicationCollectParticles uses j at the affected call, and StarParticleFindAll guards a zero local count. Aeos deliberately retains the allocated send buffer instead of replacing it with NULL. Do not replay the historical patch wholesale.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/CommunicationCollectParticles.C`, `src/enzo/StarParticleFindAll.C`.

**Files:** `src/enzo/CommunicationCollectParticles.C`, `src/enzo/StarParticleFindAll.C`.

**Patch locations:** `@@ -235,7 +235,7 @@ int CommunicationCollectParticles(LevelHierarchyEntry *LevelArray[],`; `@@ -153,7 +153,11 @@ int StarParticleFindAll(LevelHierarchyEntry *LevelArray[], Star *&AllStars)`.

<a id="commit-004"></a>
## 004 — `bcaf0b601` — 2020-05-20

Merge pull request #140 from aemerick/sp-memfix

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#001](batch-01.md#commit-001), [#002](batch-01.md#commit-002), [#003](batch-01.md#commit-003).

**Aeos-modified paths since common ancestor:** `src/enzo/CommunicationCollectParticles.C`, `src/enzo/StarParticleFindAll.C`.

**Files:** `src/enzo/CommunicationCollectParticles.C`, `src/enzo/StarParticleFindAll.C`.

<a id="commit-005"></a>
## 005 — `9be8a3564` — 2019-12-09

updated Make.mach.sdsc-comet to new compilers/hdf5 version

**Categories:** 4.

Comet compiler, MPI and HDF5 paths only; site-specific and later removed by the CMake migration. No scientific prescription changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.sdsc-comet`.

**Patch locations:** `@@ -8,6 +8,9 @@`; `@@ -17,15 +20,16 @@ MACH_FILE  = Make.mach.sdsc-comet`; `@@ -92,8 +96,8 @@ MACH_OPT_AGGRESSIVE  = -O3 -march=native # Flags for aggressive optimization`; `@@ -112,7 +116,7 @@ LOCAL_LIBS_HDF5   = -L$(LOCAL_HDF5_INSTALL)/lib -lhdf5 -lz # HDF5 libraries`.

<a id="commit-006"></a>
## 006 — `9bba9b4f0` — 2020-03-03

Merge branch 'master' of github.com:enzo-project/enzo-dev

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** none; incoming history is already in the Aeos ancestry.

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Make.config.objects`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/pop3_maker.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `README.md`, `doc/manual/source/parameters/index.rst`, `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_AddH2Dissociation.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/Grid_ZeusSolver.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.darwin`, `src/enzo/RadiativeTransferParameters.h`, `src/enzo/RadiativeTransferReadParameters.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/pop3_maker.F`, `src/enzo/typedefs.h`.

<a id="commit-007"></a>
## 007 — `30f124336` — 2020-03-06

changed hdf5 library to hdf5-serial/1.10.3

**Categories:** 4.

Comet serial-HDF5 module and MPI include placement; use only for that historical machine environment.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.sdsc-comet`.

**Patch locations:** `@@ -20,7 +20,19 @@ MACH_FILE  = Make.mach.sdsc-comet`; `@@ -96,8 +108,8 @@ MACH_OPT_AGGRESSIVE  = -O3 -march=native # Flags for aggressive optimization`.

<a id="commit-008"></a>
## 008 — `bbec987a5` — 2020-05-20

Merge pull request #130 from nsimakov/master

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#005](batch-01.md#commit-005), [#006](batch-01.md#commit-006), [#007](batch-01.md#commit-007).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.sdsc-comet`.

<a id="commit-009"></a>
## 009 — `f11fa90f3` — 2020-05-20

Merge pull request #144 from aemerick/grackle-parameters

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** none; incoming history is already in the Aeos ancestry.

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Make.config.objects`, `src/enzo/WriteParameterFile.C`.

**Files:** `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Make.config.objects`, `src/enzo/WriteParameterFile.C`.

<a id="commit-010"></a>
## 010 — `dd9e3d21a` — 2020-05-21

[docs] Removing bad links to sample data and updating input/ listing

**Categories:** 1.

Removes dead sample-output links and refreshes the input-directory listing; documentation and ignore rules only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `.gitignore`.

**Files:** `.gitignore`, `doc/manual/source/user_guide/RunTestProblem.rst`.

**Patch locations:** `@@ -53,5 +53,6 @@ src/enzo/Make.mach.mymac`; `@@ -129,42 +129,10 @@ directory. They are kept in input:`.

<a id="commit-011"></a>
## 011 — `db1113175` — 2020-05-22

[docs] Adding a new page with sample parameter files

**Categories:** 1.

Adds published cosmological example parameters and MUSIC configuration; examples are opt-in, not changes to Aeos runtime defaults. Do not substitute these parameters for the isolated disk configuration.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/SampleParameterFiles.rst`, `doc/manual/source/user_guide/index.rst`, `doc/manual/source/user_guide/samples/SG64-L2.conf`, `doc/manual/source/user_guide/samples/wise2014_zoomin_update.enzo`.

**Patch locations:** `@@ -0,0 +1,82 @@`; `@@ -58,4 +58,4 @@ inquiries and comments should be directed to the Enzo Users' List`; `@@ -0,0 +1,45 @@`; `@@ -0,0 +1,181 @@`.

<a id="commit-012"></a>
## 012 — `4cd76b2de` — 2020-05-22

Adding _build to doc make clean that's used with vscode

**Categories:** 1.

Documentation clean target removes the Sphinx _build directory only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/Makefile`.

**Patch locations:** `@@ -34,7 +34,7 @@ help:`.

<a id="commit-013"></a>
## 013 — `4628d2f26` — 2020-06-17

Merge pull request #152 from jwise77/sample-param-file

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#010](batch-01.md#commit-010), [#011](batch-01.md#commit-011), [#012](batch-01.md#commit-012).

**Aeos-modified paths since common ancestor:** `.gitignore`.

**Files:** `.gitignore`, `doc/manual/Makefile`, `doc/manual/source/user_guide/RunTestProblem.rst`, `doc/manual/source/user_guide/SampleParameterFiles.rst`, `doc/manual/source/user_guide/index.rst`, `doc/manual/source/user_guide/samples/SG64-L2.conf`, `doc/manual/source/user_guide/samples/wise2014_zoomin_update.enzo`.

<a id="commit-014"></a>
## 014 — `6b836c2e0` — 2020-04-03

Fixes an incorrect statement in the docs and an error for some configurations in the StochasticForcing problem

**Categories:** 3.

Initializes forcing amplitudes outside the selected spectrum to zero in 1D/2D/3D; otherwise the forcing array may retain undefined amplitudes. Conditional on stochastic-forcing use. Clean patch check succeeds.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/StochasticForcing_Init.C`.

**Patch locations:** `@@ -5020,7 +5020,7 @@ Turbulence Simulation with Stochastic Forcing (59)`; `@@ -180,6 +180,7 @@ AutoCorrlTime[0],AutoCorrlTime[1],AutoCorrlTime[2]);`; `@@ -229,6 +230,7 @@ AutoCorrlTime[0],AutoCorrlTime[1],AutoCorrlTime[2]);`; `@@ -279,6 +281,7 @@ AutoCorrlTime[0],AutoCorrlTime[1],AutoCorrlTime[2]);`.

<a id="commit-015"></a>
## 015 — `d8bd274eb` — 2020-06-17

Fixing comment in header per pgrete's comments on the PR

**Categories:** 1.

Corrects the forcing-spectrum header comment; no executable changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/StochasticForcing_Init.C`.

**Patch locations:** `@@ -17,8 +17,8 @@`.

<a id="commit-016"></a>
## 016 — `d23665b5b` — 2020-06-17

Merge pull request #141 from jcforbes/master

**Categories:** 1,3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#014](batch-01.md#commit-014), [#015](batch-01.md#commit-015).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `src/enzo/StochasticForcing_Init.C`.

<a id="commit-017"></a>
## 017 — `c3cde82b9` — 2020-06-02

Small(?) memory leak fix in radiation sources. Sources would sometimes (all the time?) not get deleted properly in the main EvolvePhotons loop. Placing an additional check after the loop to see if there are any sources with lifetimes < PhotonTime.

**Categories:** 3.

Expired-source cleanup at the end of EvolvePhotons is already present in Aeos, including the LoopTime/DeleteSources conditions. Missing ancestry does not mean missing fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolvePhotons.C`.

**Files:** `src/enzo/EvolvePhotons.C`.

**Patch locations:** `@@ -214,6 +214,9 @@ int EvolvePhotons(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; `@@ -236,8 +239,8 @@ int EvolvePhotons(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; `@@ -716,6 +719,28 @@ int EvolvePhotons(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`.

<a id="commit-018"></a>
## 018 — `e0412f0c5` — 2020-06-02

Larger memory leak fix in radiation sources. Global sources get deleted every timestep in StarParticleRadTransfer and this was not being done correctly

**Categories:** 3.

Aeos already walks source nodes through DeleteRadiationSource, which releases subsidiary source allocations. Preserve its custom radiation bin setup.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/StarParticleRadTransfer.C`.

**Patch locations:** `@@ -51,10 +51,11 @@ int StarParticleRadTransfer(LevelHierarchyEntry *LevelArray[], int level,`.

<a id="commit-019"></a>
## 019 — `11cbd28e5` — 2020-06-02

forgot function definition in last commit

**Categories:** 3.

Declaration prerequisite for #18; equivalent declaration already supports the existing Aeos cleanup. No independent physics change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/StarParticleRadTransfer.C`.

**Patch locations:** `@@ -34,6 +34,8 @@ int GetUnits(float *DensityUnits, float *LengthUnits,`.

<a id="commit-020"></a>
## 020 — `8d8249df8` — 2020-06-03

One last missing delete in StarParticleRadTransfer. Deleting the initial GlobalRadiationSource poitner

**Categories:** 3.

Exact patch-equivalent fix already incorporated: deletes and nulls the global source-list sentinel. Reverse patch check succeeds.

**Incorporation:** exact patch-equivalent in Aeos history. **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/StarParticleRadTransfer.C`.

**Patch locations:** `@@ -58,6 +58,8 @@ int StarParticleRadTransfer(LevelHierarchyEntry *LevelArray[], int level,`.

<a id="commit-021"></a>
## 021 — `3cc265f66` — 2020-06-03

And it looks like the incorrect GlobalRadiationSource deletion occured in ActiveParticles as well. Fixing this using same code from StarParticleRadTransfer

**Categories:** 3.

ActiveParticleInitialize still directly deletes source nodes. Adopt subsidiary-allocation cleanup for active-particle runs; retain TRANSFER guards from #22. Clean patch check succeeds.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticleInitialize.C`.

**Patch locations:** `@@ -30,6 +30,8 @@`; `@@ -56,10 +58,13 @@ int ActiveParticleInitialize(HierarchyEntry *Grids[], TopGridData *MetaData,`.

<a id="commit-022"></a>
## 022 — `b5e2339bb` — 2020-06-03

missed ifdef

**Categories:** 3.

Guards the radiation-source declaration for photon-disabled builds; apply together with #21, not in isolation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ActiveParticleInitialize.C`.

**Patch locations:** `@@ -30,7 +30,9 @@`.

<a id="commit-023"></a>
## 023 — `72159a9ee` — 2020-06-24

moving spaces and tabs

**Categories:** 1.

Whitespace cleanup around the existing EvolvePhotons expiry cleanup; clean patch check succeeds.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolvePhotons.C`.

**Files:** `src/enzo/EvolvePhotons.C`.

**Patch locations:** `@@ -727,17 +727,21 @@ int EvolvePhotons(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`.

<a id="commit-024"></a>
## 024 — `a1455524a` — 2020-06-24

Moving function to delete and clean up global radiation source list into its own routine

**Categories:** 4.

Extracts duplicated radiation-list deletion into DeleteGlobalRadiationSources. Helpful maintenance, but Aeos already has correct star-source cleanup; reconcile active-particle cleanup and custom source generation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/ActiveParticleInitialize.C`, `src/enzo/DeleteRadiationSource.C`, `src/enzo/StarParticleRadTransfer.C`.

**Patch locations:** `@@ -31,7 +31,7 @@`; `@@ -59,15 +59,9 @@ int ActiveParticleInitialize(HierarchyEntry *Grids[], TopGridData *MetaData,`; `@@ -15,7 +15,9 @@`; `@@ -50,3 +52,18 @@ RadiationSourceEntry* DeleteRadiationSource(RadiationSourceEntry *RS)`; `@@ -34,7 +34,7 @@ int GetUnits(float *DensityUnits, float *LengthUnits,`; additional hunks in the same patch.

<a id="commit-025"></a>
## 025 — `0332c0104` — 2020-07-17

Merge pull request #153 from aemerick/radsource-delete

**Categories:** 1,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#017](batch-01.md#commit-017), [#018](batch-01.md#commit-018), [#019](batch-01.md#commit-019), [#020](batch-01.md#commit-020), [#021](batch-01.md#commit-021), [#022](batch-01.md#commit-022), [#023](batch-01.md#commit-023), [#024](batch-01.md#commit-024).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolvePhotons.C`, `src/enzo/StarParticleRadTransfer.C`.

**Files:** `src/enzo/ActiveParticleInitialize.C`, `src/enzo/DeleteRadiationSource.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/StarParticleRadTransfer.C`.

<a id="commit-026"></a>
## 026 — `dc7be1999` — 2020-08-12

Avoid matplotlib version that clashes with stable yt.

**Categories:** 4.

Historical matplotlib/yt compatibility pins and CI image update; superseded by later dependency changes. No production solver changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -26,7 +26,8 @@ commands:`; `@@ -160,7 +161,7 @@ commands:`; `@@ -207,7 +208,7 @@ jobs:`; `@@ -234,7 +235,7 @@ jobs:`.

<a id="commit-027"></a>
## 027 — `a18c7585e` — 2020-08-12

Update dependencies cache.

**Categories:** 1.

CI dependency cache key only; mechanically applicable but obsolete as a present-day cache choice.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -171,13 +171,13 @@ jobs:`.

<a id="commit-028"></a>
## 028 — `4612039af` — 2020-08-12

Add name for each command.

**Categories:** 4.

Names and restructures CI shell steps; differs from current CI context and should be incorporated as part of a coherent CI refresh.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -4,73 +4,83 @@ commands:`; `@@ -85,78 +95,84 @@ commands:`.

<a id="commit-029"></a>
## 029 — `8f75306d8` — 2020-08-12

Change references to yt.enzotools.org to yt-project.org and remove a dead link.

**Categories:** 1.

Updates yt links, removes a lost utility-script link, and changes a Cython homepage comment; no execution change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/conf.py`, `doc/manual/source/reference/NestedGridParticles.rst`, `doc/manual/source/supplementary_info/EmbeddedPython.rst`, `src/enzo/python_bridge/problemtype_handler.pyx`.

**Patch locations:** `@@ -224,7 +224,6 @@ intersphinx_mapping = {'http://docs.python.org/': None,`; `@@ -93,17 +93,9 @@ and ParticleVelocities files. CosmologySimulationParticleMassName`; `@@ -55,7 +55,7 @@ How to Run`; `@@ -3,7 +3,7 @@ The beginnings of a mechanism for interacting with Enzo through Python`.

<a id="commit-030"></a>
## 030 — `d84c2415b` — 2020-08-28

Merge pull request #156 from brittonsmith/cifix

**Categories:** 1,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#026](batch-01.md#commit-026), [#027](batch-01.md#commit-027), [#028](batch-01.md#commit-028), [#029](batch-01.md#commit-029).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `doc/manual/source/conf.py`, `doc/manual/source/reference/NestedGridParticles.rst`, `doc/manual/source/supplementary_info/EmbeddedPython.rst`, `src/enzo/python_bridge/problemtype_handler.pyx`.

<a id="commit-031"></a>
## 031 — `c31adc43c` — 2021-02-23

Add SmartStarAccretion Parameter

**Categories:** 4.

Introduces SmartStarAccretion with default 8 and parameter I/O. Optional active-particle model interface; must accompany #32. It separates smart-star selection from MBHAccretion and can change existing smart-star runs.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -145,7 +145,7 @@ int grid::GrackleWrapper()`; `@@ -1345,6 +1345,7 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`; `@@ -1023,6 +1023,7 @@ int SetDefaultGlobalValues(TopGridData &MetaData)`; `@@ -332,6 +332,7 @@ int WriteParameterFile(FILE *fptr, TopGridData &MetaData, char *name = NULL)`; `@@ -1162,6 +1162,7 @@ class ActiveParticleType_info;`.

<a id="commit-032"></a>
## 032 — `86547baf3` — 2021-02-23

Replace MBHAccretion in relevant routine

**Categories:** 4.

Replaces MBHAccretion with SmartStarAccretion in the accretion branches. Explicitly migrate parameter files if adopting; irrelevant to individual-star disk feedback when smart stars are disabled.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_CalculateSmartStarAccretionRate.C`.

**Patch locations:** `@@ -178,10 +178,10 @@ float grid::CalculateSmartStarAccretionRate(ActiveParticleType* ThisParticle,`; `@@ -190,10 +190,10 @@ float grid::CalculateSmartStarAccretionRate(ActiveParticleType* ThisParticle,`; `@@ -215,9 +215,9 @@ float grid::CalculateSmartStarAccretionRate(ActiveParticleType* ThisParticle,`; `@@ -234,9 +234,9 @@ float grid::CalculateSmartStarAccretionRate(ActiveParticleType* ThisParticle,`; `@@ -247,9 +247,9 @@ float grid::CalculateSmartStarAccretionRate(ActiveParticleType* ThisParticle,`; additional hunks in the same patch.

<a id="commit-033"></a>
## 033 — `78909cf42` — 2021-02-23

Undo unintended change

**Categories:** 1.

Removes an accidental incomplete comment in the Grackle wrapper; no numerical change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`.

**Files:** `src/enzo/Grid_GrackleWrapper.C`.

**Patch locations:** `@@ -145,7 +145,7 @@ int grid::GrackleWrapper()`.

<a id="commit-034"></a>
## 034 — `0191ff5ad` — 2020-10-13

HDF5 reference fix

**Categories:** 1.

Despite its bug-fix subject, installed HDF5 1.8.23 defines hdset_reg_ref_t as unsigned char[H5R_DSET_REG_REF_BUF_SIZE]. Both old reference and new reference[1] occupy one reference buffer, and reference/&reference identify the same initial bytes passed through void*. No invalid-buffer defect is demonstrated by this patch; clean behavior-preserving array spelling refactor. Do not count it as a missing HDF5 correctness fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_CreateParticleTypeGrouping.C`.

**Patch locations:** `@@ -33,7 +33,7 @@ int grid::CreateParticleTypeGrouping(hid_t ptype_dset,`; `@@ -54,7 +54,7 @@ int grid::CreateParticleTypeGrouping(hid_t ptype_dset,`.

<a id="commit-035"></a>
## 035 — `a665ed233` — 2021-02-15

Merge pull request #158 from michaelkuhn/hdf5-ref-fix

**Categories:** 1.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#034](batch-01.md#commit-034).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_CreateParticleTypeGrouping.C`.

<a id="commit-036"></a>
## 036 — `a20abc765` — 2021-04-05

Download hypre from github.

**Categories:** 4.

Historical HYPRE download source/version update for CI; take the completed #36-38 sequence if relevant, not the broken intermediate download/extract commands.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -10,7 +10,7 @@ commands:`; `@@ -36,7 +36,7 @@ commands:`.

<a id="commit-037"></a>
## 037 — `7202ac328` — 2021-04-05

Fix filenames.

**Categories:** 4.

Aligns downloaded HYPRE archive and extracted directory names, but introduces v{$HYPRE} typo fixed in #38. Do not adopt alone.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -10,7 +10,7 @@ commands:`; `@@ -36,9 +36,9 @@ commands:`.

<a id="commit-038"></a>
## 038 — `001bc4b0a` — 2021-04-05

Typo.

**Categories:** 3.

Fixes the HYPRE shell archive interpolation introduced by #37; build infrastructure only and conditional on that earlier change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -37,7 +37,7 @@ commands:`.

<a id="commit-039"></a>
## 039 — `16b9cbd84` — 2021-04-12

Merge pull request #170 from brittonsmith/hypre

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#036](batch-01.md#commit-036), [#037](batch-01.md#commit-037), [#038](batch-01.md#commit-038).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-040"></a>
## 040 — `0a9a5d7e4` — 2021-03-03

Add uuid compile option.

**Categories:** 4.

Adds UUID compilation option and guards UUID generation. Preserve default-on behavior and check metadata consumers when disabled; integrate Aeos Make configuration entries manually where needed.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/uuid.C`.

**Patch locations:** `@@ -974,6 +974,37 @@`; `@@ -1031,6 +1062,7 @@`; `@@ -1049,7 +1081,8 @@`; `@@ -951,16 +951,6 @@ OBJS_CONFIG_LIB = \`; `@@ -1240,4 +1230,15 @@ OBJS_ECUDA_ALL = \`; additional hunks in the same patch.

<a id="commit-041"></a>
## 041 — `e1aba7e14` — 2021-04-12

Merge pull request #166 from brittonsmith/uuid

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#040](batch-01.md#commit-040).

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/uuid.C`.

<a id="commit-042"></a>
## 042 — `0f89eb892` — 2021-02-26

Exit with error if metal cooling on but no metal field present.

**Categories:** 3,2.

Aeos still silently disables MetalCooling without a metal field, mutating a global flag and assigning MetalNum=0. Adopt a fail-fast field contract adapted to the Grackle backend profiles; this changes behavior of invalid configurations and overlaps the customized wrapper.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`.

**Files:** `src/enzo/Grid_GrackleWrapper.C`.

**Patch locations:** `@@ -142,10 +142,7 @@ int grid::GrackleWrapper()`.

<a id="commit-043"></a>
## 043 — `99b3761db` — 2021-04-12

Merge pull request #165 from brittonsmith/metalerror

**Categories:** 2,3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#042](batch-01.md#commit-042).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`.

**Files:** `src/enzo/Grid_GrackleWrapper.C`.

<a id="commit-044"></a>
## 044 — `6025141cd` — 2021-04-12

Merge branch 'master' into change_MBHAccretion

**Categories:** 3,2.

Remerge-diff resolves the customized metal-field branch in favor of fail-fast ENZO_FAIL rather than silent MetalCooling disable. Same substantive decision as #42; Aeos still has the silent path, so adapt to backend profiles.

**Merge inspection:** combined diff 0 bytes; remerge diff 857 bytes. Positive results are discussed above.

**Constituents in inventory:** [#034](batch-01.md#commit-034), [#035](batch-01.md#commit-035), [#036](batch-01.md#commit-036), [#037](batch-01.md#commit-037), [#038](batch-01.md#commit-038), [#039](batch-01.md#commit-039), [#040](batch-01.md#commit-040), [#041](batch-01.md#commit-041), [#042](batch-01.md#commit-042), [#043](batch-01.md#commit-043).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `.circleci/config.yml`, `src/enzo/Grid_CreateParticleTypeGrouping.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/uuid.C`.

<a id="commit-045"></a>
## 045 — `919383a16` — 2021-04-12

Merge pull request #164 from simonetgordon/change_MBHAccretion

**Categories:** 1,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#031](batch-01.md#commit-031), [#032](batch-01.md#commit-032), [#033](batch-01.md#commit-033), [#044](batch-01.md#commit-044).

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/Grid_CalculateSmartStarAccretionRate.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

<a id="commit-046"></a>
## 046 — `eb570bc57` — 2021-08-10

Fixed MPI issue

**Categories:** 4,2.

Resizes persistent MPI star buffers downward and resets empty-rank buffers. Aeos already guards empty LocalStars and retains a valid allocated buffer at zero count, so the original claimed MPI fix is not independently proven necessary here. Evaluate buffer lifetime transitions before adapting this optimization.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/StarParticleFindAll.C`.

**Files:** `src/enzo/StarParticleFindAll.C`.

**Patch locations:** `@@ -4,7 +4,8 @@`; `@@ -142,22 +143,52 @@ int StarParticleFindAll(LevelHierarchyEntry *LevelArray[], Star *&AllStars)`.

<a id="commit-047"></a>
## 047 — `397e39336` — 2021-08-29

updated circleci image

**Categories:** 4.

CI image namespace update only; historical image pin should be replaced coherently with final CI requirements.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -177,7 +177,7 @@ commands:`; `@@ -224,7 +224,7 @@ jobs:`; `@@ -251,7 +251,7 @@ jobs:`.

<a id="commit-048"></a>
## 048 — `437f87c09` — 2021-08-29

fix yt version import

**Categories:** 4.

Updates the yt version import in test_runner; later yt4 changes supersede it. Runtime simulation physics unaffected.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `run/test_runner.py`.

**Patch locations:** `@@ -42,7 +42,7 @@ ytcfg["yt","suppressStreamLogging"] = "True"`.

<a id="commit-049"></a>
## 049 — `71acdedb1` — 2021-09-01

Force yt 3.6 install to (temporarily) fix test_runner problems in gold standard.

**Categories:** 4.

Temporary yt 3.6.1 CI pin; explicitly superseded by yt4 modernization. Do not reinstate.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -31,7 +31,7 @@ commands:`.

<a id="commit-050"></a>
## 050 — `6537e464e` — 2021-10-19

Merge pull request #179 from gregbryan/master

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#047](batch-01.md#commit-047), [#048](batch-01.md#commit-048), [#049](batch-01.md#commit-049).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/test_runner.py`.
