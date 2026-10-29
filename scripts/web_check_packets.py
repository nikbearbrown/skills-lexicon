"""Split the certifications that have not been web-checked yet into input files for web-check agents.

    python3 -I scripts/web_check_packets.py OUTDIR --size 25

Writes OUTDIR/in/wNNN.json: a list of {name, also_written, kind, draft_definition} for entries whose class is certification
and that no web-check run has touched. An agent searches the web for each and writes OUTDIR/out/wNNN.json in the findings
shape that scripts/apply_web_check.py reads (see data/web-checks/ for an example); apply that file with a run label that
contains "web-check". Only search results are seen in a cloud session, so the evidence it records backs nothing.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import lexicon as L  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out")
    ap.add_argument("--size", type=int, default=25)
    ap.add_argument("--root", default=str(L.ROOT))
    a = ap.parse_args(argv)
    entries, _ = L.load(Path(a.root) / "entries")
    todo = [e for e in sorted(entries, key=lambda e: e["key"])
            if L.top_class(e) == "certification" and e.get("certification") is True
            and not any("web-check" in str(v.get("run", "")) for v in e.get("evidence", []))]
    d = Path(a.out)
    (d / "in").mkdir(parents=True, exist_ok=True)
    (d / "out").mkdir(exist_ok=True)
    n = 0
    for i in range(0, len(todo), a.size):
        n += 1
        items = [{"name": e["preferred_name"], "also_written": [v["label"] for v in e.get("variants", [])], "kind": e["kind"],
                  "draft_definition": e["definition"]} for e in todo[i:i + a.size]]
        (d / "in" / f"w{n:03d}.json").write_text(json.dumps(items, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print(f"{len(todo)} certifications to web-check in {n} files under {d / 'in'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
