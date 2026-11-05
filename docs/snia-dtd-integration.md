# SNIa cumulative-probability initialization

`InitializeDTD` tabulates total SNIa delays from 1 Myr to 14 Gyr.
Previously, the first integration panel started at zero even though its
left-hand rate was evaluated at 1 Myr. The first cumulative entry was also
initialized with a rate rather than an integrated probability.

The correction starts the previous integration time at 1 Myr and sets the
first cumulative entry to zero. Subsequent Simpson panels integrate the
rate between successive tabulated ages. The final cumulative distribution
is still normalized to `IndividualStarSNIaFraction` (0.1508 in our setup).

This defines the input distribution on the existing 1 Myr–14 Gyr support;
it assigns no continuous probability below 1 Myr. The sampled time grid,
sampling algorithm, WD-stage gate, channel rates, and existing 14 Gyr
endpoint lookup are unchanged.

## Validation

The rate regression now checks the CDF against an independent analytic
integral of the original piecewise log-linear total rate, using
`tests/snia_rates/reference-knots.csv`. The reference integrates each
exponential rate segment exactly and normalizes over 1 Myr–14 Gyr; it does
not repeat the production Simpson integration.

On 2026-11-06:

- CDF entry zero is exactly zero.
- The first nonzero CDF entry is 1.3215553502e-7, replacing about 2.76956e-5.
- Maximum absolute CDF discrepancy from the independent reference is
  7.30119e-8 over all 2000 entries.
- The CDF is finite, nonnegative, monotonic, and ends at 0.1508.
- CDF, knot, and interior tests reported zero Valgrind errors.
- The pre-fix revision `3ac9f686e` fails the zero-initial-CDF regression.
- The controlled WD feedback timing regression passed.
- The configured Intel/newchem executable rebuilt and linked successfully.
  The build emitted ignored dependency-generation errors.

Reproduce:

```sh
python3 tests/snia_rates/check.py --valgrind \
  --case cdf --case knots --case interiors
python3 tests/snia_timing/check.py
```

The full rate suite still includes the known unsafe exact-14-Gyr endpoint
test and is expected to fail its memory diagnostics. That earlier fix was
reverted at the user's request and is not restored here. A finite CDF in
these checks does not establish that endpoint safety.

Previously saved WD delays are not resampled by this correction. Earlier
committed rate plots used the previous CDF initialization; regenerating
them with the current plotting script uses the corrected distribution.
