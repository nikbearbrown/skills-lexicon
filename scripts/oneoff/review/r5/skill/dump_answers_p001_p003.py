"""Dump reviewer answers for packets p001-p003 (skills lexicon review r5)."""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

S = "supports"
C = "contradicts"
U = "unsure"

# Per-entry overrides. Anything not listed defaults to supports / all variants ok /
# all relations ok / vote yes.
#   def, kind, cert: (verdict, note)  -- note may be None
#   bad_variants: {label: note}
#   bad_relations: {rel: note}
#   vote: (answer, reason)
OVR = {
    # ---------------- p001 ----------------
    "apache-tiles": {"def": (S, "Project retired to the Apache Attic.")},
    "apache-predictionio": {"def": (S, "Project has since been retired by Apache.")},
    "aws-cloud9": {"def": (S, "Closed to new customers since July 2024.")},
    "aws-opsworks": {"def": (S, "All OpsWorks services reached end of life in 2024.")},
    "azure-cognitive-services": {"def": (S, "Renamed Azure AI services in 2023.")},
    "batman-js": {"def": (S, "Project discontinued.")},
    "basic-block": {"vote": ("no", "Compiler-theory term; listings ask for compiler skills, not this concept by name.")},
    "berkeley-data-analytics-stack": {"vote": (U, "Listings name Spark or Mesos; the stack as a whole is rarely asked for.")},
    "bidirectional-streams-over-synchronous-http": {"vote": (U, "Niche XMPP transport; only occasionally named in messaging-developer listings.")},
    # ---------------- p002 ----------------
    "binary-options": {"vote": (U, "Niche product knowledge; appears in few listings, often scam-linked brokers.")},
    "biological-applications-of-bifurcation-theory": {"vote": ("no", "Academic research topic, not something job listings ask for.")},
    "bismuth-sulfite-agar": {"vote": ("no", "A single culture medium; listings ask for microbiology techniques instead.")},
    "blender-game-engine": {"def": (S, "Last shipped in Blender 2.79; removed in 2.80 (2019).")},
    "bodypump": {"bad_variants": {"BodyPumps": "Not a real form of the brand name BODYPUMP."}},
    "boiler-draft": {"vote": (U, "Narrow engineering concept; listings ask for boiler operation rather than draft.")},
    "border-studies": {"vote": (U, "Academic field; appears mainly in academic hiring, rarely in general listings.")},
    "branding-2": {"bad_relations": {"related:branding": "Target looks like the same-named concept (a duplicate) or another sense, not a related one."}},
    "breeze-js": {"bad_variants": {"Breeze.js ((Javascript Library)": "Malformed label with a doubled parenthesis."}},
    "bridal-consulting": {"bad_variants": {"Professional Bridal Consultanting": "Misspelling of 'Consulting'."}},
    "brute-force-search": {
        "bad_variants": {"Brute Force": "Also means a brute-force attack on passwords or keys."},
        "vote": (U, "Basic algorithm idea; rarely named as a requirement."),
    },
    "btrieve": {"def": (C, "Btrieve was created by SoftCraft and sold by Novell before Pervasive took it over; not originally Pervasive's.")},
    # ---------------- p003 ----------------
    "business-integration-software": {"bad_variants": {"Business Integration Softwares": "Non-standard plural 'softwares'."}},
    "butter-knife": {"def": (S, "Now deprecated in favour of Android View Binding.")},
    "bzip2": {"vote": (U, "Command-line utility rarely listed as a job requirement.")},
    "cakewalk": {"def": (S, "Now sold by BandLab as Cakewalk Sonar; Cakewalk was also the original vendor's name.")},
    "callback-function": {"vote": (U, "Granular programming concept; occasionally named with promises/async.")},
    "canon-eos-flash-systems": {"vote": (U, "Product-line knowledge; photography listings rarely name it.")},
    "capture-one": {"def": (S, "Developed by Phase One; spun off as Capture One A/S in 2019.")},
}


def claim(v):
    verdict, note = v
    d = {"verdict": verdict}
    if note:
        d["note"] = note
    return d


def review(entry):
    o = OVR.get(entry["key"], {})
    claims = {}
    if "definition" in entry:
        claims["definition"] = claim(o.get("def", (S, None)))
    if "kind" in entry:
        claims["kind"] = claim(o.get("kind", (S, None)))
    if "certification" in entry:
        claims["certification"] = claim(o.get("cert", (S, None)))
    for extra in ("certification_scope", "language_type"):
        if extra in entry:
            claims[extra] = claim(o.get(extra, (S, None)))

    bad_v = o.get("bad_variants", {})
    for lbl in bad_v:
        assert lbl in entry["variants"], (entry["key"], lbl)
    variants = {
        "ok": [v for v in entry["variants"] if v not in bad_v],
        "bad": [{"label": k, "note": n} for k, n in bad_v.items()],
    }

    bad_r = o.get("bad_relations", {})
    for r in bad_r:
        assert r in entry["relations"], (entry["key"], r)
    relations = {
        "ok": [r for r in entry["relations"] if r not in bad_r],
        "bad": [{"rel": k, "note": n} for k, n in bad_r.items()],
    }

    ans, reason = o.get("vote", ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason

    return {
        "key": entry["key"],
        "claims": claims,
        "variants": variants,
        "relations": relations,
        "job_listing_vote": vote,
    }


def main():
    used = set()
    for p in ("p001", "p002", "p003"):
        with open(os.path.join(BASE, "packets", p + ".json")) as f:
            pk = json.load(f)
        out = []
        for e in pk["entries"]:
            used.add(e["key"])
            out.append(review(e))
        # length checks
        for a in out:
            for c in a["claims"].values():
                assert len(c.get("note", "")) <= 150, (a["key"], c)
                if c["verdict"] == C:
                    assert c.get("note"), a["key"]
            assert len(a["job_listing_vote"].get("reason", "")) <= 150, a["key"]
        with open(os.path.join(BASE, "answers", p + ".json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        cnt = {S: 0, C: 0, U: 0}
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in out:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            votes[a["job_listing_vote"]["answer"]] += 1
        print(p, len(out), "entries", cnt, votes,
              "bad variants", sum(len(a["variants"]["bad"]) for a in out),
              "bad relations", sum(len(a["relations"]["bad"]) for a in out))
    missing = set(OVR) - used
    assert not missing, missing


if __name__ == "__main__":
    main()
