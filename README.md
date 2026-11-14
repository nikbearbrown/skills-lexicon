# Skills Lexicon

Skills Lexicon is an open dictionary and developing ontology of the capabilities and qualifications employers ask for: **skills, knowledge, abilities, languages, and credentials**. Each concept has a canonical name, spelling variants and synonyms, a definition, and evidence about its classification and relationships. It supports consistent matching across job postings, resumes, and course tags—for example, resolving **Postgres** and **PostgreSQL** to one concept.

The project is led by **Nik Bear Brown**. Repository copyright: **Humanitarians AI Incorporated**.

## Current inventory at a glance

**Recounted on November 14, 2026, from `main` at [`82498e3`](https://github.com/nikbearbrown/skills-lexicon/commit/82498e33f014ad0a138d242aba12312a9bfeef10).** These are inventory counts, not counts of human-reviewed concepts or labor-market demand. Work on separate branches is listed below and is excluded from these totals.

| Class | Concepts | What is counted |
|---|---:|---|
| **Skills** | **1,954** | Developed skills plus tools, platforms, methods, libraries, frameworks, and standards |
| **Knowledge** | **518** | Fields, facts, principles, and subject-matter concepts |
| **Abilities** | **67** | 52 O*NET abilities plus 15 additional draft concepts |
| **Languages** | **290** | 158 human languages and 132 formal/computer languages, counted by `kind` |
| **Certifications and other credentials** | **859** | Certifications, licences, degrees, certificates, permits, endorsements, and clearances |
| **Total canonical concepts** | **3,688** | One JSON entry per concept; variants are not additional concepts |

**Review readiness:** 3,555 entries are `machine-drafted`, 133 are `proposed`, **0 are `reviewed`**, and 0 are `deprecated`. Of 17,097 individual claims, **1,321 (7.73%)** meet the repository's source-backing rule; **0 are backed by a human check**. Having a source-backed description does not make the whole entry reviewed. Under the project's policy, only reviewed entries should feed published skill counts.

The older figure of 2,472 skills included the 518 knowledge concepts. Knowledge is now a separate class: **1,954 + 518 = 2,472**.

Read the [detailed state and terminology report](docs/SKILLS-LEXICON-REPORT.md) for definitions, limitations, job-title mapping, branch results, and priorities. The [machine-readable snapshot](docs/summary-stats-2026-11-14.json) and [recount script](scripts/summary_stats.py) make these numbers reproducible.

## What kinds of skills do we have?

The broad **skill class** contains several finer `kind` values. A tool name represents a technology someone may need to use; it is not itself a measured level of proficiency.

| Kind within the skill class | Concepts |
|---|---:|
| Developed skills (`skill`) | 689 |
| Tools | 498 |
| Platforms | 219 |
| Methods | 219 |
| Libraries | 129 |
| Standards and regulations | 115 |
| Frameworks | 85 |
| Work activities | 0 |
| **Total** | **1,954** |

`work-activity` is supported by the schema but has no entries yet. The broad class is computed by [`lexicon.top_class`](tools/lexicon.py); it is not an independently maintained label.

## What kind of knowledge do we have?

There are **518 entries with `kind: knowledge`**. They range from broad disciplines to specific technical concepts. These examples are present in the data; the thematic groupings below are explanatory, not an implemented classification or counted sub-taxonomy.

| Subject area | Examples in the lexicon |
|---|---|
| Computing, data, and AI | Computer science, Database systems, Computer networking, Artificial intelligence, Large language models, Knowledge graphs |
| Mathematics and engineering | Mathematics, Statistics, Boolean algebra, Engineering statics, Fluid statics, Ohm's law |
| Medicine and life sciences | Cardiovascular physiology, Neurobiology, Food microbiology, Pharmacogenetics, Clinical medical ethics |
| Business, finance, and accounting | Corporate finance, Cost accounting, Capital asset pricing model, Counterparty risk, Debits and credits |
| Law, policy, and governance | Administrative law, Human rights law, Labour law, Intellectual property, Public policy |
| Education, arts, and humanities | Art history, Music theory, Ancient philosophy, Historical linguistics, Special education |
| Environment and infrastructure | Climate variability and change, Renewable energy, Circular economy, Urban sustainability, Sustainable infrastructure |

These are the lexicon's current classifications, not a verified import of O*NET's 33 Knowledge areas. Some assignments need correction: reviewers have flagged entries such as NFPA 70E and ABEC scale as standards rather than knowledge. See [review flags](docs/REVIEW-FLAGS.md).

## Abilities and occupational ratings

An **ability** is an underlying attribute that influences performance; a **skill** is a developed capacity to perform work; **knowledge** is understanding of facts and principles. These distinctions follow the project's O*NET-based approach. Abilities can develop, and a name alone does not establish a person's ability or competence. See [class definitions](docs/CLASSES.md) and the [report's explanation](docs/SKILLS-LEXICON-REPORT.md#skills-abilities-and-knowledge).

| O*NET ability category | Definitions |
|---|---:|
| Cognitive | 21 |
| Psychomotor | 10 |
| Physical | 9 |
| Sensory | 12 |
| **O*NET total** | **52** |
| Additional draft ability concepts | 15 |
| **Lexicon ability total** | **67** |

The additional 15 include Adaptability, Attention to detail, Patience, and Self-starter. Several are better understood as work styles or personal characteristics; a separate class is planned.

The [`abilities/`](abilities/README.md) dataset also contains:

- **1,016 occupation codes and titles**, of which **894** have ability ratings and **122** do not.
- **46,488 occupation–ability rating rows**: 894 occupations × 52 abilities, from O*NET 30.2.
- Level ratings on the **0–7 scale**, including rater counts, standard errors, confidence intervals, and dates.
- **68 rows marked for suppression** and **7,410 marked not relevant**; consumers must preserve those flags.
- A smaller six-occupation view with **312 ratings**, already included in the full set.

These ratings describe occupational requirements. They are not ratings of individual workers, counts of job postings, or estimates of AI replacement.

## Languages and credentials

| Language kind | Concepts |
|---|---:|
| Human language | 158 |
| Programming language (including query languages such as SQL) | 112 |
| Markup language | 10 |
| Modeling language | 7 |
| Style language | 3 |
| **Total** | **290** |

These totals use `kind`, which drives the top-level class. The optional `language_type` flags are incomplete: 157 `human`, 116 `programming`, and 17 unset. They should not replace the kind-based inventory totals. Language entries name systems of communication; a person's proficiency, such as a CEFR level or demonstrated programming competence, is not yet represented as a capability assessment.

The **859 credential concepts** have 321 `single-issuer`, 522 `many-issuers`, and 16 unset issuer-scope flags. The schema can hold issuers, credential type, status, requirements, renewal, jurisdiction, and sources, but field support does not imply that those facts have been verified for every credential. A degree or certificate is evidence about a qualification, not automatic proof of every associated skill.

## Synonyms, relationships, and job titles

| Lexical or relationship measure | Count |
|---|---:|
| Canonical concepts | 3,688 |
| Variant records attached to concepts | 2,940 |
| Concepts with at least one variant | 2,023 |
| Distinct normalized names and variants | 6,625 |
| Concept-to-concept relation records | 443 |
| `related` relations | 350 |
| `broader` relations | 79 |
| `part_of` relations | 9 |
| `contrast` relations | 5 |
| Relations with count roll-up enabled | 0 |

**Concept synonyms work today.** Variants attach to one canonical concept, so `Postgres` resolves to PostgreSQL and `Golang` to Go. Case-sensitive matching, context requirements, and ambiguity flags help distinguish short or overloaded terms. Variants are draft assertions subject to review; related concepts must not automatically be treated as synonyms. The 6,625 normalized forms are deduplicated labels, not 6,625 skills.

**Job-title synonym mapping is a separate, unfinished layer.** The repository has 1,016 O*NET occupation titles and a [job-title pilot script](scripts/cluster/title_pilot.py) that normalizes titles and proposes matches to supplied O*NET title tables. It returns `same`, `ambiguous`, or `none`; `same` means one candidate occupation code, not human-verified equivalence. No completed job-title alias mapping dataset is committed on `main`.

The intended mapping is **raw job title → normalized title/alias → canonical occupation → associated capabilities**. Two titles can refer to the same occupation without being interchangeable in seniority, specialty, or duties. For example, an abbreviation can be an alias, while “Senior Software Engineer” carries seniority that must be retained. Occupations are not yet a class in `entries/`, and skill-to-occupation mappings are not a completed general-purpose service. See the [title-mapping analysis](docs/SKILLS-LEXICON-REPORT.md#job-title-synonyms-and-occupation-mapping).

## Evidence and review coverage

| Measure | Count |
|---|---:|
| Individual claims | 17,097 |
| Claims backed under the repository rule | 1,321 |
| O*NET-backed ability claims | 104 (kind and definition for 52 abilities) |
| Source-backed Wikipedia descriptions | 1,217 |
| Human-backed claims | 0 |
| Assessment vote records | 13,697 |
| Model contradiction records | 675 |
| Entries with model contradictions | 456 |
| Claims contradicted by at least two different models | 114 |
| Existing descriptions with contradiction flags | 20 |

A supporting human check or a supporting source match verified by `page-read` or `dump-match` backs a claim. A model draft, another model agreeing, a vote, or a search snippet does not. Evidence belongs to individual claims: classification, definition, variant, relation, description, or other supported fields. See [schemas and evidence](docs/SCHEMAS.md).

Wikipedia resolution covers all 3,688 entries: **1,284 `same`, 425 `related`, 77 `ambiguous`, and 1,902 `none`**. Of the 1,284 `same` matches, 1,217 have descriptions; 67 were set aside. These are automated article-identity decisions, not human review. Use `resolved.jsonl`, not the older first-pass `confident` totals in `summary.json`.

The three legacy CSV lists contain **4,880 distinct normalized tags**: 3,721 match a current canonical name or variant, and 1,159 have only a recorded decision. All have a recorded disposition, but an `unsure` decision remains substantively unresolved. The decision file has **1,162 records** (564 `not_a_skill`, 598 `unsure`); three tags also match current entries, so these totals overlap. Earlier documentation's 4,652-tag figure does not reproduce across the current three lists.

## What the software does

1. Loads and validates one JSON record per concept, including stable IDs, former IDs, external identifiers, evidence, and relation targets.
2. Builds a surface-form index for matching canonical names and variants in supplied posting text.
3. Extracts known concepts and proposes unfamiliar candidate terms with short supporting excerpts.
4. Prepares drafting requests for a person or language model, validates answers, and records new entries, aliases, or `not_a_skill`/`unsure` decisions.
5. Records model runs, votes, claim checks, contradictions, and source matches without treating model agreement as verification.
6. Resolves Wikipedia candidates and attaches adapted descriptions with revision-specific attribution.
7. Provides O*NET ability definitions and occupational level ratings for downstream analysis.

See [the pipeline](docs/PIPELINE.md), [entry format](docs/ENTRY-FORMAT.md), [drafting workflow](skills/draft-entry/SKILL.md), and [outside-review workflow](reviews/README.md). The extractor has a documented 126-posting pilot; precision and recall against human labels remain unmeasured. The repository provides data and command-line tools, not a complete hosted job-matching application.

## Additional work on separate branches

These results were inspected on November 14, 2026. They are **not included in the main-branch inventory above**.

| Branch | Existing work |
|---|---|
| [`data/onet-hot-tech-entries-20261107`](https://github.com/nikbearbrown/skills-lexicon/tree/data/onet-hot-tech-entries-20261107) | 110 added draft entry files and 17 modified existing entries; commit describes 17 added variants. Its additional entries are not part of main's 3,688. |
| [`data/onet-tech-match-20261101`](https://github.com/nikbearbrown/skills-lexicon/tree/data/onet-tech-match-20261101/data/onet-match) | O*NET 31.0: 8,753 technology names, with 193 exact matches, 426 containment hints, and 8,134 unmatched names. Also includes a separate 30.2 comparison. Unmatched names are not automatically missing concepts. |
| [`data/job-fields-survey-20261102`](https://github.com/nikbearbrown/skills-lexicon/tree/data/job-fields-survey-20261102/data/job-fields-survey) | November 6 survey reports 3,325 archives; title-like columns in 978 datasets and structured skill-list columns in 203. Includes non-job datasets and false positives; this is a structural survey, not verified posting coverage. |
| [`data/kaggle-occurrence-evidence-20261030`](https://github.com/nikbearbrown/skills-lexicon/tree/data/kaggle-occurrence-evidence-20261030/data/source-occurrences/kaggle-publication-2026-10-30) | 19,766 occurrence observations across 30 datasets, linked to 2,568 existing entries, plus 303 pending candidates. Records are not independent jobs; source terms and overlap need review before integration. |

## Main gaps

- Human review and correction of classification, synonym, and description flags; no reviewed release yet.
- A completed occupation/title-alias dataset that preserves seniority, specialization, ambiguity, source, and taxonomy version.
- Broader technology coverage and integration of separately drafted entries.
- Sourced knowledge subcategories and mappings to occupational knowledge requirements.
- A work-style/personal-characteristics class; sourced `draws_on` and `attests` relationships.
- Capability evidence and proficiency: portfolios, assessments, language levels, and experience linked to a specific capability.
- Measured extraction accuracy and representative, deduplicated posting coverage. Dataset frequency alone does not establish labor-market demand.
- Source-backed WordNet and ESCO integration, with provenance and applicable terms recorded.

The [handoff](docs/handoff/HANDOFF.md) records the earlier project state and prepared workflows. Some of its “not run” statements have been superseded by the branch results above.

## Reproduce the counts and validate

From the repository root:

```bash
python3 -I scripts/summary_stats.py
python3 -I tools/lexicon.py validate
python3 -I tools/lexicon.py index
```

The recount script reads the current checkout, validates entries and model-run references, and emits JSON without modifying data. Class counts use `top_class`; source-backed counts use `backs`; labels use the existing Unicode/case/whitespace normalization. The dated snapshot remains a record of the audited data revision. Refresh this README's tables and snapshot when entries change.

Tests live in `tests/`: lexicon, pipeline, provenance, schema, descriptions, and Wikipedia resolution. **140 tests passed in the November 14 audit** (one localhost HTTP test required a rerun outside the sandbox). The schema suite requires `jsonschema`; the other suites use the Python standard library.

## Sources and licensing

Original code and original repository material are under [MIT](LICENSE), copyright Humanitarians AI Incorporated. O*NET-derived data is **CC BY 4.0** with [third-party attribution](THIRD-PARTY-NOTICES.md). Wikipedia-adapted `description` text is **CC BY-SA 4.0**, with attribution and a revision permalink stored on each description; it is not relicensed as MIT. Source-specific terms remain relevant when reusing or integrating data. See [source policy](docs/SOURCES.md).
