"""Turn unknown candidate terms into request files any language model can answer.

    python3 -I tools/make_requests.py work --min-postings 3 [--limit 50]

Reads work/candidates.json, writes work/requests/<slug>.json. Each request is self-contained: the
instructions (from skills/draft-entry/SKILL.md), the term, quotes, the nearest existing entries and
the allowed values. A model needs nothing else.
"""
import argparse
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lexicon as L  # noqa: E402

SKILL = L.ROOT / "skills" / "draft-entry" / "SKILL.md"


def instructions(path=SKILL):
    """The model-facing task: the section from '## The task' up to the agent-only section."""
    t = Path(path).read_text("utf-8")
    t = t.split("## The task", 1)[1]
    return "## The task" + t.split("## If you are an agent", 1)[0].rstrip() + "\n"


def nearest(term, quotes, entries, k=8):
    """Entries that are close in spelling, or that appear in the same quote as the term (AWS next to GCP).
    Shared stray words are not enough: an irrelevant neighbour invites a false relation."""
    blob = " ".join(q["quote"] for q in quotes)
    scored = []
    for e in entries:
        if e["status"] == "deprecated":
            continue
        names = [e["preferred_name"]] + [v["label"] for v in e.get("variants", [])]
        sim = max(difflib.SequenceMatcher(None, L.norm(term), L.norm(n)).ratio() for n in names)
        cooc = any(re.search(r"(?<![\w])" + re.escape(n) + r"(?![\w])", blob, 0 if len(n) <= 3 else re.I) for n in names)
        score = sim + (0.6 if cooc else 0)
        if score >= 0.6:
            scored.append((score, e))
    scored.sort(key=lambda x: -x[0])
    return [{"id": e["id"], "name": e["preferred_name"], "kind": e["kind"], "definition": e["definition"],
             "variants": [v["label"] for v in e.get("variants", [])]} for s, e in scored[:k]]


def slug(term):
    base = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-") or "term"
    return f"{base[:40]}-{hashlib.sha1(term.encode()).hexdigest()[:6]}"


def make(cands, entries, min_postings=3, limit=None, text=None):
    text = text or instructions()
    kinds = sorted(L.KINDS)
    out = {}
    for c in cands:
        if c["n_postings"] < min_postings:
            continue
        if limit and len(out) >= limit:
            break
        req = {
            "task": "skills-lexicon draft-entry", "version": 1, "instructions": text,
            "term": c["term"], "n_postings": c["n_postings"], "quotes": c["quotes"],
            "nearest": nearest(c["term"], c["quotes"], entries),
            "allowed": {"kinds": kinds, "relation_types": sorted(L.REL_TYPES), "basis": ["posting", "general-knowledge", "guess"]}}
        if c.get("origin"):
            # A term from a list rather than a posting: say so, so nothing is claimed as seen in an ad.
            req["origin"] = c["origin"]
            lists = c["origin"].get("in_lists") or []
            req["context"] = ("This term comes from a legacy tag list, not from a posting. There are no quotes, "
                              "so no claim can have basis 'posting'. Use 'general-knowledge' only for what you know, "
                              "and answer 'unsure' if you do not know what the term is. "
                              + ("The legacy " + " and ".join(lists) + " list(s) include this tag. That is a hint from an "
                                 "unchecked list, not an answer: decide `certification` and `language_type` yourself, and if you "
                                 "disagree with a list, say so in `annotation_note`."
                                 if lists else
                                 "No legacy certification or language list includes this tag."))
        out[slug(c["term"]) + ".json"] = req
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("work")
    ap.add_argument("--min-postings", type=int, default=3)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--root", default=str(L.ROOT))
    a = ap.parse_args(argv)
    entries, _ = L.load(Path(a.root) / "entries")
    cands = json.loads((Path(a.work) / "candidates.json").read_text("utf-8"))
    reqs = make(cands, entries, a.min_postings, a.limit)
    d = Path(a.work) / "requests"
    d.mkdir(parents=True, exist_ok=True)
    for name, r in reqs.items():
        (d / name).write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", "utf-8")
    print(f"wrote {len(reqs)} requests to {d} ({len(cands) - len(reqs)} candidates below {a.min_postings} postings or over the limit)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
