# Stellar-property and yield interpolation boundary fixes

An exact upper-axis knot previously produced the last element index, even
though interpolation then accessed both that element and the next one.
The next element is outside the allocation. The generic stellar-property
lookup and the separate yield-position lookup both had this defect.

The corrected lookup selects the final valid interval at an exact maximum.
Its interpolation weight is one, reproducing the final tabulated value.
This applies independently to mass, metallicity, and other axes that use
the shared stellar interpolation overloads. The generic element-search
routine is unchanged because its other callers may need an element index.
Interior lookup and existing out-of-range policies are retained.

Generic linear interpolation explicitly rejects axes shorter than two
points. Yield-position lookup requires at least two masses and one
metallicity. A one-metallicity PopIII table returns `j=0`; its mass-only
consumer ignores that metallicity position. This does not add singleton
metallicity support to the separate bilinear yield evaluator.

Exact endpoint values are valid simulation inputs. They can result from
tabulated masses, prescribed inputs, or values clamped to a table boundary.
Continuously sampled masses might hit an exact upper endpoint infrequently,
but no measurement established that these queries never occur in galaxy
runs. These fixes address reproducible memory errors, not a measured bias
in the fiducial simulation.

## Validation

On 2026-11-06:

- Synthetic minimum, interior, exact maximum, just-inside and out-of-range
  queries passed, including two-point axes and 2D/3D upper corners.
- Every knot of both actual PARSEC axes and the mass/metallicity combinations
  of all five groups in `IndividualStarYields-Mix0.1.h5` passed.
- Single-metallicity PopIII lookup, explicit mass extrapolation, metallicity
  flooring, empty axes, and invalid singleton mass axes passed.
- Both test suites reported zero errors under Valgrind.
- The same regression failed against pre-fix revision `fad01fb91` for both
  stellar and yield lookup.
- The configured Intel/newchem Enzo executable rebuilt and linked.
  The build emitted ignored dependency-generation errors.

Reproduce:

```sh
python3 tests/interpolation/check.py --valgrind \
  --stellar-table /path/to/parsec_zams.in \
  --yield-table /path/to/IndividualStarYields-Mix0.1.h5
```

Without table arguments, synthetic tests still run. `--source-ref fad01fb91`
checks the pre-fix routines and is expected to fail. The harness extracts the
actual functions and compiles them with double precision matching this Enzo
configuration; it does not execute a complete stellar lifecycle or galaxy.

The Ruiter rate function bypasses this interval selector. Its duplicate
2 Gyr knots are addressed in the separate
[SNIa rate-table correction](snia-rate-interpolation.md); its direct
upper-index lookup remains unchanged. Historical reports describe the
pre-fix implementation.
