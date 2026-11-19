# AEOS local FUV coupling to Grackle

With `IndividualStarFUVHeating=1` and Grackle enabled, Enzo now resolves
`use_isrf_field=1`, including inputs/restarts that previously specified zero.
The existing parameter writer records the resolved value. No Grackle changes
or new Enzo parameters are required.

This implementation supports `RadiativeTransferOpticallyThinFUV=1`, including
background, direct stellar sources and the source tree. AEOS stores their sum
in `FUVRate`, in code flux units. Both the chemistry wrapper and cooling-time
diagnostic convert it using

```
flux_cgs = FUVRate * DensityUnits * VelocityUnits^2 * LengthUnits / TimeUnits
G_Habing = flux_cgs / 1.59e-3 * PE_dust_attenuation
```

The attenuation function is shared with AEOS PE heating: PE model 0 applies
none; PE model 1 applies its existing local RR optical depth. The stored field
is unchanged, so attenuation is applied once to each consumer. Proper units
from `GetUnits` include cosmological expansion; no extra scale factor is added.
The existing radiation update precedes the coupled chemistry call. As before,
operator splitting can leave radiation inputs from the most recent radiation
update; this is not a new radiation transport solver.

The PE temperature cutoff does not erase the radiation field. Internal Grackle
PE must remain disabled (`PhotoelectricHeating=0`) and external volumetric
heating must be enabled (`use_volumetric_heating_rate=1`). Conflicting settings
fail at startup. Fully ray-traced FUV is explicitly rejected: its field storage
and attenuation must be handled separately, rather than attenuating it twice.
That check occurs in the RT parameter reader, where its transport flags are
first initialized.

Dust abundance prescriptions, normalizations and PE efficiency are unchanged.
The band-integrated AEOS field supplies Grackle's existing Habing convention;
Grackle's fixed spectral assumptions remain an approximation, particularly for
stellar spectra. This change also affects Grackle's dust temperature and hence
potentially gas–grain exchange/H2 formation, not only grain recombination.

Validation:

```
python3 tests/photoelectric_density/check.py
python3 tests/photoelectric_radiation/check.py
python3 tests/photoelectric_radiation/check_grackle.py GRACKLE_PREFIX CLOUDY_TABLE
```

The first radiation test compiles the production helper, PE formulas and
parameter checks in single/double precision. It covers zero/background/stellar
flux, linear/RR attenuation, atomic/molecular gas, unit transformations, source
addition and invalid configurations. The Grackle test compares scalar and
per-cell inputs through cooling-time and chemistry APIs, with a deliberately
wrong scalar value in field mode to verify that the field takes precedence.
It tests three code-unit systems. These tests do not replace an evolved galaxy
comparison or establish the adequacy of the spectral/attenuation assumptions.

The PE-counting-only comparison is preserved at commit `b439f0eff`, local
branch `aeos-v2-pe-counting-only`. Use identical inputs/Grackle for the planned
comparison; the newer revision resolves local ISRF automatically.
