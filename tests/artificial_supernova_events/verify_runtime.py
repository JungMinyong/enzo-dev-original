"""Validate event replay logs and saved fields in an integration-test directory."""
import argparse
import json
from pathlib import Path
import re

import h5py
import numpy as np

EVENT = re.compile(
    r"ArtificialSN: event=(\d+) time_Myr=(\S+) code_time=(\S+) "
    r"actual_code_time=(\S+) position=(\S+) (\S+) (\S+)")


def events(directory):
    rows = []
    for match in EVENT.finditer((directory / "run.log").read_text()):
        row = [int(match[1]), *map(float, match.groups()[1:])]
        assert row[2] == row[3], ("Event did not land at requested code time", row)
        rows.append(row)
    return rows


def scan(directory):
    count = 0
    bad = {}
    for path in sorted(directory.glob("DD*/DD*.cpu*")):
        if not h5py.is_hdf5(path):
            continue
        with h5py.File(path) as f:
            def check(name, obj):
                nonlocal count
                if isinstance(obj, h5py.Dataset) and obj.dtype.kind == "f":
                    count += 1
                    nbad = int(np.count_nonzero(~np.isfinite(obj[...])))
                    if nbad:
                        bad[str(path) + "/" + name] = nbad
            f.visititems(check)
    assert count > 0
    assert not bad, bad
    return {"floating_datasets": count, "nonfinite": bad}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", type=Path)
    a = p.parse_args()
    r = a.directory
    reference = events(r / "repeat-a")
    assert [x[0] for x in reference] == [0, 1, 2]
    requested = np.loadtxt(r / "events-short.txt")
    np.testing.assert_array_equal(
        np.array([[x[1], *x[4:]] for x in reference]), requested)
    assert reference[0][2] == reference[1][2]
    assert events(r / "repeat-b") == reference
    assert events(r / "restart") == reference[2:]
    assert "next=2;" in (r / "restart/run.log").read_text()
    assert "changed since the checkpoint" in (r / "changed-file/stderr.log").read_text()
    assert "outside the simulation domain" in (r / "invalid-file/stderr.log").read_text()
    names = ["repeat-a", "repeat-b", "restart"]
    if (r / "rank32/run.log").exists():
        assert events(r / "rank32") == reference
        names.append("rank32")
    if (r / "exhausted/run.log").exists():
        assert events(r / "exhausted") == []
        assert "next=3;" in (r / "exhausted/run.log").read_text()
        names.append("exhausted")
    if (r / "roundoff-finished.txt").exists():
        assert [x[0] for x in events(r / "at-event")] == [0]
        assert [x[0] for x in events(r / "at-event-restart")] == [1]
        assert "next=1;" in (r / "at-event-restart/run.log").read_text()
        names.extend(["at-event", "at-event-restart"])
    result = {"events": reference, "repeat_identical": True,
              "restart_only_remaining_event": True,
              "changed_file_rejected": True, "outside_domain_rejected": True,
              "same_events_32_and_64_ranks": "rank32" in names,
              "exhausted_restart_no_events": "exhausted" in names,
              "restart_at_rounded_event_time": "at-event-restart" in names,
              "fields": {name: scan(r / name) for name in names}}
    (r / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
