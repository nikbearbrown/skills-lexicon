---
name: draft-entry
description: Draft one skills-lexicon dictionary entry from a request file (a term seen in job postings, its quotes, and the nearest existing entries). Use when asked to answer a request in work/requests/.
---

## The task

You are helping build an open dictionary of skills as they appear in job postings. You get one request: a **term** that appeared in postings, a few **quotes** showing it in use, and the **nearest** entries already in the dictionary. Answer with one JSON object, and nothing else.

Decide first:

- `not_a_skill`: the term is a company, a place, a benefit, a job title, a generic word or anything else that is not a skill, tool, method, language, credential or ability.
- `variant_of`: the term means exactly the same concept as one entry in `nearest` (a different spelling, abbreviation or product name). Related is **not** the same: Angular and AngularJS, two languages that share a name, and a tool and the field it belongs to are separate concepts. Put that entry's id in `variant_of`.
- `new`: it is a skill and no entry in `nearest` is the same concept. Fill in `entry`.
- `unsure`: you cannot tell from the quotes and what you know. A person will look. This is a good answer when it is true.

For `new`, the entry has:

- `preferred_name`: the official spelling (PostgreSQL, not Postgres). The term as seen is added as a variant for you.
- `kind`: exactly one of `allowed.kinds`. Keep skills and abilities apart, as O*NET does: an **ability** is an enduring attribute a person has (Oral Comprehension, Spatial Orientation); a **skill** is a developed capacity to do something (Critical Thinking, Equipment Maintenance); **knowledge** is a body of facts or a field; a named product you use is a **tool**, **platform**, **framework** or **library**; a **credential** is a certification, certificate, licence, permit, endorsement, degree or clearance; a published standard or regulation is a **standard**. If none fits, answer `unsure`.
- `definition`: one plain sentence, and `definition_basis`.
- `variants`: other ways to write the same concept, each with a `basis`. Leave empty if you know none.
- `relations`: only to entries in `nearest`, by id. Types: `broader` (the target is a broader concept), `part_of` (this is a part of the target), `related`, `contrast`. Each has a `basis`.
- `verbs`: what a posting asks you to do with it (query, deploy, maintain), each with a `basis`.
- `certification`: `{"value": true|false, "basis": ...}`. **True** when the concept is a credential attested by an official body: a certification, certificate, licence, permit, endorsement, or an academic degree (associate, bachelor's, master's, doctorate). Each level of a leveled scheme is a certification (DoD IAM Level I, a vendor's Associate and Professional levels). **False** otherwise, including a standard or regulation that a credential may test for (NFPA 70E, Regulation SHO) and a school subject. Always answer it.
- `certification_scope`: `{"value": "single-issuer"|"many-issuers", "basis": ...}`, only when `certification` is true. **single-issuer** when one organization defines and awards the credential, even if many providers teach toward it (an AWS certification, an FAA certificate, a CompTIA exam). **many-issuers** when many independent bodies award the same kind of credential: academic degrees (associate, bachelor's, master's, doctorate), graduate certificates, and licences or endorsements that each state or country issues under a common standard.
- `language_type`: `{"value": "human"|"programming"|null, "basis": ...}`. **human** for a human language: spoken, signed or extinct (French, Marathi, Phoenician). **programming** for any formal language a computer reads: a programming language, and also a markup, style, query or modelling language (Python, HTML, CSS, SQL, UML). **null** when the concept is not a language at all. A field of study about language (natural language processing) is not a language. Always answer it.
- `annotation_note`: one short sentence, needed only when a legacy list in the request says the term is a certification or a language and you disagree. Say why.

A request may say that a legacy certification or language list includes the tag. That list has not been checked. Treat it as a hint, decide for yourself, and disagree with it when you have reason to.

`basis` says where each claim came from, and it must be honest:

- `posting`: the quotes show it.
- `general-knowledge`: you know it, but the quotes do not show it.
- `guess`: you are not sure. **Guesses are thrown away**, so include one only if you want it logged as dropped.

Rules:

- Do not fill a field to look complete. An empty list is a correct answer. A short entry with true claims is better than a long one with doubtful ones.
- Do not invent relations to entries you were not shown.
- Never state something as `posting` unless the quotes show it.
- Your answer is a draft. A person checks it later, and nothing you write counts as confirmed.

Output exactly this shape (no code fence, no commentary):

```
{"decision": "new|variant_of|not_a_skill|unsure",
 "variant_of": null,
 "reason": "one short sentence",
 "entry": {
   "preferred_name": "", "kind": "", "definition": "", "definition_basis": "posting|general-knowledge|guess",
   "variants": [{"label": "", "basis": ""}],
   "relations": [{"type": "", "target": "<id of an entry in nearest>", "basis": ""}],
   "verbs": [{"verb": "", "basis": ""}],
   "certification": {"value": false, "basis": ""},
   "certification_scope": {"value": "single-issuer|many-issuers", "basis": ""},
   "language_type": {"value": null, "basis": ""},
   "annotation_note": ""
 }}
```

Leave out `certification_scope` unless `certification` is true.

`entry` is needed only when the decision is `new`; otherwise use `null`.

## If you are an agent with file access

1. Read each file in `work/requests/` that has no file of the same name in `work/responses/`.
2. Write your JSON answer to `work/responses/<same file name>`.
3. Do not edit anything in `entries/`. A script checks your answers and saves them: `python3 -I tools/ingest.py work --model-id <your model id> --run <a run label>`. The operator supplies the model id, not you, so the record cannot be wrong about who said it.
