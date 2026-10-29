import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

# Per-claim overrides: (key, claim) -> (verdict, note)
NOTES = {
    ("hack", "definition"): ("supports", "Hack is gradually typed (static and dynamic typing mixed), not purely statically typed."),
    ("kazakh", "definition"): ("supports", "Kazakh is the state language; Russian also has official status."),
    ("kyrgyz", "definition"): ("supports", "Kyrgyz is the state language; Russian is also an official language."),
    ("japanese", "definition"): ("supports", "True but thin; could name the Japonic family."),
    ("macedonian", "definition"): ("supports", "Albanian has also been co-official nationally since 2019."),
    ("persian", "definition"): ("supports", "Western Iranian; Dari and Tajik are usually treated as varieties of Persian, not just relatives."),
    ("somali", "definition"): ("supports", "Arabic is also an official language of Somalia."),
    ("urdu", "definition"): ("supports", "In India Urdu is an Eighth Schedule language, official in several states rather than at Union level."),
    ("u-sql", "definition"): ("supports", "Azure Data Lake Analytics was retired in February 2024."),
    ("unityscript", "definition"): ("supports", "Deprecated by Unity in 2017 and removed soon after."),
    ("j", "definition"): ("supports", "Visual J#; discontinued, support ended around 2015."),
    ("lingo", "definition"): ("supports", "Adobe Director was discontinued in 2017."),
    ("xul", "definition"): ("supports", "Largely phased out of Firefox in favour of HTML."),
    ("shell-scripting", "kind"): ("supports", "Name reads like a skill, but as defined (the shell languages) programming-language fits."),
    ("systemverilog", "kind"): ("supports", "HDL/HVL; filing as programming-language would also be defensible."),
    ("verilog", "kind"): ("supports", "HDL; filing as programming-language would also be defensible."),
    ("vhdl", "kind"): ("supports", "HDL; filing as programming-language would also be defensible."),
}

BAD_VARIANTS = {
    # key -> {label: note}
    "ladder-logic": {"Ladder diagram": "Also the ordinary electrical relay/control schematic (reading ladder diagrams), not only the PLC language."},
}

BAD_RELATIONS = {}

VOTES = {
    "swabian-german": ("unsure", "A German dialect; listings almost always ask for German, rarely for Swabian itself."),
}


def claim(verdict, note=None):
    d = {"verdict": verdict}
    if note:
        d["note"] = note
    return d


def review(entry):
    k = entry["key"]
    claims = {}
    for c in ("definition", "kind", "certification", "certification_scope", "language_type"):
        if c in entry:
            v, n = NOTES.get((k, c), ("supports", None))
            claims[c] = claim(v, n)
    bad_v = BAD_VARIANTS.get(k, {})
    variants = {"ok": [v for v in entry.get("variants", []) if v not in bad_v],
                "bad": [{"label": l, "note": n} for l, n in bad_v.items()]}
    bad_r = BAD_RELATIONS.get(k, {})
    relations = {"ok": [r for r in entry.get("relations", []) if r not in bad_r],
                 "bad": [{"rel": r, "note": n} for r, n in bad_r.items()]}
    ans, reason = VOTES.get(k, ("yes", None))
    vote = {"answer": ans}
    if reason:
        vote["reason"] = reason
    return {"key": k, "claims": claims, "variants": variants,
            "relations": relations, "job_listing_vote": vote}


for p in ("p002", "p003", "p004", "p005"):
    with open(os.path.join(BASE, "packets", p + ".json")) as f:
        packet = json.load(f)
    out = [review(e) for e in packet["entries"]]
    for o in out:
        for c in o["claims"].values():
            assert len(c.get("note", "")) <= 150, (o["key"], c)
        assert len(o["job_listing_vote"].get("reason", "")) <= 150
    with open(os.path.join(BASE, "answers", p + ".json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    cnt = {"supports": 0, "contradicts": 0, "unsure": 0}
    vc = {"yes": 0, "no": 0, "unsure": 0}
    for o in out:
        for c in o["claims"].values():
            cnt[c["verdict"]] += 1
        vc[o["job_listing_vote"]["answer"]] += 1
    print(p, len(out), cnt, vc)
