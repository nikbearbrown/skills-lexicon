import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import lexicon as L  # noqa: E402

try:
    import jsonschema
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
except ImportError:                                  # the repo itself needs only the standard library
    jsonschema = None


def registry():
    """The three schemas know each other by $id; resolve them from the files, offline."""
    res = []
    for p in sorted((ROOT / "schemas").glob("*.schema.json")):
        d = json.loads(p.read_text("utf-8"))
        res.append((d["$id"], Resource.from_contents(d, default_specification=DRAFT202012)))
    return Registry().with_resources(res)

GOOD = {
    "certification": True, "certification_scope": "single-issuer",
    "credential": {
        "official_name": "Advanced Trauma Life Support", "acronym": "ATLS", "credential_type": "course-completion",
        "issuers": [{"name": "American College of Surgeons", "type": "professional-body", "country": "US",
                     "url": "https://www.facs.org/", "wikidata": "Q466113"}],
        "fields": [{"label": "trauma care"}, {"label": "Medicine", "scheme": "isced-f-2013", "code": "0912"}],
        "level": {"label": "Professional", "scheme": "vendor-ladder", "rank": 2, "of": 3}, "requirements": "Physicians, physician assistants and nurse practitioners.",
        "renewal": {"required": True, "period_months": 48},
        "jurisdiction": ["US", "INT"], "wikidata": "Q4686912",
        "wikipedia": {"title": "Advanced trauma life support", "page_id": 1, "dump": "enwiki-20261001", "match": "redirect"},
        "sources": [{"kind": "issuer", "url": "https://www.facs.org/quality-programs/trauma/atls/", "verification": "page-read",
                     "retrieved": "2026-10-29", "snippet": "short quote"},
                    {"kind": "wikipedia", "url": "https://en.wikipedia.org/wiki/Advanced_trauma_life_support", "verification": "dump-match"}],
    },
}


@unittest.skipIf(jsonschema is None, "jsonschema is not installed")
class Schema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schemas" / "certification.schema.json").read_text("utf-8"))
        cls.v = jsonschema.Draft202012Validator(cls.schema)

    def errors(self, doc):
        return [e.message for e in self.v.iter_errors(doc)]

    def mutate(self, fn):
        d = copy.deepcopy(GOOD)
        fn(d)
        return self.errors(d)

    def test_schema_is_well_formed(self):
        jsonschema.Draft202012Validator.check_schema(self.schema)

    def test_every_real_entry_conforms(self):
        entries, _ = L.load()
        for e in entries:
            self.assertEqual(self.errors({k: v for k, v in e.items() if not k.startswith("_")}), [], e["_file"])

    def test_a_full_credential_passes(self):
        self.assertEqual(self.errors(GOOD), [])

    def test_a_single_issuer_credential_needs_exactly_one_issuer(self):
        self.assertTrue(self.mutate(lambda d: d["credential"].pop("issuers")))
        self.assertTrue(self.mutate(lambda d: d["credential"].update(issuers=[])))
        self.assertTrue(self.mutate(lambda d: d["credential"]["issuers"].append({"name": "Other"})))

    def test_a_many_issuers_credential_may_have_no_issuers_yet(self):
        def f(d):
            d["certification_scope"] = "many-issuers"
            d["credential"]["issuers"] = []
        self.assertEqual(self.mutate(f), [])

    def test_scope_and_credential_need_certification_true(self):
        self.assertTrue(self.mutate(lambda d: d.update(certification=False)))
        self.assertTrue(self.mutate(lambda d: d.pop("certification")))
        self.assertEqual(self.errors({"certification": False}), [])

    def test_a_credential_needs_a_type_and_a_source(self):
        self.assertTrue(self.mutate(lambda d: d["credential"].pop("credential_type")))
        self.assertTrue(self.mutate(lambda d: d["credential"].update(sources=[])))

    def test_a_page_read_source_needs_a_retrieval_date(self):
        self.assertTrue(self.mutate(lambda d: d["credential"]["sources"][0].pop("retrieved")))
        self.assertEqual(self.mutate(lambda d: d["credential"]["sources"][0].update(verification="search-results-only") or d["credential"]["sources"][0].pop("retrieved")), [])

    def test_a_source_must_say_how_much_was_verified(self):
        self.assertTrue(self.mutate(lambda d: d["credential"]["sources"][0].pop("verification")))

    def test_bad_values_are_rejected(self):
        self.assertTrue(self.mutate(lambda d: d["credential"].update(wikidata="4686912")))
        self.assertTrue(self.mutate(lambda d: d["credential"]["issuers"][0].update(country="USA")))
        self.assertTrue(self.mutate(lambda d: d["credential"].update(credential_type="diploma")))
        self.assertTrue(self.mutate(lambda d: d["credential"].update(surprise=1)))
        self.assertTrue(self.mutate(lambda d: d["credential"]["sources"][0].update(snippet="x" * 201)))
        self.assertTrue(self.mutate(lambda d: d["credential"]["wikipedia"].update(dump="enwiki-latest")))

    def test_a_level_is_a_label_in_a_ladder(self):
        self.assertEqual(self.mutate(lambda d: d["credential"].update(level={"label": "Level I", "scheme": "dod-8570-iam", "rank": 1, "of": 3})), [])
        self.assertEqual(self.mutate(lambda d: d["credential"].update(level={"label": "Master's"})), [])
        self.assertTrue(self.mutate(lambda d: d["credential"].update(level="professional")))            # a bare string is the old form
        self.assertTrue(self.mutate(lambda d: d["credential"].update(level={"rank": 1})))                # needs a label
        self.assertTrue(self.mutate(lambda d: d["credential"].update(level={"label": "L", "rank": 0})))

    def test_a_coded_field_needs_its_code(self):
        self.assertTrue(self.mutate(lambda d: d["credential"]["fields"][1].pop("code")))


@unittest.skipIf(jsonschema is None, "jsonschema is not installed")
class EntryAndEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = json.loads((ROOT / "schemas" / "entry.schema.json").read_text("utf-8"))
        cls.evidence = json.loads((ROOT / "schemas" / "evidence.schema.json").read_text("utf-8"))
        cls.ve = jsonschema.Draft202012Validator(cls.entry, registry=registry())
        cls.vv = jsonschema.Draft202012Validator(cls.evidence, registry=registry())

    def test_both_schemas_are_well_formed(self):
        jsonschema.Draft202012Validator.check_schema(self.entry)
        jsonschema.Draft202012Validator.check_schema(self.evidence)

    def test_every_real_entry_conforms_to_the_entry_schema(self):
        entries, _ = L.load()
        for e in entries:
            errs = [x.message for x in self.ve.iter_errors({k: v for k, v in e.items() if not k.startswith("_")})]
            self.assertEqual(errs, [], e["_file"])

    def test_every_real_evidence_record_conforms(self):
        entries, _ = L.load()
        n = 0
        for e in entries:
            for ev in e.get("evidence", []):
                n += 1
                self.assertEqual([x.message for x in self.vv.iter_errors(ev)], [], e["_file"])
        self.assertGreater(n, 300)

    def evok(self, **kw):
        base = {"field": "certification", "by": "model:m", "action": "drafted", "date": "2026-10-29"}
        base.update(kw)
        return [x.message for x in self.vv.iter_errors(base)]

    def test_a_dump_match_record_passes(self):
        self.assertEqual(self.evok(action="matched_source", by="source:enwiki-20261001", kind="wikipedia", verification="dump-match",
                                   organization={"name": "Wikimedia Foundation", "url": "https://www.wikimedia.org/"}, outcome="supports", ref="wikidata:Q4686912", run="wikipedia-dump-1",
                                   match={"dataset": "enwiki-20261001", "dataset_id": "page_id:123", "method": "redirect",
                                          "categories": ["Professional certification"]}), [])

    def test_evidence_rules(self):
        org = {"name": "X", "url": "https://x.example/"}
        self.assertTrue(self.evok(action="matched_source", by="source:x", outcome="supports", verification="dump-match", organization=org))   # needs a ref
        self.assertTrue(self.evok(action="matched_source", by="source:x", outcome="supports", ref="u", organization=org))                    # needs verification
        self.assertTrue(self.evok(action="matched_source", by="source:x", outcome="supports", ref="u", verification="page-read"))            # needs an organization
        self.assertTrue(self.evok(action="matched_source", by="source:x", outcome="supports", ref="u", verification="page-read",
                                  organization={"name": "X"}))                                                                                 # and a link to it
        self.assertTrue(self.evok(action="matched_source", by="model:m", outcome="supports", ref="u", verification="page-read", organization=org))   # a model is not a source
        self.assertTrue(self.evok(action="checked", by="human:Bear"))                                            # needs an outcome
        self.assertTrue(self.evok(by="source:enwiki"))                                                           # a source cannot draft
        self.assertTrue(self.evok(by="Bear"))
        self.assertTrue(self.evok(note="x" * 201))
        self.assertTrue(self.evok(match={"dataset": "d", "method": "guess"}))

    def test_language_type_is_human_or_programming(self):
        base = {"id": "a1b2c3d4e5", "preferred_name": "A", "kind": "human-language", "definition": "d", "status": "proposed",
                "provenance": {"source": "s", "date": "2026-10-29"}}
        for v in ("human", "programming"):
            self.assertEqual([x.message for x in self.ve.iter_errors({**base, "language_type": v})], [], v)
        for v in ("spoken", "other", "markup"):
            self.assertTrue([x.message for x in self.ve.iter_errors({**base, "language_type": v})], v)

    def test_entry_rules(self):
        base = {"id": "a1b2c3d4e5", "preferred_name": "A", "kind": "skill", "definition": "d", "status": "reviewed",
                "provenance": {"source": "s", "date": "2026-10-29", "reviewed_by": None}}
        self.assertTrue([x.message for x in self.ve.iter_errors(base)])                                          # reviewed needs a reviewer
        base["provenance"]["reviewed_by"] = "human:Bear"
        self.assertEqual([x.message for x in self.ve.iter_errors(base)], [])
        self.assertTrue([x.message for x in self.ve.iter_errors({**base, "status": "deprecated"})])             # deprecated needs replacements
        self.assertTrue([x.message for x in self.ve.iter_errors({**base, "id": "skill:0001"})])
        self.assertTrue([x.message for x in self.ve.iter_errors({**base, "certification_scope": "single-issuer"})])


@unittest.skipIf(jsonschema is None, "jsonschema is not installed")
class VotesAndRuns(unittest.TestCase):
    def test_every_stored_vote_conforms(self):
        v = jsonschema.Draft202012Validator(json.loads((ROOT / "schemas" / "assessment.schema.json").read_text("utf-8")))
        lines = [json.loads(x) for x in (ROOT / "data" / "assessments.jsonl").read_text("utf-8").splitlines() if x.strip()]
        self.assertGreaterEqual(len(lines), 300)
        for rec in lines:
            self.assertEqual([x.message for x in v.iter_errors(rec)], [], rec["tag"])

    def test_the_run_registry_conforms_and_a_bad_one_does_not(self):
        v = jsonschema.Draft202012Validator(json.loads((ROOT / "schemas" / "run.schema.json").read_text("utf-8")))
        runs = json.loads((ROOT / "data" / "runs.json").read_text("utf-8"))
        self.assertEqual([x.message for x in v.iter_errors(runs)], [])
        self.assertTrue(list(v.iter_errors({"r": {"model": "m", "effort": "extra", "agent": "main-session"}})))
        self.assertTrue(list(v.iter_errors({"r": {"model": "m", "effort": "high"}})))

    def test_a_vote_needs_an_assessor_who_is_a_model_with_effort_or_a_named_person(self):
        v = jsonschema.Draft202012Validator(json.loads((ROOT / "schemas" / "assessment.schema.json").read_text("utf-8")))
        base = {"tag": "T", "key": "t", "question": "skill", "answer": "yes", "run": "r", "date": "2026-10-29"}
        ok = lambda a: not list(v.iter_errors({**base, "assessor": a}))  # noqa: E731
        self.assertTrue(ok({"type": "model", "model": "m", "effort": "xhigh"}))
        self.assertTrue(ok({"type": "human", "name": "Bear"}))
        self.assertFalse(ok({"type": "model", "model": "m"}))
        self.assertFalse(ok({"type": "human"}))
        self.assertFalse(list(v.iter_errors({**base, "assessor": {"type": "human", "name": "B"}, "answer": "maybe"})) == [])


if __name__ == "__main__":
    unittest.main()
