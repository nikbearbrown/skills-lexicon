# Brief for an agent drafting a round of tags

You are drafting dictionary entries for the open skills lexicon (things job listings ask for: skills, abilities, certifications, languages). Work only in your own folder, the current directory (a private copy with no .git). Do not read or write anywhere else except `work/` here for scratch; do not run git or contact GitHub.

**Goal.** Answer the request files already in `work/requests/` (one per legacy tag) from your own knowledge, honestly. A script validates and saves your answers later; humans review every claim. A short entry with true claims beats a long one with doubtful ones. Do not run `make_requests.py`, `tags_to_candidates.py` or a real (non-dry) ingest.

**Read first, in full:** `skills/draft-entry/SKILL.md` (the exact answer shape), `docs/ENTRY-FORMAT.md`, and the section "Drafting from the legacy tag lists" of `docs/PIPELINE.md`.

**Steps.**
1. Print a compact summary of the requests with a short Python snippet (term, origin class, in_lists, nearest id=name); open a full request only when you need it.
2. Write one answer per request to `work/responses/<same file name as the request>`, in exactly the shape in SKILL.md. One Python script that builds the dicts and dumps them is fine.
3. Check: `python3 -I tools/ingest.py work --model-id claude-sonnet-5-5 --effort xhigh --run draft-check --dry-run`. Fix rejections caused by the shape of your answers. Never run it without `--dry-run`.

**Rules.**
- Never pad. If you do not know what a term is, answer `unsure` with a one-sentence reason; do not invent a definition. A generic word, company, place, job title, industry, UI element, symptom or benefit is `not_a_skill`.
- `basis` is `general-knowledge` (there are no postings). Use `guess` only to have a claim thrown away.
- `kind` is exactly one of `allowed.kinds`. ability = an enduring attribute (Oral Comprehension); skill = a developed capacity (Critical Thinking); knowledge = a field or body of facts; named products are tool / platform / framework / library; credential = a certification, certificate, licence, permit, endorsement, degree or clearance; standard = a standard or regulation; method for an approach; the language kinds for languages.
- `certification`: true for a credential attested by an official body and for each level of a leveled scheme; else false. `certification_scope` only when certification is true: `single-issuer` (one body defines and awards it) or `many-issuers` (degrees, state licences). `language_type`: `human` (spoken, signed, extinct), `programming` (any formal language a computer reads: programming, markup, style, query, modelling) or null. If a legacy list in the request says certification or language and you disagree, say why in `annotation_note`.
- Relations only to ids in that request's `nearest`, only when genuinely true. Empty lists are correct. Never give a variant a short form that also matches everyday words.
- If two tags in your slice are the same concept ("X" and "X (Software)"), answer both as `new` with the identical `preferred_name`; the central ingest rejects the second and it is retried later as a variant.
- Use `variant_of` only when the term is exactly the same concept as an entry in that request's `nearest`.
- Official spelling for `preferred_name`; one plain sentence for `definition`, in your own words. Give a variant only if you are sure it means the same.

**Report back** (under 200 words): decision counts (new / variant_of / not_a_skill / unsure), the dry-run result, the five entries you are least sure about. Do not paste entries.
