"""Answer request files with any language model: an OpenAI-compatible HTTP endpoint, or a command.

    # HTTP (Ollama, llama.cpp server, vLLM, LM Studio, a hosted API ...)
    python3 -I tools/run_endpoint.py work --url http://localhost:11434/v1 --model llama3.1 [--api-key-env KEY]
    # Command that reads the prompt on stdin and prints the answer (e.g. ollama run, llm, a wrapper script)
    python3 -I tools/run_endpoint.py work --cmd "ollama run llama3.1"

Writes work/responses/<request name>. If the reply is not valid JSON the raw text goes to
work/responses/<name>.raw.txt and the request is left unanswered. This script only fetches answers;
tools/ingest.py checks and saves them, and records which model said it.
"""
import argparse
import json
import os
import shlex
import subprocess
import sys
import urllib.request
from pathlib import Path


def extract_json(text):
    """Pull the first JSON object out of a reply, tolerating code fences and chatter around it."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        text = text.rsplit("```", 1)[0]
    start = text.find("{")
    if start == -1:
        raise ValueError("no JSON object in the reply")
    depth, in_str, esc = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unterminated JSON object in the reply")


def split_request(req):
    body = {k: v for k, v in req.items() if k != "instructions"}
    return req["instructions"], json.dumps(body, ensure_ascii=False, indent=1)


def ask_http(url, model, key, req, timeout=300):
    system, user = split_request(req)
    payload = {"model": model, "temperature": 0, "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = "Bearer " + key
    r = urllib.request.Request(url.rstrip("/") + "/chat/completions", json.dumps(payload).encode(), headers)
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        return json.loads(resp.read())["choices"][0]["message"]["content"]


def ask_cmd(cmd, req, timeout=600):
    system, user = split_request(req)
    p = subprocess.run(shlex.split(cmd), input=system + "\n\n" + user, capture_output=True, text=True, timeout=timeout)
    if p.returncode:
        raise RuntimeError(f"command exited {p.returncode}: {p.stderr.strip()[:200]}")
    return p.stdout


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("work")
    ap.add_argument("--url")
    ap.add_argument("--model")
    ap.add_argument("--api-key-env")
    ap.add_argument("--cmd")
    ap.add_argument("--limit", type=int)
    a = ap.parse_args(argv)
    if bool(a.url) == bool(a.cmd) or (a.url and not a.model):
        ap.error("give either --url with --model, or --cmd")
    key = os.environ.get(a.api_key_env, "") if a.api_key_env else ""
    work = Path(a.work)
    (work / "responses").mkdir(parents=True, exist_ok=True)
    done = failed = 0
    for rp in sorted((work / "requests").glob("*.json")):
        out = work / "responses" / rp.name
        if out.exists():
            continue
        if a.limit and done + failed >= a.limit:
            break
        req = json.loads(rp.read_text("utf-8"))
        try:
            reply = ask_http(a.url, a.model, key, req) if a.url else ask_cmd(a.cmd, req)
        except Exception as e:  # network or command failure: leave unanswered, say why
            print(f"{rp.name}: {e}")
            failed += 1
            continue
        try:
            out.write_text(json.dumps(extract_json(reply), indent=1, ensure_ascii=False) + "\n", "utf-8")
            done += 1
        except ValueError as e:
            (work / "responses" / (rp.name + ".raw.txt")).write_text(reply, "utf-8")
            print(f"{rp.name}: {e}; raw reply kept")
            failed += 1
    print(f"answered {done}, failed {failed}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
