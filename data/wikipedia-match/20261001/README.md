# Wikipedia match results, dump 20261001

Output of matching skills-lexicon entries against English Wikipedia (dump date **20261001**). Produced on the Explorer cluster by `scripts/wikipedia_match/match_entries.py` and `scripts/wikipedia_match/categories_for_pages.py`.

## Files

- `matches.jsonl` — one line per lexicon entry (`entry_id`, `entry_key`, `preferred_name`), with its candidate Wikipedia pages (`page_id`, `title`, how each matched: by title or redirect, which form of the entry matched, preferred or variant), the `reasons` it needs a person (if any), and a `tier`: `confident`, `needs-a-person` or `no-match`.
- `candidates.jsonl` — one line per Wikipedia page: `page_id`, `title`, `rev_id` (revision id), `rev_timestamp`, the cleaned lead paragraph (`lead`), and a `disambiguation` flag.
- `categories.jsonl` — one line per candidate page: `page_id`, `title`, and the page's Wikipedia `categories`.
- `summary.json` — counts: 3,688 entries (1,421 confident, 698 needs-a-person, 1,569 no-match), 4,822 candidate pages, 7,249,099 articles and 12,065,403 redirects scanned.

**Matches are candidates and flags, not decisions.** A `confident` tier means the title/redirect evidence agreed on one page; it is not a verified identification.

## Licence and attribution

The lead text in `candidates.jsonl` is cleaned plain text from English Wikipedia, licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). It was authored by the Wikipedia contributors of each article. The revision each lead came from is:

`https://en.wikipedia.org/w/index.php?title=<title with underscores>&oldid=<rev_id>`

## sha256

```
86241ccaaa931f83530e963aef9f6a038ef6975566a175a3fa957c9e7620a1b6  matches.jsonl
9c7c4eae2a103c821cdc264d72982f936eb03e233d7f146aba9a743c6a891990  candidates.jsonl
b44c5ac95b5224f091c31634d6bcb6f966dd1c1029d27844e0f166802a967626  categories.jsonl
e31b8f1c58089ea7ff700cea0fe58269c6cd40cbe276f9da7ee70b9ff95c2ac9  summary.json
```

## resolved.jsonl: one relation per entry

Produced by `scripts/wikipedia_match/resolve_matches.py` from the three files above. The first matching step gave a tier that was too generous: in a sample, about one in eight `confident` matches was wrong, mostly redirects through abbreviations or variants (an entry for a credential matched an airport, an ability matched an album). The resolver replaces the tier with a relation, using each page's categories.

| Relation | Meaning | Use |
|---|---|---|
| `same` | The entry's own name is the page's title, or the title less a parenthetical that fits the kind (Python to Python (programming language)), or the page title extends the name (Czech to Czech language); the categories do not contradict the kind | link, and eligible for a description written from the lead |
| `related` | A redirect or a variant leads to a broader, narrower or renamed page (Azure Data Factory to Microsoft Azure, Office 365 to Microsoft 365) | link only; the lead describes a different thing |
| `ambiguous` | Several pages remain, or the plain-name page is a disambiguation page (Java: language or platform); the top three are listed with scores and notes | a person decides |
| `none` | No usable page, or the entry is an O*NET ability, which is already matched to its source | nothing |

Each `page` or `top` item shows its `basis` (how it matched), a `score` and `notes` saying what raised or lowered it, so the decision can be checked. Scores are heuristics, not probabilities.

Counts on dump 20261001: 1,284 `same`, 425 `related`, 77 `ambiguous`, 1,902 `none`, of 3,688 entries. By class, `same` is 1,049 of 2,472 skills, 182 of 290 languages, 49 of 859 certifications (most credentials have no article of their own) and 4 of 67 abilities.

**How far to trust it.** The relation was checked by a language model reading random samples (about 100 `same` and 20 `related` entries), not by a person. In those samples `same` was wrong about once in 30 and the errors found were fixed in the rules. That is an estimate from a small sample. Titles that add a word to the entry's name (the entry Tableau and the article Tableau Software) are not proposed at all, so some real matches are missing from `none` and `ambiguous`.
