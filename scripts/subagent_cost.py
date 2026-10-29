"""Estimate what the subagents cost, from their own transcripts, since the session's reported figure seems to cover only the main session.

    python3 -I scripts/subagent_cost.py

Sums each transcript's token usage by model and prices it with the rates implied by the session's own cost figures:
input about $1.8 per million tokens, cache read a tenth of that, cache write 1.25 times, output 5 times (Sonnet). Opus is priced
at 5 times Sonnet, which is a pessimistic guess. Prints the Sonnet and Opus estimates and their sum.
"""
import collections
import glob
import json

TASKS = "/tmp/claude-0/-home-user/51e956f7-ba36-520a-915f-8cd07d641b86/tasks"
P, OPUS_X = 1.8, 5


def main():
    tot = collections.defaultdict(collections.Counter)
    for f in glob.glob(f"{TASKS}/*.output"):
        seen, model = set(), None
        for line in open(f, errors="replace"):
            try:
                m = json.loads(line).get("message")
            except Exception:
                continue
            if isinstance(m, dict):
                model = m.get("model") or model
                u, mid = m.get("usage"), m.get("id")
                if u and mid and mid not in seen:
                    seen.add(mid)
                    for k, kk in (("in", "input_tokens"), ("cw", "cache_creation_input_tokens"), ("cr", "cache_read_input_tokens"), ("out", "output_tokens")):
                        tot[model][k] += u.get(kk, 0)
    cost = {}
    for m, c in tot.items():
        base = (c["in"] * P + c["cw"] * 1.25 * P + c["cr"] * 0.1 * P + c["out"] * 5 * P) / 1e6
        cost[m] = base * (OPUS_X if "opus" in str(m) else 1)
    for m, v in cost.items():
        print(f"{m}: ${v:.2f}  (tokens {dict(tot[m])})")
    print(f"subagents, estimated: ${sum(cost.values()):.2f}")


main()
