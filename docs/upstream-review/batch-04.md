# Batch 04: commits 151–200

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-151"></a>
## 151 — `c83572fa0` — 2022-06-29

Update src/enzo/Make.mach.nasa-aitken-rome

**Categories:** 4.

Removes obsolete Python 2.7 headers from the added Aitken machine file; prerequisite-specific cleanup.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.nasa-aitken-rome`.

**Patch locations:** `@@ -108,8 +108,6 @@ MACH_OPT_AGGRESSIVE  = -O3  -ip -ipo -march=core-avx2`.

<a id="commit-152"></a>
## 152 — `6f2f7c2cb` — 2022-06-29

Update src/enzo/Make.mach.nasa-aitken-rome

**Categories:** 4.

Removes obsolete Python linker setup from Aitken machine configuration; no runtime physics change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.nasa-aitken-rome`.

**Patch locations:** `@@ -124,7 +124,6 @@ LOCAL_LIBS_HDF5   = -L$(LOCAL_HDF5_INSTALL)/lib -lhdf5 -lz`.

<a id="commit-153"></a>
## 153 — `9ea66d30a` — 2022-06-29

Update src/enzo/Make.mach.nasa-aitken-rome

**Categories:** 4.

Removes stale commented Python-library reference from Aitken linker settings.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.nasa-aitken-rome`.

**Patch locations:** `@@ -127,5 +127,5 @@ LOCAL_LIBS_GRACKLE = -L$(LOCAL_GRACKLE_INSTALL)/lib -lgrackle`.

<a id="commit-154"></a>
## 154 — `99c949fb6` — 2022-06-29

Update src/enzo/Make.mach.nasa-pleiades

**Categories:** 4.

Updates Pleiades CPU dispatch flags; site-specific optimization, not a necessary physics correction.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.nasa-pleiades`.

**Files:** `src/enzo/Make.mach.nasa-pleiades`.

**Patch locations:** `@@ -113,8 +113,8 @@ MACH_OPT_DEBUG       = -g -O0`.

<a id="commit-155"></a>
## 155 — `de5c187cb` — 2022-06-29

Update src/enzo/Make.mach.nasa-pleiades

**Categories:** 4.

Removes leftover Python include/comment setup in the Pleiades machine file.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.nasa-pleiades`.

**Files:** `src/enzo/Make.mach.nasa-pleiades`.

**Patch locations:** `@@ -110,7 +110,7 @@ MACH_LDFLAGS  =`.

<a id="commit-156"></a>
## 156 — `805cc522e` — 2022-07-01

Merge remote-tracking branch 'main/main'

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#047](batch-01.md#commit-047), [#048](batch-01.md#commit-048), [#049](batch-01.md#commit-049), [#050](batch-01.md#commit-050), [#051](batch-02.md#commit-051), [#052](batch-02.md#commit-052), [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056), [#057](batch-02.md#commit-057), [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068), [#069](batch-02.md#commit-069), [#070](batch-02.md#commit-070), [#071](batch-02.md#commit-071), [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074), [#075](batch-02.md#commit-075), [#076](batch-02.md#commit-076), [#077](batch-02.md#commit-077), [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079), [#080](batch-02.md#commit-080), [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`, `run/test_runner.py`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.tigercpu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/lcaperf.h`, `src/enzo/star_maker2.F`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

<a id="commit-157"></a>
## 157 — `227d23b40` — 2022-07-10

Merge branch 'fix-test-suite' into new pleiades machine file

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

<a id="commit-158"></a>
## 158 — `c92a00fcd` — 2022-07-13

Merge branch 'fix-test-suite'

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-159"></a>
## 159 — `539e81e88` — 2022-07-14

Merge remote-tracking branch 'upstream/main'

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

<a id="commit-160"></a>
## 160 — `d83599453` — 2022-07-15

Merge pull request #173 from peeples/master

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#148](batch-03.md#commit-148), [#149](batch-03.md#commit-149), [#150](batch-03.md#commit-150), [#151](batch-04.md#commit-151), [#152](batch-04.md#commit-152), [#153](batch-04.md#commit-153), [#154](batch-04.md#commit-154), [#155](batch-04.md#commit-155), [#156](batch-04.md#commit-156), [#157](batch-04.md#commit-157), [#158](batch-04.md#commit-158), [#159](batch-04.md#commit-159).

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.nasa-pleiades`.

**Files:** `src/enzo/Make.mach.nasa-aitken-rome`, `src/enzo/Make.mach.nasa-pleiades`.

<a id="commit-161"></a>
## 161 — `2dee1c9a8` — 2020-03-20

add particle IC following a given FDM IC

**Categories:** 4.

Adds particles sampled from FDM initial conditions; optional FDM initializer behavior, not individual-star physics.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`.

**Patch locations:** `@@ -48,7 +48,6 @@ int CosmologyComputeExpansionFactor(FLOAT time, FLOAT *a, FLOAT *dadt);`; `@@ -109,14 +108,18 @@ int grid::FDMCollapseInitializeGrid()`; `@@ -130,9 +133,114 @@ if(QuantumPressure){`.

<a id="commit-162"></a>
## 162 — `692718371` — 2020-03-20

add particle IC following a given FDM IC

**Categories:** 4.

Adds FDM particle-selection/density parameters and extends initializer signatures. Port caller and declaration changes together.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/FDMCollapse.C`, `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`.

**Patch locations:** `@@ -59,6 +59,8 @@ int FDMCollapseInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -67,11 +69,28 @@ int FDMCollapseInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -2673,7 +2673,7 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -48,7 +48,7 @@ int CosmologyComputeExpansionFactor(FLOAT time, FLOAT *a, FLOAT *dadt);`; `@@ -136,9 +136,7 @@ if(QuantumPressure){`.

<a id="commit-163"></a>
## 163 — `b37bd488c` — 2020-03-20

add particle IC following a given FDM IC

**Categories:** 4.

Brace/loop cleanup in the newly added FDM particle sampling; dependent development cleanup.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`.

**Patch locations:** `@@ -230,10 +230,10 @@ if(QuantumPressure){`.

<a id="commit-164"></a>
## 164 — `07bbc7b97` — 2020-03-20

add particle IC following a given FDM IC

**Categories:** 4.

Removes a QuantumPressure guard around FDM setup and formats the initializer call; relevant to that optional problem's supported configurations.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/FDMCollapse.C`.

**Patch locations:** `@@ -87,7 +87,7 @@ int FDMCollapseInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -100,11 +100,11 @@ int FDMCollapseInitialize(FILE *fptr, FILE *Outfptr,`.

<a id="commit-165"></a>
## 165 — `9c3eacf47` — 2020-11-26

move UseHydro in EvolveLevel

**Categories:** 3,2.

Moves UseHydro around both legacy and RK solver dispatch so UseHydro=0 suppresses legacy hydro too. This overlaps Aeos EvolveLevel; adapt the dispatch deliberately and check both RK stages rather than replacing the file.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/EvolveLevel.C`.

**Patch locations:** `@@ -571,11 +571,11 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; `@@ -583,8 +583,8 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`.

<a id="commit-166"></a>
## 166 — `3ad367e2b` — 2020-12-21

add option of absorbing boundary and initiation particles in FDMCollapse

**Categories:** 4.

Declares FDMCollapseAbsorbingBoundary; requires initialization, I/O and implementation from subsequent commits. Not usable alone.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/global_data.h`.

**Patch locations:** `@@ -132,6 +132,10 @@ EXTERN int QuantumPressure;`.

<a id="commit-167"></a>
## 167 — `d833377a3` — 2020-12-21

add option of absorbing boundary and initiation particles in FDMCollapse

**Categories:** 4.

Adds FDM absorbing-boundary mask/potential output and particle initialization controls. Boundary damping is an intentional new physical/numerical choice.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `src/enzo/FDMCollapse.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Patch locations:** `@@ -59,6 +59,7 @@ int FDMCollapseInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -105,6 +106,8 @@ int FDMCollapseInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -69,12 +69,14 @@ int grid::FDMCollapseInitializeGrid(int UseParticles, float ParticleMeanDensity)`; `@@ -93,6 +95,7 @@ int grid::FDMCollapseInitializeGrid(int UseParticles, float ParticleMeanDensity)`; `@@ -111,13 +114,13 @@ int grid::FDMCollapseInitializeGrid(int UseParticles, float ParticleMeanDensity)`; additional hunks in the same patch.

<a id="commit-168"></a>
## 168 — `9b0770f2f` — 2020-03-23

add particle IC following a given FDM IC

**Categories:** 4.

Corrects FDM ghost-cell/index handling during particle initialization and removes unnecessary QuantumPressure wrappers; conditional on the FDM particle feature.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`.

**Patch locations:** `@@ -69,11 +69,11 @@ int grid::FDMCollapseInitializeGrid(int UseParticles, float ParticleMeanDensity)`; `@@ -111,7 +111,7 @@ int grid::FDMCollapseInitializeGrid(int UseParticles, float ParticleMeanDensity)`; `@@ -133,7 +133,7 @@ if(QuantumPressure){`; `@@ -175,70 +175,73 @@ if(QuantumPressure){`.

<a id="commit-169"></a>
## 169 — `a44d5e310` — 2020-12-21

add option of absorbing boundary and initiation particles in FDMCollapse

**Categories:** 4.

Remerge-diff keeps FDMCollapseAbsorbingBoundary-gated GridDensity input and reconciles particle-initialization comments. Optional FDM model integration; no additional disk-physics fix.

**Merge inspection:** combined diff 0 bytes; remerge diff 2225 bytes. Positive results are discussed above.

**Constituents in inventory:** [#168](batch-04.md#commit-168).

**Aeos-modified paths since common ancestor:** none.

**Files:** .

<a id="commit-170"></a>
## 170 — `07ee2dc3b` — 2020-12-21

add option of absorbing boundary in FDMCollapse

**Categories:** 4.

Adds density-mask wavefunction damping for FDMCollapse; also changes global default optimization from debug to high. Split out the build-default change if porting this optional physical boundary model.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.settings`.

**Files:** `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/Make.config.settings`.

**Patch locations:** `@@ -294,19 +294,23 @@ int grid::SchrodingerSolver( int nhy )`; `@@ -213,7 +213,7 @@`.

<a id="commit-171"></a>
## 171 — `9b6156d73` — 2021-06-23

merge upstream

**Categories:** 3.

Remerge-diff restores the active GrackleWriteParameters call rather than the FDM branch's commented-out version. Aeos already writes Grackle parameters; do not remove that restart/provenance support.

**Merge inspection:** combined diff 0 bytes; remerge diff 874 bytes. Positive results are discussed above.

**Constituents in inventory:** [#001](batch-01.md#commit-001), [#002](batch-01.md#commit-002), [#003](batch-01.md#commit-003), [#004](batch-01.md#commit-004), [#005](batch-01.md#commit-005), [#006](batch-01.md#commit-006), [#007](batch-01.md#commit-007), [#008](batch-01.md#commit-008), [#009](batch-01.md#commit-009), [#010](batch-01.md#commit-010), [#011](batch-01.md#commit-011), [#012](batch-01.md#commit-012), [#013](batch-01.md#commit-013), [#014](batch-01.md#commit-014), [#015](batch-01.md#commit-015), [#016](batch-01.md#commit-016), [#017](batch-01.md#commit-017), [#018](batch-01.md#commit-018), [#019](batch-01.md#commit-019), [#020](batch-01.md#commit-020), [#021](batch-01.md#commit-021), [#022](batch-01.md#commit-022), [#023](batch-01.md#commit-023), [#024](batch-01.md#commit-024), [#025](batch-01.md#commit-025), [#026](batch-01.md#commit-026), [#027](batch-01.md#commit-027), [#028](batch-01.md#commit-028), [#029](batch-01.md#commit-029), [#030](batch-01.md#commit-030), [#031](batch-01.md#commit-031), [#032](batch-01.md#commit-032), [#033](batch-01.md#commit-033), [#034](batch-01.md#commit-034), [#035](batch-01.md#commit-035), [#036](batch-01.md#commit-036), [#037](batch-01.md#commit-037), [#038](batch-01.md#commit-038), [#039](batch-01.md#commit-039), [#040](batch-01.md#commit-040), [#041](batch-01.md#commit-041), [#042](batch-01.md#commit-042), [#043](batch-01.md#commit-043), [#044](batch-01.md#commit-044), [#045](batch-01.md#commit-045).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/CommunicationCollectParticles.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CollectStars.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_TransferSubgridStars.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleFindAll.C`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/StarRoutines.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Files:** `.circleci/config.yml`, `.gitignore`, `doc/manual/Makefile`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/reference/NestedGridParticles.rst`, `doc/manual/source/supplementary_info/EmbeddedPython.rst`, `doc/manual/source/user_guide/RunTestProblem.rst`, `doc/manual/source/user_guide/SampleParameterFiles.rst`, `doc/manual/source/user_guide/index.rst`, `doc/manual/source/user_guide/samples/SG64-L2.conf`, `doc/manual/source/user_guide/samples/wise2014_zoomin_update.enzo`, `src/enzo/ActiveParticleInitialize.C`, `src/enzo/CommunicationCollectParticles.C`, `src/enzo/CommunicationTransferSubgridParticles.C`, `src/enzo/DeleteRadiationSource.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/GrackleWriteParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CalculateSmartStarAccretionRate.C`, `src/enzo/Grid_CollectStars.C`, `src/enzo/Grid_CommunicationSendStars.C`, `src/enzo/Grid_CommunicationTransferStarsOpt.C`, `src/enzo/Grid_CreateParticleTypeGrouping.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_TransferSubgridStars.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.objects`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`, `src/enzo/Make.mach.sdsc-comet`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleFindAll.C`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/StarRoutines.C`, `src/enzo/StochasticForcing_Init.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`, `src/enzo/python_bridge/problemtype_handler.pyx`, `src/enzo/uuid.C`.

<a id="commit-172"></a>
## 172 — `4989374f1` — 2021-08-29

remove a few comments

**Categories:** 4.

FDM field-label cleanup and removal of commented initialization experiments; includes build-setting context and is not a universal bug correction.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Make.config.settings`.

**Files:** `src/enzo/FDMCollapse.C`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Make.config.settings`.

**Patch locations:** `@@ -101,11 +101,10 @@ int FDMCollapseInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -69,11 +69,10 @@ int grid::FDMCollapseInitializeGrid(int UseParticles, float ParticleMeanDensity)`; `@@ -170,30 +169,6 @@ if(FDMCollapseAbsorbingBoundary){`; `@@ -215,7 +215,7 @@`.

<a id="commit-173"></a>
## 173 — `93e9075a5` — 2021-08-29

Add option for a point source potential to the Schrodinger solver

**Categories:** 4.

Substantively replaces the Schrodinger point-source potential with a rotating tidal potential centered on 0.5, removes cell-center offsets and introduces orbital-radius divisions. Do not treat the subject's 'option' as a harmless addition: existing PointSourceGravity behavior changes, with singular cases requiring tests.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_SchrodingerSolver.C`.

**Patch locations:** `@@ -216,39 +216,53 @@ int grid::SchrodingerSolver( int nhy )`.

<a id="commit-174"></a>
## 174 — `2a1f0d046` — 2021-10-19

Merge branch 'main' of https://github.com/enzo-project/enzo-dev

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#047](batch-01.md#commit-047), [#048](batch-01.md#commit-048), [#049](batch-01.md#commit-049), [#050](batch-01.md#commit-050).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/test_runner.py`.

<a id="commit-175"></a>
## 175 — `0534dfeb3` — 2022-01-28

Merge branch 'enzo-project:main' into master

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#051](batch-02.md#commit-051), [#052](batch-02.md#commit-052).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-176"></a>
## 176 — `e54b2be0a` — 2022-03-10

add test particle for a cluster

**Categories:** 4.

Changes hard-coded FDM test-particle count and cluster size (1000 to 10000). Test-model choice, later retuned.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`.

**Patch locations:** `@@ -167,7 +167,7 @@ if(FDMCollapseAbsorbingBoundary){`; `@@ -177,11 +177,11 @@ if(FDMCollapseAbsorbingBoundary){`.

<a id="commit-177"></a>
## 177 — `5b34caec7` — 2022-03-15

modified heating initialization

**Categories:** 4.

Retunes the FDM cluster particle count and spatial extent again; optional experiment, not a general heating repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`.

**Patch locations:** `@@ -167,7 +167,7 @@ if(FDMCollapseAbsorbingBoundary){`; `@@ -177,9 +177,9 @@ if(FDMCollapseAbsorbingBoundary){`.

<a id="commit-178"></a>
## 178 — `160a86aba` — 2022-04-15

experimenting ParallelRootGridIO

**Categories:** 4,2.

Adds parallel FDM initialization/reinitialization, problem dispatch and machine file. Overlaps common Grid and initialization interfaces; adopt only for an intentional FDM project.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_ParallelFDMCollapseInitialize.C`, `src/enzo/InitializeLocal.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.niagara`, `src/enzo/ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -2675,6 +2675,14 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; `@@ -144,6 +144,7 @@ if(FDMCollapseAbsorbingBoundary){`; `@@ -177,9 +178,9 @@ if(FDMCollapseAbsorbingBoundary){`; `@@ -0,0 +1,372 @@`; `@@ -37,7 +37,9 @@ int NestedCosmologySimulationReInitialize(HierarchyEntry *TopGrid,`; additional hunks in the same patch.

<a id="commit-179"></a>
## 179 — `bc7125b71` — 2022-04-26

ParallelRootGridIO for FDMCollapse

**Categories:** 4.

Completes FDM parallel particle sampling and problem dispatch; changes cluster scale/count. Requires preceding feature and deterministic/MPI sampling verification if used.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`, `src/enzo/InitializeNew.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_ParallelFDMCollapseInitialize.C`, `src/enzo/InitializeNew.C`.

**Patch locations:** `@@ -144,7 +144,7 @@ if(FDMCollapseAbsorbingBoundary){`; `@@ -168,7 +168,7 @@ if(FDMCollapseAbsorbingBoundary){`; `@@ -43,9 +43,6 @@ void my_exit(int status);`; `@@ -235,7 +232,6 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`; `@@ -244,6 +240,8 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`; additional hunks in the same patch.

<a id="commit-180"></a>
## 180 — `40db2133a` — 2022-04-26

Merge branch 'heating'

**Categories:** 2,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#176](batch-04.md#commit-176), [#177](batch-04.md#commit-177), [#178](batch-04.md#commit-178), [#179](batch-04.md#commit-179).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`.

**Files:** `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_ParallelFDMCollapseInitialize.C`, `src/enzo/InitializeLocal.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.niagara`, `src/enzo/ParallelFDMCollapseInitialize.C`.

<a id="commit-181"></a>
## 181 — `2624b12aa` — 2022-07-13

Merge remote-tracking branch 'upstream/main'

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056), [#057](batch-02.md#commit-057), [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068), [#069](batch-02.md#commit-069), [#070](batch-02.md#commit-070), [#071](batch-02.md#commit-071), [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074), [#075](batch-02.md#commit-075), [#076](batch-02.md#commit-076), [#077](batch-02.md#commit-077), [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079), [#080](batch-02.md#commit-080), [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.tigercpu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/lcaperf.h`, `src/enzo/star_maker2.F`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

<a id="commit-182"></a>
## 182 — `0f690d2d7` — 2022-07-13

fetch gold-standard-v15 tag

**Categories:** 4.

Despite its tag-fetch message, changes FDM cluster radius to 200 pc and radial sampling to R*u^(1/3). This intentionally changes ICs; not a CI-only patch.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -241,7 +241,7 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`; `@@ -275,7 +275,7 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`.

<a id="commit-183"></a>
## 183 — `713c6cb5f` — 2022-07-10

Merge branch 'fix-test-suite' into fdm-update

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#053](batch-02.md#commit-053), [#054](batch-02.md#commit-054), [#055](batch-02.md#commit-055), [#056](batch-02.md#commit-056), [#057](batch-02.md#commit-057), [#058](batch-02.md#commit-058), [#059](batch-02.md#commit-059), [#060](batch-02.md#commit-060), [#061](batch-02.md#commit-061), [#062](batch-02.md#commit-062), [#063](batch-02.md#commit-063), [#064](batch-02.md#commit-064), [#065](batch-02.md#commit-065), [#066](batch-02.md#commit-066), [#067](batch-02.md#commit-067), [#068](batch-02.md#commit-068), [#069](batch-02.md#commit-069), [#070](batch-02.md#commit-070), [#071](batch-02.md#commit-071), [#072](batch-02.md#commit-072), [#073](batch-02.md#commit-073), [#074](batch-02.md#commit-074), [#075](batch-02.md#commit-075), [#076](batch-02.md#commit-076), [#077](batch-02.md#commit-077), [#078](batch-02.md#commit-078), [#079](batch-02.md#commit-079), [#080](batch-02.md#commit-080), [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114), [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

**Files:** `.circleci/config.yml`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/amr_cosmology.enzotest`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/RayleighTaylor_CT_Suppressed/RayleighTaylor_CT_Suppressed.enzotest`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/ExternalBoundary_SetExternalBoundaryIO.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/Make.mach.tigercpu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_CollapseMHD3DInitializeGrid.C`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/lcaperf.h`, `src/enzo/star_maker2.F`, `src/enzo/star_maker_ssn.F`, `src/enzo/typedefs.h`.

<a id="commit-184"></a>
## 184 — `9c346ba73` — 2022-07-13

Merge branch 'master' of https://github.com/suniverse/enzo-dev

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131), [#183](batch-04.md#commit-183).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

<a id="commit-185"></a>
## 185 — `98adda7d5` — 2022-07-13

fetch new tags

**Categories:** 4.

Despite its tag-fetch message, adds a blank line in the new FDM initializer. No executable change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -364,6 +364,7 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`.

<a id="commit-186"></a>
## 186 — `5e4907c5f` — 2022-07-13

Fetching tags from PR issuing repo in CI

**Categories:** 4.

Actually adds a CI origin-tag fetch; infrastructure only, superseded by final CI workflow.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -11,8 +11,9 @@ commands:`.

<a id="commit-187"></a>
## 187 — `adf82bc39` — 2022-07-13

Merge branch 'fix-test-suite' into fdm-update

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#186](batch-04.md#commit-186).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-188"></a>
## 188 — `c60ff78eb` — 2022-07-13

Fixing conflict

**Categories:** 4.

Remerge-diff chooses the CI environment-sourced PR repository tag fetch over origin-only fetching. Infrastructure resolution only despite vague subject.

**Merge inspection:** combined diff 0 bytes; remerge diff 1083 bytes. Positive results are discussed above.

**Constituents in inventory:** [#133](batch-03.md#commit-133).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-189"></a>
## 189 — `d2c9825f1` — 2022-07-13

Merge branch 'fix-test-suite' into fdm-update

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#134](batch-03.md#commit-134).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-190"></a>
## 190 — `68b7c8d2e` — 2022-07-13

fetch new tags

**Categories:** 4.

Removes the same FDM blank line; no executable change despite tag-fetch subject.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -364,7 +364,6 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`.

<a id="commit-191"></a>
## 191 — `775d5c832` — 2022-07-13

fetch new tag

**Categories:** 4.

Readds the FDM blank line; no executable change despite tag-fetch subject.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -364,6 +364,7 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`.

<a id="commit-192"></a>
## 192 — `3d54eef3b` — 2022-07-14

Merge remote-tracking branch 'upstream/main' into fdm-update

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

<a id="commit-193"></a>
## 193 — `632e05adb` — 2022-07-21

Update src/enzo/Grid_FDMCollapse.C

**Categories:** 4.

Replaces the FDM approximate kpc conversion with kpc_cm; small numerical change in the optional initializer.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`.

**Patch locations:** `@@ -144,7 +144,7 @@ if(FDMCollapseAbsorbingBoundary){`.

<a id="commit-194"></a>
## 194 — `202979ad5` — 2022-07-21

Update src/enzo/Grid_ParallelFDMCollapseInitialize.C

**Categories:** 4.

Changes FDM diagnostic stream and message only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -251,7 +251,7 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`.

<a id="commit-195"></a>
## 195 — `3de94c3d0` — 2022-07-21

Update src/enzo/Grid_ParallelFDMCollapseInitialize.C

**Categories:** 4.

Uses M_PI rather than a rounded decimal in FDM azimuth sampling; minor numerical portability/accuracy change, not Aeos stellar physics.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -274,7 +274,7 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`.

<a id="commit-196"></a>
## 196 — `b59141e15` — 2022-07-21

Update src/enzo/Grid_ParallelFDMCollapseInitialize.C

**Categories:** 4.

Adds processor identification to FDM particle-count logging only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_ParallelFDMCollapseInitialize.C`.

**Patch locations:** `@@ -362,7 +362,7 @@ int grid::ParallelFDMCollapseInitializeGrid(char *FDMCollapseRePsiName,`.

<a id="commit-197"></a>
## 197 — `fc009e030` — 2022-07-21

Update src/enzo/Make.mach.niagara

**Categories:** 4.

Updates the Niagara machine identifier to its namespaced spelling; apply with the actual file move.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.niagara`.

**Patch locations:** `@@ -12,7 +12,7 @@`.

<a id="commit-198"></a>
## 198 — `4e5be796a` — 2022-07-21

update suggested changes

**Categories:** 4.

Adds the renamed Niagara machine configuration and shared physical-constants include to the FDM initializer; opt-in platform support.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_FDMCollapse.C`.

**Files:** `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Make.mach.scinet-niagara`.

**Patch locations:** `@@ -23,6 +23,7 @@`; `@@ -0,0 +1,127 @@`.

<a id="commit-199"></a>
## 199 — `3929adf79` — 2022-07-21

rename niagara make file

**Categories:** 4.

Removes the old Niagara filename after adding scinet-niagara. Reverse check alone does not mean a missing code fix; preserve locally useful machine files.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.niagara`.

**Patch locations:** `@@ -1,127 +0,0 @@`.

<a id="commit-200"></a>
## 200 — `48ca38478` — 2022-07-21

Merge pull request #175 from suniverse/master

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#161](batch-04.md#commit-161), [#162](batch-04.md#commit-162), [#163](batch-04.md#commit-163), [#164](batch-04.md#commit-164), [#165](batch-04.md#commit-165), [#166](batch-04.md#commit-166), [#167](batch-04.md#commit-167), [#168](batch-04.md#commit-168), [#169](batch-04.md#commit-169), [#170](batch-04.md#commit-170), [#171](batch-04.md#commit-171), [#172](batch-04.md#commit-172), [#173](batch-04.md#commit-173), [#174](batch-04.md#commit-174), [#175](batch-04.md#commit-175), [#176](batch-04.md#commit-176), [#177](batch-04.md#commit-177), [#178](batch-04.md#commit-178), [#179](batch-04.md#commit-179), [#180](batch-04.md#commit-180), [#181](batch-04.md#commit-181), [#182](batch-04.md#commit-182), [#183](batch-04.md#commit-183), [#184](batch-04.md#commit-184), [#185](batch-04.md#commit-185), [#186](batch-04.md#commit-186), [#187](batch-04.md#commit-187), [#188](batch-04.md#commit-188), [#189](batch-04.md#commit-189), [#190](batch-04.md#commit-190), [#191](batch-04.md#commit-191), [#192](batch-04.md#commit-192), [#193](batch-04.md#commit-193), [#194](batch-04.md#commit-194), [#195](batch-04.md#commit-195), [#196](batch-04.md#commit-196), [#197](batch-04.md#commit-197), [#198](batch-04.md#commit-198), [#199](batch-04.md#commit-199).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/EvolveLevel.C`, `src/enzo/FDMCollapse.C`, `src/enzo/Grid.h`, `src/enzo/Grid_FDMCollapse.C`, `src/enzo/Grid_ParallelFDMCollapseInitialize.C`, `src/enzo/Grid_SchrodingerSolver.C`, `src/enzo/InitializeLocal.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.scinet-niagara`, `src/enzo/ParallelFDMCollapseInitialize.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.
