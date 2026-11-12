# Batch 11: commits 501–550

Static review against aeos-v2 `0dbaa4bea`; upstream endpoint `7409c9a3e`. See [method and limits](README.md). Commit numbering follows frozen reverse topological order, not calendar order.

<a id="commit-501"></a>
## 501 — `4a8882ac3` — 2025-05-07

Bump version.

**Categories:** 4.

Bumps documented libyt dependency versions again. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -18,7 +18,7 @@ We can compile libyt using different options based on our used cases, so tha`; `@@ -36,9 +36,9 @@ Please follow the instructions in libyt documents:`.

<a id="commit-502"></a>
## 502 — `7d3f08c6e` — 2025-06-11

Make Enzo dim 3/2/1 work.

**Categories:** 3.

Sets inactive domain dimensions to one and limits ghost-cell metadata to actual dimensionality. Required 1D/2D libyt support.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -173,6 +173,10 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -312,7 +316,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -338,7 +342,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -347,7 +351,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-503"></a>
## 503 — `aaae14737` — 2025-06-11

Update docs.

**Categories:** 4.

Documents supported field/particle dimensionality and updated installation links. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -16,9 +16,9 @@ Below are links to the build and runtime requirements, which must be installed.`; `@@ -36,9 +36,9 @@ Please follow the instructions in libyt documents:`; `@@ -77,6 +77,10 @@ How to Configure`.

<a id="commit-504"></a>
## 504 — `da37013eb` — 2023-06-30

Fix GalaxySimulation boundary to work correctly with DualEnergyFormalism

**Categories:** 3,4.

Adds explicit boundary-field lookups and updates both total/internal energies and species during imposed GalaxySimulation inflow. Existing positional field assumptions fail with DualEnergyFormalism. Clean patch applies, but it also hard-codes inflow metallicity to 0.1 solar and ionization fractions: these are new boundary physics. Moreover its kinetic-energy sum adds vx only for rank==1, omitting vx in 2D/3D. Adopt the field/dual-energy repair selectively, correct the component sum, and preserve Aeos inflow composition/custom tracers.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetGalaxySimulationBoundary.C`.

**Patch locations:** `@@ -60,6 +60,20 @@ int ExternalBoundary::SetGalaxySimulationBoundary(FLOAT time)`; `@@ -145,6 +159,16 @@ int ExternalBoundary::SetGalaxySimulationBoundary(FLOAT time)`; `@@ -153,6 +177,16 @@ int ExternalBoundary::SetGalaxySimulationBoundary(FLOAT time)`; `@@ -222,6 +256,16 @@ int ExternalBoundary::SetGalaxySimulationBoundary(FLOAT time)`; `@@ -254,7 +298,16 @@ int ExternalBoundary::SetGalaxySimulationBoundary(FLOAT time)`; additional hunks in the same patch.

<a id="commit-505"></a>
## 505 — `27e25c6a7` — 2023-08-16

Applying changes in response to review.

**Categories:** 3.

Removes local shadow of MultiSpecies and corrects boundary lookups/handling after #504. Adopt with #504 as the final pair; test MultiSpecies=0/1/2/3 and optional internal energy.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetGalaxySimulationBoundary.C`.

**Patch locations:** `@@ -72,7 +72,6 @@ int ExternalBoundary::SetGalaxySimulationBoundary(FLOAT time)`; `@@ -321,7 +320,7 @@ int ExternalBoundary::SetGalaxySimulationBoundary(FLOAT time)`.

<a id="commit-506"></a>
## 506 — `d0fce2ac4` — 2024-02-19

Merge pull request #216 from gregbryan/galaxy-boundary-fix

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#504](batch-11.md#commit-504), [#505](batch-11.md#commit-505).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/ExternalBoundary_SetGalaxySimulationBoundary.C`.

<a id="commit-507"></a>
## 507 — `0f32825ef` — 2024-02-13

New issue github templates

**Categories:** 1.

Adds GitHub bug/feature templates. Clean repository-interface patch; no simulation physics.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature-or-improvement-request.md`.

**Patch locations:** `@@ -0,0 +1,43 @@`; `@@ -0,0 +1,20 @@`.

<a id="commit-508"></a>
## 508 — `8941eada2` — 2024-02-13

Manually adding PR template

**Categories:** 1.

Adds GitHub PR template. Clean repository-interface patch; no simulation physics.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.github/pull_request_template.md`.

**Patch locations:** `@@ -0,0 +1,41 @@`.

<a id="commit-509"></a>
## 509 — `cb0ec07d2` — 2024-02-19

Addressing bwoshea's comments about attachments

**Categories:** 4.

Revises template attachment instructions. Requires preceding templates; no simulation physics.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature-or-improvement-request.md`, `.github/pull_request_template.md`.

**Patch locations:** `@@ -12,7 +12,7 @@ A clear and concise description of what the bug is.`; `@@ -30,14 +30,14 @@ output, etc.`; `@@ -17,4 +17,4 @@ A clear and concise description of what you want to happen.`; `@@ -19,9 +19,9 @@ If you are able to do so, please do not create the PR out of main, but out of a`.

<a id="commit-510"></a>
## 510 — `5d6581fa9` — 2024-02-19

Merge pull request #232 from enzo-project/github-templates-new

**Categories:** 1,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#507](batch-11.md#commit-507), [#508](batch-11.md#commit-508), [#509](batch-11.md#commit-509).

**Aeos-modified paths since common ancestor:** none.

**Files:** `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature-or-improvement-request.md`, `.github/pull_request_template.md`.

<a id="commit-511"></a>
## 511 — `b8a993db5` — 2024-03-01

Merge remote-tracking branch 'enzo-dev/main'

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#256](batch-06.md#commit-256), [#257](batch-06.md#commit-257), [#333](batch-07.md#commit-333), [#334](batch-07.md#commit-334), [#335](batch-07.md#commit-335), [#336](batch-07.md#commit-336), [#337](batch-07.md#commit-337), [#338](batch-07.md#commit-338), [#339](batch-07.md#commit-339), [#340](batch-07.md#commit-340), [#341](batch-07.md#commit-341), [#342](batch-07.md#commit-342), [#343](batch-07.md#commit-343), [#344](batch-07.md#commit-344), [#345](batch-07.md#commit-345), [#346](batch-07.md#commit-346), [#347](batch-07.md#commit-347), [#348](batch-07.md#commit-348), [#349](batch-07.md#commit-349), [#350](batch-07.md#commit-350), [#351](batch-08.md#commit-351), [#352](batch-08.md#commit-352), [#353](batch-08.md#commit-353), [#354](batch-08.md#commit-354), [#355](batch-08.md#commit-355), [#356](batch-08.md#commit-356), [#357](batch-08.md#commit-357), [#358](batch-08.md#commit-358), [#359](batch-08.md#commit-359), [#360](batch-08.md#commit-360), [#361](batch-08.md#commit-361), [#362](batch-08.md#commit-362), [#363](batch-08.md#commit-363), [#364](batch-08.md#commit-364), [#365](batch-08.md#commit-365), [#366](batch-08.md#commit-366), [#367](batch-08.md#commit-367), [#368](batch-08.md#commit-368), [#369](batch-08.md#commit-369), [#370](batch-08.md#commit-370), [#371](batch-08.md#commit-371), [#372](batch-08.md#commit-372), [#373](batch-08.md#commit-373), [#374](batch-08.md#commit-374), [#375](batch-08.md#commit-375), [#376](batch-08.md#commit-376), [#377](batch-08.md#commit-377), [#378](batch-08.md#commit-378), [#379](batch-08.md#commit-379), [#380](batch-08.md#commit-380), [#381](batch-08.md#commit-381), [#382](batch-08.md#commit-382), [#383](batch-08.md#commit-383), [#384](batch-08.md#commit-384), [#385](batch-08.md#commit-385), [#386](batch-08.md#commit-386), [#387](batch-08.md#commit-387), [#388](batch-08.md#commit-388), [#389](batch-08.md#commit-389), [#390](batch-08.md#commit-390), [#405](batch-09.md#commit-405), [#406](batch-09.md#commit-406), [#407](batch-09.md#commit-407), [#408](batch-09.md#commit-408), [#409](batch-09.md#commit-409), [#410](batch-09.md#commit-410), [#411](batch-09.md#commit-411), [#412](batch-09.md#commit-412), [#413](batch-09.md#commit-413), [#414](batch-09.md#commit-414), [#415](batch-09.md#commit-415), [#416](batch-09.md#commit-416), [#417](batch-09.md#commit-417), [#418](batch-09.md#commit-418), [#419](batch-09.md#commit-419), [#420](batch-09.md#commit-420), [#421](batch-09.md#commit-421), [#422](batch-09.md#commit-422), [#423](batch-09.md#commit-423), [#424](batch-09.md#commit-424), [#425](batch-09.md#commit-425), [#426](batch-09.md#commit-426), [#427](batch-09.md#commit-427), [#428](batch-09.md#commit-428), [#429](batch-09.md#commit-429), [#430](batch-09.md#commit-430), [#431](batch-09.md#commit-431), [#432](batch-09.md#commit-432), [#433](batch-09.md#commit-433), [#434](batch-09.md#commit-434), [#435](batch-09.md#commit-435), [#436](batch-09.md#commit-436), [#437](batch-09.md#commit-437), [#438](batch-09.md#commit-438), [#439](batch-09.md#commit-439), [#440](batch-09.md#commit-440), [#441](batch-09.md#commit-441), [#442](batch-09.md#commit-442), [#504](batch-11.md#commit-504), [#505](batch-11.md#commit-505), [#506](batch-11.md#commit-506), [#507](batch-11.md#commit-507), [#508](batch-11.md#commit-508), [#509](batch-11.md#commit-509), [#510](batch-11.md#commit-510).

**Aeos-modified paths since common ancestor:** `.gitignore`, `src/enzo/EvolveLevel.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/PhotonPackage.h`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `.circleci/config.yml`, `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature-or-improvement-request.md`, `.github/pull_request_template.md`, `.gitignore`, `.readthedocs.yaml`, `doc/manual/source/conf.py`, `doc/manual/source/parameters/index.rst`, `doc/manual/source/physics/star_particles.rst`, `input/gen_equilibrium_table.py`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzo`, `run/StarParticle/RadiatingStarParticleSingleTest/TestRadiatingStarParticleSingle.enzotest`, `src/enzo/CallProblemSpecificRoutines.C`, `src/enzo/EvolveLevel.C`, `src/enzo/EvolvePhotons.C`, `src/enzo/ExternalBoundary.h`, `src/enzo/ExternalBoundary_SetGalaxySimulationBoundary.C`, `src/enzo/GalaxySimulationInitialize.C`, `src/enzo/Grid.h`, `src/enzo/Grid_AddFeedbackSphere.C`, `src/enzo/Grid_CollapseTestInitializeGrid.C`, `src/enzo/Grid_ComputeAccelerationFieldExternal.C`, `src/enzo/Grid_FindNewStarParticles.C`, `src/enzo/Grid_GalaxySimulationInitializeGrid.C`, `src/enzo/Grid_Group_ReadGrid.C`, `src/enzo/Grid_NestedCosmologySimulationInitializeGrid.C`, `src/enzo/Grid_StarParticleHandler.C`, `src/enzo/Grid_TestRadiatingStarParticleInitializeGrid.C`, `src/enzo/Grid_TestStarParticleInitializeGrid.C`, `src/enzo/Group_ReadAllData.C`, `src/enzo/Group_ReadDataHierarchy.C`, `src/enzo/InitializeNew.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.conda`, `src/enzo/Make.mach.sdsc-expanse-gnu`, `src/enzo/Make.mach.ubuntu`, `src/enzo/New_Grid_ReadGrid.C`, `src/enzo/PhotonGrid_Methods.h`, `src/enzo/PhotonPackage.h`, `src/enzo/PopIIIRotationModel.C`, `src/enzo/ReadEquilibriumTable.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/Star.h`, `src/enzo/StarParticleRadTransfer.C`, `src/enzo/Star_ComputePhotonRates.C`, `src/enzo/TestRadiatingStarParticleInitialize.C`, `src/enzo/TestStarParticleInitialize.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`, `src/enzo/solve_rate_cool.F`, `src/enzo/star_maker2.F`.

<a id="commit-512"></a>
## 512 — `f1d6b767c` — 2024-03-01

Missing space in every option's last if statement.

**Categories:** 4.

Normalizes indentation of Make option-error target declarations throughout assemble file. Preserve local custom options; inspect actual parser behavior rather than call every whitespace change a bug fix.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`.

**Files:** `src/enzo/Make.config.assemble`.

**Patch locations:** `@@ -67,8 +67,8 @@`; `@@ -95,8 +95,8 @@`; `@@ -125,8 +125,8 @@`; `@@ -163,8 +163,8 @@`; `@@ -191,8 +191,8 @@`; additional hunks in the same patch.

<a id="commit-513"></a>
## 513 — `8898b36d6` — 2024-04-23

Merge pull request #238 from cindytsai/FixMakefile

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#511](batch-11.md#commit-511), [#512](batch-11.md#commit-512).

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`.

**Files:** `src/enzo/Make.config.assemble`.

<a id="commit-514"></a>
## 514 — `439fa3eb6` — 2025-03-10

Return metal density cap.

**Categories:** 3,2.

Restores metal-density <=0.9*gas-density safeguard after upstream Grackle removed it. Aeos wrapper lacks this cap. Port deliberately: writing through MetalPointer can mutate a single tracer while summed-metal scratch fields behave differently, and a cap is not a complete elemental mass-conservation repair.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`.

**Files:** `src/enzo/Grid_GrackleWrapper.C`.

**Patch locations:** `@@ -163,6 +163,17 @@ int grid::GrackleWrapper()`.

<a id="commit-515"></a>
## 515 — `b35de3434` — 2025-03-11

Pull HydrogenFractionByMass value back from Grackle to Enzo.

**Categories:** 3.

Copies HydrogenFractionByMass back from initialized Grackle to CoolData so Enzo follows the initialized table/chemistry value. Clean patch applies. Check compatibility of all three backends and initialization paths; do not assume one fixed primordial fraction.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`.

**Files:** `src/enzo/GrackleReadParameters.C`.

**Patch locations:** `@@ -243,6 +243,13 @@ int GrackleReadParameters(FILE *fptr, FLOAT InitTime)`.

<a id="commit-516"></a>
## 516 — `f175d4f14` — 2025-03-12

Update sphinx configuration.

**Categories:** 4.

Sets explicit Sphinx configuration path for ReadTheDocs. Documentation build plumbing only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.readthedocs.yaml`.

**Patch locations:** `@@ -4,4 +4,6 @@ build:`.

<a id="commit-517"></a>
## 517 — `c0d4bf820` — 2025-03-14

Update gold standard.

**Categories:** 4.

Rebaselines CI answers after the hydrogen-fraction synchronization. Accompany with the actual physics/interface fix and documented expected numerical differences.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `.circleci/config.yml`.

**Patch locations:** `@@ -217,16 +217,16 @@ jobs:`.

<a id="commit-518"></a>
## 518 — `418ef4e26` — 2025-03-14

Merge pull request #244 from brittonsmith/hfraction

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#515](batch-11.md#commit-515), [#516](batch-11.md#commit-516), [#517](batch-11.md#commit-517).

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`.

**Files:** `.circleci/config.yml`, `.readthedocs.yaml`, `src/enzo/GrackleReadParameters.C`.

<a id="commit-519"></a>
## 519 — `8b1815bdc` — 2025-03-14

Merge branch 'main' into metalcap

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#515](batch-11.md#commit-515), [#516](batch-11.md#commit-516), [#517](batch-11.md#commit-517), [#518](batch-11.md#commit-518).

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`.

**Files:** `.circleci/config.yml`, `.readthedocs.yaml`, `src/enzo/GrackleReadParameters.C`.

<a id="commit-520"></a>
## 520 — `3ab23bfd4` — 2025-03-18

Merge pull request #245 from brittonsmith/metalcap

**Categories:** 2,3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#514](batch-11.md#commit-514), [#519](batch-11.md#commit-519).

**Aeos-modified paths since common ancestor:** `src/enzo/Grid_GrackleWrapper.C`.

**Files:** `src/enzo/Grid_GrackleWrapper.C`.

<a id="commit-521"></a>
## 521 — `becf37fd7` — 2025-03-28

Fix the bug in H2 self-shielding

**Categories:** 3,4.

Native H2 shielding changes thermal Doppler mass from m_H to 2*m_H (appropriate for molecular H2) and halves the uncapped column-length expression. This is not a central-difference-gradient repair: divrho sums one-sided negative density differences. min(L/2,Lmax) is not 0.5*min(L,Lmax), so verify the H2 mass-to-number convention and capped branch before adopting the length change as correct. Aeos retains old expressions; relevance is native solve_rate_cool.F only, not Grackle or Emerick LWbackground_model.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/solve_rate_cool.F`.

**Patch locations:** `@@ -1198,7 +1198,7 @@ c     Exclude directions with (drho/ds > 0)`; `@@ -1206,7 +1206,7 @@ c               endif`.

<a id="commit-522"></a>
## 522 — `399df6916` — 2025-05-14

Merge pull request #246 from thinhhn2/h2selfshield_corr

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#521](batch-11.md#commit-521).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/solve_rate_cool.F`.

<a id="commit-523"></a>
## 523 — `c967ff82d` — 2025-06-11

Merge remote-tracking branch 'enzo-dev/main' into fix

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#504](batch-11.md#commit-504), [#505](batch-11.md#commit-505), [#506](batch-11.md#commit-506), [#507](batch-11.md#commit-507), [#508](batch-11.md#commit-508), [#509](batch-11.md#commit-509), [#510](batch-11.md#commit-510), [#511](batch-11.md#commit-511), [#512](batch-11.md#commit-512), [#513](batch-11.md#commit-513), [#514](batch-11.md#commit-514), [#515](batch-11.md#commit-515), [#516](batch-11.md#commit-516), [#517](batch-11.md#commit-517), [#518](batch-11.md#commit-518), [#519](batch-11.md#commit-519), [#520](batch-11.md#commit-520), [#521](batch-11.md#commit-521), [#522](batch-11.md#commit-522).

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`.

**Files:** `.circleci/config.yml`, `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature-or-improvement-request.md`, `.github/pull_request_template.md`, `.readthedocs.yaml`, `src/enzo/ExternalBoundary_SetGalaxySimulationBoundary.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/solve_rate_cool.F`.

<a id="commit-524"></a>
## 524 — `eeebadc5e` — 2025-06-15

Put compile libyt example in Make.mach.darwin/linux-gnu makefile.

**Categories:** 4.

Adds libyt include/link examples to GNU/Darwin machine files and docs. Optional infrastructure; retain Aeos machine-specific dependency paths.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/Make.mach.linux-gnu`.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.linux-gnu`.

**Patch locations:** `@@ -283,6 +283,8 @@ If we installed libyt at $(LOCAL_LIBYT_INSTALL), which this folder inclu`; `@@ -46,6 +46,7 @@ LOCAL_SZIP_INSTALL   = $(LOCAL_PACKAGES)`; `@@ -114,12 +115,14 @@ LOCAL_INCLUDES_HYPRE  =`; `@@ -133,6 +136,7 @@ LOCAL_LIBS_PYTHON = -framework Python`; `@@ -140,3 +144,4 @@ MACH_LIBS_MPI    = $(LOCAL_LIBS_MPI)`; additional hunks in the same patch.

<a id="commit-525"></a>
## 525 — `ef18a5b1a` — 2024-02-21

Merge pull request #13 from cindytsai/libyt

**Categories:** 1,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#444](batch-09.md#commit-444), [#445](batch-09.md#commit-445), [#446](batch-09.md#commit-446), [#451](batch-10.md#commit-451), [#452](batch-10.md#commit-452), [#454](batch-10.md#commit-454), [#455](batch-10.md#commit-455), [#456](batch-10.md#commit-456).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `doc/manual/source/user_guide/building_enzo.rst`, `src/enzo/CallInSitulibyt.C`.

<a id="commit-526"></a>
## 526 — `cfa73a247` — 2024-02-21

Merge pull request #14 from cindytsai/libyt

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#457](batch-10.md#commit-457), [#458](batch-10.md#commit-458), [#459](batch-10.md#commit-459).

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/InitializeLibytInterface.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

<a id="commit-527"></a>
## 527 — `6c5a6eedf` — 2024-03-01

Merge pull request #15 from cindytsai/libyt

**Categories:** 1,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#460](batch-10.md#commit-460), [#461](batch-10.md#commit-461), [#462](batch-10.md#commit-462), [#463](batch-10.md#commit-463), [#464](batch-10.md#commit-464), [#465](batch-10.md#commit-465), [#466](batch-10.md#commit-466).

**Aeos-modified paths since common ancestor:** `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/reference/MakeOptions.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/Make.config.assemble`, `src/enzo/Make.config.settings`, `src/enzo/Make.config.targets`.

<a id="commit-528"></a>
## 528 — `b9603365d` — 2024-03-07

Merge pull request #16 from cindytsai/libyt

**Categories:** 3.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#467](batch-10.md#commit-467), [#468](batch-10.md#commit-468).

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Files:** `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

<a id="commit-529"></a>
## 529 — `0d5631c5e` — 2024-03-07

Merge pull request #17 from cindytsai/libyt

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#469](batch-10.md#commit-469).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

<a id="commit-530"></a>
## 530 — `606bf8598` — 2025-05-07

Merge pull request #19 from cindytsai/fix

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#470](batch-10.md#commit-470), [#471](batch-10.md#commit-471), [#472](batch-10.md#commit-472), [#473](batch-10.md#commit-473), [#474](batch-10.md#commit-474), [#475](batch-10.md#commit-475), [#476](batch-10.md#commit-476), [#477](batch-10.md#commit-477), [#478](batch-10.md#commit-478), [#479](batch-10.md#commit-479), [#480](batch-10.md#commit-480), [#481](batch-10.md#commit-481), [#482](batch-10.md#commit-482), [#483](batch-10.md#commit-483), [#484](batch-10.md#commit-484), [#485](batch-10.md#commit-485), [#486](batch-10.md#commit-486), [#487](batch-10.md#commit-487), [#488](batch-10.md#commit-488), [#489](batch-10.md#commit-489), [#490](batch-10.md#commit-490), [#491](batch-10.md#commit-491), [#492](batch-10.md#commit-492), [#493](batch-10.md#commit-493), [#494](batch-10.md#commit-494), [#495](batch-10.md#commit-495), [#496](batch-10.md#commit-496), [#497](batch-10.md#commit-497), [#498](batch-10.md#commit-498), [#499](batch-10.md#commit-499), [#500](batch-10.md#commit-500), [#501](batch-11.md#commit-501).

**Aeos-modified paths since common ancestor:** `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/ActiveParticle.h`, `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/global_data.h`, `src/enzo/macros_and_parameters.h`.

<a id="commit-531"></a>
## 531 — `ecda4eaa0` — 2025-06-11

Merge pull request #21 from cindytsai/fix

**Categories:** 3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#502](batch-11.md#commit-502), [#503](batch-11.md#commit-503).

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`.

<a id="commit-532"></a>
## 532 — `7f25c68ff` — 2025-06-11

Merge pull request #22 from cindytsai/fix

**Categories:** 1,2,3,4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#504](batch-11.md#commit-504), [#505](batch-11.md#commit-505), [#506](batch-11.md#commit-506), [#507](batch-11.md#commit-507), [#508](batch-11.md#commit-508), [#509](batch-11.md#commit-509), [#510](batch-11.md#commit-510), [#511](batch-11.md#commit-511), [#512](batch-11.md#commit-512), [#513](batch-11.md#commit-513), [#514](batch-11.md#commit-514), [#515](batch-11.md#commit-515), [#516](batch-11.md#commit-516), [#517](batch-11.md#commit-517), [#518](batch-11.md#commit-518), [#519](batch-11.md#commit-519), [#520](batch-11.md#commit-520), [#521](batch-11.md#commit-521), [#522](batch-11.md#commit-522), [#523](batch-11.md#commit-523).

**Aeos-modified paths since common ancestor:** `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`.

**Files:** `.circleci/config.yml`, `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature-or-improvement-request.md`, `.github/pull_request_template.md`, `.readthedocs.yaml`, `src/enzo/ExternalBoundary_SetGalaxySimulationBoundary.C`, `src/enzo/GrackleReadParameters.C`, `src/enzo/Grid_GrackleWrapper.C`, `src/enzo/Make.config.assemble`, `src/enzo/solve_rate_cool.F`.

<a id="commit-533"></a>
## 533 — `7cae05ee6` — 2025-06-15

Update src/enzo/CallInSitulibyt.C

**Categories:** 4.

Expands commented libyt function-argument example. No active evolution change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -403,7 +403,11 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-534"></a>
## 534 — `ecdc9aa10` — 2025-06-15

Merge remote-tracking branch 'data-exp-lab/libyt' into fix

**Categories:** 4.

Integration record; categories summarize constituent changes, not an additional independent patch to cherry-pick. Combined-diff and remerge-diff inspection found no additional resolution patch. Where incoming changes are already Aeos ancestors, only the merge ancestry is absent.

**Merge inspection:** combined diff 0 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#525](batch-11.md#commit-525), [#526](batch-11.md#commit-526), [#527](batch-11.md#commit-527), [#528](batch-11.md#commit-528), [#529](batch-11.md#commit-529), [#530](batch-11.md#commit-530), [#531](batch-11.md#commit-531), [#532](batch-11.md#commit-532), [#533](batch-11.md#commit-533).

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

<a id="commit-535"></a>
## 535 — `b071cc3a4` — 2025-06-15

Add more comments describing the yt_run_Function/Arguments API.

**Categories:** 4.

Clarifies commented Python API examples and error messages. No active evolution change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`.

**Patch locations:** `@@ -397,17 +397,23 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`.

<a id="commit-536"></a>
## 536 — `f438281e0` — 2025-06-15

Fix adding code specific parameters.

**Categories:** 3.

Corrects generated metadata accessor types for double-valued disk-gravity parameters. Conditional exporter ABI correctness; regenerate against actual Aeos types rather than copy the upstream map.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/InitializeLibytInterface_finderfunctions.inc`.

**Patch locations:** `@@ -108,13 +108,13 @@ YT_SET_USERPARAM_NONINTEGER("PointSourceGravityCoreRadius", 1, &PointSourceGravi`.

<a id="commit-537"></a>
## 537 — `ba00b97b9` — 2025-06-18

Fix in situ python analysis doc.

**Categories:** 4.

Corrects documentation of mutually exclusive libyt modes. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -15,7 +15,7 @@ Below are links to the build and runtime requirements, which must be installed.`.

<a id="commit-538"></a>
## 538 — `5fc03f647` — 2025-06-28

Zeus face-centered field.

**Categories:** 3.

Marks Zeus velocities face-centered and provides corresponding face dimensions in libyt adapter. Necessary analysis consistency if Zeus plus libyt is used.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -18,6 +18,7 @@`; `@@ -314,7 +315,16 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -83,6 +83,21 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-539"></a>
## 539 — `19bad1593` — 2025-06-30

Mention `libyt` in analyzing enzo data.

**Categories:** 1.

Adds in-situ yt cross reference and CPU-resident data limitation to analysis guide. Clean documentation patch.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/AnalyzingWithYT.rst`.

**Patch locations:** `@@ -20,6 +20,10 @@ For more information on yt, see the yt website <http://yt-project.org>_,`.

<a id="commit-540"></a>
## 540 — `6d939a4b7` — 2025-06-30

Add input param libyt_fig_basename, CycleLastLibytCall, CycleSkipLibytCall

**Categories:** 4.

Adds libyt figure basename and cycle scheduling parameter I/O/defaults. Optional public analysis controls; accompany with final call scheduling implementation.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -129,7 +129,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -1192,6 +1192,9 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`; `@@ -970,6 +970,10 @@ int SetDefaultGlobalValues(TopGridData &MetaData)`; `@@ -182,6 +182,9 @@ int WriteParameterFile(FILE *fptr, TopGridData &MetaData, char *name = NULL)`; `@@ -982,6 +982,9 @@ EXTERN PyObject *my_processor;`.

<a id="commit-541"></a>
## 541 — `fa31b3069` — 2025-07-01

Move CallInSitulibyt from EvolveLevel to EvolveHierarchy.

**Categories:** 4,2.

Moves analysis from level subcycles to the synchronized hierarchy. Better global-state interpretation, but overlaps custom evolution hooks; port deliberately if enabling libyt.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`.

**Files:** `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`.

**Patch locations:** `@@ -130,6 +130,8 @@ int SetEvolveRefineRegion(FLOAT time);`; `@@ -615,6 +617,12 @@ int EvolveHierarchy(HierarchyEntry &TopGrid, TopGridData &MetaData,`; `@@ -846,12 +846,12 @@ int EvolveLevel(TopGridData *MetaData, LevelHierarchyEntry *LevelArray[],`.

<a id="commit-542"></a>
## 542 — `5709b67bc` — 2025-07-01

Input parameter for controlling cycle based libyt call.

**Categories:** 4.

Adds CheckForLibytCall and cycle cadence controls. New optional analysis scheduling interface; preserve restart counters.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/Make.config.objects`.

**Files:** `src/enzo/CheckForLibytCall.C`, `src/enzo/EvolveHierarchy.C`, `src/enzo/Make.config.objects`.

**Patch locations:** `@@ -0,0 +1,44 @@`; `@@ -100,6 +100,7 @@ int CheckForOutput(HierarchyEntry *TopGrid, TopGridData &MetaData,`; `@@ -619,7 +620,7 @@ int EvolveHierarchy(HierarchyEntry &TopGrid, TopGridData &MetaData,`; `@@ -69,6 +69,7 @@ OBJS_CONFIG_LIB = \`.

<a id="commit-543"></a>
## 543 — `25363d0bf` — 2025-07-01

Update docs for cycle-based libyt call and figure basename.

**Categories:** 4.

Documents cycle cadence, figure naming and default script behavior. No solver change.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/user_guide/ControllingDataOutput.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -3881,7 +3881,21 @@ libyt In Situ Python Analysis`; `@@ -89,6 +89,8 @@ Timing Methods`; `@@ -83,7 +83,7 @@ General`; `@@ -93,6 +93,28 @@ General`; `@@ -125,7 +147,7 @@ General`.

<a id="commit-544"></a>
## 544 — `46db77b6d` — 2025-07-11

Mention what is not supported in the doc.

**Categories:** 4.

Documents Zeus face-centered-field and particle-type support limits. Check consistency with #538; support limitations remain an adoption concern.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -7,6 +7,9 @@ This feature enables Enzo to do in situ analysis using Python, by calling and us`.

<a id="commit-545"></a>
## 545 — `e7b53a173` — 2025-08-16

Set particle units, and correct particle_mass.

**Categories:** 3.

Converts Enzo particle pseudo-density to particle mass using cell volume and sets particle attribute units. Essential analysis mass normalization if porting libyt. Temporary io type naming is reverted in #554.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `src/enzo/CallInSitulibyt.C`, `src/enzo/Grid_ConvertToLibyt.C`.

**Patch locations:** `@@ -228,7 +228,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -257,8 +257,33 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -52,11 +52,12 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`; `@@ -122,13 +123,21 @@ void grid::ConvertToLibyt(int LocalGridID, int GlobalGridID, int ParentID, int l`.

<a id="commit-546"></a>
## 546 — `70c6e0ddb` — 2025-08-17

Set and initialize dtLibytCall and TimeLastLibytCall.

**Categories:** 4.

Adds time-cadence parameters/defaults/restart I/O for libyt. New optional public interface, requiring guards from #561.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/InitializeNew.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `src/enzo/InitializeNew.C`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Patch locations:** `@@ -881,6 +881,9 @@ int InitializeNew(char *filename, HierarchyEntry &TopGrid,`; `@@ -1195,6 +1195,8 @@ int ReadParameterFile(FILE *fptr, TopGridData &MetaData, float *Initialdt)`; `@@ -974,6 +974,9 @@ int SetDefaultGlobalValues(TopGridData &MetaData)`; `@@ -185,6 +185,8 @@ int WriteParameterFile(FILE *fptr, TopGridData &MetaData, char *name = NULL)`; `@@ -985,6 +985,8 @@ EXTERN char libyt_script_name[512];`.

<a id="commit-547"></a>
## 547 — `aa249312e` — 2025-08-17

Call libyt routine time-based.

**Categories:** 4.

Implements time-based libyt scheduling and initial invocation. Includes temporary std::cout debugging; prefer final feature behavior.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`.

**Files:** `src/enzo/CheckForLibytCall.C`, `src/enzo/EvolveHierarchy.C`.

**Patch locations:** `@@ -29,7 +29,7 @@ int CallInSitulibyt(LevelHierarchyEntry *LevelArray[], TopGridData *MetaData,`; `@@ -38,7 +38,19 @@ int CheckForLibytCall(LevelHierarchyEntry *LevelArray[], TopGridData &MetaData)`; `@@ -262,6 +262,12 @@ int EvolveHierarchy(HierarchyEntry &TopGrid, TopGridData &MetaData,`.

<a id="commit-548"></a>
## 548 — `cd68440e2` — 2025-08-18

Make sure dt is set to not skipping dtLibytCall.

**Categories:** 2,4.

Caps the physical evolution timestep at analysis output times. Even read-only analysis now changes the numerical timestep sequence when enabled. Default-off timing interval is not enough to claim no physics impact for enabled runs; compare with matched timestep schedules.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward PASS; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`.

**Files:** `src/enzo/EvolveHierarchy.C`.

**Patch locations:** `@@ -420,6 +420,12 @@ int EvolveHierarchy(HierarchyEntry &TopGrid, TopGridData &MetaData,`.

<a id="commit-549"></a>
## 549 — `27d998b51` — 2025-06-19

Update doc/manual/source/user_guide/InSituPythonAnalysis.rst

**Categories:** 4.

Clarifies that the imported libyt script supplies named functions and examples must be enabled deliberately. Documentation only.

**Incorporation:** not established by patch identity; see assessment. **Direct patch checks:** forward FAIL; reverse FAIL. A failed check can reflect prerequisites or changed context; it is not by itself a scientific conflict.

**Aeos-modified paths since common ancestor:** none.

**Files:** `doc/manual/source/user_guide/InSituPythonAnalysis.rst`.

**Patch locations:** `@@ -95,9 +95,10 @@ General`.

<a id="commit-550"></a>
## 550 — `fe6b6768f` — 2025-07-09

Merge pull request #23 from cindytsai/fix

**Categories:** 4.

Combined merge hunks reconcile libyt cycle scheduling/figure documentation. No new executable physics; follow constituent scheduling commits.

**Merge inspection:** combined diff 1832 bytes; remerge diff 0 bytes. Positive results are discussed above.

**Constituents in inventory:** [#524](batch-11.md#commit-524), [#534](batch-11.md#commit-534), [#535](batch-11.md#commit-535), [#536](batch-11.md#commit-536), [#537](batch-11.md#commit-537), [#538](batch-11.md#commit-538), [#539](batch-11.md#commit-539), [#540](batch-11.md#commit-540), [#541](batch-11.md#commit-541), [#542](batch-11.md#commit-542), [#543](batch-11.md#commit-543).

**Aeos-modified paths since common ancestor:** `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.

**Files:** `doc/manual/source/parameters/index.rst`, `doc/manual/source/user_guide/AnalyzingWithYT.rst`, `doc/manual/source/user_guide/ControllingDataOutput.rst`, `doc/manual/source/user_guide/InSituPythonAnalysis.rst`, `src/enzo/CallInSitulibyt.C`, `src/enzo/CheckForLibytCall.C`, `src/enzo/EvolveHierarchy.C`, `src/enzo/EvolveLevel.C`, `src/enzo/Grid_ConvertToLibyt.C`, `src/enzo/InitializeLibytInterface_finderfunctions.inc`, `src/enzo/Make.config.objects`, `src/enzo/Make.mach.darwin`, `src/enzo/Make.mach.linux-gnu`, `src/enzo/ReadParameterFile.C`, `src/enzo/SetDefaultGlobalValues.C`, `src/enzo/WriteParameterFile.C`, `src/enzo/global_data.h`.
