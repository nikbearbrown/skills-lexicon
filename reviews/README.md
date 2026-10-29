# Outside review: vote on what is in the lexicon

This folder is where models and people outside the project give their opinion on the lexicon, so that every claim has more than one set of eyes on it. Nothing here decides anything. An opinion is recorded as evidence with who gave it (the model and the effort it ran at, or a person's name), and later passes decide.

The lexicon holds what job listings ask for, in four classes: **abilities**, **certifications**, **languages** (spoken and programming) and **skills** (everything else). The entries were drafted by a model from general knowledge, with no source checked. Many are wrong in small ways. Your job is to say where.

## What you are asked to give an opinion on

1. **Tag votes.** Is this tag something job listings ask for: yes, no or unsure? (`reviews/tags/`: 2,165 tags that have no entry yet.)
2. **Claim checks.** For an existing entry, is each claim right: its `definition`, its `kind`, whether it is a `certification`, the `certification_scope` (one issuer or many), the `language_type` (human or programming)? Also each variant (an alternative spelling or abbreviation) and each relation to another entry. (`reviews/skill/`, `certification/`, `language/`, `ability/`.)
3. **A vote on the entry's tag**, in the same answer: is this concept something job listings ask for?

Read [BRIEF.md](BRIEF.md) for the exact questions and the answer shape.

## Where the packets are

Each packet is a JSON file of about 40 entries (100 tags for tag packets), written so you do not need to open anything else.

| Folder | What | Packets |
|---|---|---|
| `skill/packets/` | skills: tools, methods, standards, knowledge. Never had a second-model check | p001 to p054 (2,134 entries) |
| `tags/packets/` | tags with no entry yet, to vote yes, no or unsure on | p001 to p022 (2,165 tags) |
| `certification/packets/` | certifications | p001 to p011 (427 entries) |
| `language/packets/` | human and programming languages | p001 to p003 (120 entries) |
| `ability/packets/` | abilities not taken from O\*NET | p001 (13 entries) |

Do the packets in that order if you cannot do them all. A single packet is useful. Several models voting on the same packet is the point, so do not skip a packet because another model did it. Skip one only if you already answered it.

## How to hand back your opinion

Write one answer file per packet into `answers/`, named `<model>__<effort>__<folder>-<packet>.json`, for example `answers/gemini-3-pro__high__skill-p001.json` or `answers/gpt-5__unknown__tags-p004.json`. Do not edit anything else: not `entries/`, not `data/`. Those are changed only by the project's own tool, which checks everything before it writes. A new file in `answers/` cannot clash with anyone else's.

An answer file wraps your answers with who you are:

```json
{
  "reviewer": {"model": "gemini-3-pro", "effort": "high", "date": "2026-10-30"},
  "packet": "skill/p001",
  "answers": [ ... ]
}
```

- `model`: your model name, as you would write it. `effort`: `low`, `medium`, `high`, `xhigh`, `max`, or `unknown` if you do not know or have no such setting. Both are taken on your word and recorded as self-reported.
- `packet`: the folder and packet name, `skill/p001`, `tags/p004` and so on. A packet starting `tags/` is read as tag votes; any other is read as entry checks.
- `date`: the day you did it, `YYYY-MM-DD`. Leave it out and the day it is recorded is used.

**Entry packets.** One object per entry in the packet, answering every entry:

```json
{"key": "1password",
 "claims": {"definition": {"verdict": "supports"},
            "kind": {"verdict": "supports"},
            "certification": {"verdict": "supports"}},
 "variants": {"ok": [], "bad": []},
 "relations": {"ok": [], "bad": []},
 "job_listing_vote": {"answer": "yes"}}
```

`verdict` is `supports`, `contradicts` or `unsure`. A `contradicts` needs a `note` of at most 150 characters saying what is wrong. A note is also allowed on `supports` for a caveat. `unsure` records nothing, which is better than a guess. Judge each variant and relation in the view: put it under `ok` or `bad` (`variants.bad` takes `{"label": "...", "note": "..."}`, `relations.bad` takes `{"rel": "<type>:<key>", "note": "..."}`). Leave out any you cannot judge. Only answer the claims the entry's view shows.

**Tag packets.** One object per tag:

```json
{"tag": "Abacus", "job_listing_vote": {"answer": "no", "reason": "a counting device, not something an employer asks for"}}
```

A `reason` of at most 150 characters is required for `no` and `unsure`.

**Check the file before you send it** if you can run Python 3:

```bash
python3 -I tools/check_claims.py check-answers reviews/answers/your-file.json
```

**Sending it.**

- If you can push to GitHub: open a pull request against the `overnight-1` branch that adds only your files in `reviews/answers/`.
- If you cannot: give the answer file as a single JSON code block per packet, with its file name above it. The person who started you saves it into `reviews/answers/`.

## For the maintainer: recording what comes back

```bash
python3 -I tools/check_claims.py apply-reviews
```

This reads every file in `answers/`, refuses any that are malformed (leaving them where they are), and for the good ones:

- registers a run named `external-<date>-<model>-<effort>` in `data/runs.json` with agent `external`, noting that the model and effort are self-reported and not verified;
- adds a `checked` evidence record, by that model, on each claim it judged (`supports` or `contradicts`; `unsure` adds nothing);
- adds the model's tag votes to `data/assessments.jsonl`;
- moves the file to `applied/`, so it is not read twice.

A model's check never backs a claim, and an unresolved `contradicts` blocks `reviewed`. It is evidence for a person to weigh. `python3 -I scripts/review_flags.py` lists the entries where reviewers disagree with the draft.

To rebuild the packets after the dictionary changes: `python3 -I tools/check_claims.py build-reviews`.
