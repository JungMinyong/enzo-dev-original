# Batch 05: commits 201–250

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-201"></a>
## 201 — `e124b6ad3` — 2022-04-17

Create sse2neon.h

**Categories:** 4.

Vendors SSE2NEON at the wrong initial location. Superseded by #202/#203. Filewise review of scope/header use, not an independent audit of 8801 lines of third-party SIMD intrinsics.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/sse2neon.h`.

**Patch locations:** `@@ -0,0 +1,8801 @@`.

<a id="commit-202"></a>
## 202 — `432de5029` — 2022-04-17

Delete sse2neon.h

**Categories:** 4.

Removes the first SSE2NEON location; part of header relocation, not deletion of a required Aeos physics method.

**Incorporation:** reverse check succeeds (evidence of current patch content, not proof of identical intent). **Direct patch checks:** forward FAIL; reverse PASS. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/sse2neon.h`.

**Patch locations:** `@@ -1,8801 +0,0 @@`.

<a id="commit-203"></a>
## 203 — `c15b05f26` — 2022-04-17

Create sse2neon.h

**Categories:** 4.

Vendors SSE2NEON in src/enzo for ARM portability. Review covers integration and target guards, not mathematical certification of every third-party intrinsic; requires ARM build/source-clustering comparisons.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/sse2neon.h`.

**Patch locations:** `@@ -0,0 +1,8801 @@`.

<a id="commit-204"></a>
## 204 — `8c9913605` — 2022-04-17

add sse2neon.h

**Categories:** 4.

Selects SSE2NEON for aarch64 and xmmintrin otherwise in FindSuperSourceByPosition. Clean integration patch; use together with the header on ARM. Numerical source clustering should be compared across architectures.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/FindSuperSourceByPosition.C`.

**Files:** `src/enzo/FindSuperSourceByPosition.C`.

**Patch locations:** `@@ -1,7 +1,11 @@`.

<a id="commit-205"></a>
## 205 — `7bc03558e` — 2022-05-08

Merge branch 'enzo-project:main' into main

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#081](batch-02.md#commit-081), [#082](batch-02.md#commit-082), [#083](batch-02.md#commit-083), [#084](batch-02.md#commit-084), [#085](batch-02.md#commit-085), [#086](batch-02.md#commit-086), [#087](batch-02.md#commit-087), [#088](batch-02.md#commit-088), [#089](batch-02.md#commit-089), [#090](batch-02.md#commit-090), [#091](batch-02.md#commit-091), [#092](batch-02.md#commit-092), [#093](batch-02.md#commit-093), [#094](batch-02.md#commit-094), [#095](batch-02.md#commit-095), [#096](batch-02.md#commit-096), [#097](batch-02.md#commit-097), [#098](batch-02.md#commit-098), [#099](batch-02.md#commit-099), [#100](batch-02.md#commit-100), [#101](batch-03.md#commit-101), [#102](batch-03.md#commit-102), [#103](batch-03.md#commit-103), [#104](batch-03.md#commit-104), [#105](batch-03.md#commit-105), [#106](batch-03.md#commit-106), [#107](batch-03.md#commit-107), [#108](batch-03.md#commit-108), [#109](batch-03.md#commit-109), [#110](batch-03.md#commit-110), [#111](batch-03.md#commit-111), [#112](batch-03.md#commit-112), [#113](batch-03.md#commit-113), [#114](batch-03.md#commit-114).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/cosmic_rays.rst`, `src/enzo/CRShockTubesInitialize.C`, `src/enzo/CRTransportTestInitialize.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid.h`, `src/enzo/Grid_CRShockTubesInitializeGrid.C`, `src/enzo/Grid_CRTransportTestInitialize.C`, `src/enzo/Grid_ComovingExpansionTerms.C`, `src/enzo/Grid_ComputeAnisotropicCRDiffusion.C`, `src/enzo/Grid_ComputeCRDiffusionTimeStep.C`, `src/enzo/Grid_ComputeCRStreaming.C`, `src/enzo/Grid_ComputeCRStreamingTimeStep.C`, `src/enzo/Grid_ComputeTimeStep.C`, `src/enzo/Grid_CosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/expand_terms.F`, `src/enzo/global_data.h`, `src/enzo/hydro_rk/Grid_MHDRK2_1stStep.C`, `src/enzo/hydro_rk/Grid_MHDSourceTerms.C`, `src/enzo/hydro_rk/Grid_ReturnHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_ReturnOldHydroRKPointers.C`, `src/enzo/hydro_rk/Grid_UpdateMHDPrim.C`, `src/enzo/hydro_rk/LLF_PLM_MHD.C`, `src/enzo/hydro_rk/LLF_Zero_MHD.C`, `src/enzo/hydro_rk/MHD3DTestInitialize.C`, `src/enzo/hydro_rk/MHDSweepX.C`, `src/enzo/hydro_rk/MHDSweepY.C`, `src/enzo/hydro_rk/MHDSweepZ.C`, `src/enzo/hydro_rk/Riemann_LLF_MHD.C`, `src/enzo/star_maker2.F`.

<a id="commit-206"></a>
## 206 — `f7731d18e` — 2022-07-10

Merge branch 'fix-test-suite' into emfisk/main

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`.

<a id="commit-207"></a>
## 207 — `3df203965` — 2022-07-13

Merge branch 'fix-test-suite' into emfisk/main

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

<a id="commit-208"></a>
## 208 — `52e7a546b` — 2022-07-14

Merge remote-tracking branch 'upstream/main' into emfisk/main

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`.

<a id="commit-209"></a>
## 209 — `e9a1bb8ff` — 2022-08-10

Merge pull request #188 from emfisk/main

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#201](batch-05.md#commit-201), [#202](batch-05.md#commit-202), [#203](batch-05.md#commit-203), [#204](batch-05.md#commit-204), [#205](batch-05.md#commit-205), [#206](batch-05.md#commit-206), [#207](batch-05.md#commit-207), [#208](batch-05.md#commit-208).

**Aeos-modified paths since common ancestor:** `src/enzo/FindSuperSourceByPosition.C`.

**Files:** `src/enzo/FindSuperSourceByPosition.C`, `src/enzo/sse2neon.h`.

<a id="commit-210"></a>
## 210 — `0eb04854c` — 2022-05-24

Copied relevant files from clairekope/enzo-isogal

**Categories:** 2,4.

Broad isolated-galaxy/CGM feature import replacing initializer, external potentials, equilibrium chemistry and star-formation controls, with accidental unrelated copies later reverted. Conflicts with Aeos disk setup, element tracers and feedback. Do not adopt wholesale; assess final PR #191 by subsystem.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveHierarchy.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleData.h`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/typedefs.h`.

**Files:** `.gitignore`, `input/gen_equilibrium_table.py`, `src/enzo/EquilibriumTable.h`, `src/enzo/EvolveHierarchy.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_ComputeTemperatureField.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_GrackleCustomCoolRate.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/InitializeCloudyCooling.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadEquilibriumTable.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/RotatingDiskInitialize.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/SetStellarFeedbackEfficiency.C`, `src/enzo/StarParticleData.h`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/libconfig/libconfig.c`, `src/enzo/star_maker2.F`, `src/enzo/typedefs.h`.

**Patch locations:** `@@ -10,6 +10,8 @@ syntax: glob`; `@@ -53,6 +55,5 @@ src/enzo/Make.mach.mymac`; `@@ -0,0 +1,88 @@`; `@@ -0,0 +1,29 @@`; `@@ -67,9 +67,16 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; additional hunks in the same patch.

<a id="commit-211"></a>
## 211 — `643f2b65d` — 2022-05-24

Performing an actual merge

**Categories:** 2,4.

Reverts accidental foreign branch/file replacements from #210 while retaining selected galaxy features. It is an ordinary commit despite its merge subject; do not assume it only records ancestry.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveHierarchy.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleData.h`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/typedefs.h`.

**Files:** `.gitignore`, `src/enzo/EvolveHierarchy.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/InitializeCloudyCooling.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/RotatingDiskInitialize.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleData.h`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/libconfig/libconfig.c`, `src/enzo/star_maker2.F`, `src/enzo/typedefs.h`.

**Patch locations:** `@@ -10,8 +10,6 @@ syntax: glob`; `@@ -55,5 +53,6 @@ src/enzo/Make.mach.mymac`; `@@ -67,16 +67,9 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`; `@@ -135,6 +128,7 @@ int MagneticFieldResetter(LevelHierarchyEntry *LevelArray[], int ThisLevel,`; `@@ -278,21 +272,26 @@ int EvolveHierarchy(HierarchyEntry &TopGrid, TopGridData &MetaData,`; additional hunks in the same patch.

<a id="commit-212"></a>
## 212 — `923701580` — 2022-05-24

It compiles!

**Categories:** 2,4.

Reworks galaxy-grid fields, disk/halo ICs and initializer interfaces; removes imported magnetic setup and adjusts stellar code. Would replace Aeos-specific initialization. Keep existing Aeos disk/tracer/chemistry contracts unless deliberately adding a separate initializer mode.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/macros_and_parameters.h`, `src/enzo/star_maker6.F`.

**Patch locations:** `@@ -37,8 +37,6 @@`; `@@ -142,8 +140,6 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -191,8 +187,8 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -237,8 +233,8 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -281,12 +277,6 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; additional hunks in the same patch.

<a id="commit-213"></a>
## 213 — `740108357` — 2022-05-25

Just remove new redundant Jeans Mass param entirely

**Categories:** 4.

Removes redundant StarMakerUseJeansCrit alias added by the feature branch. No need to create and remove this transient interface in Aeos.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`.

**Files:** `src/enzo/ReadParameterFile.C`.

**Patch locations:** `@@ -979,8 +979,6 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`.

<a id="commit-214"></a>
## 214 — `e9d7589c4` — 2022-07-01

Merged Hopkins+13 changes in star_maker2; SF docs

**Categories:** 2,4.

Adds molecular-H2 and self-gravity star_maker2 criteria and feedback-efficiency ramp controls, with new Fortran/C++ arguments and parameter defaults. New science/selection rules, not a drop-in correctness fix; Aeos uses custom individual-star creation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/macros_and_parameters.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/macros_and_parameters.h`, `src/enzo/star_maker2.F`.

**Patch locations:** `@@ -2058,7 +2058,7 @@ General Star Formation`; `@@ -2103,9 +2103,33 @@ General Star Formation`; `@@ -2154,7 +2178,8 @@ The parameters below are considered in StarParticleCreation method`; `@@ -2176,14 +2201,23 @@ The parameters below are considered in StarParticleCreation method`; `@@ -26,7 +26,7 @@ parameter link above for more information.`; additional hunks in the same patch.

<a id="commit-215"></a>
## 215 — `0e2472c15` — 2022-07-05

Docs & cleanup on GalSim changes

**Categories:** 2,4.

Documents and cleans the new disk/CGM and star-formation choices. Contains initializer edits as well as documentation; preserve Aeos-specific modes/parameters and do not replace the galaxy setup wholesale.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -1306,7 +1306,11 @@ added to the acceleration field for the baryons and particles.`; `@@ -4694,7 +4698,7 @@ Test Orbit (29)`; `@@ -4847,8 +4851,13 @@ Cosmology Simulation (30)`; `@@ -4862,41 +4871,159 @@ Isolated Galaxy Evolution (31)`; `@@ -4941,6 +5068,7 @@ Isolated Galaxy Evolution (31)`; additional hunks in the same patch.

<a id="commit-216"></a>
## 216 — `efb1631e3` — 2022-07-05

Removed extraneous files

**Categories:** 4.

Removes imported extraneous star_maker6 and restores generic GNU machine settings. Cleanup of #210 side effects, not an instruction to remove locally maintained stellar algorithms.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.linux-gnu`.

**Files:** `src/enzo/Make.mach.linux-gnu`, `src/enzo/star_maker6.F`.

**Patch locations:** `@@ -2,18 +2,33 @@`; `@@ -21,9 +36,9 @@ MACH_FILE  = Make.mach.linux-gnu`; `@@ -33,11 +48,11 @@ MACH_CPP       = cpp # C preprocessor command`; `@@ -63,7 +78,7 @@ MACH_CFLAGS   =`; `@@ -79,7 +94,7 @@ MACH_OPT_AGGRESSIVE  = -O3 -g`; additional hunks in the same patch.

<a id="commit-217"></a>
## 217 — `00edcc9bb` — 2022-07-05

Docs for efficiency ramp

**Categories:** 4.

Documents new time-dependent stellar minimum-mass and thermal-efficiency ramps. Useful only if those optional controls are adopted.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`.

**Patch locations:** `@@ -2253,11 +2253,11 @@ The parameters below are considered in StarParticleCreation method`; `@@ -2265,17 +2265,41 @@ The parameters below are considered in StarParticleCreation method`.

<a id="commit-218"></a>
## 218 — `3ed875b38` — 2022-07-05

warning in docs re: overriding mu

**Categories:** 4.

Documents the equilibrium-table molecular-weight override in ComputeTemperatureField. This caveat signals coupling between IC chemistry and reported temperature; not a validation of the new halo method for Aeos.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`.

**Patch locations:** `@@ -5011,7 +5011,7 @@ Isolated Galaxy Evolution (31)`; `@@ -5034,7 +5034,10 @@ Isolated Galaxy Evolution (31)`.

<a id="commit-219"></a>
## 219 — `c85a68fe9` — 2022-07-12

Remove manual def of constants

**Categories:** 4.

Removes local physical constant definitions from the rewritten galaxy initializer; incomplete until #220 restores required coefficients. Do not port alone.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -28,18 +28,6 @@`.

<a id="commit-220"></a>
## 220 — `3f01953bf` — 2022-07-12

Some of those definitions were still needed

**Categories:** 4.

Uses shared Mpc_cm/kboltz/mh and restores nonstandard coefficients needed by disk/halo profiles. Conditional cleanup; changes rounded constants and must accompany the new initializer.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -20,6 +20,7 @@`; `@@ -28,6 +29,12 @@`; `@@ -464,7 +471,7 @@ int grid::GalaxySimulationInitializeGrid(FLOAT DiskRadius,`; `@@ -501,14 +508,14 @@ int grid::GalaxySimulationInitializeGrid(FLOAT DiskRadius,`; `@@ -556,7 +563,7 @@ int grid::GalaxySimulationInitializeGrid(FLOAT DiskRadius,`; additional hunks in the same patch.

<a id="commit-221"></a>
## 221 — `73d145ce3` — 2022-07-15

Fixes to docs & python script

**Categories:** 4.

Revises equilibrium-table generator and feature documentation/initializer parameter handling. Use later corrected generator #439/#441 if adding this optional chemistry-IC workflow.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`.

**Files:** `doc/manual/source/parameters/index.rst`, `input/gen_equilibrium_table.py`, `src/enzo/GalaxySimulationInitialize.C`.

**Patch locations:** `@@ -2205,14 +2205,10 @@ The parameters below are considered in StarParticleCreation method`; `@@ -2262,20 +2258,25 @@ The parameters below are considered in StarParticleCreation method`; `@@ -2286,20 +2287,25 @@ The parameters below are considered in StarParticleCreation method`; `@@ -4957,7 +4963,7 @@ Isolated Galaxy Evolution (31)`; `@@ -5041,7 +5047,8 @@ Isolated Galaxy Evolution (31)`; additional hunks in the same patch.

<a id="commit-222"></a>
## 222 — `1df18184b` — 2022-07-15

Use doubles except for positions & grackle

**Categories:** 2,4.

Promotes galaxy/halo/gravity quantities to double while retaining FLOAT positions and Grackle-facing types. Helpful precision work but changes many Aeos initializer signatures and numerical values; selectively port only with agreement among declarations, readers and callers.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_ComputeTemperatureField.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -91,7 +91,7 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -100,21 +100,23 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -129,9 +131,9 @@ int GalaxySimulationInitialize(FILE *fptr, FILE *Outfptr,`; `@@ -621,17 +621,17 @@ gradient force to gravitational force for one-zone collapse test. */`; `@@ -2320,42 +2320,42 @@ int zEulerSweep(int j, int NumberOfSubgrids, fluxes *SubgridFluxes[],`; additional hunks in the same patch.

<a id="commit-223"></a>
## 223 — `8dddf0f47` — 2022-07-15

Merge branch 'enzo-project:main' into isogal-CGM-sim

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#046](batch-01.md#commit-046), [#115](batch-03.md#commit-115), [#116](batch-03.md#commit-116), [#117](batch-03.md#commit-117), [#118](batch-03.md#commit-118), [#119](batch-03.md#commit-119), [#120](batch-03.md#commit-120), [#121](batch-03.md#commit-121), [#122](batch-03.md#commit-122), [#123](batch-03.md#commit-123), [#124](batch-03.md#commit-124), [#125](batch-03.md#commit-125), [#126](batch-03.md#commit-126), [#127](batch-03.md#commit-127), [#128](batch-03.md#commit-128), [#129](batch-03.md#commit-129), [#130](batch-03.md#commit-130), [#131](batch-03.md#commit-131), [#132](batch-03.md#commit-132), [#133](batch-03.md#commit-133), [#134](batch-03.md#commit-134), [#135](batch-03.md#commit-135), [#136](batch-03.md#commit-136), [#137](batch-03.md#commit-137), [#138](batch-03.md#commit-138), [#139](batch-03.md#commit-139), [#140](batch-03.md#commit-140), [#141](batch-03.md#commit-141), [#142](batch-03.md#commit-142), [#143](batch-03.md#commit-143), [#144](batch-03.md#commit-144), [#145](batch-03.md#commit-145), [#146](batch-03.md#commit-146), [#147](batch-03.md#commit-147), [#148](batch-03.md#commit-148), [#149](batch-03.md#commit-149), [#150](batch-03.md#commit-150), [#151](batch-04.md#commit-151), [#152](batch-04.md#commit-152), [#153](batch-04.md#commit-153), [#154](batch-04.md#commit-154), [#155](batch-04.md#commit-155), [#156](batch-04.md#commit-156), [#157](batch-04.md#commit-157), [#158](batch-04.md#commit-158), [#159](batch-04.md#commit-159), [#160](batch-04.md#commit-160).

**Aeos-modified paths since common ancestor:** `src/enzo/EnzoTiming.h`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/StarParticleFindAll.C`.

**Files:** `.circleci/config.yml`, `run/Cooling/CoolingTest_Cloudy/CoolingTest_Cloudy__test_cooling.py`, `run/Cooling/CoolingTest_Grackle/CoolingTest_Grackle__test_cooling.py`, `run/Cooling/CoolingTest_JHW/CoolingTest_JHW__test_cooling.py`, `run/Cooling/OneZoneFreefallTest/OneZoneFreefallTest__test_freefall.py`, `run/Cosmology/AMRZeldovichPancake/AMRZeldovichPancake__test_almost_standard.py`, `run/Cosmology/MHDZeldovichPancake/MHDZeldovichPancake.enzo`, `run/Cosmology/ZeldovichPancake/ZeldovichPancake__test_almost_standard.py`, `run/CosmologySimulation/amr_cosmology/test_amr_cosmology.py`, `run/CosmologySimulation/amr_nested_cosmology/test_amr_nested_cosmology.py`, `run/CosmologySimulation/dm_only/test_dm_only.py`, `run/GravitySolver/GravityTest/GravityTest__test_gravity.py`, `run/GravitySolver/TestOrbit/TestOrbit__test_orbit.py`, `run/Hydro/Hydro-1D/FreeExpansion/FreeExpansion__test_free_expansion.py`, `run/Hydro/Hydro-1D/ShockInABox/ShockInABox__test_shockinabox.py`, `run/Hydro/Hydro-1D/SodShockTube/SodShockTube__test_sod.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTube/Toro-1-ShockTube__test_toro1.py`, `run/Hydro/Hydro-1D/Toro-1-ShockTubeAMR/Toro-1-ShockTubeAMR__test_toro1_amr.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTube/Toro-2-ShockTube__test_toro2.py`, `run/Hydro/Hydro-1D/Toro-2-ShockTubeAMR/Toro-2-ShockTubeAMR__test_toro2_amr.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTube/Toro-3-ShockTube__test_toro3.py`, `run/Hydro/Hydro-1D/Toro-3-ShockTubeAMR/Toro-3-ShockTubeAMR__test_toro3_amr.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTube/Toro-4-ShockTube__test_toro4.py`, `run/Hydro/Hydro-1D/Toro-4-ShockTubeAMR/Toro-4-ShockTubeAMR__test_toro4_amr.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTube/Toro-5-ShockTube__test_toro5.py`, `run/Hydro/Hydro-1D/Toro-5-ShockTubeAMR/Toro-5-ShockTubeAMR__test_toro5_amr.py`, `run/Hydro/Hydro-1D/Toro-6-ShockTube/Toro-6-ShockTube__test_toro6.py`, `run/Hydro/Hydro-1D/Toro-7-ShockTube/Toro-7-ShockTube__test_toro7.py`, `run/Hydro/Hydro-2D/FreeExpansionAMR/FreeExpansionAMR__test_free_expansion.py`, `run/Hydro/Hydro-2D/NohProblem2D/NohProblem2D__test_noh2d.py`, `run/Hydro/Hydro-2D/NohProblem2DAMR/NohProblem2DAMR__test_noh2damr.py`, `run/Hydro/Hydro-3D/NohProblem3D/NohProblem3D__test_noh3d.py`, `run/Hydro/Hydro-3D/NohProblem3DAMR/NohProblem3DAMR__test_noh3damr.py`, `run/Hydro/Hydro-3D/RotatingCylinder/RotatingCylinder__test_rotating_cylinder.py`, `run/Hydro/Hydro-3D/RotatingSphere/profile_script.py`, `run/MHD/1D/BrioWu-MHD-1D/BrioWu-MHD-1D__test_briowu.py`, `run/MHD/1D/MHD_Metal_Advection_CT/MHD_Metal_Advection_CT__test_metal.py`, `run/MHD/1D/MHD_Metal_Advection_Dedner/MHD_Metal_Advection_Dedner__test_metal.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_almost_standard.py`, `run/MHD/2D/MHD2DRotorTest/MHD2DRotorTest__test_rotor.py`, `run/MHD/2D/MHDCTOrszagTang/MHDCTOrszagTang__test_DivB_CT.py`, `run/MHD/2D/MHDCTOrszagTangAMR/MHDCTOrszagTangAMR__test_DivB_CT.py`, `run/MHD/2D/SedovBlast-MHD-2D-Fryxell/SedovBlast-MHD-2D-Fryxell__test_fryxell.py`, `run/MHD/2D/SedovBlast-MHD-2D-Gardiner/SedovBlast-MHD-2D-Gardiner__test_gardiner.py`, `run/RadiationTransport/PhotonShadowing/PhotonShadowing__test_photonshadowing.py`, `run/RadiationTransport/PhotonTest/PhotonTest__test_photontest.py`, `run/RadiationTransport/PhotonTestAMR/PhotonTestAMR__test_amrphotontest.py`, `run/test_runner.py`, `run/test_type.py.template`, `src/enzo/EnzoTiming.h`, `src/enzo/Make.mach.nasa-aitken-rome`, `src/enzo/Make.mach.nasa-pleiades`, `src/enzo/StarParticleFindAll.C`.

<a id="commit-224"></a>
## 224 — `d578b443d` — 2022-07-15

CircleCI caught a compiler problem

**Categories:** 3.

Adds missing WriteListOfFloats(double*) declaration needed after #222. Conditional compilation repair for that precision conversion.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GalaxySimulationInitialize.C`.

**Files:** `src/enzo/GalaxySimulationInitialize.C`.

**Patch locations:** `@@ -38,6 +38,7 @@`.

<a id="commit-225"></a>
## 225 — `43c6a1930` — 2022-07-15

Add compiler check for Grackle

**Categories:** 3.

Fails explicitly if GasHalo=6 requires Grackle in a build without it. Required configuration guard if porting that new initializer; not a current Aeos GasHalo contract.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Files:** `src/enzo/Grid_GalaxySimulationInitializeGrid.C`.

**Patch locations:** `@@ -1585,6 +1585,7 @@ double halo_S_of_r(FLOAT r){`; `@@ -1636,7 +1637,11 @@ double halo_S_of_r(FLOAT r, grid* Grid){`.

<a id="commit-226"></a>
## 226 — `7147f5b13` — 2022-07-18

Explicitly set H2INum when MultiSpecies=0

**Categories:** 3,2.

Supplies valid H2 array indices when chemistry is disabled and narrows IdentifySpeciesFields gating. Apply the safety principle selectively: Aeos has custom H2/individual-star conditions, and aliasing density is valid only when the molecular criterion is disabled. Never silently interpret total density as molecular density.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_StarParticleHandler.C`.

**Files:** `src/enzo/Grid_StarParticleHandler.C`.

**Patch locations:** `@@ -547,7 +547,7 @@ int grid::StarParticleHandler(HierarchyEntry* SubgridPointer, int level,`; `@@ -602,6 +602,10 @@ int grid::StarParticleHandler(HierarchyEntry* SubgridPointer, int level,`.

<a id="commit-227"></a>
## 227 — `4447dc182` — 2022-08-18

Add check for therm eff ramp that all params defined

**Categories:** 3.

Rejects an enabled thermal-efficiency ramp with undefined endpoints. Necessary validation if adopting ramp parameters; also test equal/reversed times before enabling.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`.

**Files:** `src/enzo/ReadParameterFile.C`.

**Patch locations:** `@@ -2142,7 +2142,16 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`.

<a id="commit-228"></a>
## 228 — `06145ef80` — 2022-08-18

Comment updates & float correction

**Categories:** 4.

Executable change is only the literal 1e12 to 1.0e12 (same double value); remaining edits clarify comments in gravity and custom Grackle rates. Not a substantive float/science repair despite the subject.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/SetDefaultGlobalValues.C`.

**Files:** `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GrackleCustomCoolRate.C`, `src/enzo/SetDefaultGlobalValues.C`.

**Patch locations:** `@@ -429,9 +429,8 @@ int grid::ComputeAccelerationFieldExternal()`; `@@ -439,8 +438,8 @@ int grid::ComputeAccelerationFieldExternal()`; `@@ -105,12 +105,14 @@ int grid::GrackleCustomCoolRate(int rank, int *dim, float *cool_rate,`; `@@ -393,7 +393,7 @@ int SetDefaultGlobalValues(TopGridData &MetaData)`.

<a id="commit-229"></a>
## 229 — `671728759` — 2022-08-18

Merge pull request #191 from clairekope/isogal-CGM-sim

**Categories:** 2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#210](batch-05.md#commit-210), [#211](batch-05.md#commit-211), [#212](batch-05.md#commit-212), [#213](batch-05.md#commit-213), [#214](batch-05.md#commit-214), [#215](batch-05.md#commit-215), [#216](batch-05.md#commit-216), [#217](batch-05.md#commit-217), [#218](batch-05.md#commit-218), [#219](batch-05.md#commit-219), [#220](batch-05.md#commit-220), [#221](batch-05.md#commit-221), [#222](batch-05.md#commit-222), [#223](batch-05.md#commit-223), [#224](batch-05.md#commit-224), [#225](batch-05.md#commit-225), [#226](batch-05.md#commit-226), [#227](batch-05.md#commit-227), [#228](batch-05.md#commit-228).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/StarParticleData.h`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/typedefs.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `input/gen_equilibrium_table.py`, `src/enzo/EquilibriumTable.h`, `src/enzo/EvolveHierarchy.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_ComputeTemperatureField.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_GrackleCustomCoolRate.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Make.config.objects`, `src/enzo/ReadEquilibriumTable.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/SetStellarFeedbackEfficiency.C`, `src/enzo/StarParticleData.h`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/star_maker2.F`, `src/enzo/typedefs.h`.

<a id="commit-230"></a>
## 230 — `df16c63f6` — 2022-08-22

Subtract previous B-field contribution

**Categories:** 3.

MagneticFieldResetter subtracts the old magnetic specific energy before adding the replacement field energy; previously non-dual-energy resets did not adjust total energy, and clearing a field in low-density cells left old magnetic energy behind. Clean patch applies. Validate gas thermal energy preservation in both energy formalisms.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_MagneticFieldResetter.C`.

**Patch locations:** `@@ -94,27 +94,23 @@ int grid::MagneticFieldResetter(int level)`.

<a id="commit-231"></a>
## 231 — `b004866c0` — 2022-08-25

Merge pull request #197 from nirmitsakre/patch-1

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#230](batch-05.md#commit-230).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Grid_MagneticFieldResetter.C`.

<a id="commit-232"></a>
## 232 — `a1eba01ca` — 2022-09-06

Update README.md

**Categories:** 1.

Contributor list update only; clean documentation patch.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `README.md`.

**Patch locations:** `@@ -66,6 +66,7 @@ list of the people who have recently contributed, in alphabetical order:`; `@@ -85,7 +86,7 @@ list of the people who have recently contributed, in alphabetical order:`.

<a id="commit-233"></a>
## 233 — `39630d92b` — 2022-10-12

Add config option for libyt

**Categories:** 4.

Adds default-off libyt build option; optional in-situ analysis infrastructure. Integrate complete final option handling, including later syntax fixes, rather than early snapshots.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Files:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Patch locations:** `@@ -418,6 +418,35 @@`; `@@ -24,6 +24,7 @@`; `@@ -169,6 +170,15 @@`; `@@ -268,6 +268,7 @@ show-config:`; `@@ -640,6 +641,23 @@ CONFIG_PYTHON-%: suggest-clean`.

<a id="commit-234"></a>
## 234 — `bff2b98d7` — 2022-10-12

Add conda-based makefile

**Categories:** 4.

Adds conda machine file with example dependency paths; site-specific and later superseded by CMake.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.conda`.

**Patch locations:** `@@ -0,0 +1,106 @@`.

<a id="commit-235"></a>
## 235 — `10732ce76` — 2022-10-23

Add initial libyt hooks

**Categories:** 4.

Adds libyt macros, startup and linker hooks; touches common startup/config interfaces but is an optional analysis feature requiring final guards.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/Make.config.assemble`, `src/enzo/Make.mach.conda`, `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Patch locations:** `@@ -1068,6 +1068,7 @@`; `@@ -1100,6 +1101,7 @@`; `@@ -1119,6 +1121,7 @@`; `@@ -77,7 +77,7 @@ MACH_OPT_AGGRESSIVE  = -O3 -g`; `@@ -93,14 +93,17 @@ MACH_INCLUDES_GRACKLE = $(LOCAL_INCLUDES_GRACKLE)`; additional hunks in the same patch.

<a id="commit-236"></a>
## 236 — `214e6e1d2` — 2022-10-24

Start filling out the libyt functions

**Categories:** 4.

Initial libyt unit/metadata export and finalize hook. Incomplete feature development; prefer final libyt interface rather than this scaffold.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.objects`, `src/enzo/enzo.C`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Make.config.objects`, `src/enzo/enzo.C`.

**Patch locations:** `@@ -0,0 +1,156 @@`; `@@ -68,6 +68,7 @@ OBJS_CONFIG_LIB = \`; `@@ -910,6 +910,10 @@ void my_exit(int status)`.

<a id="commit-237"></a>
## 237 — `cdfbc38d1` — 2023-04-17

Add empty interactive mode

**Categories:** 4.

Adds interactive-mode stub and startup call; optional feature, later removed/refactored. Do not require interactive libyt for ordinary builds.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.objects`, `src/enzo/enzo.C`.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.conda`, `src/enzo/enzo.C`.

**Patch locations:** `@@ -0,0 +1,50 @@`; `@@ -69,6 +69,7 @@ OBJS_CONFIG_LIB = \`; `@@ -99,7 +99,7 @@ LOCAL_LIBS_PAPI   = # PAPI libraries`; `@@ -790,7 +790,10 @@ Eint32 MAIN_NAME(Eint32 argc, char *argv[])`.

<a id="commit-238"></a>
## 238 — `dd592d828` — 2023-04-18

Add call to stub

**Categories:** 4.

Adds EvolveLevel interactive-analysis call. This adds an execution hook and overhead; later moved to the synchronized hierarchy in #541.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/EvolveLevel.C`.

**Patch locations:** `@@ -257,6 +257,8 @@ void my_exit(int status);`; `@@ -843,6 +845,12 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`.

<a id="commit-239"></a>
## 239 — `50805651f` — 2023-04-18

first bit of mapping for libyt

**Categories:** 4.

Adds generated-parameter mapping script based on CppHeaderParser. Optional development tool; regenerate for custom Aeos variables rather than using a stale upstream map.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/create_libyt_mapping.py`.

**Patch locations:** `@@ -0,0 +1,27 @@`.

<a id="commit-240"></a>
## 240 — `211e448ae` — 2023-04-19

Add mapping system for libyt parameters

**Categories:** 4,2.

Adds generated global-parameter exporters and startup mapping. Aeos adds many globals and changes interfaces; generated declarations/types require regeneration and review before enabling libyt.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.objects`, `src/enzo/enzo.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/Make.config.objects`, `src/enzo/create_libyt_mapping.py`, `src/enzo/enzo.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -0,0 +1,136 @@`; `@@ -0,0 +1,592 @@`; `@@ -713,6 +713,7 @@ OBJS_CONFIG_LIB = \`; `@@ -4,7 +4,18 @@`; `@@ -15,13 +26,58 @@ def preprocess_header_file(fn = "global_data.h"):`; additional hunks in the same patch.

<a id="commit-241"></a>
## 241 — `a1e5b7e96` — 2023-04-19

Continue mapping

**Categories:** 4.

Updates libyt parameter API names, current redshift and generated scalar mappings. Prerequisite-specific development; final mappings must match Aeos FLOAT/integer types.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/create_libyt_mapping.py`.

**Patch locations:** `@@ -41,7 +41,7 @@ int InitializeLibytInterface(int argc, char *argv[])`; `@@ -83,7 +83,7 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`; `@@ -95,13 +95,13 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`; `@@ -115,19 +115,19 @@ void ExportParameterFileToLibyt(TopGridData *MetaData, FLOAT CurrentTime, FLOAT`; `@@ -1,57 +1,55 @@`; additional hunks in the same patch.

<a id="commit-242"></a>
## 242 — `7d9d12fd2` — 2023-04-19

Update libyt initialize/finalize/interactive API.

**Categories:** 4.

Updates libyt initialize/finalize/interactive APIs and introduces developer-specific machine paths. Port API integration only, not personal filesystem settings.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`, `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/Make.mach.libyt`, `src/enzo/enzo.C`, `src/enzo/macros_and_parameters.h`.

**Patch locations:** `@@ -25,8 +25,8 @@`; `@@ -0,0 +1,116 @@`; `@@ -797,7 +797,8 @@ Eint32 MAIN_NAME(Eint32 argc, char *argv[])`; `@@ -26,7 +26,7 @@`.

<a id="commit-243"></a>
## 243 — `43e0bf787` — 2023-04-19

Fix order of includes

**Categories:** 4.

Reorders includes and adds analysis-call counter parameter I/O. Requires the optional libyt feature and later USE_LIBYT guards.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Patch locations:** `@@ -12,6 +12,11 @@`; `@@ -24,11 +29,6 @@`; `@@ -13,6 +13,8 @@`; `@@ -25,7 +27,6 @@`; `@@ -1183,6 +1183,12 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`; additional hunks in the same patch.

<a id="commit-244"></a>
## 244 — `8e22e992d` — 2023-04-19

Add initialize call to the interactive mode

**Categories:** 4.

Adds an interactive stop point during initialization; optional interactive behavior, not necessary for evolution correctness.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface.C`.

**Patch locations:** `@@ -14,6 +14,7 @@`; `@@ -53,6 +54,11 @@ int InitializeLibytInterface(int argc, char *argv[])`.

<a id="commit-245"></a>
## 245 — `92e238389` — 2023-04-19

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Remerge-diff removes duplicated libyt includes after include-order changes. Conditional optional-feature build integration.

**Merge inspection:** combined diff 0 bytes; remerge diff 659 bytes. Positive results are discussed above.

**Constituents in inventory:** [#243](batch-05.md#commit-243), [#244](batch-05.md#commit-244).

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/WriteParameterFile.C`.

<a id="commit-246"></a>
## 246 — `01da39b60` — 2023-04-19

Only include libyt in the one file.

**Categories:** 4.

Concentrates libyt initialization in its interface translation unit and changes global opaque-pointer handling. Use the final interface design.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Patch locations:** `@@ -41,10 +41,13 @@ void ExposeGridHierarchy(int NumberOfGrids);`; `@@ -65,6 +68,7 @@ int FinalizeLibytInterface()`; `@@ -793,11 +793,7 @@ Eint32 MAIN_NAME(Eint32 argc, char *argv[])`; `@@ -949,4 +945,3 @@ void my_exit(int status)`; `@@ -963,7 +963,7 @@ EXTERN PyObject *my_processor;`; additional hunks in the same patch.

<a id="commit-247"></a>
## 247 — `3fe941aa3` — 2023-04-19

Merge remote-tracking branch 'data-exp-lab/libyt' into libyt

**Categories:** 4.

Remerge-diff selects InitializeLibytInterface instead of duplicate inline malloc/startup and removes globally exposed libyt include. Conditional startup integration.

**Merge inspection:** combined diff 0 bytes; remerge diff 1633 bytes. Positive results are discussed above.

**Constituents in inventory:** [#246](batch-05.md#commit-246).

**Aeos-modified paths since common ancestor:** `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/InitializeLibytInterface.C`, `src/enzo/enzo.C`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

<a id="commit-248"></a>
## 248 — `a52319dd1` — 2023-04-19

Align with include header in matt's repo

**Categories:** 4.

Temporary libyt include-path convention in developer machine file; superseded by public header installation changes.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/Make.mach.libyt`.

**Patch locations:** `@@ -86,7 +86,7 @@ LOCAL_INCLUDES_HDF5   = -I$(LOCAL_HDF5_INSTALL)/include`.

<a id="commit-249"></a>
## 249 — `79971cbdd` — 2023-04-19

Change include to libyt.h

**Categories:** 4.

Normalizes libyt header and installation include path; prerequisite-specific portability cleanup.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallEmptyInteractivePython.C`, `src/enzo/CallInSitulibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/Make.mach.libyt`.

**Patch locations:** `@@ -13,8 +13,8 @@`; `@@ -12,6 +12,7 @@`; `@@ -13,8 +13,8 @@`; `@@ -86,7 +86,7 @@ LOCAL_INCLUDES_HDF5   = -I$(LOCAL_HDF5_INSTALL)/include`.

<a id="commit-250"></a>
## 250 — `e8b235982` — 2023-04-20

More libyt updates

**Categories:** 4.

Updates libyt parameter-pointer handling, API spelling and generated mappings. Conditional on feature adoption; must retain correct lifetime/typed mapping.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/create_libyt_mapping.py`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -12,6 +12,11 @@`; `@@ -44,7 +49,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -100,15 +105,15 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -121,33 +126,33 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -43,6 +43,7 @@ int InitializeLibytInterface(int argc, char *argv[])`; additional hunks in the same patch.
