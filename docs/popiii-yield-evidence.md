# PopIII ejecta-table evidence

Reviewed 2026-11-06. This is a read-only investigation: no production yield table,
physics source, executable, or run input was changed.

## Direct comparison with the author's source data

The subsequent download and comparison identifies the current elemental
dataset numerically: **HW2010, S4 piston, 1.2 Bethe, mixing 0.1**, converted
from elemental molar abundances using terrestrial/natural atomic weights.
The exact local file-generation history remains unverified.

Downloaded primary sources:

- [Author-hosted machine-readable isotope table](https://2sn.org/firststars/znuc/ApJ/datafile9.txt.gz).
  Its 660,546 data records are identical to the locally recovered
  `heger_woosley_2010_yields.dat`, ignoring header/whitespace differences.
  This ASCII file contains only four mixing choices, through 0.00251.
- [HW2010 S4 elemental database](https://2sn.org/starfit/data/znuc.S4.star.el.y.stardb.gz).
- [HW2010 S4 stable-isotope database](https://2sn.org/starfit/data/znuc.S4.star.deciso.y.stardb.gz).
  The databases contain 16,800 models: 120 masses, 10 energies, 14 mixing
  choices including 0.1. They are the `znuc` HW2010 datasets, rather than
  the separately labeled unpublished `znuc2012` update, as distinguished on
  the [author's data page](https://2sn.org/starfit/).

The database metadata specifies molar abundances normalized to ejecta, includes
SN ejecta plus winds, and provides remnant mass as a separate field.

For each available S4 energy/mixing selection, the comparison tests

```text
predicted element mass =
    source elemental molar abundance
    × natural atomic weight
    × (progenitor mass − source remnant mass)
```

Only the 1.2 Bethe, mixing 0.1 selection matches all 81 shared elements across
all 120 CCSN masses at relative tolerance `1e-6`; its maximum absolute
elemental difference is `9.323e-7` solar masses. The second-best selection
differs by as much as 0.606 solar masses. Tc and Pm are absent from the
author's stable elemental database but appear in our table at at most
`4.60e-14` and `5.22e-15` solar masses; their origin is not resolved.

The stable-isotope database independently supplies the mass-consistent
conversion:

```text
element ejecta =
    Σ over its isotopes [source isotope molar abundance × isotope A]
    × (progenitor mass − source remnant mass)
```

The isotope mass fractions sum to unity within `1.50e-9` across this model
selection. Summing the resulting isotope masses reproduces source ejecta
mass. Using natural atomic weights for elemental number abundances instead
introduces a smaller conversion discrepancy because the stellar ejecta's
isotope mixture is not a terrestrial isotope mixture.

| Progenitor | Source remnant | Source ejecta / isotope sum | Current elemental sum | Current `Mtot` |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 1.276 | 8.724 | 8.768543 | 10 |
| 23 | 4.509 | 18.491 | 18.580053 | 23 |
| 55 | 12.597 | 42.403 | 42.556632 | 55 |
| 70 | 35.352 | 34.648 | 34.805752 | 70 |
| 100 | 35.698 | 64.302 | 64.545751 | 100 |

All values are solar masses. For example, the 70 solar-mass hydrogen yield
is 18.499718 in the isotope-based source conversion but 18.646605 after
the natural-weight conversion, matching the current value 18.646605.
The maximum excess of the current elemental sum over source ejecta is about
0.5254% across the 120 rows.

Thus two discrepancies are distinguishable: a large incorrect total-ejecta
column, and a much smaller elemental molar-to-mass conversion discrepancy.
The source remnant mass at 70 solar masses is **35.352**, rather than the
35.194248 inferred by merely subtracting our current elemental sum.

## Finding

The current `IndividualStarYields-Mix0.1.h5` has an inconsistent PopIII
core-collapse total-ejecta column. All 120 rows from 10 through 100 solar masses
store progenitor mass in `Mtot`, while their complete elemental ejecta sum is
smaller. Enzo consumes `Mtot` as **mass ejected**, independently of the elemental
yields. This is a table/consumer contract mismatch, supported by the recovered
generator and a comparison table that obeys the contract. The comparison
file's original generation provenance is unverified.

This establishes an inconsistent injection mass budget. It does not establish
which table-editing step introduced it or that a particular published simulation
used this file.

## Direct measurements

The following three files are byte-identical:

- `/home/wispedia/AA/AeosTables/IndividualStarYields-Mix0.1.h5`
- `/home/wispedia/install/analysis_scripts/isolated_dwarf/tables/IndividualStarYields-Mix0.1.h5`
- `/home/wispedia/AA/isolated/runs/deterministic-150Myr/newchem/IndividualStarYields-Mix0.1.h5`

Their SHA256 is
`31b72501574c6488eb65a49dbeb6d6a4b885192a43603a92a5d452c795801189`.

The independent comparison file is
`/home/wispedia/AA/isolated/runs/deterministic-150Myr/newchem/IndividualStarYields-Emerick.h5`,
SHA256 `beecd48bcc57` (prefix; full hash in the audit JSON).

A byte-identical copy is tracked at
`/home/wispedia/install/analysis_scripts/isolated_dwarf/tables/IndividualStarYields-Emerick.h5`,
introduced by commit `3f899df7cc430e812c1593409773e3f840763456` on 2026-10-29
(`Add required isolated dwarf input tables`). That directory's README says the
tables were copied from isolated runs, but does not identify the original file
or generation procedure. Neither that commit nor the filename proves that
Emerick generated this particular file or establishes which table is older.
The creation/copy route into the deterministic-run directory is also unverified.

| Check | Current Mix0.1 | Comparison file named Emerick |
| --- | ---: | ---: |
| CCSN rows, 10–100 solar masses | 120 | 120 |
| CCSN `Mtot` equals sum of all elements | 0/120 | 120/120 |
| PISN `Mtot` equals sum of all elements | 14/14 | 14/14 |
| CCSN `Mtot` equals progenitor mass | 120/120 | — |

Comparisons allow float32 storage rounding. The elemental columns cover every
atomic number from H through Bi; this is not a sum restricted to the species
tracked by a particular simulation. The current total-metal column also agrees
with its elemental sum (maximum relative discrepancy about `6.7e-8`).

Examples from the current table, in solar masses:

| Progenitor | Stored total ejecta | Sum of elemental ejecta | Progenitor minus elemental sum |
| ---: | ---: | ---: | ---: |
| 10 | 10 | 8.768543 | 1.231457 |
| 23 | 23 | 18.580053 | 4.419947 |
| 55 | 55 | 42.556632 | 12.443368 |
| 70 | 70 | 34.805752 | 35.194248 |
| 100 | 100 | 64.545751 | 35.454249 |

The largest CCSN ratio of stored total to summed elemental ejecta is about
2.011. This discrepancy is much larger than rounding.

## Recovered generator and comparison data

The generator is present locally in
`/home/wispedia/install/galaxy_analysis`, revision
`a47c41e000a9b4fa5bad768010fb5ee03ed79e13`.

In `individualstar_data/construct_tables/compile_popIII.py`:

- Lines 102–114 sum isotope ejecta into elemental yields.
- Lines 121–129 construct `Total, Total metals, H, He, …, Bi`.
  Line 128 explicitly sets the total to the sum of the elemental yields.
- The PISN routine uses the same total-mass convention at line 221.

The total-sum assignment is already present in historical commit `8693134`
(2020-04-24). The recovered `popIII_yields.in` also closes its own mass budget.
Its PopIII yields match `IndividualStarYields-Emerick.h5` at float32
storage precision. This numerical match supports a shared data lineage but
does not prove how this HDF5 file was created.

`benoit_to_hdf5.py:165–197` reads this ASCII file, retains its yield columns,
and labels the first yield column `Mtot`. This conversion routine does not
replace the ejecta total with progenitor mass.

These findings correct the older investigation's statement that the generator
had not been found locally. The CCSN mass range here is 10–100, not 10–130.

The current Mix0.1 elemental yields differ from the comparison table by up to
1.388766 solar masses in an individual element. An independent isotope sum
over all complete energy/piston/mixing selections available in the recovered
HW2010 raw file does not exactly reproduce the current elemental dataset
(best maximum absolute discrepancy: 1.363726 solar masses).
That initial comparison was limited to the recovered ASCII file's four mixing
choices. The larger author database comparison above now identifies the
0.1-mixing model and elemental conversion numerically. The exact local
production history of the current Mix0.1 file remains unresolved.

## Physical interpretation and Enzo consumption

[Heger & Woosley (2010)](https://doi.org/10.1088/0004-637X/724/1/341)
models the explosions, ejecta, and remnant masses of 10–100 solar-mass metal-free
stars. The local machine-readable source distinguishes progenitor mass from
post-supernova ejecta, including wind. A universal assumption that the whole
progenitor is ejected is inconsistent with both that distinction and the
recovered generator's mass convention.

The consumer chain in this Enzo checkout is:

1. `src/enzo/StellarYields_Initialize.C:724–741` explicitly identifies the first
   yield column as total mass ejected and loads it into `Mtot`.
2. `StellarYieldsRoutines.C:520–578` returns interpolated `Mtot` for a negative
   atomic-number query, and returns the separate elemental columns for species
   queries.
3. `IndividualStarProperties.C:1640–1707` assigns the negative-query result to
   `m_eject` and obtains metals/species separately, when stellar yields are
   enabled with `MultiMetals == 2`.
4. `IndividualStarParticleAddFeedback.C` subtracts `m_eject` from particle mass
   around line 629, adds the corresponding ejecta to gas around lines 906–922,
   and adds elemental yields separately around lines 1010–1036.

For a 70 solar-mass PopIII particle still carrying its birth mass at explosion,
the current table therefore requests 70 solar masses of gas ejecta and leaves
zero particle mass, despite supplying only 34.805752 solar masses in its full
elemental ejecta vector. Using that vector's sum as total ejecta would instead
leave 35.194248 solar masses in the particle.

This does **not** by itself imply creation of total baryonic mass: the gas
addition has a corresponding particle subtraction. It misallocates mass
between ejecta and remnant and makes total gas injection inconsistent with its
elemental injection. Later chemical renormalization and the quantitative
hydrodynamic consequences have not been tested here.

The normal CCSN explosion energy in this routine is set separately by
`IndividualStarSupernovaEnergy`; changing the ejecta-total column would not
directly change that prescribed energy.

## Scope and proposed repair

The 14 PISN rows already close their elemental mass budgets. Their generator
converts helium-core masses to a progenitor-mass axis; the smaller ejecta sum
than the listed progenitor mass must not be diagnosed using the CCSN
`Mtot == birth mass` pattern. Envelope accounting is a separate question.

For the CCSN inconsistency, merely replacing the total column with the current
elemental sum would repair internal closure but retain the smaller conversion
discrepancy. With the author dataset now identified, the better source-faithful
candidate is to regenerate elemental mass yields from the isotope molar
abundances and mass numbers, and set total ejecta to progenitor minus source
remnant mass (checking the isotope sum within source precision). Preserve the
original file and record source hashes, model choice, and conversion.
Copying totals from the comparison table while retaining current elemental
yields would leave a mismatch. Prefer a documented table correction over
silently redefining the reader's convention.

Before adopting a corrected table, validate mass/species closure across all
groups and exercise one PopIII feedback event to check gas, species, remaining
particle mass, and energy. This investigation checks files, provenance, and
the source path; it does not execute a full grid-feedback event or demonstrate
that PopIII feedback occurred in the isolated-disk comparison.

## Reproduction

The audit reads production files without modifying them and writes reports in
its own directory:

```bash
python3 /home/wispedia/AA/isolated/physics-audit/popiii-evidence/audit.py
```

Dependencies are Python, NumPy, h5py, and Git. Paths are specific to this
installation. Outputs:

- `/home/wispedia/AA/isolated/physics-audit/popiii-evidence/results.json`:
  hashes, generator revision, comparisons, and raw-model matching results.
- `/home/wispedia/AA/isolated/physics-audit/popiii-evidence/current-mass-budget.csv`:
  every current PopIII row.
- `/home/wispedia/AA/isolated/physics-audit/popiii-evidence/run.log`:
  captured successful audit output.

The direct author-data comparison is reproduced with:

```bash
python3 /home/wispedia/AA/isolated/physics-audit/popiii-evidence/compare_author.py
```

Its additional dependencies are yt's periodic table and the StarFit reader
checkout under `source/starfit`, revision
`21c59a9cc5ace231296ed7fd141b7d35e40e0962`.
The script applies an in-memory reader compatibility shim removing an
unsupported `isotope=True` keyword from isotope construction; the downloaded
database contents and reader checkout are not edited.
Outputs `author-comparison.json`, `author-comparison.csv`, and
`author-comparison.log` record source URLs, SHA256 hashes, reader revision,
all-row mass budgets, and model-match statistics. Downloaded source files are
retained under `physics-audit/popiii-evidence/source/`.
