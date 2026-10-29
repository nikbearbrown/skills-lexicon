# O*NET abilities

The 52 abilities of the O*NET content model, which is the basis the lexicon uses for what counts as an **ability**: an enduring attribute a person has, such as Oral Comprehension or Spatial Orientation. O*NET is the U.S. Department of Labor's occupational database and is widely accepted as the reference for abilities.

| File | What it holds |
|---|---|
| `onet-abilities.json` | The 52 abilities: O*NET element id, name, definition, category (cognitive, psychomotor, physical, sensory) and subcategory. |
| `onet-ability-ratings.json` | O*NET level ratings (0 to 7) of each ability for six occupations, with confidence intervals and sample sizes. They rate what an occupation demands, not a person. |

Every ability here is also an entry in `entries/`, kind `ability`, with the O*NET element id as an identifier and `matched_source` evidence naming O*NET and linking to it.

O*NET may miss some abilities that job listings ask for. Those are drafted like any other entry and carry whatever evidence they have; they simply lack the O*NET match.

**Licence.** O*NET data is CC BY 4.0. This is a selection and reformatting of O*NET 30.2. USDOL/ETA has not approved, endorsed or tested the changes. See `THIRD-PARTY-NOTICES.md`.

Source of this copy: the O*NET 30.2 subset kept in the jobs.humanitarians.ai repository (`data/explorer/`). Only O*NET's own fields were copied; that repository's project-specific interpretation fields are not O*NET's and are left out.
