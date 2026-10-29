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
        "level": "professional", "requirements": "Physicians, physician assistants and nurse practitioners.",
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
                                   outcome="supports", ref="wikidata:Q4686912", run="wikipedia-dump-1",
                                   match={"dataset": "enwiki-20261001", "dataset_id": "page_id:123", "method": "redirect",
                                          "categories": ["Professional certification"]}), [])

    def test_evidence_rules(self):
        self.assertTrue(self.evok(action="matched_source", by="source:x", outcome="supports", verification="dump-match"))   # needs a ref
        self.assertTrue(self.evok(action="matched_source", by="source:x", outcome="supports", ref="u"))                    # needs verification
        self.assertTrue(self.evok(action="matched_source", by="model:m", outcome="supports", ref="u", verification="page-read"))   # a model is not a source
        self.assertTrue(self.evok(action="checked", by="human:Bear"))                                            # needs an outcome
        self.assertTrue(self.evok(by="source:enwiki"))                                                           # a source cannot draft
        self.assertTrue(self.evok(by="Bear"))
        self.assertTrue(self.evok(note="x" * 201))
        self.assertTrue(self.evok(match={"dataset": "d", "method": "guess"}))

    def test_entry_rules(self):
        base = {"id": "a1b2c3d4e5", "preferred_name": "A", "kind": "skill", "definition": "d", "status": "reviewed",
                "provenance": {"source": "s", "date": "2026-10-29", "reviewed_by": None}}
        self.assertTrue([x.message for x in self.ve.iter_errors(base)])                                          # reviewed needs a reviewer
        base["provenance"]["reviewed_by"] = "human:Bear"
        self.assertEqual([x.message for x in self.ve.iter_errors(base)], [])
        self.assertTrue([x.message for x in self.ve.iter_errors({**base, "status": "deprecated"})])             # deprecated needs replacements
        self.assertTrue([x.message for x in self.ve.iter_errors({**base, "id": "skill:0001"})])
        self.assertTrue([x.message for x in self.ve.iter_errors({**base, "certification_scope": "single-issuer"})])


if __name__ == "__main__":
    unittest.main()
