# What to judge

## Entry packets (certification, language, ability, skill)

Each packet is a list of dictionary entries about things job listings ask for. Judge every claim from your own
knowledge, independently. You are a reviewer: say `contradicts` when a claim is wrong or misleading, `supports` when it is right,
`unsure` when you cannot tell. Do not be agreeable; a wrong definition marked `supports` is worse than an honest `unsure`.
Drafts written from memory are often wrong about issuers, scope and kind, so check those closely.
- A note is allowed on any verdict, including `supports`: use it for a caveat (for example "retired in 2017").
- A definition that is true but uninformative: `supports` with a note, or `unsure`. Use `contradicts` only when it is wrong or misleading.
- A short form (abbreviation) is an ok variant only if it means this concept and not something else; otherwise mark it bad.
- A course-completion card, a licence endorsement and a level of a leveled scheme all count as certifications if an official body attests them.
Answer shape, one object per entry, in a JSON list:
{"key": "<entry key>",
 "claims": {"definition": {"verdict": "supports|contradicts|unsure", "note": "<=150 chars, required when contradicts"},
            "kind": {...}, "certification": {...}, "certification_scope": {...}, "language_type": {...}},   // only the claims the entry has
 "variants": {"ok": ["<label>"], "bad": [{"label": "<label>", "note": "..."}]},        // judge each variant; leave out any you cannot judge
 "relations": {"ok": ["<type>:<target key>"], "bad": [{"rel": "<type>:<target key>", "note": "..."}]},
 "job_listing_vote": {"answer": "yes|no|unsure", "reason": "<=150 chars, required unless yes"}}
`kind` must be one of the allowed kinds; `certification` is true for a credential attested by an official body (and each level of a
leveled scheme); `certification_scope` is single-issuer (one body issues it, such as AWS Certified Solutions Architect) or many-issuers
(many bodies issue it, such as a bachelor's degree); `language_type` is human (spoken, signed, extinct) or programming (any formal
language a computer reads).
`job_listing_vote`: is the concept something job listings ask for (a skill, ability, certification or language)?

## Tag packets (tags)

Each packet is a list of tags from job-listing tag lists. For each, vote on one question: is this something job listings ask for,
as an ability, a certification, a language (spoken or programming) or a skill (a tool, method, standard, area of knowledge)?
- `yes`: a real, specific thing an employer could ask a candidate for. `no`: not that (a person or company name, a physical object, a
  sentence fragment, a section heading, a typo, a generic word). `unsure`: you do not know what the tag is, or it could go either way.
- Give a `reason` (at most 150 characters) for every `no` and every `unsure`. A reason is optional for `yes`.
- Vote on the tag as written. Do not look up other models' answers; they are not in the packet on purpose.
Answer shape, one object per tag, in a JSON list:
{"tag": "<the tag exactly as shown>", "job_listing_vote": {"answer": "yes|no|unsure", "reason": "<=150 chars"}}
