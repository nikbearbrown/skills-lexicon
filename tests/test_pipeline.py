import json
import shutil
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import annotate as A  # noqa: E402
import extract as X  # noqa: E402
import ingest as I  # noqa: E402
import lexicon as L  # noqa: E402
import make_requests as M  # noqa: E402
import run_endpoint as R  # noqa: E402

_REAL = L.load()[0]


def rid(old):
    """The current id of a real entry, found by the id it had before ids became random."""
    return L.find(_REAL, old)["id"]

AD = {"id": "gh:1", "title": "Data Engineer", "text": (
    "We use Postgres and Kubernetes. Experience with Terraform, Snowflake and dbt is a plus.\n"
    "You will build LLM observability tooling. Strong PG skills with our database tier. Based in NYC, EEO employer.")}


def temp_root():
    d = Path(tempfile.mkdtemp())
    shutil.copytree(ROOT / "entries", d / "entries")
    return d


def run_pipeline(root, ads, answers, model="test-model-1"):
    """Extract -> requests -> write answers (term -> response) -> ingest. Returns (report, work dir)."""
    work = root / "work"
    entries, _ = L.load(root / "entries")
    recs, cands = X.process(ads, entries, X.load_decisions(root))
    (work / "requests").mkdir(parents=True)
    (work / "responses").mkdir()
    for name, req in M.make(cands, entries, min_postings=1).items():
        (work / "requests" / name).write_text(json.dumps(req))
        if req["term"] in answers:
            (work / "responses" / name).write_text(json.dumps(answers[req["term"]]))
    return I.ingest(work, root, "model:" + model, "run-1", "2026-10-27"), work


class Extract(unittest.TestCase):
    def setUp(self):
        self.entries, _ = L.load()
        self.rec, self.cands = X.process([AD], self.entries)
        self.skills = {s["concept"]: s for s in self.rec[0]["skills"]}

    def test_variant_resolves_to_canonical(self):
        self.assertEqual(self.skills[rid("skill:0082")]["form"], "Postgres")
        self.assertIn("Postgres", self.skills[rid("skill:0082")]["quote"])

    def test_rollup_counts_sql_for_postgresql(self):
        self.assertEqual(self.rec[0]["rolled_up"], [rid("skill:0046")])

    def test_longest_span_wins(self):
        self.assertIn(rid("skill:0008"), self.skills)       # LLM observability
        self.assertNotIn(rid("skill:0007"), self.skills)    # not also plain Observability

    def test_context_gates_the_short_form(self):
        with_ctx = X.process([{"id": "a", "text": "Strong PG skills with our database tier."}], self.entries)[0][0]["skills"]
        without = X.process([{"id": "b", "text": "Strong PG skills needed."}], self.entries)[0][0]["skills"]
        self.assertEqual([s["concept"] for s in with_ctx], [rid("skill:0082")])
        self.assertEqual(without, [])

    def test_exact_case_short_forms(self):
        rec = X.process([{"id": "a", "text": "We like pg and we use the database daily."}], self.entries)[0][0]
        self.assertEqual(rec["skills"], [])

    def test_ambiguous_form_is_reported_not_counted(self):
        rec = X.process([{"id": "a", "text": "Hold a CPC credential."}], self.entries)[0][0]
        self.assertEqual(rec["skills"], [])
        self.assertEqual(sorted(rec["ambiguous"][0]["candidates"]), [rid("skill:0030"), rid("skill:0031")])

    def test_unknown_terms_found_with_quotes_and_known_ones_skipped(self):
        terms = {c["term"] for c in self.cands}
        self.assertTrue({"Kubernetes", "Terraform", "Snowflake", "dbt"} <= terms)
        self.assertFalse({"Postgres", "NYC", "EEO"} & terms)
        k = next(c for c in self.cands if c["term"] == "Kubernetes")
        self.assertIn("Kubernetes", k["quotes"][0]["quote"])

    def test_decided_terms_are_not_asked_again(self):
        dec = {L.norm("Terraform"): {"term": "Terraform", "decision": "not_a_skill"}}
        terms = {c["term"] for c in X.process([AD], self.entries, dec)[1]}
        self.assertNotIn("Terraform", terms)

    def test_cli_end_to_end(self):
        root = temp_root()
        (root / "ads.jsonl").write_text(json.dumps(AD) + "\n")
        self.assertEqual(X.main([str(root / "ads.jsonl"), "--out", str(root / "w"), "--root", str(root)]), 0)
        self.assertTrue((root / "w" / "records.jsonl").exists() and (root / "w" / "candidates.json").exists())


class Noise(unittest.TestCase):
    def terms(self, ads):
        return {c["term"] for c in X.process(ads, L.load()[0])[1]}

    def test_boilerplate_lists_are_not_candidates(self):
        t = self.terms([{"id": "a", "text": "We do not discriminate, including on gender identity, sexual orientation or age.\n"
                                            "Benefits including dental, vision and a 401k match."}])
        self.assertFalse({"gender identity", "sexual orientation", "dental", "vision"} & t)

    def test_ci_cd_is_one_term_and_and_or_is_not_a_term(self):
        t = self.terms([{"id": "a", "text": "You know CI/CD and/or similar tooling."}])
        self.assertIn("CI/CD", t)
        self.assertFalse({"CI", "CD", "and/or"} & t)

    def test_headings_and_recruiter_tags_are_ignored(self):
        t = self.terms([{"id": "a", "text": "ABOUT THE ROLE\nWHAT YOU WILL DO\nApply now. #LI-Remote"}])
        self.assertFalse({"ABOUT", "ROLE", "WHAT", "LI", "Remote"} & t)

    def test_ordinary_capitalised_words_are_dropped_by_the_corpus(self):
        ads = [{"id": "a", "text": "We use Kubernetes and the Engineer role. Our engineer will use tools."},
               {"id": "b", "text": "Experience with Terraform. Each engineer matters; an engineer leads."}]
        t = self.terms(ads)
        self.assertIn("Kubernetes", t)
        self.assertNotIn("Engineer", t)

    def test_plain_words_outside_a_skill_sentence_are_dropped(self):
        t = self.terms([{"id": "a", "text": "Our office is in San Francisco near Market Street."}])
        self.assertFalse({"San", "Francisco", "Market", "Street"} & t)


class Requests(unittest.TestCase):
    def test_request_is_self_contained(self):
        entries, _ = L.load()
        cands = X.process([AD], entries)[1]
        req = next(iter(M.make([c for c in cands if c["term"] == "Kubernetes"], entries, 1).values()))
        self.assertIn("## The task", req["instructions"])
        self.assertNotIn("If you are an agent", req["instructions"])
        self.assertEqual(req["term"], "Kubernetes")
        self.assertTrue(req["quotes"] and req["allowed"]["kinds"])

    def test_nearest_finds_the_related_entry(self):
        entries, _ = L.load()
        near = M.nearest("PostgreSQL 15", [{"quote": "run PostgreSQL databases"}], entries)
        self.assertEqual(near[0]["id"], rid("skill:0082"))

    def test_nearest_uses_cooccurrence_not_stray_words(self):
        entries, _ = L.load()
        near = M.nearest("Kubernetes", [{"quote": "Experience with infrastructure systems, security, and AWS or React"}], entries)
        names = {n["name"] for n in near}
        self.assertTrue({"Amazon Web Services", "React"} <= names)        # AWS and React appear in the quote
        self.assertFalse({"Cybersecurity", "Operating systems"} & names)  # only a stray word in common

    def test_min_postings_filters(self):
        entries, _ = L.load()
        cands = X.process([AD], entries)[1]
        self.assertEqual(M.make(cands, entries, min_postings=2), {})


NEW = {"decision": "new", "variant_of": None, "reason": "a container orchestrator", "entry": {
    "preferred_name": "Kubernetes", "kind": "platform", "definition": "A system for running containerised applications across machines.",
    "definition_basis": "general-knowledge",
    "variants": [{"label": "k8s", "basis": "general-knowledge"}, {"label": "K8", "basis": "guess"}],
    "relations": [{"type": "related", "target": rid("skill:0019"), "basis": "general-knowledge"},
                  {"type": "broader", "target": "skill:9999", "basis": "general-knowledge"},
                  {"type": "related", "target": rid("skill:0082"), "basis": "guess"}],
    "verbs": [{"verb": "deploy", "basis": "posting"}, {"verb": "tune", "basis": "guess"}]}}


class Ingest(unittest.TestCase):
    def test_new_entry_saved_with_evidence_naming_the_operators_model(self):
        root = temp_root()
        rep, _ = run_pipeline(root, [AD], {"Kubernetes": NEW}, model="my-local-model")
        self.assertEqual(rep["new"], ["Kubernetes"])
        e = json.loads((root / "entries" / "kubernetes.json").read_text())
        others, _ = L.load(root / "entries")
        self.assertEqual(e["status"], "machine-drafted")
        self.assertRegex(e["id"], L.ID_RE)                                           # a random 10-character id
        self.assertNotIn(e["id"], {x["id"] for x in others if x["key"] != "kubernetes"})
        self.assertEqual({v["label"] for v in e["variants"]}, {"k8s"})              # guess dropped
        self.assertEqual([r["target"] for r in e["relations"]], [rid("skill:0019")])     # bad target and guess dropped
        self.assertEqual(e["verbs"], ["deploy"])
        self.assertEqual({v["by"] for v in e["evidence"]}, {"model:my-local-model"})
        self.assertEqual({v["field"] for v in e["evidence"]}, L.claim_keys(e))
        self.assertEqual(rep["dropped_claims"], 4)
        entries, errs = L.load(root / "entries")
        self.assertEqual(errs + L.validate(entries), [])

    def test_the_models_own_identity_claim_is_ignored(self):
        root = temp_root()
        ans = json.loads(json.dumps(NEW))
        ans["model"] = "gpt-pretend"
        ans["entry"]["by"] = "human:Somebody"
        run_pipeline(root, [AD], {"Kubernetes": ans}, model="real-model")
        e = json.loads((root / "entries" / "kubernetes.json").read_text())
        self.assertEqual({v["by"] for v in e["evidence"]}, {"model:real-model"})

    def test_duplicate_name_is_rejected_and_dictionary_untouched(self):
        root = temp_root()
        dup = json.loads(json.dumps(NEW))
        dup["entry"]["preferred_name"] = "PostgreSQL"
        before = sorted(p.name for p in (root / "entries").iterdir())
        rep, work = run_pipeline(root, [AD], {"Kubernetes": dup})
        self.assertEqual(len(rep["rejected"]), 1)
        self.assertEqual(sorted(p.name for p in (root / "entries").iterdir()), before)
        self.assertTrue(any((work / "rejected").iterdir()))

    def test_a_rejected_answer_does_not_poison_the_next_one(self):
        root = temp_root()
        dup = json.loads(json.dumps(NEW))
        dup["entry"]["preferred_name"] = "PostgreSQL"
        good = json.loads(json.dumps(NEW))
        good["entry"]["preferred_name"] = "Terraform"
        # 'Kubernetes' (rejected) sorts before 'Terraform' (good) by request file name
        rep, _ = run_pipeline(root, [AD], {"Kubernetes": dup, "Terraform": good})
        self.assertEqual(rep["new"], ["Terraform"])
        self.assertEqual(len(rep["rejected"]), 1)
        entries, errs = L.load(root / "entries")
        self.assertEqual(errs + L.validate(entries), [])

    def test_guessed_definition_is_rejected(self):
        root = temp_root()
        bad = json.loads(json.dumps(NEW))
        bad["entry"]["definition_basis"] = "guess"
        rep, _ = run_pipeline(root, [AD], {"Kubernetes": bad})
        self.assertEqual(len(rep["rejected"]), 1)

    def test_not_a_skill_and_unsure_are_remembered(self):
        root = temp_root()
        rep, _ = run_pipeline(root, [AD], {"Terraform": {"decision": "not_a_skill", "reason": "x"},
                                           "Snowflake": {"decision": "unsure", "reason": "company or tool?"}})
        d = json.loads((root / "data" / "term-decisions.json").read_text())
        self.assertEqual({x["term"]: x["decision"] for x in d}, {"Terraform": "not_a_skill", "Snowflake": "unsure"})
        entries, _ = L.load(root / "entries")
        terms = {c["term"] for c in X.process([AD], entries, X.load_decisions(root))[1]}
        self.assertFalse({"Terraform", "Snowflake"} & terms)

    def test_variant_of_adds_a_claim_to_the_existing_entry(self):
        root = temp_root()
        ad = {"id": "gh:2", "text": "We run PostgreSQL 15 clusters. Experience with PG15 required."}
        rep, _ = run_pipeline(root, [ad], {"PG15": {"decision": "variant_of", "variant_of": rid("skill:0082"), "reason": "version name"}})
        self.assertEqual(len(rep["variant"]), 1)
        e = json.loads((root / "entries" / "postgresql.json").read_text())
        self.assertIn("PG15", [v["label"] for v in e["variants"]])
        self.assertEqual(e["evidence"][-1]["field"], "variant:pg15")

    def test_variant_of_a_reviewed_entry_is_held_back(self):
        root = temp_root()
        p = root / "entries" / "postgresql.json"
        e = json.loads(p.read_text())
        e["status"] = "reviewed"
        e["provenance"]["reviewed_by"] = "human:Bear"
        e["evidence"] = [{"field": k, "by": "human:Bear", "action": "checked", "outcome": "supports", "date": "2026-10-27"}
                         for k in L.claim_keys(e)]
        p.write_text(json.dumps(e))
        ad = {"id": "gh:2", "text": "Experience with PG15 required."}
        rep, _ = run_pipeline(root, [ad], {"PG15": {"decision": "variant_of", "variant_of": rid("skill:0082"), "reason": "x"}})
        self.assertEqual(rep["variant"], [])
        self.assertEqual(len(rep["rejected"]), 1)
        self.assertIn("pull request", rep["rejected"][0][1])     # the clear reason, not just a validator error

    def test_dry_run_writes_nothing(self):
        root = temp_root()
        work = root / "work"
        entries, _ = L.load(root / "entries")
        cands = X.process([AD], entries)[1]
        (work / "requests").mkdir(parents=True)
        (work / "responses").mkdir()
        for name, req in M.make([c for c in cands if c["term"] == "Kubernetes"], entries, 1).items():
            (work / "requests" / name).write_text(json.dumps(req))
            (work / "responses" / name).write_text(json.dumps(NEW))
        before = sorted(p.name for p in (root / "entries").iterdir())
        rep = I.ingest(work, root, "model:x", "r", "2026-10-27", dry=True)
        self.assertEqual(rep["new"], ["Kubernetes"])
        self.assertEqual(sorted(p.name for p in (root / "entries").iterdir()), before)
        self.assertFalse((work / "done").exists())


def tag_run(answer, in_lists=(), cls="Skill"):
    """Draft one tag with no posting: build its request from a legacy-tag candidate, answer it, ingest."""
    root = temp_root()
    work = root / "work"
    entries, _ = L.load(root / "entries")
    cand = {"term": "Frobnicate Cert", "n_postings": 0, "quotes": [],
            "origin": {"sources": [{"file": "data/skills_tags.csv", "rows": [7], "class": cls}], "class": cls,
                       "in_lists": list(in_lists)}}
    (work / "requests").mkdir(parents=True)
    (work / "responses").mkdir()
    for name, req in M.make([cand], entries, 0).items():
        (work / "requests" / name).write_text(json.dumps(req))
        (work / "responses" / name).write_text(json.dumps(answer))
    return I.ingest(work, root, "model:m1", "run-t", "2026-10-29"), root


def tag_answer(**ann):
    e = {"preferred_name": "Frobnicate Cert", "kind": "credential", "definition": "A made-up credential.",
         "definition_basis": "general-knowledge", "variants": [], "relations": [], "verbs": []}
    e.update(ann)
    return {"decision": "new", "variant_of": None, "reason": "r", "entry": e}


class Annotations(unittest.TestCase):
    def test_tag_origin_is_recorded_and_no_posting_is_claimed(self):
        rep, root = tag_run(tag_answer(certification={"value": True, "basis": "general-knowledge"}), ["certification"], "Certification")
        self.assertEqual(rep["new"], ["Frobnicate Cert"])
        e = json.loads((root / "entries" / "frobnicate-cert.json").read_text())
        self.assertTrue(e["certification"])
        self.assertEqual(e["provenance"]["legacy_tag"]["sources"][0]["rows"], [7])
        self.assertIn("legacy tag list alone", e["provenance"]["source"])
        self.assertNotIn("posting", " ".join(v["note"] for v in e["evidence"] if v["field"] != "variant:frobnicate cert").replace("basis: general-knowledge", ""))
        self.assertEqual(L.validate(L.load(root / "entries")[0]), [])

    def test_model_disagreeing_with_a_legacy_list_is_flagged(self):
        ans = tag_answer(certification={"value": False, "basis": "general-knowledge"}, annotation_note="It is a software tool.")
        _, root = tag_run(ans, ["certification"], "Certification")
        e = json.loads((root / "entries" / "frobnicate-cert.json").read_text())
        self.assertIs(e["certification"], False)
        rec = next(v for v in e["evidence"] if v["field"] == "certification")
        self.assertEqual(rec["flag"], "disagrees_with_legacy")
        self.assertIn("software tool", rec["note"])
        self.assertEqual([x for x in L.claim_keys(e) if x == "certification"], ["certification"])
        self.assertFalse(L.backs(rec))                    # a list and a model do not back a claim

    def test_model_adding_a_certification_the_lists_do_not_know_is_flagged(self):
        _, root = tag_run(tag_answer(certification={"value": True, "basis": "general-knowledge"}))
        rec = next(v for v in json.loads((root / "entries" / "frobnicate-cert.json").read_text())["evidence"] if v["field"] == "certification")
        self.assertEqual(rec["flag"], "not_in_legacy")

    def test_not_a_language_leaves_no_field_but_keeps_the_disagreement(self):
        ans = tag_answer(kind="knowledge", language_type={"value": None, "basis": "general-knowledge"}, annotation_note="A field of study.")
        _, root = tag_run(ans, ["language"], "Language")
        e = json.loads((root / "entries" / "frobnicate-cert.json").read_text())
        self.assertNotIn("language_type", e)
        self.assertIn("not a language", e["notes"])

    def test_language_type_values(self):
        _, root = tag_run(tag_answer(kind="programming-language", language_type={"value": "programming", "basis": "general-knowledge"}))
        self.assertEqual(json.loads((root / "entries" / "frobnicate-cert.json").read_text())["language_type"], "programming")
        rep, root = tag_run(tag_answer(language_type={"value": "klingon", "basis": "general-knowledge"}))
        e = json.loads((root / "entries" / "frobnicate-cert.json").read_text())
        self.assertNotIn("language_type", e)               # a value outside the allowed set is dropped, not saved

    def test_ids_are_case_insensitive_and_former_ids_resolve(self):
        near = rid("skill:0019")
        _, root = tag_run(tag_answer(relations=[{"type": "related", "target": near.upper(), "basis": "general-knowledge"},
                                                {"type": "related", "target": "skill:0082", "basis": "general-knowledge"}]))
        e = json.loads((root / "entries" / "frobnicate-cert.json").read_text())
        self.assertEqual([r["target"] for r in e["relations"]], [near, rid("skill:0082")])   # stored as the current lower-case id

    def test_certification_scope_is_saved_with_its_own_evidence_and_note(self):
        ans = tag_answer(certification={"value": True, "basis": "general-knowledge"},
                         certification_scope={"value": "many-issuers", "basis": "general-knowledge"}, annotation_note="Each state issues its own.")
        _, root = tag_run(ans, ["certification"], "Certification")
        e = json.loads((root / "entries" / "frobnicate-cert.json").read_text())
        self.assertEqual(e["certification_scope"], "many-issuers")
        rec = next(v for v in e["evidence"] if v["field"] == "certification_scope")
        self.assertIn("Each state issues its own", rec["note"])
        self.assertEqual({v["field"] for v in e["evidence"]}, L.claim_keys(e))
        self.assertEqual(L.validate(L.load(root / "entries")[0]), [])

    def test_scope_on_a_non_certification_is_dropped(self):
        ans = tag_answer(certification={"value": False, "basis": "general-knowledge"},
                         certification_scope={"value": "single-issuer", "basis": "general-knowledge"})
        _, root = tag_run(ans)
        self.assertNotIn("certification_scope", json.loads((root / "entries" / "frobnicate-cert.json").read_text()))

    def test_scope_value_outside_the_set_is_dropped(self):
        ans = tag_answer(certification={"value": True, "basis": "general-knowledge"},
                         certification_scope={"value": "several", "basis": "general-knowledge"})
        _, root = tag_run(ans, ["certification"], "Certification")
        self.assertNotIn("certification_scope", json.loads((root / "entries" / "frobnicate-cert.json").read_text()))

    def test_guessed_annotation_is_dropped(self):
        _, root = tag_run(tag_answer(certification={"value": True, "basis": "guess"}))
        self.assertNotIn("certification", json.loads((root / "entries" / "frobnicate-cert.json").read_text()))

    def test_validator_rejects_bad_values(self):
        base = {"id": "abcdefghi1", "preferred_name": "A", "kind": "skill", "definition": "d", "status": "proposed",
                "provenance": {"source": "t", "date": "2026-10-29"}, "_file": "a.json"}
        self.assertTrue(any("certification must be" in m for m in L.validate([dict(base, certification="yes")])))
        self.assertTrue(any("language_type must be" in m for m in L.validate([dict(base, language_type="klingon")])))
        self.assertEqual(L.validate([dict(base, certification=True, language_type="spoken")]), [])


class AnnotateExisting(unittest.TestCase):
    def setUp(self):
        _, self.root = tag_run(tag_answer(certification={"value": True, "basis": "general-knowledge"}), ["certification"], "Certification")
        self.answers = self.root / "answers.json"

    def go(self, answers, dry=False):
        self.answers.write_text(json.dumps(answers))
        argv = [str(self.answers), "--model-id", "m2", "--run", "scope-run", "--root", str(self.root), "--date", "2026-10-29"]
        return A.main(argv + (["--dry-run"] if dry else []))

    def entry(self):
        return json.loads((self.root / "entries" / "frobnicate-cert.json").read_text())

    def test_adds_a_scope_with_evidence_from_the_operators_model(self):
        self.go({"frobnicate-cert": {"certification_scope": {"value": "single-issuer", "basis": "general-knowledge"}}})
        e = self.entry()
        self.assertEqual(e["certification_scope"], "single-issuer")
        rec = next(v for v in e["evidence"] if v["field"] == "certification_scope")
        self.assertEqual((rec["by"], rec["run"], rec["action"]), ("model:m2", "scope-run", "drafted"))
        self.assertEqual(L.validate(L.load(self.root / "entries")[0]), [])

    def test_dry_run_writes_nothing(self):
        before = self.entry()
        self.go({"frobnicate-cert": {"certification_scope": {"value": "single-issuer", "basis": "general-knowledge"}}}, dry=True)
        self.assertEqual(self.entry(), before)

    def test_an_existing_field_is_not_overwritten(self):
        self.go({"frobnicate-cert": {"certification_scope": {"value": "single-issuer", "basis": "general-knowledge"}}})
        self.go({"frobnicate-cert": {"certification_scope": {"value": "many-issuers", "basis": "general-knowledge"}}})
        self.assertEqual(self.entry()["certification_scope"], "single-issuer")

    def test_a_reviewed_entry_is_refused(self):
        p = self.root / "entries" / "frobnicate-cert.json"
        e = self.entry()
        e["status"] = "reviewed"
        e["provenance"]["reviewed_by"] = "human:Bear"
        e["evidence"] = [{"field": k, "by": "human:Bear", "action": "checked", "outcome": "supports", "date": "2026-10-29"} for k in L.claim_keys(e)]
        p.write_text(json.dumps(e))
        self.go({"frobnicate-cert": {"certification_scope": {"value": "single-issuer", "basis": "general-knowledge"}}})
        self.assertNotIn("certification_scope", self.entry())

    def test_scope_is_dropped_when_the_entry_is_not_a_certification(self):
        _, root = tag_run(tag_answer(certification={"value": False, "basis": "general-knowledge"}))
        self.root = root
        self.answers = root / "answers.json"
        self.go({"frobnicate-cert": {"certification_scope": {"value": "single-issuer", "basis": "general-knowledge"}}})
        self.assertNotIn("certification_scope", self.entry())


class Runner(unittest.TestCase):
    def test_extract_json_handles_fences_chatter_and_escaped_quotes(self):
        self.assertEqual(R.extract_json('Sure!\n```json\n{"a": "x \\" } y", "b": [1]}\n```\nDone'), {"a": 'x " } y', "b": [1]})
        with self.assertRaises(ValueError):
            R.extract_json("no json here")

    def _work(self):
        root = temp_root()
        work = root / "work"
        entries, _ = L.load(root / "entries")
        cands = [c for c in X.process([AD], entries)[1] if c["term"] == "Kubernetes"]
        (work / "requests").mkdir(parents=True)
        for name, req in M.make(cands, entries, 1).items():
            (work / "requests" / name).write_text(json.dumps(req))
        return work

    def test_http_endpoint(self):
        seen = {}

        class H(BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                seen.update(path=self.path, model=body["model"], auth=self.headers.get("Authorization"),
                            roles=[m["role"] for m in body["messages"]])
                out = json.dumps({"choices": [{"message": {"content": "```json\n" + json.dumps(NEW) + "\n```"}}]}).encode()
                self.send_response(200)
                self.send_header("Content-Length", str(len(out)))
                self.end_headers()
                self.wfile.write(out)

            def log_message(self, *a):
                pass
        srv = HTTPServer(("127.0.0.1", 0), H)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        work = self._work()
        import os
        os.environ["TEST_KEY"] = "k"
        rc = R.main([str(work), "--url", f"http://127.0.0.1:{srv.server_port}/v1", "--model", "m1", "--api-key-env", "TEST_KEY"])
        srv.shutdown()
        self.assertEqual(rc, 0)
        self.assertEqual((seen["path"], seen["model"], seen["auth"], seen["roles"]), ("/v1/chat/completions", "m1", "Bearer k", ["system", "user"]))
        self.assertEqual(json.loads(next((work / "responses").glob("*.json")).read_text())["decision"], "new")

    def test_command_runner_and_bad_reply_kept_raw(self):
        work = self._work()
        good = sys.executable + " -c \"import sys,json; sys.stdin.read(); print('ok:', json.dumps(dict(decision='unsure', reason='r')))\""
        self.assertEqual(R.main([str(work), "--cmd", good]), 0)
        self.assertEqual(json.loads(next((work / "responses").glob("*.json")).read_text())["decision"], "unsure")
        work2 = self._work()
        self.assertEqual(R.main([str(work2), "--cmd", sys.executable + " -c \"print('no json')\""]), 1)
        self.assertTrue(list((work2 / "responses").glob("*.raw.txt")))
        self.assertFalse(list((work2 / "responses").glob("*.json")))


if __name__ == "__main__":
    unittest.main()
