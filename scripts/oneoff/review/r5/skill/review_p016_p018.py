"""Reviewer answers for packets p016-p018 (skills lexicon). Dumps answers/p016.json .. p018.json."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

# Per-entry overrides. Defaults: every claim "supports", every variant/relation ok, vote "yes".
# Fields: def=(verdict, note), kind=(verdict, note), cert=(verdict, note),
#         badvar={label: note}, badrel={rel: note}, vote=(answer, reason)
R = {
    # ---------------- p016 ----------------
    "field-programmable-gate-array": {"def": ("supports", "Designs are usually written in an HDL (or HLS) and loaded as a bitstream.")},
    "file-control-block": {
        "def": ("supports", "DOS/CP/M sense; OS textbooks also use FCB for the per-file metadata record (like a Unix inode)."),
        "vote": ("unsure", "Narrow OS-internals data structure; rarely named as a requirement in job listings."),
    },
    "finacle": {"def": ("supports", "Marketed as Infosys Finacle via EdgeVerve Systems, an Infosys subsidiary.")},
    "finance-software": {"badvar": {"Finance Softwares": "Non-standard plural 'softwares'; an error form, not a true variant."}},
    "fincen-314-program": {"kind": ("supports", "A regulatory programme (314(a)/314(b)); 'standard' is the nearest allowed kind.")},
    "flexisign": {"def": ("supports", "Scanvec Amiable is now SAi; product still sold as FlexiSIGN.")},
    "fluid-statics": {"vote": ("unsure", "Usually requested as fluid mechanics; standalone 'fluid statics' is rare in listings.")},
    "flux-analysis": {"def": ("supports", "Accounting sense; 'flux analysis' also names metabolic flux analysis in biology.")},
    "flux-cd": {"def": ("supports", "CNCF graduated project; original sponsor Weaveworks closed in 2024.")},
    "foglight": {"def": ("supports", "Today mainly sold as Foglight for Databases.")},
    "folk-music": {"vote": ("unsure", "A music genre; only occasionally sought for music teaching or performance roles.")},
    "food-economics": {"vote": ("unsure", "Academic field; seldom named in listings outside research or policy roles.")},
    # ---------------- p017 ----------------
    "food-systems-management": {"def": ("supports", "Dietetics/foodservice sense; 'food systems' can also mean the wider farm-to-fork system.")},
    "forced-draft-systems": {
        "def": ("supports", "Forced-draft fans are also used in cooling towers, not only boilers and furnaces."),
        "vote": ("unsure", "Narrow boiler concept; appears mainly in some boiler-operator or stationary-engineer listings."),
    },
    "foreign-account-tax-compliance-act": {"kind": ("supports", "A law; 'standard' is the nearest allowed kind.")},
    "forensic-dentistry": {"vote": ("unsure", "Niche specialty usually done by consulting dentists; rarely appears in job listings.")},
    "free-body-diagrams": {"vote": ("unsure", "Basic engineering-mechanics tool; seldom named in listings except tutoring roles.")},
    "free-lossless-audio-codec": {
        "def": ("supports", "Developed by the Xiph.Org Foundation."),
        "vote": ("unsure", "Audio file format; only occasionally named in audio or media engineering listings."),
    },
    "functional-independence-measure": {"def": ("supports", "Dropped from US IRF-PAI reporting in 2019 (replaced by Section GG items).")},
    "fuse-esb": {"def": ("supports", "Earlier sold as IONA FUSE ESB; later JBoss Fuse / Red Hat Fuse, itself now end-of-life.")},
    "gallio": {"vote": ("unsure", "Obsolete .NET test platform (inactive since about 2013); rare in listings.")},
    "gatsby": {"def": ("supports", "Acquired by Netlify in 2023; development has slowed since.")},
    # ---------------- p018 ----------------
    "general-finance": {
        "def": ("supports", "True but very broad."),
        "vote": ("unsure", "Vague umbrella phrase; listings usually name finance or a specific finance skill."),
    },
    "general-packet-radio-service": {"def": ("supports", "A 2.5G GSM service; its core network was reused by 3G UMTS.")},
    "generic-routing-encapsulation": {"def": ("supports", "First described in RFC 1701 (Cisco); RFC 2784 is the current base spec.")},
    "gold-panning": {"vote": ("no", "Recreational or tourist activity; essentially never asked for in job listings.")},
    "google": {"def": ("supports", "Correct for Google+; note the entry key 'google' could be confused with Google itself.")},
    "google-bard": {"vote": ("unsure", "Short-lived product name (2023-24); listings now ask for Gemini or generative AI tools.")},
    "google-jamboard": {
        "def": ("supports", "Jamboard was also a 55-inch whiteboard display; app shut down 31 Dec 2024."),
        "vote": ("unsure", "Retired product; occasionally named in older teaching listings."),
    },
    "google-optimize": {"def": ("supports", "Sunset on 30 September 2023.")},
    "google-workspace": {"def": ("supports", "Also called Google Apps before 2016.")},
    "gosystem-tax-rs": {"badvar": {"GoSystems (Tax Software)": "Misspelling; the product line is GoSystem (no s)."}},
    "graphical-evaluation-and-review-technique": {"vote": ("unsure", "Textbook project-network technique; rarely named in job listings.")},
}


def claim(v):
    out = {"verdict": v[0]}
    if v[1]:
        out["note"] = v[1]
    return out


def answer(entry):
    o = R.get(entry["key"], {})
    claims = {}
    if "definition" in entry:
        claims["definition"] = claim(o.get("def", ("supports", "")))
    if "kind" in entry:
        claims["kind"] = claim(o.get("kind", ("supports", "")))
    if "certification" in entry:
        claims["certification"] = claim(o.get("cert", ("supports", "")))
    for extra in ("certification_scope", "language_type"):
        if extra in entry:
            claims[extra] = claim(o.get(extra, ("unsure", "Not reviewed")))
    badvar = o.get("badvar", {})
    variants = {"ok": [v for v in entry.get("variants", []) if v not in badvar],
                "bad": [{"label": k, "note": n} for k, n in badvar.items() if k in entry.get("variants", [])]}
    badrel = o.get("badrel", {})
    relations = {"ok": [r for r in entry.get("relations", []) if r not in badrel],
                 "bad": [{"rel": k, "note": n} for k, n in badrel.items() if k in entry.get("relations", [])]}
    vote = o.get("vote", ("yes", ""))
    jv = {"answer": vote[0]}
    if vote[1]:
        jv["reason"] = vote[1]
    return {"key": entry["key"], "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": jv}


def main():
    used = set()
    for p in ("p016", "p017", "p018"):
        entries = json.load(open(os.path.join(BASE, "packets", p + ".json")))["entries"]
        res = [answer(e) for e in entries]
        used |= {e["key"] for e in entries}
        json.dump(res, open(os.path.join(BASE, "answers", p + ".json"), "w"), indent=1, ensure_ascii=False)
        from collections import Counter
        c = Counter(cl["verdict"] for r in res for cl in r["claims"].values())
        v = Counter(r["job_listing_vote"]["answer"] for r in res)
        vb = sum(len(r["variants"]["bad"]) for r in res)
        rb = sum(len(r["relations"]["bad"]) for r in res)
        print(p, len(res), dict(c), dict(v), "bad variants", vb, "bad rels", rb)
    missing = set(R) - used
    assert not missing, missing
    for r in R.values():
        for k in ("def", "kind", "cert", "vote"):
            if k in r and r[k][1]:
                assert len(r[k][1]) <= 150, r[k][1]


if __name__ == "__main__":
    main()
