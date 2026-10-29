"""Reviewer answers for packets p019-p021 (skills lexicon). Writes answers/p019.json .. p021.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CLAIM_FIELDS = ["definition", "kind", "certification", "certification_scope", "language_type"]

# Per-entry overrides. Anything not listed: claim = supports, variant = ok, relation = ok, vote = yes.
# claims: {field: (verdict, note)}; bad_variants: {label: note}; bad_rels: {rel: note}; vote: (answer, reason)
R = {}


def o(key, claims=None, bad_variants=None, bad_rels=None, vote=None):
    R[key] = dict(claims=claims or {}, bad_variants=bad_variants or {}, bad_rels=bad_rels or {}, vote=vote)


# ---------------- p019 ----------------
o("graphite", claims={"definition": ("supports", "Name also means the mineral and an unrelated code-review tool; definition fits the monitoring tool.")})
o("great-circle", vote=("unsure", "Geodesy/navigation concept; seldom named as a requirement outside marine or aviation navigation."))
o("groupme", vote=("unsure", "Consumer group-chat app; occasionally mentioned for team comms but rarely a stated requirement."))
o("hadron-physics", bad_variants={"Hadrons (Partical Physics)": "Misspelling ('Partical') and names the particles, not the field of study."})
o("hammer-file-system", claims={"definition": ("supports", "By Matthew Dillon; HAMMER2 has since replaced it as DragonFly's default.")},
  vote=("no", "Niche DragonFly BSD file system; essentially never named in job listings."))
o("hammer-js", vote=("unsure", "Small touch-gesture library; only occasionally listed among front-end libraries."))
o("handle-system", claims={"definition": ("contradicts", "Developed by CNRI, but the DONA Foundation has administered the Handle System since 2014.")},
  vote=("unsure", "Niche persistent-identifier infrastructure; appears mainly in digital-repository roles."))
o("hashistack", claims={"definition": ("supports", "HashiCorp is now owned by IBM (2025).")})
o("hcfa-regulations",
  bad_variants={"Health Care Finance Administration (HCFA) Regulations": "Wrong agency name: it was the Health Care Financing Administration."},
  vote=("unsure", "Agency renamed CMS in 2001; the term survives mainly in older or billing-form (HCFA-1500) listings."))
o("healthcare-delivery-science", vote=("unsure", "Niche academic field (e.g. Dartmouth); rarely named in listings."))

# ---------------- p020 ----------------
o("heritrix", vote=("yes", None))
o("hincii",
  claims={"definition": ("contradicts", "HincII (H. influenzae Rc) was never named HindII; HindII is a separate isoschizomer from H. influenzae Rd.")},
  bad_variants={"HindII": "A different enzyme (isoschizomer from H. influenzae Rd), not a former name of HincII."},
  vote=("no", "Individual restriction enzymes are not job requirements; listings ask for restriction digestion or cloning."))
o("hindiii", vote=("no", "Individual restriction enzymes are not job requirements; listings ask for restriction digestion or cloning."))
o("hindsight-bias", vote=("no", "A cognitive bias, not a skill or qualification that listings ask for."))
o("historical-linguistics",
  bad_rels={"related:applied-linguistics": "Distinct linguistics subfields sharing only a parent; no meaningful relation."})
o("hockett-s-design-features", vote=("no", "A narrow linguistics theory topic; not asked for in job listings."))
o("host-based-security-system", claims={"definition": ("supports", "Being replaced by DoD's Endpoint Security Solutions (Trellix).")})
o("hotjava", vote=("no", "Obsolete 1990s browser; not a job requirement."))
o("hp-2100", vote=("no", "Obsolete minicomputer line; not asked for in current listings."))
o("hp-9845c", vote=("no", "Obsolete 1980 desktop computer; not a job requirement."))
o("hp-application-lifecycle-management", claims={"definition": ("supports", "Later Micro Focus ALM, now OpenText ALM.")})
o("hp-brio", vote=("no", "Discontinued business PC line; owning a PC model is not a job skill."))
o("hp-jornada", vote=("no", "Discontinued handheld line; not a job requirement."))
o("hp-newwave", vote=("no", "Obsolete late-1980s desktop environment; not asked for in listings."))
o("hp-quality-center", claims={"definition": ("supports", "Later Micro Focus/OpenText ALM Quality Center.")})
o("hp-winrunner", claims={"definition": ("supports", "Discontinued around 2008 in favour of QuickTest Professional.")})

# ---------------- p021 ----------------
o("html5shiv", vote=("no", "Tiny legacy IE polyfill; not something listings ask for as a skill."))
o("human-machine-interface", bad_variants={"Human -Machine Interface": "Typo: stray space before the hyphen."})
o("hypercompact-stellar-systems",
  claims={"definition": ("supports", "Strictly, the black hole is kicked from the galaxy's nucleus; it need not leave the galaxy.")},
  vote=("no", "Specialised astrophysics research topic; not a job-listing skill."))
o("iad", vote=("no", "Apple ad network discontinued in 2016; no longer requested."))
o("ibeacon", claims={"kind": ("contradicts", "iBeacon is a BLE advertising protocol/specification; 'standard' fits, not 'platform'.")})
o("ibm-cl-supersession",
  claims={"definition": ("supports", "Originally Candle Corporation's product; IBM acquired Candle in 2004.")},
  vote=("unsure", "Niche mainframe session manager; seldom named in listings."))
o("ibm-eserver", vote=("unsure", "Umbrella brand; listings name the series (pSeries, iSeries, zSeries) rather than eServer."))
o("ibm-informix", claims={"definition": ("supports", "Since 2017 HCL develops it under partnership; IBM also still markets it.")})
o("ibm-officevision",
  claims={"definition": ("supports", "Also had AS/400 (OfficeVision/400) and OS/2 versions, not only mainframes.")},
  vote=("no", "Discontinued office suite; not requested in listings."))
for k in ("ibm-power10", "ibm-power7", "ibm-power9"):
    o(k, vote=("unsure", "Listings usually ask for IBM Power Systems/AIX, rarely a specific processor generation."))
o("ibm-qradar", claims={"definition": ("supports", "QRadar SaaS was sold to Palo Alto Networks in 2024.")})
o("ibm-tivoli-enterprise-console",
  bad_variants={"Trivoli Enterprise Console": "Misspelling of Tivoli."})
o("icmpv6", vote=("unsure", "Usually covered under IPv6 networking; seldom named on its own in listings."))


def review(packet):
    path = os.path.join(HERE, "packets", f"{packet}.json")
    with open(path) as f:
        data = json.load(f)
    out = []
    seen = set()
    for e in data["entries"]:
        key = e["key"]
        seen.add(key)
        ov = R.get(key, dict(claims={}, bad_variants={}, bad_rels={}, vote=None))
        claims = {}
        for fld in CLAIM_FIELDS:
            if fld in e:
                verdict, note = ov["claims"].get(fld, ("supports", None))
                c = {"verdict": verdict}
                if note:
                    assert len(note) <= 150, (key, fld, len(note))
                    c["note"] = note
                claims[fld] = c
        for fld in ov["claims"]:
            assert fld in e, (key, fld)
        variants = {"ok": [], "bad": []}
        for v in e.get("variants", []):
            if v in ov["bad_variants"]:
                n = ov["bad_variants"][v]
                assert len(n) <= 150
                variants["bad"].append({"label": v, "note": n})
            else:
                variants["ok"].append(v)
        for v in ov["bad_variants"]:
            assert v in e.get("variants", []), (key, v)
        rels = {"ok": [], "bad": []}
        for r in e.get("relations", []):
            if r in ov["bad_rels"]:
                rels["bad"].append({"rel": r, "note": ov["bad_rels"][r]})
            else:
                rels["ok"].append(r)
        for r in ov["bad_rels"]:
            assert r in e.get("relations", []), (key, r)
        ans, reason = ov["vote"] or ("yes", None)
        vote = {"answer": ans}
        if reason:
            assert len(reason) <= 150, (key, len(reason))
            vote["reason"] = reason
        assert ans == "yes" or reason, key
        out.append({"key": key, "claims": claims, "variants": variants,
                    "relations": rels, "job_listing_vote": vote})
    return out, seen


def main():
    all_seen = set()
    for p in ("p019", "p020", "p021"):
        out, seen = review(p)
        all_seen |= seen
        with open(os.path.join(HERE, "answers", f"{p}.json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {"supports": 0, "contradicts": 0, "unsure": 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
        bv = sum(len(a["variants"]["bad"]) for a in out)
        br = sum(len(a["relations"]["bad"]) for a in out)
        print(p, len(out), "claims", cnt, "votes", votes, "bad variants", bv, "bad rels", br)
    missing = set(R) - all_seen
    assert not missing, missing


if __name__ == "__main__":
    main()
