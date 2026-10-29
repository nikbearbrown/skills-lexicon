# Entry format

One file per concept: `entries/<key>.json`. The validator (`tools/lexicon.py`) is the authority; this page explains the fields.

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | A random 10-character id of lower-case letters and digits, with at least one digit, starting with a letter (so a spreadsheet never reads it as a number). It carries no meaning and no order. Compared case-insensitively, stored lower case. Never reused. |
| `former_ids` | no | Ids this entry had before, such as the registry's `skill:0082`. `lexicon.find()` resolves them. A former id belongs to one entry only. |
| `key` | no | Short slug; if present it must match the file name. |
| `preferred_name` | yes | The canonical name. Use the official spelling (PostgreSQL, not Postgres). |
| `kind` | yes | Lower-case words joined by hyphens, e.g. `programming-language`, `method`, `tool`. |
| `definition` | yes | One plain sentence. |
| `certification` | no | `true` if the concept is a credential attested by an official body: a certification, certificate, licence, permit, endorsement, or an academic degree (associate, bachelor's, master's, doctorate). `false` if it was assessed and is not. Absent if nobody has assessed it. A standard or regulation that a credential tests for is `false`. A claim, so it has its own evidence. |
| `language_type` | no | Only on a language: `programming`, `spoken` (human, including signed and extinct), or `other` (markup, query and modelling languages such as HTML or XBRL). Absent when the concept is not a language. A claim, so it has its own evidence. |
| `name_match` | no | `word_ci` (default) or `exact_case`. Use `exact_case` for short names like `R` or `Go`. |
| `needs_context` | no | Context tags that must be present for the name and variants to match (e.g. `["finance"]`). |
| `name_ambiguous` | no | `true` if another concept shares this name and context cannot separate them. |
| `variants` | no | Other ways of writing it: `{label, match, needs_context?, ambiguous?}`. Abbreviations, spelling and punctuation variants, product names that mean the same thing. |
| `relations` | no | `{type, target, rolls_up?, source?}`. See below. |
| `verbs` | no | What an ad asks you to do with it (query, deploy, maintain). |
| `status` | yes | `machine-drafted`, `proposed`, `reviewed`, `deprecated`. |
| `provenance` | yes | `{source, date, reviewed_by}`. |
| `evidence` | see below | Who said what, and what checked it, per claim. |
| `replacements` | if deprecated | Ids that replace this entry. |
| `notes` | no | Reasoning a reviewer needs, including open disagreements. |

## Relations

Stored on one side only; the index derives the inverse.

| Stored type | Read as | Derived inverse |
|---|---|---|
| `broader` | the target is a broader concept (PostgreSQL → SQL) | `narrower` |
| `part_of` | this is a part of the target (PL/pgSQL → PostgreSQL) | `has_part` |
| `related` | linked but not the same and not broader | `related` |
| `contrast` | commonly set against the target (NoSQL ↔ SQL). Not a strict antonym. | `contrast` |

`rolls_up` (only on `broader` and `part_of`): `true` means a mention of this concept also counts toward the target. Unset means no: count the direct mention only. A reviewer decides, and shows both counts.

## Evidence (provenance per claim)

A claim is one assertion: `kind`, `definition`, each variant, each relation, each verb. Its key is:
`kind`, `definition`, `variant:<normalized label>`, `relation:<type>:<target id>`, `verb:<normalized verb>`.

Each evidence record is `{field, by, action, date, outcome?, ref?, note?, run?}`:

| `action` | `by` | Meaning |
|---|---|---|
| `drafted` | `model:<model id>` or `human:<name>` | Someone proposed this claim. For a model, put the prompt version or run id in `run`, and the posting sentence it saw in `note`. |
| `checked` | `human:<name>` or `model:<model id>` | Someone checked it. `outcome` is `supports` or `contradicts`. |
| `matched_source` | `source:<name>` | The claim was matched to an outside record. Needs `ref` (URL, code or ad id) and an `outcome`. |

An evidence record may also carry `flag`: `disagrees_with_legacy` (the model and a legacy certification/language list or class differ) or `not_in_legacy` (the model says certification or language and no legacy list does). A flag asks a person to look. It never backs or contradicts a claim.

An entry drafted from a legacy tag has `provenance.legacy_tag`: `{sources: [{file, rows, class}], class, in_lists, class_conflict?}`. The lists are `data/skills_tags.csv`, `data/skills-certification.csv` and `data/skills-language.csv`. They are unchecked hints, not evidence.

What counts: only a person's `checked`+`supports`, or a `matched_source`+`supports`, backs a claim. A model checking a model's claim is recorded and visible but never backs it, because two models can share one mistake.

## Rules the validator enforces

- A `machine-drafted` entry has a `drafted` record for every claim.
- A `reviewed` entry has a backing record for every claim, a named `reviewed_by`, and no `contradicts` record outstanding. To resolve a contradiction, change the claim or remove it; the history stays in git.
- Evidence must point at a claim that exists in the entry.

- Two concepts may share a surface form only if their `needs_context` differ, or both mark it ambiguous. Related is not synonym.
- Relation targets exist; no self-relations; no loops in `broader`/`part_of`.
- A `deprecated` entry names its replacements.
