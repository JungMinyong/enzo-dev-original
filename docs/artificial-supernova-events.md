# Reproducible artificial supernova driving

Set this runtime parameter to inject the same artificial supernova events in
different runs and Grackle builds:

```ini
IndividualStarICSupernovaEventFile = sn-events.txt
IndividualStarICSupernovaInjectionMethod = 1
```

The feature is independent of the Grackle backend. Omitting the event-file
parameter retains the existing rate-based, random-position driving.
`IndividualStarICSupernovaFromFile` is the older **rate-table** option; it is
not the new event-list option.

## Stop after the first stellar birth

To stop artificial driving 25 physical Myr after the first stellar birth:

```ini
IndividualStarICSupernovaStopAfterFirstStarMyr = 25
```

The default is -1 (disabled); zero stops at the first birth. This option
requires an event file. The earliest birth among newly created Aeos particle
types 11–15, including unresolved stellar populations, starts the clock.
Dark matter and other particle types do not. Births are collected locally
and reduced across MPI ranks once per root timestep before time actions.
Only candidate events strictly before first birth plus the requested delay
are injected. Events exactly at the cutoff are excluded. Without any stellar
birth, the full candidate schedule remains available.

`IndividualStarICSupernovaFirstStarTime` is checkpoint state in code units,
initially -1. It is written automatically; do not set it in a fresh input.
The saved birth time, event cursor, and fingerprint preserve shutdown across
restarts, including when suppressed candidates lie before the restart time.
This feature tracks births from its first enabled fresh startup; it does not
recover historical births from an older checkpoint lacking that state.
Ordinary stellar feedback is unaffected. No shutdown restart is necessary.

The shared `sn-events-fiducial-seed42-150Myr.txt` contains 60 candidates at
2.5 Myr intervals through 150 Myr. Its first 43 rows reproduce the original
truncated schedule. Use the extended file from the beginning of a fresh run;
replacing an event file in an existing realization invalidates its fingerprint.

## File format

One event per line, with four whitespace-separated numbers:

```text
# time_Myr x_code y_code z_code
2.5 0.49957099377422470 0.49948520680590802 0.49923738751989533
5.0 0.50060919145547211 0.50358496021527221 0.50059898131329805
```

- Times are absolute simulation times in Myr, not delays from a restart.
  Conversion uses Enzo's `Myr_s / TimeUnits`. This branch defines `Myr_s` as
  3.1556952e13 seconds; if `TimeUnits=3.15576e13`, a file time of 5 corresponds
  to code time 4.99989733.
- Positions are absolute code coordinates, as in `DomainLeftEdge` and
  `DomainRightEdge`, not offsets from the galaxy center.
- Times must be positive and in nondecreasing order. Equal-time events are
  injected in file order during the same root-level time action.
- Coordinates must lie inside the domain, including the left edge and
  excluding the right edge. Blank lines and `#` comments are allowed.
- Empty files, extra columns, missing columns, nonfinite values, descending
  times, and out-of-domain positions are rejected.
- This implementation supports three-dimensional, noncomoving runs with
  spherical thermal injection (`IndividualStarICSupernovaInjectionMethod=1`).

The file overrides the legacy SN rate, cutoff time, rate-table flag, spatial
sampling method, radius, height, and center for scheduling and positions.
It reuses one existing type-3 time-action slot or allocates one automatically.
Remove duplicate type-3 actions; multiple slots are rejected.
Other time-action types continue to operate.

The existing artificial-SN injection physics is retained: 10 Msun ejecta per
event and `IndividualStarSupernovaEnergy * 1e51` erg, with the configured
feedback radius/stencil. This option does not add individual stellar yields,
per-event energies, or new dust physics.

## Generate a table once

From the repository root:

```bash
python3 run/generate_artificial_sn_events.py sn-events.txt \
  --seed 42 --duration-myr 5 --rate-per-year 4e-7 \
  --box-pc 59000 --radius-pc 250 --half-height-pc 100
```

This produces the two events shown above. Positions are sampled uniformly in
the volume of a cylinder: radius is proportional to the square root of a
uniform deviate, azimuth is uniform, and height is uniform.
The default periodic times preserve the constant-rate convention used in the
isolated-disk comparison: events at 2.5 and 5 Myr.

Add `--time-sampling poisson` to sample exponential waiting times as well as
positions. `--start-myr` sets the absolute start of sampling; the first event
occurs after it. The generator assumes a cubic `[0,1)^3` domain, with the
physical box width supplied by `--box-pc`. It refuses to overwrite an existing
file. Reuse the **same saved table** for comparisons; the file, rather than the
runtime RNG state, defines the experiment.

## Restart and MPI behavior

Only the root MPI rank reads the file, then broadcasts the complete event
table. No runtime random draws are made for file-driven SN positions.
Root timesteps are shortened to the next event time without the legacy
time-action overshoot factor. Each event logs its index, requested time,
actual code time, and position.

Checkpoints write:

```ini
IndividualStarICSupernovaEventFile = /absolute/path/sn-events.txt
IndividualStarICSupernovaNextEvent = 2
IndividualStarICSupernovaEventFingerprint = ...
```

The cursor is the zero-based index of the next event. It advances only after
injection and projection to parent grids. A restart therefore resumes without
repeating completed events, and a fully consumed table stays inactive.
The file must remain available. The saved FNV-1a 64-bit fingerprint rejects
file changes, including comments or whitespace changes, on restart.
An identical copy at a different path is acceptable if the checkpoint path is
updated. Paths containing whitespace are not supported by the parameter reader.

For a fresh run, omit the cursor and fingerprint. The default cursor is zero
and the first event must be strictly later than `InitialTime`. For an existing
checkpoint that predates this option, an intentional migration must specify
the correct next-event index for the new table; inconsistent indices are
rejected. Do not reset the index to zero in a normal restart.

Identical events remove the artificial-driving randomness from a comparison.
They do not guarantee bitwise identical fluid evolution across MPI layouts,
compiler options, or different chemistry/physics models.

## Tests

The first-star cutoff regression compiles the production event implementation
with controlled units and globals:

```bash
g++ -std=c++11 -Wno-literal-suffix \
  -DCONFIG_PFLOAT_8 -DCONFIG_PINT_8 -DCONFIG_BFLOAT_8 -DSMALL_INTS \
  -D__max_baryons=60 -D__max_subgrids=100000 \
  -D__max_particle_attr=20 -D__max_cpu_per_node=64 \
  tests/artificial_supernova_events/cutoff.cpp -o /tmp/sn-cutoff-test
/tmp/sn-cutoff-test /path/to/sn-events-fiducial-seed42-150Myr.txt
```

This checks stellar-type filtering, exact and between-event cutoff boundaries,
disabled and exhausted schedules, invalid saved state, and restart equivalence.
An MPI build of the same fixture also exercises earliest-birth reduction across
ranks; the serial command above does not test that collective.

Parser and generator tests:

```bash
g++ -std=c++11 tests/artificial_supernova_events/parser.cpp -o /tmp/sn-parser-test
/tmp/sn-parser-test /tmp/sn-parser-input.txt
python3 tests/artificial_supernova_events/test_generator.py
```

Integration artifacts for this implementation are in
`/home/wispedia/AA/isolated/grackle-compatibility/deterministic-sn-tests`.
The runtime test uses the full 128^3 isolated disk with AMR enabled, a short
three-event table (two simultaneous events), repeated runs, and a restart
after the first two events. Results are recorded in that directory.

The newchem executable compiled and linked successfully. On node01:

| Check | Result |
| --- | --- |
| Two independent 64-rank runs | Identical requested and actual event times and positions |
| 32 versus 64 MPI ranks | Identical event records |
| Two events at the same time | Both injected in file order at that time |
| Restart after two of three events | Only event 2 injected |
| Restart after all events | No additional events |
| Restart exactly at an event, with checkpoint time rounded downward | Consumed event retained; only the next event injected |
| Changed file on restart | Rejected with fingerprint diagnostic |
| Position outside domain | Rejected before evolution |

Across these successful runs, 48,603 saved floating-point datasets were
checked, including energies; none contained nonfinite values.
`verification.json` records the assertions and counts. The parser tests also
cover malformed rows, nonfinite numbers, negative/zero or descending times,
missing files, and empty files.

The checkpoint-rounding check uses the existing `PFLOAT_EPSILON` tolerance
only when checking the last consumed event against the saved time; it does
not skip unconsumed events or broaden their injection time.

The runtime tests stop at 0.01 Myr (0.011 for the exhausted-table check).
These test event delivery and restart behavior, not long-term evolution.
The final executable is `bin/enzo` in this worktree, built for newchem.
The old frozen Emerick executable used in the earlier comparison does not
implement this parameter: use rebuilt aeos-v2 executables for a comparison
with file-driven events.

A subsequent 5 Myr comparison rebuilt the Emerick profile and completed all
three cases (newchem standard dust, Emerick legacy dust, and Emerick standard
dust) with identical event times and positions. All checked saved fields were
finite. Artifacts and the comparison report are in
`/home/wispedia/AA/isolated/grackle-compatibility/deterministic-comparison`.
The main Grackle profile was not rerun with event files. These tests do not
validate all stellar physics; the later audit identified separate interpolation,
SNIa timing, and yield-data concerns that remain unfixed in this baseline.
