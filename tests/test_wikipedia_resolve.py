import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("resolve_matches", ROOT / "scripts" / "wikipedia_match" / "resolve_matches.py")
RM = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RM)


def cand(pid, title, how, form, kind="preferred", via=None):
    c = {"page_id": pid, "title": title, "how": how, "form": form, "form_kind": kind}
    if via:
        c["via"] = via
    return c


class Resolve(unittest.TestCase):
    """The resolver turns match candidates and categories into a relation, so a plain name that is a disambiguation page, or a
    redirect to a broader page, is not reported as the same thing."""
    def run_resolver(self, entries, matches, pages, categories):
        d = Path(tempfile.mkdtemp())
        (d / "lex" / "entries").mkdir(parents=True)
        (d / "lex" / "tools").symlink_to(ROOT / "tools")
        for e in entries:
            e.setdefault("provenance", {"source": "drafted"})
            (d / "lex" / "entries" / (e["key"] + ".json")).write_text(json.dumps(e))
        (d / "in").mkdir()
        (d / "in" / "matches.jsonl").write_text("\n".join(json.dumps(m) for m in matches) + "\n")
        (d / "in" / "candidates.jsonl").write_text("\n".join(json.dumps(p) for p in pages) + "\n")
        (d / "in" / "categories.jsonl").write_text("\n".join(json.dumps({"page_id": k, "title": "", "categories": v}) for k, v in categories.items()) + "\n")
        old = sys.argv
        sys.argv = ["resolve_matches.py", "--lexicon", str(d / "lex"), "--in", str(d / "in"), "--out", str(d / "out.jsonl")]
        try:
            RM.main()
        finally:
            sys.argv = old
        return {json.loads(l)["entry_key"]: json.loads(l) for l in (d / "out.jsonl").read_text().splitlines()}

    def test_disambiguation_and_qualifier_and_redirects(self):
        ent = [{"id": "aaaaaaaaa1", "key": "python", "preferred_name": "Python", "kind": "programming-language"},
               {"id": "aaaaaaaaa2", "key": "ingenuity", "preferred_name": "Ingenuity", "kind": "ability"},
               {"id": "aaaaaaaaa3", "key": "czech", "preferred_name": "Czech", "kind": "human-language"},
               {"id": "aaaaaaaaa4", "key": "azure-data-factory", "preferred_name": "Azure Data Factory", "kind": "tool"},
               {"id": "aaaaaaaaa5", "key": "butter-knife", "preferred_name": "Butter Knife", "kind": "library"}]
        mt = [{"entry_id": "aaaaaaaaa1", "entry_key": "python", "preferred_name": "Python", "tier": "needs-a-person",
               "candidates": [cand(1, "Python", "title", "Python"), cand(2, "Python (programming language)", "title-minus-qualifier", "Python"),
                              cand(3, "Python (genus)", "title-minus-qualifier", "Python")]},
              {"entry_id": "aaaaaaaaa2", "entry_key": "ingenuity", "preferred_name": "Ingenuity", "tier": "needs-a-person",
               "candidates": [cand(4, "Ingenuity (Crespi)", "title-minus-qualifier", "Ingenuity")]},
              {"entry_id": "aaaaaaaaa3", "entry_key": "czech", "preferred_name": "Czech", "tier": "confident",
               "candidates": [cand(5, "Czech language", "redirect", "Czech", via="Czech")]},
              {"entry_id": "aaaaaaaaa4", "entry_key": "azure-data-factory", "preferred_name": "Azure Data Factory", "tier": "confident",
               "candidates": [cand(6, "Microsoft Azure", "redirect", "Azure Data Factory", via="Azure Data Factory")]},
              {"entry_id": "aaaaaaaaa5", "entry_key": "butter-knife", "preferred_name": "Butter Knife", "tier": "confident",
               "candidates": [cand(7, "Butter knife", "title", "Butter Knife")]}]
        pages = [{"page_id": 1, "title": "Python", "disambiguation": True}, {"page_id": 2, "title": "Python (programming language)", "disambiguation": False},
                 {"page_id": 3, "title": "Python (genus)", "disambiguation": False}, {"page_id": 4, "title": "Ingenuity (Crespi)", "disambiguation": False},
                 {"page_id": 5, "title": "Czech language", "disambiguation": False}, {"page_id": 6, "title": "Microsoft Azure", "disambiguation": False},
                 {"page_id": 7, "title": "Butter knife", "disambiguation": False}]
        cats = {1: [], 2: ["Programming languages", "Object-oriented programming languages"], 3: ["Pythonidae", "Snake genera"], 4: ["1690s paintings"],
                5: ["Czech language", "West Slavic languages"], 6: ["Cloud computing", "Microsoft cloud services"], 7: ["Cutlery", "Knives"]}
        r = self.run_resolver(ent, mt, pages, cats)
        self.assertEqual((r["python"]["relation"], r["python"]["page"]["title"]), ("same", "Python (programming language)"))
        self.assertEqual(r["ingenuity"]["relation"], "none")                # a parenthetical page is not evidence for an ability
        self.assertEqual((r["czech"]["relation"], r["czech"]["page"]["title"]), ("same", "Czech language"))
        self.assertEqual(r["azure-data-factory"]["relation"], "related")    # a redirect to a broader page is a link, not an identity
        self.assertEqual(r["butter-knife"]["relation"], "none")             # a library is not cutlery

    def test_onet_abilities_are_left_alone(self):
        ent = [{"id": "bbbbbbbbb1", "key": "time-sharing", "preferred_name": "Time Sharing", "kind": "ability",
                "provenance": {"source": "imported from O*NET 30.2"}}]
        mt = [{"entry_id": "bbbbbbbbb1", "entry_key": "time-sharing", "preferred_name": "Time Sharing", "tier": "confident",
               "candidates": [cand(1, "Time-sharing", "title", "Time Sharing")]}]
        r = self.run_resolver(ent, mt, [{"page_id": 1, "title": "Time-sharing", "disambiguation": False}], {1: ["Operating system technology"]})
        self.assertEqual(r["time-sharing"]["relation"], "none")


if __name__ == "__main__":
    unittest.main()
