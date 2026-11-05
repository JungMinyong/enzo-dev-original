# SNIa duplicate-knot correction

The model-2 Ruiter rate table contained two identical rows at 2 Gyr.
An exact query could select the zero-width interval and return NaN.
The correction removes the redundant row from the time axis and each of
the five rate arrays. The remaining 45 knots retain their original values.

Interpolation remains linear in log10(rate) versus age in Gyr.
Extrapolation beyond 14 Gyr retains the previous final-segment slope.
The probability parameter, integration method, WD-stage timing, and
negative-age handling are unchanged.

## Endpoint fix reverted

At the user's request, the 14 Gyr endpoint correction was removed before
amending this commit. The original direct lookup is retained. An exact
14 Gyr query can still read beyond the arrays; its printed value can look
correct despite undefined behavior.

The configured `InitializeDTD` horizon is 14 Gyr, with a final query that
can round slightly below that value in floating-point arithmetic. An exact
14 Gyr query is still a valid table input. The full Valgrind suite retains
checks for the endpoint and CDF so this limitation remains visible.

## Validation

`tests/snia_rates/reference-knots.csv` preserves all 46 original rows,
including the duplicate. Tests verify that duplicate rows have identical
rates before deduplication and compare all five channels against the
original tabulated values.

Run the duplicate-knot and interior checks:

```sh
python3 tests/snia_rates/check.py --valgrind --case knots --case interiors
```

These cover 655 knot/adjacent queries and 660 interior queries.
The full suite also runs final-endpoint and CDF checks:

```sh
python3 tests/snia_rates/check.py --valgrind
```

The full suite is expected to fail memory diagnostics because the endpoint
fix was reverted. Add `--source-ref 00d1d82df` to reproduce the original
duplicate-knot failure. Tests compile the actual routines in double
precision, matching the configured Enzo build.

After the reversion, the knot and interior cases passed with zero Valgrind
errors. The endpoint case printed matching values but reported 22 memory
diagnostic errors; the full suite exited with status 1. The tested CDF
remained finite and normalized with no detected errors. The WD timing
regression also passed.
The configured Intel/newchem executable rebuilt successfully; ignored
dependency-generation errors were emitted by the build system.
