# Enzo main → Aeos v2 upstream review

Historical review against the frozen baseline below. Later adoption is recorded
in [upstream-fixes-20261112.md](../upstream-fixes-20261112.md):
`c8657fc94` directly cherry-picks upstream `b35de343` (hydrogen synchronization),
and `4a184506b` partially ports upstream `5ed618ce` (flux rollback indices only).
The remaining recommendations here are review dispositions, not implemented fixes.

Reviewed 2026-10-31. **All 577 commits in the frozen upstream-only inventory have a disposition in 12 reports of at most 50 commits.** This is a static adoption review, not a claim that 577 independent improvements are missing or that the proposed ports have passed simulation tests.

Read [findings and adoption priorities](findings.md) first. The batch reports provide the individual decisions; [inventory.json](inventory.json) retains full hashes, parents, file lists, dry-run diagnostics and assessments. [progress.json](progress.json) records coverage and category totals; [validation.json](validation.json) records the completed reconciliation checks.

For the actual galaxy configurations, see [h277 and isolated-dwarf result impact](h277-isolated-impact.md). It checks runtime gates and saved outputs, including an observed Enzo/Grackle hydrogen-fraction mismatch in newchem, and distinguishes the enabled flux defect from fixes to unused algorithms.

## Frozen comparison

| Item | Value |
| --- | --- |
| Upstream repository / branch | `/home/wispedia/install/enzo-dev`, `main` |
| Upstream tip | `7409c9a3ee0a8f53e3ada7a053098e2c559df71e` |
| Working repository / branch | `/home/wispedia/enzo/EnzoAeos-v2`, `aeos-v2` |
| Aeos tip | `0dbaa4beae8f1e411a6dd99680b9650d5960791b` |
| Common ancestor | `50fc0d53478bb276f23ebe26335eda1d44f30257` (2020-04-10) |
| Aeos-only / main-only ancestry | 971 / 577 commits |
| Main-only ordinary / merge commits | 416 / 161 |
| Author-date span in inventory | 2019-06-28 through 2026-10-29 |
| Commits touching `src` relative to first parent | 285, including merges |

The inventory is the full repository's `aeos-tip..main-tip`, including old side-branch history subsequently merged into main. A date cutoff or first-parent-only log would miss changes. Topological order keeps prerequisites before descendants; it does not imply monotonically increasing dates. Local branch tips were used without a network fetch.

## Categories

| Category | Decision |
| --- | --- |
| **1** | Mechanically compatible, preserves intended runtime physics; usually documentation or maintenance |
| **2** | Requires adaptation/decision because Aeos code, interfaces, model choices or build controls conflict |
| **3** | Correctness repair worth adopting **where the defective path exists**; may already be implemented in Aeos |
| **4** | Optional improvement, new feature, portability work, or historical development step; no obligation to follow |

Multiple categories are intentional: a required bug fix may also conflict with custom Aeos code. Category 3 is not a count of missing bugs: many are repairs to libyt, CR or galaxy features not installed in Aeos. Superseded, reverted and already incorporated changes retain an explicit disposition.

For ordinary commits the category counts overlap: **1: 19; 2: 47; 3: 116; 4: 285**. Merge classifications summarize incoming changes unless a resolution has its own assessment; they are excluded from these totals to avoid double counting.

## Method and evidence limits

1. Enumerated every reachable upstream commit absent from Aeos ancestry using `git rev-list --reverse --topo-order AEOS..MAIN` and inspected ordinary patches. Large optional feature imports are assessed by subsystem/final integration; third-party SSE2NEON is reviewed for scope and integration, not certified intrinsic by intrinsic.
2. Compared relevant current Aeos implementations, including radiation cleanup, MPI star gathering, HDF5 references, Grackle interfaces, gravity, IC masses, feedback, inflow boundaries and flux rollback. Inspected later corrections/reversions to distinguish final behavior from intermediate experiments. The notes identify where current-code equivalence is established; absence of a patch-ID match alone never proves a missing implementation.
3. Ran `git cherry AEOS MAIN`: one exact equivalent ordinary patch, `8d8249df8`, is already incorporated. Ran **forward and reverse `git apply --check` for all 416 ordinary patches** against the current Aeos working tree. Its source/configuration content matches the frozen Aeos tip; pre-existing documentation edits do not overlap these patch paths.
4. Results: **65 forward passes; 9 reverse passes; 342 fail both**. These are independent checks against the frozen baseline, not a sequential cherry-pick trial. A failure may mean missing prerequisites, changed context, removed files or partial incorporation. A pass proves textual applicability, not scientific compatibility. Reverse success can reflect an absent optional file, not an incorporated bug fix.
5. Inspected **all 161 merges with both combined diffs and remerge diffs**. Six have nonempty combined diffs; twelve have nonempty remerge diffs. These sets differ. Explicit resolutions are documented; all merges link to their incoming inventory commits. Git's present-day reconstructed merge is evidence about resolution differences, not a perfect recreation of historical Git behavior.
6. No production source fixes, cherry-picks, builds or galaxy runs were performed. Suggested regression scenarios in the findings are acceptance criteria for future ports, not claimed test results. Scientific calibration, published-run exposure and cross-backend equivalence still require targeted experiments.

Git object access used `GIT_ALTERNATE_OBJECT_DIRECTORIES=/home/wispedia/install/enzo-dev/.git/objects` while reading from the Aeos repository; neither branch was changed. Reproduce ordinary patches with `git show HASH` and merge resolutions with `git show --remerge-diff HASH`. The JSON includes full commit IDs and raw patch-check errors; use those IDs even if branches later move.

## Batch reports

| Batch | Inventory entries | Ordinary / merges | Focus |
| --- | --- | --- | --- |
| [01](batch-01.md) | 001–050 | 33 / 17 | Radiation cleanup, MPI stars, HDF5, Grackle guards |
| [02](batch-02.md) | 051–100 | 36 / 14 | Boundaries, single-SN fixes, CR development |
| [03](batch-03.md) | 101–150 | 32 / 18 | CR integration, yt4 tests, timing |
| [04](batch-04.md) | 151–200 | 32 / 18 | FDM initialization and machine support |
| [05](batch-05.md) | 201–250 | 40 / 10 | SIMD, galaxy/CGM import, libyt start |
| [06](batch-06.md) | 251–300 | 33 / 17 | libyt grid hierarchy and startup |
| [07](batch-07.md) | 301–350 | 42 / 8 | libyt metadata, rotating PopIII, galaxy gravity |
| [08](batch-08.md) | 351–400 | 34 / 16 | Galaxy/restarters, chemistry, documentation |
| [09](batch-09.md) | 401–450 | 37 / 13 | Star-formation cadence, IC masses, CI |
| [10](batch-10.md) | 451–500 | 48 / 2 | libyt fields, units and active particles |
| [11](batch-11.md) | 501–550 | 31 / 19 | Galaxy boundaries, Grackle contracts, analysis cadence |
| [12](batch-12.md) | 551–577 | 18 / 9 | CMake migration, precision conversion, flux rollback |

The pre-existing `docs/physics-review.md` concerns custom Emerick/Aeos stellar routines. This upstream review complements it and does not establish authorship or publication exposure of those defects. Documentation changes were left uncommitted for review.
