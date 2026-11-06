# Aeos-v2 Grackle integration

Enzo aeos-v2 targets the main-based Grackle `aeos-v2` branch, including its
corrected Rémy-Ruyer dust prescription. There are no backend profiles or
capability macros. The old Emerick and newchem APIs are no longer supported.

## Build

Set `LOCAL_GRACKLE_INSTALL` to the matching Grackle installation in your
machine file or local `src/enzo/Make.config.override`. For a shared library
installed under `lib64`, the local override can contain:

```make
LOCAL_GRACKLE_INSTALL = /absolute/path/to/grackle-aeos-v2
LOCAL_LIBS_GRACKLE = -L$(LOCAL_GRACKLE_INSTALL)/lib64 -Wl,-rpath,$(LOCAL_GRACKLE_INSTALL)/lib64 -lgrackle
```

Then build from `src/enzo`:

```sh
make grackle-yes
make show-config
make -j8
```

Use matching headers and libraries from the same installation. The executable
logs Grackle's version, branch, revision, and dust selection. Unmodified main
may silently treat unknown positive dust modes as standard dust, so it is
not a replacement for the patched library when selecting mode 5.

A build fingerprint tracks compiler flags, includes, and library flags;
changing the installation path rebuilds objects. Clean rebuild if replacing
headers or libraries in place. Intel-compiled Enzo requires its own Fortran
runtime libraries independently of Grackle; the happiness2 machine file
provides `-lifcore -lifport`.

## Runtime physics choices

`dust_chemistry` is the single dust-model selector:

| Value | Meaning |
| --- | --- |
| 0 | No dust chemistry |
| 1 | Standard dust abundance proportional to metallicity |
| 5 | Corrected absolute Rémy-Ruyer broken-power-law abundance |

Other values, including historical mode 4, are rejected. An explicit dust
field takes precedence over inferred abundance. The dust prescription itself
is implemented in Grackle, not Enzo.

Omit `H2FormationOnDust` to let enabled dust chemistry activate H2 formation
when `MultiSpecies > 1`. Existing boolean uses remain supported. Legacy value
2 is accepted only with mode 5 and translated to a boolean; it cannot select
a dust prescription on its own. An explicit H2-off request conflicting with
enabled molecular dust chemistry is rejected. Resolved choices are written
to restart parameters.

The removed `GrackleDustAbundanceModel` parameter produces a migration error.
Replace old abundance choice 0 with `dust_chemistry=1` (or retain dust mode 0
if disabled), and old choice 1 with `dust_chemistry=5`. Old choice 2 selected
the historical normalization, which this integration no longer supports.

`LWbackground_model` defaults to 0 and accepts only 0. Analytic LW models 1/2
are unsupported, with no build option. Table-based LW, constant intensity,
and sawtooth controls remain available. Enzo's external photoelectric heating
is unchanged.

## Integration safeguards

- Parse `local_dust_to_gas_ratio` as a double.
- Initialize optional Grackle field pointers to zero and require a metal field
  when metal cooling is enabled.
- Read photon-timestep k1/k2 arrays directly from Grackle, checking that tables
  are initialized and have at least two bins.
- Retain corrected zero-based interpolation indices, including the upper
  endpoint; reverting these would restore out-of-bounds accesses.
- Stop if Grackle initialization fails.

## Validation

Compile the parameter fixture against the actual installation:

```sh
c++ -std=c++11 -DUSE_GRACKLE -Isrc/enzo -I"$GRACKLE_PREFIX/include" \
  tests/grackle_compatibility/parameters.cpp \
  -L"$GRACKLE_PREFIX/lib64" -Wl,-rpath,"$GRACKLE_PREFIX/lib64" \
  -lgrackle -o /tmp/aeos-grackle-check
python3 tests/grackle_compatibility/check.py /tmp/aeos-grackle-check
/tmp/aeos-grackle-check 5 1 0 /absolute/path/CloudyData_HM2012_highz_shielded.h5
```

Fixture arguments are `dust_chemistry`, `H2FormationOnDust`,
`LWbackground_model`, and an optional data-file path for actual library
initialization and rate-table checks. Grackle's separate single-cell tests
validate the dust abundance against independent explicit dust-density cells.
These checks do not establish full galaxy evolution equivalence. Production
input decks are not modified.
