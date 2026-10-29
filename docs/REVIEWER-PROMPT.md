# Prompt for outside reviewers

Paste the prompt below into any model that can open web pages (Claude, ChatGPT, Gemini, Grok, Perplexity, or a coding agent such as Codex, Jules or Copilot). It sends the model to the public repo, tells it what to vote on, and tells it how to write its opinion into the JSON. Nothing in it needs editing.

What comes back is recorded as evidence with the model's name and the effort it says it ran at. Both are taken on its word, so the run is marked `external` and the note says they are self-reported. A model's opinion never backs a claim and never changes an entry by itself.

The packets live on the branch `overnight-1`. If you merge that branch into `main`, change the branch name in the prompt (two places).

## 1. The prompt (paste this)

```
You are an independent reviewer for the open "skills lexicon", a dictionary of the things job listings ask for. A model drafted it from general knowledge and no source was checked, so some of it is wrong. I want your honest opinion on it, recorded under your name. Do not be agreeable. A wrong claim marked "supports" is worse than an honest "unsure", and finding the errors is the point.

WHERE TO GO

The repo is public. Read it directly. Do not answer from memory of what it might contain.
  https://github.com/nikbearbrown/skills-lexicon/tree/overnight-1
Everything you need is on the branch "overnight-1" (if that branch no longer exists, use "main"). A file's raw text is at https://raw.githubusercontent.com/nikbearbrown/skills-lexicon/overnight-1/<path>, for example .../overnight-1/reviews/skill/packets/p001.json
If you cannot open GitHub pages or raw files, say so and stop. Do not guess what is in them.

Read these first, in this order:
1. reviews/README.md (what to do and how to hand it back)
2. reviews/BRIEF.md (the exact questions and the answer shape)
3. docs/SCHEMAS.md, only the section "What is in the lexicon, and the four classes"

WHAT YOU ARE VOTING ON

The lexicon holds what job listings ask for, in four classes: abilities, certifications, languages (spoken or programming) and skills (everything else). You give two kinds of opinion.
A. Tags. For each tag in reviews/tags/packets/: is it something job listings ask for? yes, no or unsure.
B. Entries. For each entry in reviews/skill/packets/, reviews/certification/packets/, reviews/language/packets/ and reviews/ability/packets/: is each claim right (definition, kind, certification, certification_scope, language_type)? Is each variant (alternative spelling or abbreviation) ok or bad? Is each relation to another entry ok or bad? And the same yes/no/unsure vote on whether the entry is something job listings ask for.

WHICH PACKETS

A packet is one JSON file of about 40 entries (100 tags for tags). Work in this order: reviews/skill/packets/, reviews/tags/packets/, reviews/certification/packets/, reviews/language/packets/, reviews/ability/packets/. Start at p001 and go as far as you can. If you start a packet, answer every entry in it. Before you start, list reviews/answers/ and reviews/applied/ and skip a packet only if a file from you (your model name in the file name) is already there. Do not skip a packet because a different model did it. Several models voting on the same packet is the point.

STAY INDEPENDENT

Do not open entries/, data/assessments.jsonl, reviews/applied/ or other models' answer files before you answer. They hold other models' opinions, and an independent opinion is worth more. Judge from your own knowledge. You may look things up on the web, but what you record is your opinion, not a quotation.

HOW TO RECORD YOUR OPINION IN THE JSON

You add one new file per packet in reviews/answers/. Never edit entries/, data/ or any file that already exists. The project's own tool reads your file, checks it, and writes your opinion into the entries as evidence carrying your model name, your effort and the date.

File name: reviews/answers/<model>__<effort>__<folder>-<packet>.json
For example: reviews/answers/gemini-3-pro__high__skill-p001.json or reviews/answers/gpt-5__unknown__tags-p004.json
Write the model in lowercase letters, digits, dots and hyphens. For effort write low, medium, high, xhigh or max, or unknown if you do not know or have no such setting. Tell the truth about your model and effort: they are recorded as self-reported.

An entry packet gets this file:

  {"reviewer": {"model": "<your model>", "effort": "<effort>", "date": "<today, YYYY-MM-DD>"},
   "packet": "skill/p001",
   "answers": [
     {"key": "<the entry's key, copied exactly>",
      "claims": {"definition": {"verdict": "supports"},
                 "kind": {"verdict": "contradicts", "note": "a method, not a tool"},
                 "certification": {"verdict": "supports"}},
      "variants": {"ok": ["<label>"], "bad": [{"label": "<label>", "note": "means something else"}]},
      "relations": {"ok": ["<type>:<target key>"], "bad": [{"rel": "<type>:<target key>", "note": "wrong direction"}]},
      "job_listing_vote": {"answer": "yes"}}
   ]}

A tag packet gets this file:

  {"reviewer": {"model": "<your model>", "effort": "<effort>", "date": "<today, YYYY-MM-DD>"},
   "packet": "tags/p001",
   "answers": [
     {"tag": "<the tag exactly as shown>",
      "job_listing_vote": {"answer": "no", "reason": "a physical object, not something an employer asks for"}}
   ]}

Rules:
- verdict is supports, contradicts or unsure. A contradicts needs a note of at most 150 characters saying what is wrong. A note on supports is allowed for a caveat. unsure records nothing, so use it instead of guessing.
- Answer only the claims the entry shows in its packet (definition and kind always; certification, certification_scope and language_type when shown). Judge every variant and relation shown. Leave out any you cannot judge.
- kind must be one of the allowed_kinds listed in the packet. certification is true for a credential an official body attests, including each level of a leveled scheme. certification_scope is single-issuer or many-issuers. language_type is human or programming.
- job_listing_vote answer is yes, no or unsure. A reason of at most 150 characters is required for no and unsure.
- Valid JSON only. No comments, no trailing commas.

HOW TO HAND IT BACK

- If you can run Python and push to GitHub: check each file with  python3 -I tools/check_claims.py check-answers <your file>  and then open a pull request against the branch overnight-1 that adds only your files in reviews/answers/.
- Otherwise: output each answer file as its own JSON code block, with the full file path on the line above it and nothing else in the block. The person who started you will save the files into reviews/answers/. Do not give a summary in place of the files.

When you finish, say in two lines which packets you completed and how many claims you marked contradicts.
```

## 2. Optional: aim a model at one folder (paste one after the prompt)

Without this, the model starts at the first skill packet and goes as far as it can.

Skills (the largest set, never given a second-model check):

```
Do only reviews/skill/packets/p001.json to p005.json.
```

Tags with no entry yet:

```
Do only reviews/tags/packets/p001.json to p005.json.
```

Certifications:

```
Do only reviews/certification/packets/.
```

Languages and abilities:

```
Do only reviews/language/packets/ and reviews/ability/packets/.
```

## 3. When the answers come back

Save each answer file into `reviews/answers/` (or merge the pull request), then:

```bash
python3 -I tools/check_claims.py apply-reviews
```

```bash
python3 -I scripts/review_flags.py
```

The first records the opinions as evidence and votes and moves the files to `reviews/applied/`. A malformed file is refused whole and left where it is, with the reason printed. The second rewrites `docs/REVIEW-FLAGS.md`, the list of entries where a reviewer disagrees with the draft.
