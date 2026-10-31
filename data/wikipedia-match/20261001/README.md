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
