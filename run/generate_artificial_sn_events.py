#!/usr/bin/env python3
"""Sample a reusable artificial-SN event table for noncomoving Enzo runs."""
import argparse
import math
from pathlib import Path
import random


def generate(seed, duration_myr, rate_per_year, box_pc, radius_pc,
             half_height_pc, center, time_sampling="periodic", start_myr=0.0):
    values = [duration_myr, rate_per_year, box_pc, radius_pc, half_height_pc,
              start_myr, *center]
    if not all(math.isfinite(x) for x in values):
        raise ValueError("All numeric arguments must be finite.")
    if min(duration_myr, rate_per_year, box_pc) <= 0:
        raise ValueError("Duration, rate, and box size must be positive.")
    if min(radius_pc, half_height_pc, start_myr) < 0:
        raise ValueError("Radius, half-height, and start time must be nonnegative.")
    if time_sampling not in ("periodic", "poisson"):
        raise ValueError("Time sampling must be periodic or poisson.")
    # Positions are absolute code coordinates in a unit-cube domain.
    for c, extent in zip(center, [radius_pc, radius_pc, half_height_pc]):
        if c - extent / box_pc < 0 or c + extent / box_pc >= 1:
            raise ValueError("The sampling cylinder must fit inside [0,1)^3.")
    rng = random.Random(seed)
    interval = 1.0 / (rate_per_year * 1e6)
    if not math.isfinite(interval) or interval <= 0:
        raise ValueError("Rate is outside the representable range.")
    end = start_myr + duration_myr
    time = start_myr
    events = []
    while True:
        next_time = (start_myr + (len(events) + 1) * interval
                     if time_sampling == "periodic"
                     else time + rng.expovariate(rate_per_year * 1e6))
        if next_time > end:
            break
        if next_time <= time:
            raise ValueError("Time interval is too small to represent.")
        time = next_time
        theta = rng.uniform(0, 2 * math.pi)
        radius = radius_pc * math.sqrt(rng.random())
        z = rng.uniform(-half_height_pc, half_height_pc)
        events.append((time, center[0] + radius * math.cos(theta) / box_pc,
                       center[1] + radius * math.sin(theta) / box_pc,
                       center[2] + z / box_pc))
    if not events:
        raise ValueError("No events sampled; increase duration or rate.")
    return events


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("output", type=Path)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--duration-myr", type=float, default=5)
    p.add_argument("--start-myr", type=float, default=0,
                   help="Absolute start time; the first event occurs after this.")
    p.add_argument("--rate-per-year", type=float, default=4e-7)
    p.add_argument("--box-pc", type=float, default=59000)
    p.add_argument("--radius-pc", type=float, default=250)
    p.add_argument("--half-height-pc", type=float, default=100)
    p.add_argument("--center", type=float, nargs=3, default=(0.5, 0.5, 0.5))
    p.add_argument("--time-sampling", choices=("periodic", "poisson"),
                   default="periodic",
                   help="Periodic mimics constant-rate driving; poisson samples waiting times.")
    a = p.parse_args()
    try:
        events = generate(a.seed, a.duration_myr, a.rate_per_year, a.box_pc,
                          a.radius_pc, a.half_height_pc, a.center,
                          a.time_sampling, a.start_myr)
        with a.output.open("x") as f:
            f.write(f"# seed={a.seed} time_sampling={a.time_sampling} "
                    f"rate_per_year={a.rate_per_year:.17g}\n")
            f.write(f"# box_pc={a.box_pc:.17g} radius_pc={a.radius_pc:.17g} "
                    f"half_height_pc={a.half_height_pc:.17g}\n")
            f.write("# time_Myr x_code y_code z_code\n")
            for event in events:
                f.write(" ".join(f"{x:.17g}" for x in event) + "\n")
    except (ValueError, OSError) as error:
        p.error(str(error))
    print(f"Wrote {len(events)} events to {a.output}")


if __name__ == "__main__":
    main()
