# Abilities, knowledge, skills, languages and certifications: why they are kept apart

Job listings ask for all of these in the same breath ("strong written communication, Python, fluent Spanish, PMP certified, good eyesight"). The lexicon keeps them apart because **how a person gets or improves each one differs**, and that difference is what a worker, a trainer or an employer acts on.

## The rule

| Class | Defining idea | How it improves | Basis |
|---|---|---|---|
| **Ability** | An enduring attribute of the individual: strength, vision, coordination, spatial orientation. | Slowly, within limits set by the person; it can be trained but it has a ceiling. | O\*NET's 52 Abilities |
| **Skill** | A developed capacity: something learned and improved with practice and instruction. | With practice and teaching; no fixed ceiling. People with certain abilities pick some skills up faster, but the skill itself is learned. | O\*NET's Skills and Knowledge, then other sources |
| **Knowledge** | An organised body of facts and principles a person has learned and can apply: "knowing that". Contract law, organic chemistry, network protocols. | By study; checked by explaining or answering, not by performing. | The `knowledge` kind; O\*NET's 33 Knowledge areas |
| **Language** | A learned system of communication, human or programming. The entry names the system (Spanish, Python); what a listing asks for is *proficiency* in it, a developed capacity, so it belongs with the learned things, not with abilities. It has its own scale of levels (human languages: CEFR). | With study and use, up a level ladder. | `language_type`: `human` or `programming` |
| **Certification** | A credential an official body attests: certification, licence, degree, clearance. | By meeting the body's requirements; it is awarded, not practised. | The body's name and a link to it |

**The test, for an entry that could be either an ability or a skill:** what improves it, by how much, and is there a ceiling? An enduring attribute with a ceiling is an ability. A capacity that is built by practice is a skill.

The definitions are O\*NET's: abilities are enduring attributes of the individual that influence performance; skills are developed capacities. The wording here is paraphrased from memory of the O\*NET Content Model; before it is quoted in a paper, copy the exact sentences from the O\*NET Content Model page and cite the release.

## Knowledge, skill, ability and other characteristics (KSAO)

Industrial-organisational psychology's frame for what a job needs is KSAO: knowledge, skills, abilities and other characteristics. The lexicon's classes follow it: knowledge, skill (including the tools and methods a person uses) and ability are classes of their own, and "other characteristics" (self-starter, detail-oriented, patient; dispositions that are neither abilities nor skills) is the one class not built yet (open item 1). Languages and certifications are the lexicon's own additions, because KSAO has no place for a communication system with a level ladder, or for a credential that is awarded.

Language is a mix of all of them, which is why it is a class of its own. Proficiency draws on abilities (aptitude for language, O\*NET's Oral Comprehension and Oral Expression), on knowledge (grammar, vocabulary, notation) and on skill (using it fluently), and for a human language it also comes from **experience**: a person who grew up speaking one or more languages did not acquire them by instruction or deliberate practice, and a native speaker, a heritage speaker and a classroom learner reach the same level by different routes with different evidence. Whatever the route, it is learned, not inherited. A programming language is the same: a formal notation, where proficiency is knowledge of the notation plus the skill of writing programs in it.

**Evidence for a language** differs from the other classes for the same reason. The strongest kinds are an attestation (a CEFR level from an exam such as DELF, DELE, TOEFL or IELTS; for programming languages, a portfolio of code) and, for human languages, a lived-in history (native or heritage speaker, years living in the language). A listing that says "native speaker" asks for the upbringing route, not for a score; one that says "C1" asks for an attested level. Neither is recorded yet; the class exists first, and its evidence types follow.

## What the databases do

- **O\*NET** keeps the split: 52 abilities, 35 skills, 33 knowledge areas. The lexicon follows it.
- **ESCO** folds skills, knowledge and language into one pile ("skills and knowledge concepts"). We do not follow it on this point. We use ESCO to find skills and wording we are missing, with its licence recorded, and we classify what we take from it by the rule above.
- **Job listings** blur all of it. That is a finding, not a model to copy.

The two layers line up imperfectly: O\*NET has the ability "Oral Expression" and the skill "Speaking", which describe nearly the same thing at two levels. That is not a conflict. The ability is the underlying attribute, the skill is its trained use. A relation between them (a skill draws on abilities) is planned, but it stays empty until a source supports each link; neither O\*NET nor ESCO records one.

## Open items

1. **A class for personal characteristics.** Industrial-organisational psychology's KSAO frame (knowledge, skills, abilities, **other characteristics**) has a place for self-starter, detail-oriented, patient and team player. Those are dispositions, neither abilities nor skills. About 15 entries in the ability class are not O\*NET abilities, and several of these (Adaptability, Self-starter, Patience) are really dispositions. They should move to their own class once it exists.
2. **Knowledge versus skill.** Knowing about something is not the same as being able to do it. The `knowledge` kind already marks this; the class column does not yet.
3. **The skill-to-ability relation (`draws_on`)**, as above.

4. **Evidence of capability, and years of experience as an amount of it.** Knowledge, skills and abilities are what a person has; portfolios, publications, projects, references, assessments and certifications are evidence of them, and a listing often asks for the evidence by name ("portfolio required", "5+ years"). The idea recorded here: years of experience can be read as *a lot or a little evidence* for a capability. If it is built, keep it as a stated quantity (bands such as under 1, 1 to 3, 3 to 5, over 5 years, with the mapping written down), attach it to the capability and not to the person as a whole, treat it as the weakest kind of evidence (self-reported, silent on quality), and count independent kinds of evidence (a portfolio, a reference and a certification together) in preference to adding up years. Do not collapse it into one score until a scheme has been tested against real outcomes. Not built; may belong in a separate paper.

5. **A degree is evidence of knowledge of a field.** Agreed 2026-11-01. A degree is a credential an accredited body attests, so it is the strongest kind of evidence of *knowledge*, but it is weaker evidence of *skill* (degrees mostly test what was learned, not whether the work can be done; placements, labs and theses add some practice evidence), and it attests the field as a whole, to a depth set by how specific the degree is (a Master's in Chemical Engineering says more about that field than a general science degree does). It does not attest any single fact in the field. If built: an `attests` relation from a credential to the knowledge fields it covers, filled from a source (the programme's accreditation, its Wikipedia or ESCO entry) and never guessed. Not built.

## Decision record

2026-11-01, Bear: (0) knowledge is its own class, taken out of skill (518 entries); (1) adopt O\*NET's distinction between ability (enduring attribute) and skill (developed capacity) as the basis for the lexicon and the paper; use ESCO to add what is missing, not to change this distinction. (2) A degree is evidence of knowledge of a field, not of skill and not of a single fact in it (open item 5).
