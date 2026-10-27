# Pipeline: from postings to new entries

Scripts do everything that can be done by rule. The language model does one job: answer a request file. Any model can do it.

```
postings.jsonl ──extract.py──> work/records.jsonl      one structured record per posting (known skills, quotes)
                         └───> work/candidates.json    terms we do not know, with quotes
candidates ──make_requests.py──> work/requests/*.json  self-contained: instructions, term, quotes, nearest entries
requests ──(any model)──> work/responses/*.json        the model's answer
responses ──ingest.py──> entries/*.json                saved only if the whole dictionary still validates
```

## Steps

```bash
python3 -I tools/extract.py postings.jsonl --out work
python3 -I tools/make_requests.py work --min-postings 3
```

Then get the requests answered, any one of these ways:

1. **An HTTP endpoint** (Ollama, llama.cpp server, vLLM, LM Studio, a hosted API; anything with `/v1/chat/completions`):
   `python3 -I tools/run_endpoint.py work --url http://HOST:11434/v1 --model llama3.1`
2. **A command** that reads the prompt on stdin and prints the answer:
   `python3 -I tools/run_endpoint.py work --cmd "ollama run llama3.1"`
3. **An agent with file access** (Claude Code, Codex, anything similar): point it at `skills/draft-entry/SKILL.md` and `work/requests/`; it writes `work/responses/`.
4. **A person**, by hand, with the same files.

Then check and save:

```bash
python3 -I tools/ingest.py work --model-id <the model's id> --run <label> --dry-run   # look first
python3 -I tools/ingest.py work --model-id <the model's id> --run <label>
python3 -I tools/lexicon.py validate
```

Use several models on the same requests by pointing each at its own copy of `work/` (different `--run` labels). Disagreement between models is then visible in the records. It does not back a claim.

## What ingest does with an answer

| Answer | Result |
|---|---|
| `new` | Saved as a `machine-drafted` entry. Every claim gets a `drafted` evidence record naming the model **the operator gave**, the run and the basis. Claims marked `guess` are dropped. Relations to ids that do not exist are dropped. A guessed definition rejects the whole answer. |
| `variant_of` | Adds the term as a variant of that entry, with evidence. If the entry is `reviewed`, nothing is changed and the answer is rejected with "propose it as a pull request". |
| `not_a_skill` / `unsure` | Recorded in `data/term-decisions.json` so the term is not asked again. `unsure` is for a person. |
| anything invalid | Goes to `work/rejected/` with the reasons. The dictionary is never left half-changed. |

## Limits

- **Finding candidate terms is rule-based and noisy.** It reads tech-shaped tokens (`C++`, `PostgreSQL`, `CI/CD`), capitalised words that do not start a sentence, and lists after cues like "experience with". It will propose company names and other non-skills (the model says `not_a_skill`, and the answer is remembered). It will miss lower-case or plain-word skills ("communication", "forecasting"). Its recall and precision have not been measured against hand-labelled postings.
- **The coverage figure printed by `extract.py` is a rough proxy**, not an accuracy measure.
- **Where postings come from is not part of this repo.** Give it a JSONL file of `id`, `title`, `text`. Fetching ad text from public job boards is a separate step, not built here. Keep `work/` out of git: it holds ad text.
- **Evidence notes hold one short quote** (up to 200 characters) so a reader can see why a claim was drafted. If you publish entries, you publish those quotes.
- **A model's answer is a draft.** Nothing here makes an entry `reviewed`.
- **No model has been run through this yet.** The HTTP and command runners are tested against a fake endpoint and a stub command, not against a real language model.
