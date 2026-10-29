"""Reviewer answers for packets p049-p051 (skills lexicon). Writes answers/p049.json, p050.json, p051.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

S = "supports"
C = "contradicts"
U = "unsure"

# Overrides per key. Anything not listed: claims supports, variants ok, relations ok, vote yes.
# claims: {claim: (verdict, note)}; vbad: {label: note}; rbad: {rel: note}; vote: (answer, reason)
OV = {
    # ---------------- p049 ----------------
    "thyroid-cancer": {"vote": (U, "A disease; listings name it as a patient population or specialty more than as a skill.")},
    "thyroid-diseases-and-disorders": {"vote": (U, "A disease group; listings mention it as clinical focus area rather than as a skill.")},
    "tibco-iprocess-suite": {"claims": {"definition": (S, "Originally Staffware Process Suite, acquired by TIBCO in 2004; legacy.")}},
    "tibco-spotfire": {"claims": {"definition": (C, "Spotfire did not originate at TIBCO: built by Spotfire AB (Sweden), acquired by TIBCO in 2007.")}},
    "time-protocol": {"claims": {"definition": (S, "Obsolete; superseded by NTP.")},
                      "vote": ("no", "Obsolete protocol (RFC 868), essentially never named in job listings.")},
    "tinydb": {"vote": ("no", "Small hobby-scale Python library; practically never asked for in job listings.")},
    "tokudb": {"claims": {"definition": (S, "Deprecated by Percona; removed from Percona Server 8.0.28.")},
               "vote": (U, "Discontinued storage engine; only rare legacy DBA listings mention it.")},
    "torch-machine-learning": {"claims": {"definition": (S, "Development stopped around 2018.")},
                               "vote": (U, "Lua Torch is discontinued; 'Torch' in listings usually means PyTorch.")},
    "trace-linear-algebra": {"vote": ("no", "A single mathematical concept, not something listings ask for as a skill.")},
    "traffic-alert-and-collision-avoidance-system": {
        "vbad": {"Traffic Collusion Avoidance System": "Misspelling of 'Collision'."}},
    "trans-proteomic-pipeline": {"vote": (U, "Niche proteomics software; occasionally named in bioinformatics listings.")},
    "treemap": {"claims": {"kind": (S, "A chart type; method is acceptable.")},
                "vote": ("no", "A single chart type; listings ask for data visualization, not treemaps.")},
    "trendline": {"vote": ("no", "A chart element; not asked for as such in job listings.")},
    # ---------------- p050 ----------------
    "ubersuggest": {"claims": {"definition": (S, "Owned by Neil Patel.")}},
    "uglifyjs": {"vote": (U, "Build-tool detail; rarely named in listings.")},
    "uikit-web-framework": {"vote": (U, "Niche front-end framework; rarely named in listings.")},
    "unisys-mapper": {"claims": {"definition": (S, "Originally Sperry Univac; later Unisys Business Information Server (BIS).")},
                      "vbad": {"MAintain Prepare SandsProduce Executive Reports (MAPPER)": "Garbled spelling ('SandsProduce')."},
                      "vote": (U, "Legacy mainframe tool; only occasional Unisys shop listings.")},
    "urological-disorders": {"vote": (U, "A disease group; listings mention urology as a specialty more than this as a skill.")},
    "usabilityhub": {"claims": {"definition": (S, "Renamed Lyssna in 2023.")},
                     "vote": (U, "Niche research tool, now renamed Lyssna; seldom named in listings.")},
    "utility-frequency": {"vote": ("no", "A physical property of power grids, not a skill listings ask for.")},
    "vax-4000": {"vote": ("no", "Obsolete DEC hardware; not asked for in current listings.")},
    "vax-8000": {"claims": {"definition": (S, "Range spanned mid-range (8200) to high-end (8800) models.")},
                 "vote": ("no", "Obsolete DEC hardware; not asked for in current listings.")},
    "vaxeln": {"vote": ("no", "Obsolete DEC real-time OS; not asked for in current listings.")},
    "vectorwise": {"vote": (U, "Niche analytic DBMS; rarely named in listings.")},
    # ---------------- p051 ----------------
    "video-js": {"vote": (U, "Specific player library; occasionally named in front-end listings.")},
    "visicalc": {"vote": ("no", "Discontinued 1980s software; not asked for in listings.")},
    "vissim": {"claims": {"definition": (S, "Now Altair Embed; not to be confused with PTV Vissim traffic simulation.")},
               "vote": (U, "Rare; listings saying 'Vissim' usually mean PTV Vissim traffic software.")},
    "vmware-aria-automation": {"claims": {"definition": (S, "Renamed VCF Automation by Broadcom in VCF 9.")}},
    "vmware-aria-operations": {"claims": {"definition": (S, "Renamed VCF Operations by Broadcom in VCF 9.")}},
    "vpython": {"vote": ("no", "Teaching tool for physics; practically never asked for in job listings.")},
}


def build(entry):
    key = entry["key"]
    ov = OV.get(key, {})
    claims = {}
    for c in ("definition", "kind", "certification", "certification_scope", "language_type"):
        if c in entry:
            v, note = ov.get("claims", {}).get(c, (S, None))
            obj = {"verdict": v}
            if note:
                obj["note"] = note
            claims[c] = obj
    out = {"key": key, "claims": claims}
    vbad = ov.get("vbad", {})
    variants = entry.get("variants", [])
    if variants:
        for lab in vbad:
            assert lab in variants, (key, lab)
        out["variants"] = {
            "ok": [v for v in variants if v not in vbad],
            "bad": [{"label": v, "note": vbad[v]} for v in variants if v in vbad],
        }
    rbad = ov.get("rbad", {})
    rels = entry.get("relations", [])
    if rels:
        out["relations"] = {
            "ok": [r for r in rels if r not in rbad],
            "bad": [{"rel": r, "note": rbad[r]} for r in rels if r in rbad],
        }
    ans, reason = ov.get("vote", ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason
    out["job_listing_vote"] = vote
    return out


def main():
    seen = set()
    for p in ("p049", "p050", "p051"):
        with open(os.path.join(HERE, "packets", p + ".json")) as f:
            pk = json.load(f)
        res = [build(e) for e in pk["entries"]]
        seen.update(e["key"] for e in pk["entries"])
        with open(os.path.join(HERE, "answers", p + ".json"), "w") as f:
            json.dump(res, f, indent=1, ensure_ascii=False)
        cnt = {S: 0, C: 0, U: 0}
        vc = {"yes": 0, "no": 0, U: 0}
        for r in res:
            for c in r["claims"].values():
                cnt[c["verdict"]] += 1
            vc[r["job_listing_vote"]["answer"]] += 1
        print(p, len(res), cnt, vc)
    missing = set(OV) - seen
    assert not missing, missing


if __name__ == "__main__":
    main()
