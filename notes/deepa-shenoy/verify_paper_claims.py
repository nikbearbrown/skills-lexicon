"""Re-check every number in the Lexicon manuscript (v0.2) against a checkout.
Run from the repository root:  python3 -I notes/deepa-shenoy/verify_paper_claims.py
Read-only; standard library only (uses tools/lexicon.py for the backing rule)."""
import glob, json, sys
from collections import Counter
sys.path.insert(0, "tools")
import lexicon as L

es = [json.load(open(f)) for f in sorted(glob.glob("entries/*.json"))]
def check(label, got, expected):
    print(f"{'OK ' if got == expected else 'DIFF'} {label}: got {got}, paper says {expected}")

classes = Counter(L.top_class(e) for e in es)
check("canonical concepts", len(es), 3754)
for k, v in [("skill", 1988), ("knowledge", 550), ("ability", 67), ("language", 290), ("certification", 859)]:
    check(f"class {k}", classes.get(k, 0), v)
check("developed-skill kind", sum(e["kind"] == "skill" for e in es), 723)
st = Counter(e["status"] for e in es)
check("machine-drafted", st["machine-drafted"], 3555); check("proposed", st["proposed"], 199); check("reviewed", st["reviewed"], 0)

claims = backed = human = 0; by = Counter()
for e in es:
    keys = set(L.claim_keys(e)); claims += len(keys); done = set()
    for ev in e.get("evidence", []):
        f = ev.get("field")
        if f in keys and f not in done and L.backs(ev):
            done.add(f); by[(f.split(":")[0], ev.get("verification"))] += 1
            human += str(ev.get("by", "")).startswith("human:")
    backed += len(done)
check("assertion fields", claims, 17229); check("backed", backed, 1455)
check("backed %", round(100 * backed / claims, 2), 8.45); check("human-backed", human, 0)
print("     backed by field/verification:", dict(by))

pg = next(e for e in es if e["key"] == "postgresql")
print("     PostgreSQL variants:", pg["variants"], "relations:", pg["relations"])
rel = [r for e in es for r in e.get("relations", [])]
n_roll = sum(bool(r.get('rolls_up')) for r in rel)
print(f"     roll-up: {n_roll} relation(s) have rolls_up true (the schema key). "
      f"A count using the wrong key 'rollup' gives {sum(bool(r.get('rollup')) for r in rel)}.")
so = next(e for e in es if e["key"] == "service-orientation")
print("     Service orientation definition:", so["definition"])
print("     Service orientation description:", so["description"]["text"][:90], "...")
