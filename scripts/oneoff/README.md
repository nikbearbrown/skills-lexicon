# One-off answer scripts

These are the scripts a model wrote to put its answers into files during the first pass. They are kept so the record shows how each set of answers was written. They are **not reusable tools**: each has the answers for one batch typed into it as Python data, and some have the paths of the machine they ran on. The reusable tools are in `tools/` and `scripts/`.

The answers themselves are already in the lexicon as evidence (`entries/`) and votes (`data/assessments.jsonl`), under the runs in `data/runs.json`. Running these again would add nothing.

| Script | What it wrote | Where it went |
|---|---|---|
| `pilot_answers.py` | the pilot model's drafts for the first 100 tags, from general knowledge | `work/responses/`, then `tools/ingest.py` |
| `blind_redraft_responses.py` | the drafts for one batch of tags, written in the second agent's copy of the repo | `work/responses/`, then `tools/ingest.py` |
| `round05_responses.py` | the drafts for one overnight round of tags | `work/responses/`, then `tools/ingest.py` |
| `review1_answers_p001.py` | a reviewer's answers for the first review packet | `answers/p001.json`, then `tools/check_claims.py apply` |
| `review2_skill_answers.py` | a reviewer's answers for the skill review packets | `answers/pNNN.json`, then `tools/check_claims.py apply` |
| `review3_certification_answers.py`, `review3_certification_dump.py` | a reviewer's answers for the certification review packets | `answers/pNNN.json`, then `tools/check_claims.py apply` |

Anything written this way is a model's opinion from general knowledge, with no source checked. See `docs/SCHEMAS.md` for what counts as evidence.

## Everything else the drafting agents and reviewers wrote

Under `rounds/` and `review/` are the scripts each drafting agent and each reviewer wrote in its own scratch folder, copied as they were:

- `rounds/round-NN-aM/` (`round-01` to `round-09`): the scripts agent M of round NN used to write its answers, with the path they had under `work/` below that. The first pilot run's is `rounds/agent1/`.
- `review/rN/`: the scripts the reviewers of review N used to write their answers (`r1` to `r4`). Review 4 is the second-model check of the certifications, languages and abilities drafted in rounds 8 and 9.

They are kept for the record and are not meant to be run again: each has one batch of answers typed in as data, and the paths are those of the machine they ran on. They contain no credentials. Some hold a few lines of a model's working notes.
