# Abilities, skills, languages and certifications: why they are kept apart

Job listings ask for all four in the same breath ("strong written communication, Python, fluent Spanish, PMP certified, good eyesight"). The lexicon keeps them apart because **how a person gets or improves each one differs**, and that difference is what a worker, a trainer or an employer acts on.

## The rule

| Class | Defining idea | How it improves | Basis |
|---|---|---|---|
| **Ability** | An enduring attribute of the individual: strength, vision, coordination, spatial orientation. | Slowly, within limits set by the person; it can be trained but it has a ceiling. | O\*NET's 52 Abilities |
| **Skill** | A developed capacity: something learned and improved with practice and instruction. | With practice and teaching; no fixed ceiling. People with certain abilities pick some skills up faster, but the skill itself is learned. | O\*NET's Skills and Knowledge, then other sources |
| **Language** | A learned system of communication, human or programming. Learned like a skill, but it has its own scale of levels (human languages: CEFR). | With study and use, up a level ladder. | `language_type`: `human` or `programming` |
| **Certification** | A credential an official body attests: certification, licence, degree, clearance. | By meeting the body's requirements; it is awarded, not practised. | The body's name and a link to it |

**The test, for an entry that could be either an ability or a skill:** what improves it, by how much, and is there a ceiling? An enduring attribute with a ceiling is an ability. A capacity that is built by practice is a skill.

The definitions are O\*NET's: abilities are enduring attributes of the individual that influence performance; skills are developed capacities. The wording here is paraphrased from memory of the O\*NET Content Model; before it is quoted in a paper, copy the exact sentences from the O\*NET Content Model page and cite the release.

## What the databases do

- **O\*NET** keeps the split: 52 abilities, 35 skills, 33 knowledge areas. The lexicon follows it.
- **ESCO** folds skills, knowledge and language into one pile ("skills and knowledge concepts"). We do not follow it on this point. We use ESCO to find skills and wording we are missing, with its licence recorded, and we classify what we take from it by the rule above.
- **Job listings** blur all of it. That is a finding, not a model to copy.

The two layers line up imperfectly: O\*NET has the ability "Oral Expression" and the skill "Speaking", which describe nearly the same thing at two levels. That is not a conflict. The ability is the underlying attribute, the skill is its trained use. A relation between them (a skill draws on abilities) is planned, but it stays empty until a source supports each link; neither O\*NET nor ESCO records one.

## Open items

1. **A class for personal characteristics.** Industrial-organisational psychology's KSAO frame (knowledge, skills, abilities, **other characteristics**) has a place for self-starter, detail-oriented, patient and team player. Those are dispositions, neither abilities nor skills. About 15 entries in the ability class are not O\*NET abilities, and several of these (Adaptability, Self-starter, Patience) are really dispositions. They should move to their own class once it exists.
2. **Knowledge versus skill.** Knowing about something is not the same as being able to do it. The `knowledge` kind already marks this; the class column does not yet.
3. **The skill-to-ability relation (`draws_on`)**, as above.

## Decision record

2026-11-01, Bear: adopt O\*NET's distinction between ability (enduring attribute) and skill (developed capacity) as the basis for the lexicon and the paper; use ESCO to add what is missing, not to change this distinction.
