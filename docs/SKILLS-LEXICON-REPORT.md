# Skills Lexicon state and terminology report

**Prepared for Nik Bear Brown • November 14, 2026**

Skills Lexicon is a substantial draft vocabulary and evidence system for understanding what employers ask for. Its main branch contains **3,688 canonical concepts**, supported by name variants, typed relationships, source attribution, model assessments, and a separate O*NET occupational ability dataset. It already provides useful machinery for normalization and evidence collection. It does **not yet provide a human-reviewed skills release or a completed job-title synonym and occupation-mapping service**.

This report separates the data on `main` from work available on other branches. Main-branch statistics were recomputed from [`82498e33f014ad0a138d242aba12312a9bfeef10`](https://github.com/nikbearbrown/skills-lexicon/commit/82498e33f014ad0a138d242aba12312a9bfeef10), rather than copied from the older README. The [JSON snapshot](summary-stats-2026-11-14.json) records the results; [`scripts/summary_stats.py`](../scripts/summary_stats.py) reproduces them from a checkout.

## What the project is for

Job advertisements, resumes, and course descriptions use inconsistent language. One document might say Postgres and another PostgreSQL. A short label can mean different things in different contexts. A technology, a capability, a subject area, and a credential can appear together in a single requirements list.

The lexicon addresses these problems with two connected layers:

- **A vocabulary layer:** stable concept IDs, preferred names, variants, definitions, and source-derived descriptions.
- **An ontology layer:** finer concept kinds and typed links such as broader, part of, related, and contrast, with evidence attached to individual claims.

A concept is distinct from the words used to name it. A canonical entry can have several labels without increasing the number of concepts. A statement about that concept is also distinct from evidence supporting the statement. This allows competing classifications and model disagreements to remain visible instead of silently becoming accepted facts. The current implementation is described by [the loader and validator](../tools/lexicon.py), [entry format](ENTRY-FORMAT.md), and [evidence model](SCHEMAS.md).

## Inventory and counting rules

| Top-level class | Count | Share of all concepts |
|---|---:|---:|
| Skill | 1,954 | 52.98% |
| Certification and other credentials | 859 | 23.29% |
| Knowledge | 518 | 14.05% |
| Language | 290 | 7.86% |
| Ability | 67 | 1.82% |
| **Total** | **3,688** | **100.00%** |

These classes are mutually exclusive in the code: `top_class` derives the class from an entry's `kind`. They count recorded classifications, not proven competence, market demand, or independently reviewed concepts.

The distinction between **class** and **kind** matters. The broad skill class has 1,954 entries, but only **689** have the specific kind `skill`. The remainder are **498 tools, 219 platforms, 219 methods, 129 libraries, 115 standards, and 85 frameworks**. `work-activity` is an allowed kind with **zero entries**. Tools, libraries, and standards are included because job listings ask for familiarity or competence with them; the object named is different from the person's proficiency in using it.

The earlier README's **2,472 skills** was a combined total before knowledge became its own class: 1,954 + 518. This is a classification change, not the removal of 518 concepts.

### Names and relationships

There are **2,940 variant records** on **2,023 entries**. Together with preferred names, these produce **6,625 distinct normalized surface forms**. Normalization applies the existing Unicode, whitespace, and case rules. The raw total of names plus variant records is larger because some labels normalize to the same text.

The **443 relation records** comprise **350 related, 79 broader, 9 part-of, and 5 contrast** links. These are directed records in the files, not necessarily unique undirected pairs. **No relation has count roll-up enabled.** The software supports explicit roll-up, but current data does not automatically count a specific concept toward a broader concept.

A variant claims equivalence of labels for a concept. A `related` link claims association, not equivalence. Confusing those relationships would inflate or misattribute counts. Current examples include Postgres → PostgreSQL and Golang → Go; even these mechanisms need contextual and evidence checks for other labels.

## Skills, abilities, and knowledge

The project's distinctions draw on O*NET. The 30.2 Content Model describes abilities as **“Enduring attributes of the individual that influence performance.”** Its current presentation distinguishes worker characteristics, worker requirements, experience requirements, and information about the work itself. The framework does not make a job title interchangeable with a capability. Sources: [O*NET 30.2 Content Model Reference](https://www.onetcenter.org/dictionary/30.2/text/content_model_reference.html), [O*NET Content Model](https://www.onetcenter.org/content.html).

| Concept | Practical definition | Example of what it means | What it does not establish |
|---|---|---|---|
| **Knowledge** | Learned facts, principles, and understanding within a subject | Understanding database systems, network topology, or cardiovascular physiology | That a person can reliably perform every related task |
| **Skill** | A developed capacity to carry out an activity | Diagnosing a fault, writing a query, or communicating findings effectively | A credential, an occupation, or an inherent trait |
| **Ability** | An underlying attribute contributing to performance across activities | Oral comprehension, spatial orientation, manual dexterity, or visual discrimination | A measured proficiency with a particular tool |

The knowledge definition aligns with [O*NET's knowledge description](https://www.onetonline.org/find/descriptor/browse/2.C/). Practical skill examples also align with [O*NET's essential skills](https://www.onetonline.org/find/descriptor/browse/2.A/), which include reading, writing, learning, and applying mathematics.

A database example makes the distinction concrete. **Knowing how relational databases are organized** is knowledge. **Writing and debugging a SQL query** is a skill. **Deductive reasoning** can contribute to doing that work. **SQL** is the language, **PostgreSQL** is the tool, and a **database credential** is an attestation with a particular scope. These are connected concepts but answer different questions.

The class document uses trainability and ceilings as a heuristic. That should not become a strict biological rule: skills have performance limits, abilities can develop, and job-ad wording alone cannot identify either. Likewise, knowledge can be demonstrated through applied work as well as explanation. A defensible classification should identify the construct and its evidence rather than rely on “innate versus learned.”

### Knowledge coverage

The **518 knowledge concepts** include broad fields, narrower topics, named systems, and some disputed classifications. Examples currently stored under `knowledge` include:

| Area | Representative existing concepts |
|---|---|
| Computing and AI | Computer science; Database systems; Artificial intelligence; Large language models; Knowledge graphs; Cybersecurity |
| Mathematics | Mathematics; Statistics; Boolean algebra; Big O notation; Random variable |
| Engineering | Engineering statics; Fluid statics; Ohm's law; Refrigeration; Optical fiber |
| Medicine and life sciences | Cardiovascular physiology; Neurobiology; Pharmacogenetics; Food microbiology; Clinical medical ethics |
| Business and finance | Corporate finance; Cost accounting; Capital asset pricing model; Counterparty risk; Debits and credits |
| Law and policy | Administrative law; Human rights law; Labour law; Intellectual property; Public policy |
| Education and humanities | Special education; Art history; Music theory; Ancient philosophy; Historical linguistics |
| Environment and infrastructure | Climate variability and change; Renewable energy; Circular economy; Urban sustainability |

These groupings are an explanatory overview, not measured partitions: there is no completed, sourced knowledge-domain taxonomy that assigns all 518 entries to these buckets. They should not be confused with O*NET's 33 broad Knowledge areas. The repository does not yet provide a complete crosswalk between the two.

Classification quality is an immediate issue. NFPA 70E, ABEC scale, and several other entries are labeled knowledge even though model reviewers argue they should be standards. Those flags are evidence of disagreement, not an automatic authorization to reclassify. See [the review queue](REVIEW-FLAGS.md).

### Ability coverage

Of **67 ability entries**, **52** correspond to O*NET definitions: **21 cognitive, 10 psychomotor, 9 physical, and 12 sensory**. Each of those 52 has O*NET-backed classification and definition claims, giving **104 backed claims**.

The other **15** are Adaptability, Attention to detail, Causal reasoning, Emotional stability, Goal-oriented, Ingenuity, Patience, Quick learning, Resilience, Results-oriented, Self-confidence, Self-starter, Spatial-temporal reasoning, Success-driven, and Team-oriented. This is the exact additional inventory, not a claim that all 15 are correctly classified. Several fit a work-style or personal-characteristics category better. O*NET itself separates work styles from abilities; [CLASSES.md](CLASSES.md) records this as open work.

The separate occupational dataset has **1,016 occupation titles**, **894 occupations with ratings**, and **46,488 unique occupation–ability pairs**. The remaining **122 occupation titles have no ratings in this export**. All ratings use the level scale, not the separate O*NET importance scale. The six-occupation JSON is a subset of 312 rows, so it must not be added to the full total.

Preserve the **68 suppression flags** and **7,410 not-relevant flags** when displaying or analyzing these rows. The ratings describe the level an occupation requires; they do not assess a particular person. The data is identified as O*NET 30.2, with rating dates reported in the dataset documentation as December 2004 through August 2025. See [the abilities documentation](../abilities/README.md).

### Languages and credentials

The **290 language entries** consist of **158 human, 112 programming, 10 markup, 7 modeling, and 3 style languages**. These are kind-based counts. The optional `language_type` field is incomplete: **157 human, 116 programming, and 17 unset**. A dashboard that counts that optional flag would give misleading class totals.

A language is a communication system. Proficiency combines knowledge and practiced use, and may draw on abilities and experience. The lexicon names the system; it does not yet store a person's assessed level, task-specific proficiency, or supporting performance evidence.

The **859 credential entries** use “certification” as a broad repository class that also includes degrees, licences, certificates, permits, endorsements, and clearances. That broad label should not imply these are all professional certifications in the narrower sense. There are **321 single-issuer, 522 many-issuer, and 16 unset scope flags**. The schema supports issuer and credential details, but their presence or schema support should not be mistaken for complete verification.

A degree can provide evidence of learning in a field. Its evidentiary strength depends on the program, assessment, relevance, and recency; it is not universally stronger than demonstrated work and does not certify every fact or skill in the field. A future `attests` link should state the particular coverage and source.

## What is implemented

The Python tools load concepts, validate schemas and cross-entry references, build a matching index, extract known terms from supplied text, propose unfamiliar terms, prepare drafting requests, ingest validated responses, and record decisions and model assessments. The pipeline accepts either posting text or legacy tags, with different provenance. It has explicit outcomes for a new concept, a variant of an existing concept, a rejected term, and an uncertain term. See [PIPELINE.md](PIPELINE.md).

The evidence system records who drafted or checked each assertion, which run and model produced it, and whether an external source supports it. The Wikipedia workflow generates candidates, resolves article identity, and attaches descriptions adapted from specific article revisions. The abilities dataset supplies an occupational comparison layer.

These pieces can support downstream search, tagging, curricula, and job analysis. The repository itself is a data and command-line project. It is not a finished job board, a hosted search application, a candidate assessment system, or a validated recommendation engine.

The pipeline documentation describes a **126-posting Software Developer extraction pilot**, with **1,882 unknown terms** and **199 appearing in at least three postings**. Those are pilot outputs, not precision or recall measurements. The older README's claim that extraction had never run on real postings is therefore outdated. Separate branch occurrence data is additional evidence; it does not establish that every stage of the model drafting pipeline has been validated end to end on representative postings.

## Evidence quality and readiness

| Measure | Recounted result |
|---|---:|
| Machine-drafted entries | 3,555 |
| Proposed entries | 133 |
| Reviewed entries | 0 |
| Deprecated entries | 0 |
| Individual claims | 17,097 |
| Backed claims under repository rules | 1,321 |
| Human-backed claims | 0 |
| Model contradiction records | 675 |
| Entries with contradiction records | 456 |
| Claims contradicted by two or more models | 114 |
| Assessment vote records | 13,697 |

Only **7.73% of claims** meet the repository's backing rule. The backed total consists of the **104 O*NET ability claims** and **1,217 Wikipedia descriptions**. It does not mean 7.73% of entries are fully verified. A supporting source match with `page-read` or `dump-match` verification can back a claim; a supporting human check can also do so. Agreement between models, a vote, and a search-result snippet do not.

The Wikipedia resolver assigns **1,284 same, 425 related, 77 ambiguous, and 1,902 none** outcomes. **1,217 entries (33.00%)** have adapted descriptions; **67** same-matched entries were set aside. **20 existing descriptions** still have contradiction flags. Automated matching can be wrong even when the text is faithfully attributed to a revision. The original candidate-tier counts in `summary.json` precede the resolver and must not be presented as final identity matches.

The project is therefore ready for **exploration, evidence collection, and review**, while a dependable published counting vocabulary still needs human review, classification corrections, and extraction evaluation. The repository's own policy reserves published skill counts for reviewed entries. There are currently none.

### Legacy tag accounting

Recounting all three legacy lists with the project's normalization produces **4,880 distinct tags**, not the older reported 4,652. Individually the files contain **4,254**, **818**, and **303** distinct normalized tags; their union is smaller than their sum because lists overlap.

Of the union, **3,721 tags match a current preferred name or variant**. **1,159 additional tags have only a recorded decision**, giving 4,880 accounted-for tags. The decision file has **1,162 records**: **564 not-a-skill and 598 unsure**. **Three decided tags also match current entries**, so the match and decision totals cannot simply be added.

“Zero unresolved” means the pipeline has recorded some disposition for every tag. It does not mean the 598 unsure decisions have been substantively settled. Similarly, 3,688 concepts need not equal the number of covered tags: one concept can cover multiple tags, and concepts can originate outside those lists.

## Job-title synonyms and occupation mapping

**Yes: identifying when different job titles refer to the same occupation belongs in the project's scope. It is partially prepared, but it is not complete on `main`.**

Three different operations must remain visible:

| Operation | Meaning | Example or boundary |
|---|---|---|
| Normalize text | Standardize formatting without deciding meaning | Case, spacing, Unicode, and punctuation |
| Resolve an alias | Identify alternative names for the same concept in context | An abbreviation and its spelled-out role name, once verified |
| Map to an occupation | Assign a title to a taxonomy category | Several employer titles may map to one occupation code while retaining distinct duties or seniority |

A shared occupation code does not prove that two job titles mean exactly the same thing. An occupation is a grouping; a job title is an employer's label for a particular role. Job requirements, seniority, specialization, industry, and country can all matter. “Software developer” and “software engineer” may be equivalent in a particular dataset, but they should not be globally merged without evidence. “Senior Software Engineer” should retain its seniority even when grouped with a base occupation. “Data analyst” and “data scientist” should not become aliases merely because their skills overlap.

The existing [`title_pilot.py`](../scripts/cluster/title_pilot.py) inventories candidate CSV/TSV files, counts titles from a selected column, normalizes strings, and matches them to supplied O*NET title tables. It labels one candidate code `same`, multiple candidates `ambiguous`, and no candidates `none`. This is deterministic candidate generation; `same` is not a human verdict.

Two concrete implementation limits need attention before treating its output as a synonym authority:

1. Its normalization removes words classified as levels, including **assistant** and **associate**. Removing “assistant” from a role such as “Physician Assistant” changes occupational meaning rather than merely removing seniority. It also drops bracketed information and some text after separators, which can remove specialization.
2. It truncates O*NET codes to the first **seven characters**, collapsing detailed O*NET-SOC suffixes into the base SOC code. Multiple detailed occupations can consequently look like one unique match.

The pilot does retain extracted level tokens in its output, but that does not undo the meaning change in its matching key. Preserve the full title, full taxonomy code, retained qualifiers, candidate list, and normalization decisions; use ambiguity rather than forced equivalence when meaning is uncertain. These are findings about the current script, not changes made by this report.

A useful future mapping record would contain the raw title, canonical occupation ID, alternate label, language, country or jurisdiction where relevant, seniority, specialization, relation type, source/version, matching method, and review state. Exact aliases, broad/narrow relationships, and related occupations should be distinct. Posting-specific requirements can then attach to the mapped occupation without assuming that every worker in that occupation has every listed capability.

## Work available outside main

Branch work advances the project beyond some statements in the November 7 handoff, but it must not silently increase main's inventory.

| Branch snapshot | Result | Interpretation |
|---|---|---|
| [Hot-technology drafts, `48e0414`](https://github.com/nikbearbrown/skills-lexicon/commit/48e0414597c16874184417b53f352c1214d50222) | 110 new entry files, 17 modified existing entry files; commit describes 17 variants | Draft additions, excluded from main's 3,688. A branch with only these additions has 3,798 entries; this is not the main total. |
| [O*NET matching, `d6a3c98`](https://github.com/nikbearbrown/skills-lexicon/blob/d6a3c986051b7e730c79c916cab208e8a50aec21/data/onet-match/README.md) | 31.0: 8,753 distinct technology names; 193 exact, 426 contains, 8,134 none; 176 hot names and 285 in-demand names | Contains is a hint; none can mean missing coverage or different naming. Occupation counts are not job counts. |
| [Field survey, `bd3fb4a`](https://github.com/nikbearbrown/skills-lexicon/blob/bd3fb4accefc449bbce435fa7c30ad171d6652c0/data/job-fields-survey/README.md) | November 6: 3,325 archives; 978 with title-like fields, 203 with structured skill lists | Includes non-job datasets, duplicates, false positives, and sampling limits. The survey is complete on this branch, although the older handoff says to run it. |
| [Occurrence evidence, `9c8d6bf`](https://github.com/nikbearbrown/skills-lexicon/blob/9c8d6bf4d67c3b04f5bc6d07b4507af6f89a3daa/data/source-occurrences/kaggle-publication-2026-10-30/summary.json) | 19,766 observations in 30 datasets, linked to 2,568 entries; 303 pending candidates | Based on 32 inspected datasets and 1,867,517 skill-field records. Source independence is not established. The summary's older class breakdown predates the knowledge split. |

The field-survey branch also reports location-like fields in **1,489** datasets, company-like fields in **901**, salary-like fields in **850**, dates in **713**, experience level in **656**, employment type in **461**, and industry in **460**. These are datasets passing heuristics, not validated job-posting datasets. Of 978 title candidates, 579 have one of five publisher-declared licence labels selected by that survey; that is a selection aid, not a guarantee of usable or redistributable records.

The O*NET branch reports only **49 of 176 hot-technology names** matching exactly, with **21 containment hints** and **106 unmatched**. This supports prioritizing technology coverage and alias quality, but it is not a claim that all 106 concepts are absent. Main lacks entries under common names such as Git, GitHub, Kubernetes, MySQL, MongoDB, and Jenkins; the hot-technology draft branch addresses part of that gap.

## What else belongs in the model

The five classes cover more than skills alone, but they do not yet exhaust what a job requires. The current [O*NET Content Model](https://www.onetcenter.org/content.html) also distinguishes work styles, interests, education, experience and training, tasks, work activities, work context, and occupation information. This suggests the following additions or explicit boundaries:

| Dimension | Current position | Useful next step |
|---|---|---|
| Occupations and job-title aliases | Occupation lookup and pilot code; no occupation class in entries | A sourced title-to-occupation crosswalk with full codes and ambiguity handling |
| Work styles and personal characteristics | Some are currently labeled abilities | Separate them and review affected entries |
| Tasks and work activities | Kind supported, zero work-activity entries | Represent work performed separately from the capabilities needed |
| Proficiency and required level | O*NET ability levels only; no general person-level model | Capability-specific proficiency, evidence, and assessment context |
| Experience | Discussed, not a complete implementation | Years, recency, domain, and role attached to the relevant capability; avoid treating years as a universal score |
| Capability evidence | Claim provenance exists; person-level evidence is a separate problem | Portfolios, projects, assessments, references, and credentials with scope |
| Capability relationships | Generic relations exist | Sourced skill-to-ability `draws_on` and credential-to-knowledge `attests` relations |
| Knowledge organization | 518 concepts without a complete domain crosswalk | Sourced subject hierarchy and O*NET/ESCO mappings with explicit relation types |
| Job context and metadata | Field survey on another branch | Preserve location, salary units, employment type, seniority, and dates outside the capability vocabulary |
| External vocabularies | O*NET abilities and Wikipedia integrated; other work partial | Add WordNet senses and ESCO labels with source/version, ambiguity, and applicable terms |
| Measurement and change over time | No representative demand measurement | Deduplicate postings, state denominators and periods, evaluate extraction, and version releases |

These are different kinds of information and need not all become top-level lexicon classes. A salary is an attribute of a job or observation; a credential is a concept plus an attestation; a proficiency assessment concerns a person and a capability. Keeping those boundaries clear prevents the dictionary from becoming a collection of unrelated labels.

## Priorities

1. **Make counts and status reproducible.** Use the new summary script and dated snapshot. Keep main inventory, branch additions, source observations, and reviewed claims separate.
2. **Resolve the high-value review queue.** Start with the 114 claims contradicted by multiple models, known standards-versus-knowledge confusion, work-style entries, and description flags. Add named human review rather than converting model consensus into approval.
3. **Complete title mapping carefully.** Select actual job datasets from the survey, preserve qualifiers and full taxonomy codes, compare to official title sources, and evaluate a hand-labeled sample of exact, ambiguous, and unmatched outcomes.
4. **Integrate technology coverage after review.** Inspect the 110 drafted entries and proposed aliases, reconcile overlapping candidate queues, and maintain source provenance.
5. **Measure extraction quality.** Establish precision, recall, ambiguity handling, and duplicate rates on a labeled set before publishing demand statistics.
6. **Expand the ontology where evidence supports it.** Add knowledge groupings, occupations, work styles, and typed capability relationships without inventing unsupported links or numerical weights.

## Verification and reuse

The audit recomputed every headline count from the main-branch entry files and associated datasets and ran the existing validator with **zero errors**. No concept data, classifications, aliases, or branch datasets were changed for this documentation update. The new script is read-only and checks class, kind, and Wikipedia outcome totals against the entry total. Its output was compared with the saved snapshot; every illustrative knowledge entry in the README was checked against its stored kind, and local documentation links were checked. Across the six existing suites, **140 tests passed**: 139 in the initial sandboxed run and the localhost HTTP test on a successful rerun outside the sandbox after socket binding was blocked. Existing resource-cleanup warnings appeared but did not fail the rerun.

Original repository material is MIT-licensed. O*NET-derived material retains CC BY 4.0 attribution. Wikipedia-adapted descriptions carry CC BY-SA 4.0 and revision-specific attribution on each entry; those fields are not made MIT by the repository's root licence. Branch datasets have their own source records and reuse conditions. See [LICENSE](../LICENSE), [third-party notices](../THIRD-PARTY-NOTICES.md), [source policy](SOURCES.md), and [description provenance](SCHEMAS.md#descriptions-adapted-from-an-outside-article).
