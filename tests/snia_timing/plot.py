#!/usr/bin/env python3
"""Plot model-2 event ages by enumerating all 65536 RNG outcomes."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--stellar-table", type=Path, required=True)
parser.add_argument("--metallicity", type=float, default=0.00054)
parser.add_argument("--birth-myr", type=float, default=83.)
parser.add_argument("--output", type=Path, default=root / "docs/figures")
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)


def extract(filename, signature):
    source = (root / "src/enzo" / filename).read_text()
    start = source.rindex(signature)
    opening = source.index("{", start)
    depth, end = 1, opening + 1
    while depth:
        depth += (source[end] == "{") - (source[end] == "}")
        end += 1
    return source[start:end]


prefix = r"""
#include <cmath>
#include <cstdio>
#include <cstdlib>
#define float double
#define POW pow
#define SUCCESS 1
#define FAIL 0
#define ISYM "d"
#define IMF_TABLE_ENTRIES 2000
#define ENZO_FAIL(...) abort()
#define ENZO_VFAIL(...) abort()
using unsigned_long_int=unsigned long;
int ComovingCoordinates=0;
double HubbleConstantNow=.701, IndividualStarSNIaFraction=.1508;
double *EventDTD;
unsigned_long_int draw=0;
unsigned_long_int mt_random() { return draw; }
"""
parts = [
    ("SearchUtilities.C", "int search_lower_bound(float *arr"),
    ("IndividualStarProperties.C",
     "float LinearInterpolationCoefficient(const int &i,\n"),
    ("IndividualStarProperties.C",
     "float Ruiter_SNIa_DTD(float time, const int model){"),
    ("StarParticleIndividual_IMFInitialize.C",
     "int InitializeDTD(float *& data){"),
    ("IndividualStarProperties.C", "int WDExplosionTime(float &WD_lifetime){"),
]
main = r"""
int main() {
  InitializeDTD(EventDTD);
  for (int i=0;i<IMF_TABLE_ENTRIES;i++)
    if (!std::isfinite(EventDTD[i]) ||
        (i && EventDTD[i]<EventDTD[i-1])) return 2;
  for (draw=0;draw<65536;draw++) {
    double delay;
    if (WDExplosionTime(delay)>0) std::printf("%.17g\n",delay);
  }
}
"""
with tempfile.TemporaryDirectory(prefix="aeos-dtd-plot-") as temp:
    temp = Path(temp)
    cpp = temp / "sample.cpp"
    cpp.write_text(prefix + "\n".join(extract(*p) for p in parts) + main)
    subprocess.run([os.environ.get("CXX", "c++"), "-std=c++11", "-O1",
                    str(cpp), "-o", str(temp / "sample")], check=True)
    result = subprocess.run([str(temp / "sample")], check=True,
                            capture_output=True, text=True)
    sampled_age = np.array([float(v) for v in result.stdout.split()]) / 1.e6

table = np.loadtxt(args.stellar_table)
year_s = 3.1556952e7
curves = [("No WD gate", sampled_age, "#222222", "-")]
summary = {
    "metallicity": args.metallicity, "birth_epoch_Myr": args.birth_myr,
    "normalization_parameter": .1508, "RNG_outcomes": 65536,
    "selected_event_fraction": len(sampled_age) / 65536,
    "stellar_table": str(args.stellar_table.resolve()), "masses": {},
    "assumptions": [
        "Time axis is age since original stellar birth.",
        "Instantaneous WD gate; timestep/injection scheduling is omitted.",
        "3 and 8 Msun cases assume WD formation; the exact 8 Msun routing "
        "boundary is unresolved.",
        "Old code adds the absolute birth epoch to the sampled age.",
        "Old mixed-unit floor is inactive for dtFixed=0.01 code units "
        "and TimeUnits=Myr_s.",
        "Finite bins display the probability atom at WD formation as a spike.",
    ],
}
for mass, color in [(3, "#2374ab"), (8, "#d55e00")]:
    rows = table[table[:, 0] == mass]
    wd = np.interp(args.metallicity, rows[:, 1], rows[:, 5]) / year_s / 1.e6
    fixed = np.maximum(wd, sampled_age)
    old = np.maximum(wd, sampled_age + args.birth_myr)
    curves.extend([
        (f"Fixed: {mass} M☉", fixed, color, "-"),
        (f"Old: {mass} M☉", old, color, "--"),
    ])
    summary["masses"][str(mass)] = {
        "WD_formation_age_Myr": float(wd),
        "fixed_probability_at_WD_formation": float(
            np.count_nonzero(sampled_age <= wd) / 65536),
        "old_probability_at_WD_formation": float(
            np.count_nonzero(sampled_age + args.birth_myr <= wd) / 65536),
        "fixed_probability_by_age_14Gyr": float(
            np.count_nonzero(fixed <= 14000) / 65536),
        "old_probability_by_age_14Gyr": float(
            np.count_nonzero(old <= 14000) / 65536),
    }

plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False})
fig, axes = plt.subplots(1, 2, figsize=(13, 5), layout="constrained")
for ax, edges, title in [
    (axes[0], np.arange(0., 710., 10.), "Early evolution · 10 Myr bins"),
    (axes[1], np.geomspace(1., 15000., 150), "Full delay range · logarithmic bins"),
]:
    columns = [edges[:-1], edges[1:]]
    for label, ages, color, style in curves:
        probability, _ = np.histogram(ages, bins=edges)
        rate = probability / 65536 / np.diff(edges)
        columns.append(rate)
        ax.stairs(rate, edges, label=label, color=color, linestyle=style,
                  linewidth=1.7, zorder=3 if style == "--" else 2)
    for mass, item in summary["masses"].items():
        ax.axvline(item["WD_formation_age_Myr"], color="#888888",
                   linewidth=.7, alpha=.5)
    ax.set(title=title, xlabel="Age since stellar birth [Myr]",
           ylabel="SNIa probability rate [Myr⁻¹ per eligible progenitor]")
    ax.set_yscale("log")
    ax.set_ylim(5.e-8, 4.e-3)
    ax.grid(alpha=.2, which="major")
    np.savetxt(args.output / ("snia-rate-early.csv" if ax is axes[0]
                             else "snia-rate-full.csv"),
               np.column_stack(columns), delimiter=",",
               header="age_left_Myr,age_right_Myr," +
               ",".join(label for label, *_ in curves), comments="")
axes[0].set_xlim(0, 700)
axes[1].set_xscale("log")
axes[1].set_xlim(1, 15000)
axes[0].legend(frameon=False, fontsize=9, loc="upper right")
axes[0].text(.03, .05, "Spikes at WD formation represent\n"
             "overdue events released at the WD stage.",
             transform=axes[0].transAxes, fontsize=9)
fig.suptitle("SNIa model 2: sampled DTD and WD-stage feedback\n"
             f"Z = {args.metallicity:g}; original birth epoch = "
             f"{args.birth_myr:g} Myr; input explosion fraction = 15.08%",
             fontsize=13)
for suffix in ["png", "pdf"]:
    fig.savefig(args.output / f"snia-timing-comparison.{suffix}", dpi=180)
(args.output / "snia-timing-summary.json").write_text(
    json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
