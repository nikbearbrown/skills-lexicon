"""Find known skills in postings, and list terms the dictionary does not know yet. No model involved.

    python3 -I tools/extract.py postings.jsonl --out work

postings.jsonl: one JSON object per line with `id`, `title`, `text`.
Writes work/records.jsonl (one structured record per posting) and work/candidates.json
(unknown terms, most widely seen first, each with short quotes). Matching is by rules, so the
numbers are only as good as the dictionary and the rules; the report says how much was matched.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lexicon as L  # noqa: E402

QUOTE_MAX = 200
CUE = re.compile(r"(?:experience (?:with|in|using)|proficien\w+ (?:in|with)|knowledge of|familiarity with|"
                 r"skilled in|expertise in|such as|including|e\.g\.|i\.e\.)\s*:?\s*([^.;\n]{3,200})", re.I)
TECH = re.compile(r"(?<![\w.])(?:[A-Z][a-z]+(?:[A-Z][a-z0-9]+)+|[A-Z][a-z]+[A-Z]{2,}[a-z]*|[A-Z][A-Z0-9]{1,5}|"
                  r"[A-Za-z][A-Za-z0-9]*(?:\+\+|#|\.js|\.NET)|[A-Za-z]{2,}/[A-Za-z]{2,})(?![\w])")
CAPS_STOP = {"US", "USA", "UK", "EU", "EEO", "EOE", "AM", "PM", "CEO", "CTO", "CFO", "VP", "HR", "PTO", "ID", "OK",
             "II", "III", "IV", "NYC", "LLC", "INC", "FAQ", "FTE", "PDF", "ASAP", "TBD", "ETC", "AND", "THE", "FOR",
             "WITH", "YOU", "OUR", "WE", "ALL", "NOT", "MAY", "CAN", "NEW"}
PLAIN = re.compile(r"(?<![\w.])[A-Z][a-z]{2,}(?![\w])")     # Kubernetes, Terraform: capitalised, not at a sentence start
TRAIL = re.compile(r"\s+(?:(?:is|are|will be|would be)\b.*|\(?(?:a plus|preferred|required|desired|nice to have)\)?)$", re.I)
ITEM_STOP = {"a", "an", "the", "our", "your", "their", "any", "all", "other", "others", "similar", "related", "strong",
             "deep", "solid", "good", "great", "excellent", "or", "and", "etc", "etc.", "more", "one", "two"}


def sentence(text, start, end):
    a = max(text.rfind(".", 0, start), text.rfind("\n", 0, start)) + 1
    b = [i for i in (text.find(".", end), text.find("\n", end)) if i != -1]
    s = text[a:min(b) if b else len(text)].strip()
    return s if len(s) <= QUOTE_MAX else s[:QUOTE_MAX - 1].rstrip() + "…"


def compile_forms(index):
    """One regex per surface form: boundaries by lookaround so C#, C++ and Node.js work."""
    out = []
    for key, cands in index["variants"].items():
        for c in cands:
            lab = re.escape(c["label"]) + (r"(?:s|es)?" if c["match"] == "word_ci" and c["label"][-1:].isalpha() else "")
            flags = 0 if c["match"] == "exact_case" else re.I
            out.append((c, re.compile(r"(?<![\w])" + lab + r"(?![\w])", flags)))
    return out


def context_ok(tags, text_lower):
    """needs_context is satisfied when ANY listed tag appears as a word in the posting."""
    return not tags or any(re.search(r"(?<![\w])" + re.escape(t.lower()) + r"(?![\w])", text_lower) for t in tags)


def known_spans(text, forms):
    low, hits = text.lower(), []
    for c, rx in forms:
        for m in rx.finditer(text):
            if context_ok(c["needs_context"], low):
                hits.append((m.start(), m.end(), c))
    # prefer the longest span; drop anything that overlaps one already kept
    kept = []
    for h in sorted(hits, key=lambda h: (-(h[1] - h[0]), h[0])):
        if not any(h[0] < k[1] and k[0] < h[1] for k in kept):
            kept.append(h)
    return sorted(kept)


def candidate_terms(text):
    """Terms that look like skills: tech-shaped tokens, plus items in lists after cues like 'experience with'."""
    found = {}
    for m in TECH.finditer(text):
        t = m.group(0)
        if t.upper() in CAPS_STOP and t == t.upper():
            continue
        found.setdefault(t, (m.start(), m.end()))
    for m in PLAIN.finditer(text):
        before = text[:m.start()].rstrip(" \t-–•*")
        if before and before[-1] not in ".!?:\n" and m.group(0) not in found:
            found[m.group(0)] = (m.start(), m.end())
    for cm in CUE.finditer(text):
        base = cm.start(1)
        for part in re.finditer(r"[^,;]+", cm.group(1)):
            for piece in re.split(r"\s+(?:and|or)\s+", part.group(0)):
                item = TRAIL.sub("", piece.strip(" \t-–•:()\"'")).strip()
                words = item.split()
                if not (1 <= len(words) <= 4) or words[0].lower() in ITEM_STOP or len(item) < 2:
                    continue
                at = text.find(item, base)
                found.setdefault(item, (at, at + len(item)) if at != -1 else (base, base))
    return found


def load_decisions(root):
    p = Path(root) / "data" / "term-decisions.json"
    return {L.norm(d["term"]): d for d in json.loads(p.read_text("utf-8"))} if p.exists() else {}


def process(postings, entries, decisions=None):
    index = L.build_index(entries)
    forms = compile_forms(index)
    decisions = decisions or {}
    known_norms = set(index["variants"])
    records, cand = [], {}
    for p in postings:
        text = p.get("text") or ""
        spans = known_spans(text, forms)
        rec = {"id": p["id"], "title": p.get("title", ""), "skills": [], "rolled_up": [], "ambiguous": []}
        seen = set()
        for a, b, c in spans:
            if c["ambiguous"]:
                rec["ambiguous"].append({"form": text[a:b], "candidates": [x["id"] for x in index["variants"][L.norm(c["label"])]]})
            elif c["id"] not in seen:
                seen.add(c["id"])
                rec["skills"].append({"concept": c["id"], "form": text[a:b], "quote": sentence(text, a, b)})
        up = []
        for cid in seen:
            for t in L.rollup(entries, cid):
                if t not in up:
                    up.append(t)
        rec["rolled_up"] = sorted(up)
        for term, (a, b) in candidate_terms(text).items():
            n = L.norm(term)
            if n in known_norms or n in decisions or any(a < s[1] and s[0] < b for s in spans):
                continue
            d = cand.setdefault(n, {"term": term, "surface": Counter(), "postings": [], "quotes": []})
            d["surface"][term] += 1
            if p["id"] not in d["postings"]:
                d["postings"].append(p["id"])
                if len(d["quotes"]) < 3:
                    d["quotes"].append({"posting": p["id"], "quote": sentence(text, a, b)})
        rec["unknown"] = sorted({c["term"] for c in cand.values() if p["id"] in c["postings"]})
        records.append(rec)
    out = []
    for d in cand.values():
        d["term"] = d["surface"].most_common(1)[0][0]
        d["n_postings"] = len(d["postings"])
        del d["surface"]
        out.append(d)
    out.sort(key=lambda d: (-d["n_postings"], d["term"].lower()))
    return records, out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("postings")
    ap.add_argument("--out", default="work")
    ap.add_argument("--root", default=str(L.ROOT))
    a = ap.parse_args(argv)
    entries, errs = L.load(Path(a.root) / "entries")
    errs += L.validate(entries)
    if errs:
        print("dictionary does not validate; fix it first:\n" + "\n".join(errs[:10]))
        return 1
    postings = [json.loads(x) for x in Path(a.postings).read_text("utf-8").splitlines() if x.strip()]
    records, cands = process(postings, entries, load_decisions(a.root))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "records.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), "utf-8")
    (out / "candidates.json").write_text(json.dumps(cands, indent=1, ensure_ascii=False) + "\n", "utf-8")
    mentions = sum(len(r["skills"]) for r in records)
    unknown_mentions = sum(c["n_postings"] for c in cands)
    with_any = sum(1 for r in records if r["skills"])
    print(f"{len(records)} postings; {with_any} have at least one known skill")
    print(f"{mentions} known-skill mentions; {len(cands)} unknown candidate terms seen in {unknown_mentions} posting-term pairs")
    if mentions + unknown_mentions:
        print(f"rough coverage of recognised terms: {mentions / (mentions + unknown_mentions):.0%} (a rule-based estimate, not measured against hand labels)")
    amb = sum(len(r["ambiguous"]) for r in records)
    if amb:
        print(f"{amb} ambiguous mentions were not counted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
