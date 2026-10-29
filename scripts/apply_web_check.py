"""Record a web check of credentials as evidence and `credential` blocks on the entries it names.

    python3 -I scripts/apply_web_check.py data/web-checks/2026-10-29-web-check-1.json --run 2026-10-29-web-check-1 \
        --model-id claude-sonnet-5-5 --effort xhigh --agent subagent

The findings file has one object per credential (see the agent brief that produced it). For each one that matches an
entry by name this adds:
  - `matched_source` evidence on `certification`, naming the organization and linking to it, with the verification
    level the check actually had. A check that saw only search results says `search-results-only`, which is recorded
    but does not back the claim;
  - `checked` evidence by the model on `definition` when the check supports or contradicts it, and on `certification`
    when the check found it is not a credential at all;
  - a `credential` block (issuer, field, level, requirements, jurisdiction, sources) in the shape of
    schemas/certification.schema.json.
Nothing already on an entry is overwritten. Findings with no matching entry are left in the file.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import lexicon as L  # noqa: E402

WIKIMEDIA = {"name": "Wikimedia Foundation", "url": "https://www.wikimedia.org/", "type": "reference-work", "country": "US"}
COUNTRY = {"united states": "US", "united kingdom": "GB", "canada": "CA", "international": "INT", "global": "INT"}
SPECIFICITY = {"IAM Level I certification": "requirement-level", "Master's certificate in project management": "generic-programme"}
LEVELS = {"IAM Level I certification": {"label": "Level I", "scheme": "dod-8570-iam", "rank": 1, "of": 3}}
STATUS = {"CompTIA Mobility+": ("retired", "Retired on 15 December 2017; existing holders keep it for life, per CompTIA's partner page."),
          "American Board of Medical Laboratory Immunology certification": ("closed-to-new-candidates", "The exam is closed to new candidates, per the check's search results."),
          "IAM Level I certification": ("being-replaced", "DoD 8570 is being replaced by DoD 8140.")}


def root(url):
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}/"


def country(text):
    t = (text or "").lower()
    for k, v in COUNTRY.items():
        if t.startswith(k) or f" {k}" in t[:40]:
            return v
    return "US" if re.match(r"(us|u\.s\.)\b", t) else None


def jurisdiction(text):
    t = (text or "").lower()
    out = []
    for k, v in (("united states", "US"), ("united kingdom", "GB"), ("canada", "CA"), ("international", "INT")):
        if k in t and v not in out:
            out.append(v)
    if re.search(r"\b(us|u\.s\.)\b", t) and "US" not in out:
        out.append("US")
    return out


def wiki_title(url):
    return re.sub(r"_", " ", urlparse(url).path.rsplit("/", 1)[-1])


def org_of(f):
    iss = f.get("issuer") or {}
    o = {"name": iss.get("name"), "url": root(f["official_url"])}
    if iss.get("type") in ("professional-body", "vendor", "government", "university-or-college", "industry-association", "nonprofit", "other"):
        o["type"] = iss["type"]
    if country(iss.get("country")):
        o["country"] = country(iss["country"])
    return o


def sources(f):
    seen, out = set(), []
    def add(kind, url, title=None, snippet=None):
        if url and url not in seen and url.startswith("http"):
            seen.add(url)
            s = {"kind": kind, "url": url, "verification": "search-results-only"}
            if title:
                s["title"] = title
            if snippet:
                s["snippet"] = snippet[:200]
            out.append(s)
    add("issuer", f.get("official_url"), None, f.get("supporting_snippet"))
    add("wikipedia", f.get("wikipedia_url"))
    for o in f.get("other_sources") or []:
        add(o.get("kind") if o.get("kind") in ("issuer", "wikipedia", "wikidata", "third-party") else "third-party", o.get("url"), o.get("title"))
    return out


def credential(e, f):
    srcs = sources(f)
    if not srcs:
        return None
    c = {"credential_type": f["credential_type"], "sources": srcs}
    for k in ("official_name", "acronym", "requirements"):
        if f.get(k):
            c[k] = f[k]
    if f.get("level"):
        c["level"] = LEVELS.get(e["preferred_name"]) or {"label": f["level"]}
    c["specificity"] = SPECIFICITY.get(e["preferred_name"], "specific-credential")
    if e["preferred_name"] in STATUS:
        c["status"], c["status_note"] = STATUS[e["preferred_name"]]
    if f.get("field"):
        c["fields"] = [{"label": x} for x in f["field"]]
    j = jurisdiction(f.get("jurisdiction"))
    if j:
        c["jurisdiction"] = j
    iss = f.get("issuer") or {}
    if e.get("certification_scope") == "single-issuer" and iss.get("name"):
        c["issuers"] = [{k: v for k, v in {"name": iss["name"], "type": iss.get("type"), "country": country(iss.get("country")),
                                           "url": root(f["official_url"]) if f.get("official_url") else None}.items() if v}]
    elif e.get("certification_scope") == "many-issuers":
        c["issuers"] = [org_of(f) | {"url": root(f["official_url"])}] if f.get("official_url") and iss.get("name") else []
    if f.get("wikipedia_url"):
        c["wikipedia"] = {"title": wiki_title(f["wikipedia_url"]), "url": f["wikipedia_url"], "match": "manual"}
    return c


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("findings")
    ap.add_argument("--run", required=True)
    ap.add_argument("--model-id", required=True)
    ap.add_argument("--effort", required=True, choices=sorted(L.EFFORTS))
    ap.add_argument("--agent", default="subagent")
    ap.add_argument("--date", default="2026-10-29")
    ap.add_argument("--root", default=str(L.ROOT))
    a = ap.parse_args(argv)
    root_ = Path(a.root)
    findings = json.loads(Path(a.findings).read_text("utf-8"))
    entries, _ = L.load(root_ / "entries")
    by_name = {e["preferred_name"]: e for e in entries}
    model = f"model:{a.model_id}"
    done = 0
    for f in findings:
        e = by_name.get(f["input_name"])
        if not e or any(x.get("run") == a.run for x in e.get("evidence", [])):
            continue
        ev, notes = [], []
        if f.get("official_url") and (f.get("issuer") or {}).get("name"):
            o = org_of(f)
            ev.append({"field": "certification", "by": f"source:{o['name']}", "action": "matched_source", "kind": "issuer",
                       "verification": "search-results-only", "outcome": "supports", "ref": f["official_url"], "date": a.date, "run": a.run,
                       "note": ((f"verdict {f['verdict']}: " if f["verdict"] != "real" else "") + (f.get("supporting_snippet") or ""))[:200],
                       "organization": o})
        if f.get("wikipedia_url"):
            ev.append({"field": "certification", "by": "source:Wikipedia", "action": "matched_source", "kind": "wikipedia",
                       "verification": "search-results-only", "outcome": "supports", "ref": f["wikipedia_url"], "date": a.date, "run": a.run,
                       "note": "Wikipedia has an article about it", "organization": WIKIMEDIA})
        chk = (f.get("draft_definition_check") or {})
        if chk.get("result") in ("supports", "contradicts"):
            ev.append({"field": "definition", "by": model, "action": "checked", "outcome": chk["result"], "date": a.date, "run": a.run,
                       "note": ("web check, search results only: " + (chk.get("note") or ""))[:200]})
        elif chk.get("result") == "partly":
            notes.append("Web check (search results only) says the definition is only partly right: " + (chk.get("note") or ""))
        if f.get("credential_type") == "other" and e.get("certification") is True:
            ev.append({"field": "certification", "by": model, "action": "checked", "outcome": "contradicts", "date": a.date, "run": a.run,
                       "note": ("web check: not a credential a body awards; " + (chk.get("note") or ""))[:200]})
        c = credential(e, f)
        if c:
            e["credential"] = c
        e.setdefault("evidence", []).extend(ev)
        if notes:
            e["notes"] = (e.get("notes", "") + " " + " ".join(notes)).strip()
        (root_ / "entries" / e["_file"]).write_text(json.dumps({k: v for k, v in e.items() if not k.startswith("_")}, indent=1, ensure_ascii=False) + "\n", "utf-8")
        done += 1
    L.register_run(root_, a.run, a.model_id, a.effort, a.agent, date=a.date, note="web search only; no page was opened")
    print(f"updated {done} entries from {len(findings)} findings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
