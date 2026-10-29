import json, os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from lib import write_all
import part1, part2, part3, part4
allA = {}
for m in (part1, part2, part3, part4):
    for k, v in m.A.items():
        assert k not in allA, k
        allA[k] = v
reqterms = {json.load(open("work/requests/" + f))["term"] for f in os.listdir("work/requests")}
print("missing", sorted(reqterms - set(allA)))
print("extra", sorted(set(allA) - reqterms))
n = write_all(allA)
print("written", n)
c = collections.Counter(v["decision"] for v in allA.values())
print(c)
