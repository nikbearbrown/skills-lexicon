"""Independent review of packets p046-p048; writes answers/p046.json .. p048.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CLAIMS = ["definition", "kind", "certification", "certification_scope", "language_type"]

# Per-entry overrides. Anything not listed: claim -> supports, variant -> ok,
# relation -> ok, vote -> yes.
#   notes:   {claim: (verdict, note)}
#   badvar:  {label: note}
#   badrel:  {"type:target": note}
#   vote:    (answer, reason)
R = {
    # ---------------- p046 ----------------
    "sql-server-analysis-services": {
        "badvar": {"SSAS": "also UK pensions 'Small Self-Administered Scheme', common in pension admin listings"},
    },
    "sql-server-express-localdb": {
        "vote": ("unsure", "niche developer runtime; rarely named on its own in listings"),
    },
    "stable-diffusion": {
        "notes": {"definition": ("supports", "developed with CompVis (LMU Munich) and Runway; released and funded by Stability AI")},
    },
    "standard-ambient-temperature-and-pressure": {
        "vote": ("no", "a chemistry reference condition, not a skill employers list"),
    },
    "standards-of-training-certification-and-watchkeeping": {
        "notes": {"certification": ("supports", "the convention itself is not a credential; STCW certificates issued under it are")},
    },
    "statement-on-auditing-standards-no-70": {
        "notes": {"definition": ("supports", "superseded by SSAE 16 for service-organisation reports in 2011")},
    },
    "statements-on-standards-for-attestation-engagements": {
        "notes": {"definition": ("supports", "strictly attestation standards (ASB), distinct from auditing standards (SASs)")},
    },
    # ---------------- p047 ----------------
    "stress-testing-computing": {
        "badvar": {"Stree Testing (Computing)": "misspelling of 'Stress'"},
    },
    "structure-chart": {
        "vote": ("unsure", "legacy structured-design diagram; rarely named in current listings"),
    },
    "stuttgart-neural-network-simulator": {
        "badvar": {"SNNS": "collides with 'SNNs', the usual plural for spiking neural networks"},
        "vote": ("no", "obsolete 1990s research simulator; not asked for in listings"),
    },
    "surface-properties-of-transition-metal-oxides": {
        "vote": ("unsure", "narrow research topic; appears only in academic research postings"),
    },
    "surgery": {
        "badvar": {"Surgeries": "plural means individual operations or (UK) GP practices, not the field"},
    },
    "surgical-incision": {
        "vote": ("unsure", "an act within surgery; rarely listed as a separate requirement"),
    },
    "sybase-unwired-platform": {
        "notes": {"definition": ("supports", "renamed SAP Mobile Platform after SAP bought Sybase; discontinued")},
    },
    # ---------------- p048 ----------------
    "syskey": {
        "vote": ("no", "removed Windows utility; not a hiring requirement"),
    },
    "system-data": {
        "vote": ("unsure", "listings name ADO.NET rather than the System.Data namespace"),
    },
    "table-data-gateway": {
        "vote": ("unsure", "a single PoEAA pattern; rarely named in listings"),
    },
    "table-etiquette": {
        "vote": ("unsure", "occasionally in butler or fine-dining roles; usually not a listed requirement"),
    },
    "tableau": {
        "badvar": {"Tableau (Busines Intelligence Software)": "misspelling 'Busines' for 'Business'"},
    },
    "tabular-data-stream": {
        "vote": ("unsure", "low-level wire protocol; seldom asked for outside database-driver work"),
    },
    "tape-recorder": {
        "vote": ("no", "obsolete consumer device; not a hiring requirement"),
    },
    "tax-deduction": {
        "vote": ("unsure", "a tax concept; listings ask for tax preparation rather than this term"),
    },
    "tax-shelter": {
        "notes": {"definition": ("supports", "some shelters are abusive or illegal schemes; legal ones fit this definition")},
        "vote": ("unsure", "a tax concept rather than a skill; occasionally in tax-planning roles"),
    },
    "technology-entrepreneurship": {
        "vote": ("unsure", "mostly an academic subject; seldom a listed job requirement"),
    },
    "telegraphy": {
        "vote": ("no", "largely obsolete; rarely asked for outside niche military radio roles"),
    },
    "theano": {
        "notes": {"definition": ("supports", "fork continued as Aesara/PyTensor")},
    },
}


def judge(entry):
    key = entry["key"]
    o = R.get(key, {})
    notes = o.get("notes", {})
    claims = {}
    for c in CLAIMS:
        if c in entry:
            verdict, note = notes.get(c, ("supports", None))
            d = {"verdict": verdict}
            if note:
                d["note"] = note
            claims[c] = d
    badvar = o.get("badvar", {})
    variants = {"ok": [], "bad": []}
    for v in entry.get("variants", []):
        if v in badvar:
            variants["bad"].append({"label": v, "note": badvar[v]})
        else:
            variants["ok"].append(v)
    badrel = o.get("badrel", {})
    relations = {"ok": [], "bad": []}
    for r in entry.get("relations", []):
        if r in badrel:
            relations["bad"].append({"rel": r, "note": badrel[r]})
        else:
            relations["ok"].append(r)
    for lab in badvar:
        assert lab in entry.get("variants", []), (key, lab)
    for r in badrel:
        assert r in entry.get("relations", []), (key, r)
    ans, reason = o.get("vote", ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason
    return {"key": key, "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": vote}


def main():
    seen = set()
    for p in ["p046", "p047", "p048"]:
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            pk = json.load(f)
        out = []
        for e in pk["entries"]:
            assert e["kind"] in pk["allowed_kinds"], e["key"]
            out.append(judge(e))
            seen.add(e["key"])
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {"supports": 0, "contradicts": 0, "unsure": 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        vok = vbad = 0
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
            vok += len(a["variants"]["ok"]) + len(a["relations"]["ok"])
            vbad += len(a["variants"]["bad"]) + len(a["relations"]["bad"])
        print(p, len(out), cnt, votes, "var/rel ok", vok, "bad", vbad)
    missing = set(R) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
