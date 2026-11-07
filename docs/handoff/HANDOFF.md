# Handoff: the Skills Lexicon project

Written 2026-11-07 for a Claude that has never seen this project. The previous Claude ran in a cloud session that has run out of credits. Everything it knew that matters is in this file and in the repository. Read this file first, then `README.md`, `docs/SCHEMAS.md`, `docs/CLASSES.md` and `docs/SOURCES.md`.

If you are Claude Code on Bear's Mac, you can reach the cluster (the previous Claude could not), so you can run the prompts in `docs/handoff/prompts/` yourself instead of handing them to someone.

## 1. What this is

An open dictionary and evidence base of the things job listings ask for, owned by Bear Brown (Humanitarians AI Incorporated), MIT-licensed, public at https://github.com/nikbearbrown/skills-lexicon (default branch `main`, which is the working branch). Bear is writing a paper that uses it.

Two layers, kept in one dataset:
- **Lexicon layer**: names, variants, definitions and descriptions of concepts, like WordNet.
- **Ontology layer**: typed kinds and relations, with evidence for each claim, aiming at an *evidence-backed skills ontology* with stable external identifiers (Wikipedia, WordNet, O\*NET, ESCO).

The distinguishing idea: **the lexicon does not decide, it accumulates provenance.** Every claim records who or what says it. Later passes, and people, decide.

## 2. How Bear wants you to work

- **Push back and critique; don't flatter.** A message starting "thoughts on" or "thoughts about" is an invitation to brainstorm and challenge. One starting "draft" means produce output immediately without discussion.
- **Long or structured answers go in a file or page, with a link Bear can click.** Bear works in an app where local file paths in a cloud container are not visible. Publish a page, or commit to GitHub, and give the link. Short conversational replies stay in chat. Markdown is the default format.
- **Prompts for other tools must be paste-ready**: the exact text in its own code block, no placeholders, no instructions mixed in. If there are several steps, number them and give each paste separately.
- **Report faithfully.** Say what was not verified. Say "I haven't run this" when you haven't. Never claim a check passed unless you saw it pass. Give cost where relevant.
- **Confirm before anything hard to reverse or outward-facing**: merging to `main` (Bear has approved specific merges, not a blanket), deleting anything (Bear said yes to exactly one deletion so far), publishing, closing someone's pull request. Bear is quick to answer.
- **Record models and effort from what actually ran, not what you assume.** Subagents' effort turned out to be `medium` in the last rounds, not the `xhigh` the earlier ones had; the transcripts say which.

## 3. The evidence model (do not weaken it)

- An entry is one JSON file in `entries/`. It has claims: `kind`, `definition`, `description` (when present), each `variant`, each `relation`, each `verb`, and the flags `certification`, `certification_scope`, `language_type`.
- Each claim can carry **evidence**: `drafted` (someone proposed it), `checked` (someone checked it, outcome supports or contradicts), `matched_source` (matched to an outside record, with the organization, a link, and how it was verified).
- **What backs a claim** (`lexicon.backs`): a named person's `checked` + supports, or `matched_source` + supports with verification `page-read` or `dump-match`. **A model agreeing with a model never backs a claim**, nor does a search result, a vote, or a model's opinion. Contradicting evidence blocks `reviewed` status until a person settles it.
- Every model run is registered in `data/runs.json` with model, effort and agent. Tag votes ("is this something job listings ask for?") are in `data/assessments.jsonl`; a vote never changes an entry.
- **Source rule** (`docs/SOURCES.md`): use a source only if its licence is clear and can be named; otherwise ignore it and say why. Facts, names and counts are copied; prose is not, unless the licence allows it and the notice says so.
- **Never invent data.** Descriptions come only from facts in a source revision. Counts are rows in datasets, not market share.

## 4. State of the data (verified 2026-11-07)

- **3,688 entries**, 0 validation errors. Classes (worked out from `kind`, never stored): skill 1,954, certification 859, knowledge 518, language 290, ability 67 (52 from O\*NET). 17,097 claims, of which **1,321 are backed**: 104 O\*NET abilities matched to O\*NET 30.2, and 1,217 Wikipedia-derived descriptions. **No claim is backed by a person. No entry is `reviewed`.** Status: 3,555 `machine-drafted`, 133 `proposed` (the original registry).
- **Every entry has had a second-model check** by Claude Opus, and about 2,700 entries also by GPT-6 (an outside reviewer; model and effort self-reported), plus 242 by Muse Spark 1.3. The reviewers disagree a lot: of 8,428 claims both GPT-6 and Opus judged, GPT-6 contradicted 184, Opus 21, and they agree on 15. `docs/REVIEW-FLAGS.md` lists 675 contradicting records and starts with the 114 claims two or more different models contradicted (the likeliest real errors; many are "kind should be standard, not knowledge").
- **13,697 votes** in the ledger. **No tag is unresolved**: all 4,652 legacy tags have an answer; 1,162 got no entry (564 judged not a skill, 598 left unsure).
- **Descriptions**: 1,217 entries have one, adapted from a Wikipedia lead with the revision permalink, dump date and CC BY-SA 4.0 licence on the entry, plus `drafted` and `matched_source` evidence. 67 matched entries were set aside (49 wrong subject or too thin when written, 18 removed after the second-model check); they are in `data/wikipedia-match/20261001/description-skipped.jsonl`. 20 remaining descriptions carry a wording flag (changes meaning or adds information). A rule, not a person, matched the article to the entry (about 97% right in small samples).
- **Wikipedia matching** (`data/wikipedia-match/20261001/`): per entry a relation to a Wikipedia article: `same` 1,284, `related` 425 (a redirect or variant leads to a broader or renamed page: link only, never use its lead as the description), `ambiguous` 77 (a person decides), `none` 1,902. The first tier from the cluster job (`confident`) was wrong about 1 in 8 times; `resolved.jsonl` and `scripts/wikipedia_match/resolve_matches.py` replace it. Known gap: a title with an extra word (entry "Tableau", article "Tableau Software") is never proposed.
- **Classes** (`docs/CLASSES.md`, decided with Bear on 2026-11-01): ability = an enduring attribute (O\*NET's 52); skill = a developed capacity; knowledge = an organised body of facts, "knowing that"; language = its own class (a mix of ability, knowledge, skill and, for human languages, upbringing); certification = a credential an official body attests. A degree is evidence of knowledge of a field, weaker evidence of skill, and not evidence of any single fact. Open items there: a class for personal characteristics (self-starter, patient; about 15 entries in the ability class are really these), `draws_on` (skill to ability) and `attests` (credential to knowledge) relations, evidence-of-capability with years of experience as an amount of evidence, and occupations as a class.
- **Abilities transfer within close occupations**: comparing O\*NET ability profiles with the general level removed, Software Developers vs Computer Programmers 0.92, vs Software QA 0.87, vs Registered Nurses -0.14, two random occupations 0.00, average within a broad SOC group 0.62. Raw ratings look similar everywhere (0.67 for two random occupations), which is the trap. Not yet written into the docs.

## 5. The repository

```
entries/            one JSON file per concept (3,688)
schemas/            JSON Schemas: entry, evidence, certification, assessment, run
tools/              lexicon.py (loader, validator, classes), ingest.py, check_claims.py, assess.py, batch.py, ...
scripts/            review_flags.py, wikipedia_match/ (matching, resolver, descriptions.py), cluster/ (scripts for cluster jobs),
                    oneoff/ (scripts earlier agents wrote to produce answers: kept for the record, not reusable)
data/               runs.json, assessments.jsonl, term-decisions.json, legacy tag lists, wikipedia-match/20261001/, skills_batch_*.md/json
abilities/          O*NET abilities, ratings for all 894 occupations (O*NET 30.2), README with attribution
reviews/            packets for outside reviewers (answers/ and applied/ are empty; both outside reviews are applied)
docs/               SCHEMAS, CLASSES, SOURCES, ENTRY-FORMAT, PIPELINE, OVERNIGHT (full run log), REVIEW-FLAGS, REVIEWER-PROMPT, handoff/
tests/              test_lexicon, test_pipeline (about 100 s), test_provenance, test_schema, test_descriptions, test_wikipedia_resolve
```

Commands (always `python3 -I`, from the repo root):
- `python3 -I tools/lexicon.py validate` must end with `0 errors`. Run it before and after anything that touches `entries/`.
- Tests: `python3 -I tests/test_<name>.py` for each suite; all pass as of the last commit.
- Outside reviewers' answer files go in `reviews/answers/`; `python3 -I tools/check_claims.py check-answers FILE` checks them and `apply-reviews` records them.
- `python3 -I scripts/review_flags.py` regenerates `docs/REVIEW-FLAGS.md`.
- `python3 -I scripts/wikipedia_match/descriptions.py --help` for the description pipeline.

## 6. The cluster (Explorer, Northeastern University Research Computing)

Only Claude Code on Bear's Mac can reach it (key-based ssh, host alias `explorer`). The cloud sessions could not. If a two-factor prompt appears, stop and tell Bear. Rules that held throughout: no sudo, stay inside `/projects/aiskunks`, no secrets anywhere, delete nothing without Bear's explicit yes, Python on the login node is 3.9, many small files are slow on `/projects` (about 2 per second; pack outputs), copy with `tar` over ssh (the Mac's rsync fails), heavy work through Slurm (`short` partition, up to 2 days).

On `/projects/aiskunks`: `skills-lexicon/` (a git checkout; older than `main`; read only for jobs), `enwiki/20261001/` (the Wikipedia dump, compressed, checksums verified), `wordnet/pwn-3.1/` and `wordnet/oewn-2025/`, `onet/30.2/` and `onet/31.0/`, the downloaded Kaggle job datasets (about 2,110 `dataset.zip` folders and growing; the ledger repeats rows from retries), and `skills-lexicon-work/` for job outputs (`wikipedia-match/`, `wikipedia-inspect/`, `data-sources/`). **ESCO was not downloaded**: it needs an email and a privacy-statement click-through (Bear must do it) and its download page states no licence. A processed searchable Wikipedia build is at `/projects/medhavy/fact-checker/data/wikipedia/20261001/` (sqlite with articles, passages, redirects; categories are only in its jsonl files; no infobox data, no link counts). O\*NET 31.0 renamed tables: Skills is now Essential Skills and Transferable Skills; Technology Skills is now Software Skills (with Hot Technology and In Demand columns). Keep both releases and state which one a claim cites.

## 7. Open work, in the order I would do it

The ready-made prompts are in `docs/handoff/prompts/` with their status. Each was written for Claude Code, tested only on fake data, and none of the "NOT RUN" ones has touched the cluster.

1. **Run `07-job-field-survey.md`.** Surveys the job datasets on the cluster for fields that sit unambiguously in their own column (job title, company, location, salary, date, employment type, skills list), with a licence breakdown. Publishes counts only. Bear's partial result so far (dataset counts by header match, which overstate): location 1,488, job title 977, company 900, salary 849, date 712, experience level 655, industry 460, employment type 460, skills list 203.
2. **Run `06-job-title-pilot.md`** on datasets the survey shows have clean title columns and a clear licence: normalise titles, match exactly to O\*NET titles, report the share same/ambiguous/none, hand-check samples. Then decide whether a model step is worth building.
3. **Run `05-onet-technology-match.md`**: O\*NET 31.0 Software Skills (with Hot Technology and In Demand flags) against the lexicon. The lexicon lacks mainstream tech (Git, Jira, Kubernetes, MySQL, MongoDB, Jenkins, Django, Redis, GitHub and others are not entries; none were in the legacy tag list).
4. **ESCO**: Bear completes its form and finds the licence in writing; then add it as a source (SOURCES.md has a row held for it). Use ESCO for vocabulary, hierarchy and alternative labels, not for measurement. Its official crosswalk to O\*NET maps occupations only (as Bear understands it; unverified).
5. **WordNet matching** (no prompt written yet): match entries to WordNet senses with the same relation scheme (same / related / ambiguous / none) and a category-fit rule, to add synonyms and hypernyms as sourced claims. Expect hits mainly on abilities, general skills and human languages; measure before assuming.
6. **Kaggle evidence branch `data/kaggle-occurrence-evidence-20261030`**: unmerged, one commit on `main` at the time, valid, entries untouched; 19,766 observations linked to 2,568 entries and 303 pending candidate skills (the first ones are the missing mainstream tech). Before merging into a public MIT repo, Bear decides about the 5 sources under CC BY-NC or CC BY-NC-SA (4 and 1; also CC BY-SA 4.0 and GPL-2 sources). Recommended: have Bear's local Codex or Claude Code regenerate the release without them and merge that. The 303 candidates then need drafting as entries, which needs a place in the entry format to record where a candidate came from (today's `provenance.legacy_tag` is for the legacy tag lists).
7. **Wikipedia categories to tags and broader relations**: the categories are extracted (`categories.jsonl`) but not attached to entries. Keep all non-maintenance categories as tags with their source; facets (year, licence, implementation language) can fill fields. Parent categories give a first draft of `broader`.
8. **People**: the 425 `related` and 77 `ambiguous` Wikipedia matches; the 20 description wording flags; the 114 claims two models contradicted (many are `kind` standard vs knowledge; probably a rule for the drafting brief).
9. **Open design items** in `docs/CLASSES.md` (characteristics class, `draws_on`, `attests`, evidence of capability) and **occupations as a class** with SOC / O\*NET-SOC identifiers, linked to skills only with sourced weights (O\*NET ratings, ESCO essential or optional, posting counts), each kept separate and never averaged. Bear agreed that occupation carries the abilities and the job description adds the specific skills.
10. **Kaggle datasets Bear wants to publish** (not started), in my suggested order: a catalogue of the job-posting datasets and which fields each has; job titles mapped to occupations; the lexicon itself with its provenance (descriptions as a separate CC BY-SA file); salary by title and country as aggregates with a minimum cell size (keep original currency and period; USD only where the source says USD); a company table; skill co-occurrence and skills by occupation. Rules: only datasets with clear licences, aggregates not scraped rows, every row names its sources, counts are not market share. Bear has company data somewhere that I never saw; ask where.
11. **PR #2** (GPT-6 answers) is redundant because its files are on `main`. It is still open against `overnight-1`. Ask Bear before closing it.
12. **The paper**: before quoting O\*NET's definitions of abilities and skills ("enduring attributes of the individual", "developed capacities"), copy the exact sentences from the O\*NET Content Model page and cite the release. `docs/CLASSES.md` paraphrases from memory and says so.

## 8. Do not

- Treat a model's agreement as evidence, or count a rule-based match as a person's check.
- Merge or push to `main` something Bear has not approved; delete anything on the cluster or in the repo without a clear yes.
- Download or publish from a source whose licence is unclear (ESCO and some Kaggle datasets are in that state).
- Copy Wikipedia text other than the lead, or any posting text or employer names, into the repository.
- Re-run the finished cluster prompts (01 to 03; 04 except ESCO).
- Present counts from datasets as demand.

## 9. Cost

The cloud credits (US$250 of included session credit) ran out. In the cloud session the reported session cost tracked Bear's credit meter closely; the earlier estimate that added subagent costs on top (`scripts/subagent_cost.py`) overstated it. Drafting and review passes cost roughly US$1 per 120 entries per agent. The remaining work above that needs a model (WordNet matching, drafting the 303 candidates, a title-matching model step) is small; the cluster jobs cost no credits.
