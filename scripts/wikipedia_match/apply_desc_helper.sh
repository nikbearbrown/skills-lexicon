#!/bin/bash
# usage: apply_desc.sh <agent id> <stage rewrite|check> <expected model> <run suffix> <packets comma list>
cd /home/user/skills-lexicon
python3 - "$1" "$3" <<'PY'
import sys
sys.path.insert(0,"scripts"); sys.path.insert(0,"tools")
import overnight_step as O
m,e = O.transcript(sys.argv[1]); print("transcript:", m, e)
assert m == sys.argv[2], (m, e)
PY
[ $? -eq 0 ] || exit 1
M=$3; E=$(python3 - "$1" <<'PY'
import sys
sys.path.insert(0,"/home/user/skills-lexicon/scripts"); sys.path.insert(0,"/home/user/skills-lexicon/tools")
import overnight_step as O
print(O.transcript(sys.argv[1])[1])
PY
)
python3 -I scripts/wikipedia_match/descriptions.py apply /home/user/wmwork/desc --stage $2 --model-id $M --effort $E --run 2026-10-31-desc-$2-$4 --only $5 2>&1 | tail -4
