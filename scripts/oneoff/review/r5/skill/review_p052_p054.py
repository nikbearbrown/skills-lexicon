#!/usr/bin/env python3
"""Reviewer answers for packets p052-p054. Writes answers/p052.json, p053.json, p054.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

S = "supports"
C = "contradicts"
U = "unsure"


def v(verdict, note=None):
    d = {"verdict": verdict}
    if note:
        d["note"] = note
    return d


def entry(key, definition=S, kind=S, cert=S, var_ok=(), var_bad=(), rel_ok=(), rel_bad=(),
          vote="yes", reason=None, extra=None):
    claims = {}
    claims["definition"] = definition if isinstance(definition, dict) else v(definition)
    claims["kind"] = kind if isinstance(kind, dict) else v(kind)
    claims["certification"] = cert if isinstance(cert, dict) else v(cert)
    if extra:
        claims.update(extra)
    jv = {"answer": vote}
    if reason:
        jv["reason"] = reason
    return {
        "key": key,
        "claims": claims,
        "variants": {"ok": list(var_ok), "bad": [{"label": l, "note": n} for l, n in var_bad]},
        "relations": {"ok": list(rel_ok), "bad": [{"rel": r, "note": n} for r, n in rel_bad]},
        "job_listing_vote": jv,
    }


P052 = [
    entry("vulkan",
          kind=v(U, "Vulkan is a Khronos API specification (open standard) implemented by drivers; 'standard' fits better than library"),
          var_ok=["Vulkan Graphics API", "Vulkan API"], rel_ok=["broader:graphics-api"]),
    entry("vulnerability-assessment", var_ok=["Vulnerability assessments"]),
    entry("vyond", definition=v(S, "GoAnimate rebranded as Vyond in 2018"), var_ok=["GoAnimate"]),
    entry("wage-and-hour-laws", var_ok=["Wage and hour law"], rel_ok=["broader:labour-law"]),
    entry("wainscot-panelling", var_ok=["Wainscot paneling"]),
    entry("warehouse-automation"),
    entry("wasapi", definition=v(S, "introduced with Windows Vista"), var_ok=["Windows Audio Session API"]),
    entry("waste-characterisation", var_ok=["Waste characterization"]),
    entry("waste-minimisation", var_ok=["Waste minimization"]),
    entry("watchkeeping"),
    entry("watchos", rel_ok=["related:macos"]),
    entry("watcom-sql", definition=v(S, "Watcom bought by Powersoft (1994), then Sybase; renamed SQL Anywhere"),
          vote="unsure", reason="Product obsolete since the mid-1990s (now SQL Anywhere); rarely if ever requested by this name"),
    entry("water-based-pipe-coating", var_ok=["Water Based Pipe Coating"]),
    entry("water-quality-modelling", var_ok=["Water quality modeling"], rel_ok=["related:hydrological-modelling"]),
    entry("wave-phase", var_ok=["Phase (Waves)"],
          vote="unsure", reason="A physics concept rather than a skill; rarely asked for on its own in listings"),
    entry("waveguide", var_ok=["Waveguides"], rel_ok=["related:optical-waveguides"]),
    entry("web-crawling", var_ok=["Web Crawlers", "Web crawler"]),
    entry("web-filtering", var_ok=["Website Filtering"]),
    entry("webct", definition=v(S, "began at the University of British Columbia; Blackboard acquired it in 2006 and later retired it")),
    entry("webctrl", definition=v(S, "Automated Logic is a Carrier company")),
    entry("webdriver", definition=v(S, "W3C Recommendation (2018) that grew out of Selenium WebDriver")),
    entry("webdriverjs",
          var_bad=[("selenium-webdriver", "Also the Ruby gem/Python package name; means Selenium WebDriver generally, not the JS bindings")]),
    entry("website-optimization", var_ok=["Website optimisation"], rel_ok=["related:landing-page-optimization"]),
    entry("website-wireframing", var_ok=["Website Wireframe", "Website wireframes"]),
    entry("webvr",
          kind=v(U, "WebVR was a browser API specification (W3C Community Group draft), not a library; 'standard' fits better")),
    entry("weed-control", var_ok=["Weed Controls"]),
    entry("welding-symbols", definition=v(S, "e.g. AWS A2.4 / ISO 2553")),
    entry("whatsapp"),
    entry("wi-fi-6", var_ok=["802.11ax", "IEEE 802.11ax"]),
    entry("wi-fi-architecture", var_ok=["WiFi Architecture"]),
    entry("wi-fi-direct", var_ok=["Wifi Direct"]),
    entry("wi-fi-security", var_ok=["WiFi Security"], rel_ok=["broader:cybersecurity"]),
    entry("wi-fi-test-engineering", var_ok=["WiFi Test Engineering"]),
    entry("wide-area-network", var_ok=["Wide Area Networks"],
          rel_ok=["broader:computer-networking", "related:software-defined-wan"]),
    entry("wildlife-observation"),
    entry("will-and-testament-preparation", var_ok=["Will preparation", "Will drafting"]),
    entry("windows-10", var_ok=["Microsoft Windows 10"]),
    entry("windows-7", var_ok=["Microsoft Windows 7"]),
    entry("windows-8", var_ok=["Microsoft Windows 8"]),
    entry("windows-meeting-space", definition=v(S, "replaced NetMeeting; dropped after Vista"),
          vote="unsure", reason="Discontinued Vista end-user feature; unlikely to be requested in listings"),
]

P053 = [
    entry("windows-performance-analyzer"),
    entry("windows-performance-recorder"),
    entry("windows-performance-toolkit", definition=v(S, "ships in the Windows ADK/SDK")),
    entry("windows-software-trace-preprocessor", definition=v(S, "WPP tracing, built on ETW")),
    entry("windows-support", definition=v(S, "true but thin")),
    entry("windows-systems-administration", var_ok=["Windows System Administration"]),
    entry("windows-vista", definition=v(S, "RTM and business release Nov 2006; consumer release Jan 2007")),
    entry("windows-vista-startup-process",
          vote="unsure", reason="Narrow technical topic; unlikely to be asked for by itself in listings"),
    entry("windows-xp-media-center-edition",
          vote="unsure", reason="Discontinued consumer edition of XP; rarely requested"),
    entry("windows-xp-professional-x64-edition",
          vote="unsure", reason="Discontinued niche XP edition; rarely requested"),
    entry("wine-education", rel_ok=["related:certified-wine-educator"]),
    entry("winemaking", var_ok=["Wine making"]),
    entry("winjs", var_ok=["Windows Library for JavaScript"]),
    entry("wireless-technologies"),
    entry("wkwebview"),
    entry("women-s-health-and-cancer-rights-act",
          kind=v(U, "a US statute; 'knowledge' (of the law) may fit better than standard"),
          var_ok=["WHCRA"],
          var_bad=[("Women'S Health And Cancer Rights Act (WHCRA)", "Malformed capitalisation ('Women'S'); not a real form of the name")]),
    entry("women-s-studies", var_ok=["Women’s Studies"]),
    entry("word-embedding", var_ok=["Word embeddings"]),
    entry("word-formation",
          vote="unsure", reason="A linguistics topic; rarely asked for in job listings"),
    entry("word-processing", var_ok=["Word Processor"]),
    entry("word-vba"),
    entry("word2vec", definition=v(S, "Mikolov et al.; CBOW and skip-gram")),
    entry("workers-compensation-claims"),
    entry("workflow-automation", rel_ok=["related:power-automate"]),
    entry("workflow-management"),
    entry("workforce-optimisation",
          definition=v(S, "describes WFM; contact-centre WFO also covers quality monitoring, recording and analytics"),
          var_ok=["Workforce optimization"]),
    entry("workforce-trends", rel_ok=["related:labor-market-trends"]),
    entry("working-with-children-aged-0-5", var_ok=["Working With Children 0-5"]),
    entry("worship-ministry", rel_ok=["related:family-ministry", "related:children-s-ministry"]),
    entry("writing-outlines"),
    entry("wsdl2java"),
    entry("wxgtk",
          var_bad=[("WXGTK (GTK+ Language Bindings)", "wxGTK is wxWidgets built on GTK, not language bindings for GTK+")]),
    entry("wxperl"),
    entry("wxpython"),
    entry("wyse-management-suite"),
    entry("xanthoproteic-reaction", var_ok=["Xanthoproteic test"], rel_ok=["broader:chemical-reactions"],
          vote="unsure", reason="A specific biochemistry test; unlikely to be requested by name in listings"),
    entry("xbox-live-vision", definition=v(S, "released 2006"),
          vote="no", reason="A consumer gaming accessory, not a skill, ability or certification"),
    entry("xcalibur"),
    entry("xtragrid", var_ok=["DevExpress XtraGrid"]),
    entry("yahoo-messenger-protocols", definition=v(S, "YMSG; service shut down in 2018"),
          rel_ok=["related:yahoo-messenger"],
          vote="unsure", reason="Defunct since 2018; very rarely requested"),
]

P054 = [
    entry("yara", var_ok=["YARA (Software)"]),
    entry("yardi", var_ok=["Yardi (Property Management Software)"]),
    entry("yellow-dog-linux", definition=v(S, "Terra Soft was acquired by Fixstars in 2008; distribution discontinued"),
          vote="unsure", reason="Discontinued niche distribution; rarely requested"),
    entry("youth-mentoring"),
    entry("youth-ministry", rel_ok=["related:family-ministry", "related:children-s-ministry"]),
    entry("yunos", definition=v(S, "renamed AliOS in 2017"), var_ok=["Yun OS"],
          vote="unsure", reason="Renamed AliOS and largely discontinued; rarely requested"),
    entry("z-os", definition=v(S, "now branded IBM Z"), var_ok=["IBM z/OS"]),
    entry("z-wave", definition=v(S, "a mesh protocol overseen by the Z-Wave Alliance"), var_ok=["Z-Wave Protocol"]),
    entry("zemax-opticstudio", definition=v(S, "Zemax was acquired by Ansys in 2021; now Ansys Zemax OpticStudio"),
          var_ok=["Zemax", "OpticStudio"]),
    entry("zenworks-asset-management", definition=v(S, "ZENworks passed to Micro Focus and then OpenText")),
    entry("zeroheight", var_ok=["Zeroheight (Software)"]),
    entry("zerto", definition=v(S, "Zerto is part of Hewlett Packard Enterprise since 2021")),
    entry("zetafax", definition=v(S, "from Equisys")),
    entry("zfs", definition=v(S, "now developed as OpenZFS"), var_ok=["Zettabyte File System"]),
]


def check(packet_name, answers):
    with open(os.path.join(HERE, "packets", packet_name + ".json")) as f:
        packet = json.load(f)
    entries = packet["entries"]
    assert [e["key"] for e in entries] == [a["key"] for a in answers], packet_name + ": key mismatch"
    for e, a in zip(entries, answers):
        pv = set(e["variants"])
        av = set(a["variants"]["ok"]) | {b["label"] for b in a["variants"]["bad"]}
        assert av <= pv, (e["key"], av - pv)
        assert av == pv, (e["key"], "unjudged variants", pv - av)
        pr = set(e["relations"])
        ar = set(a["relations"]["ok"]) | {b["rel"] for b in a["relations"]["bad"]}
        assert ar == pr, (e["key"], pr ^ ar)
        for claim in ("definition", "kind", "certification", "certification_scope", "language_type"):
            has = claim in e or (claim == "certification" and "certification" in e)
            assert (claim in a["claims"]) == has, (e["key"], claim)
        for c in a["claims"].values():
            if c["verdict"] == C:
                assert c.get("note"), e["key"]
            if c.get("note"):
                assert len(c["note"]) <= 150, (e["key"], len(c["note"]))
        jv = a["job_listing_vote"]
        if jv["answer"] != "yes":
            assert jv.get("reason") and len(jv["reason"]) <= 150, e["key"]


def main():
    os.makedirs(os.path.join(HERE, "answers"), exist_ok=True)
    for name, answers in (("p052", P052), ("p053", P053), ("p054", P054)):
        check(name, answers)
        with open(os.path.join(HERE, "answers", name + ".json"), "w") as f:
            json.dump(answers, f, indent=1, ensure_ascii=False)
        cnt = {S: 0, C: 0, U: 0}
        for a in answers:
            for c in a["claims"].values():
                cnt[c["verdict"]] += 1
            for _ in a["variants"]["ok"]:
                cnt[S] += 1
            for _ in a["variants"]["bad"]:
                cnt[C] += 1
            for _ in a["relations"]["ok"]:
                cnt[S] += 1
            for _ in a["relations"]["bad"]:
                cnt[C] += 1
        votes = {"yes": 0, "no": 0, "unsure": 0}
        for a in answers:
            votes[a["job_listing_vote"]["answer"]] += 1
        print(name, len(answers), "entries", cnt, votes)


if __name__ == "__main__":
    main()
