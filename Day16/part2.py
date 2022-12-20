import math
import re
from collections import defaultdict

f = open("in.txt", "r").read().split("\n")
valve = {}

dist = defaultdict(lambda: defaultdict(lambda: math.inf))

for vrstica in f:
    i = vrstica.split(" ")[1]
    flow = re.sub("[^0-9]", "", vrstica)
    valve[i] = int(flow)
    tunnels = []
    p = 0
    dist[i][i] = 0
    for h in vrstica.split(" "):
        if p > 8:
            tunnels.append(h.replace(",", ""))
        p += 1
    for j in tunnels:
        dist[i][j] = 1

for k in valve:
    for i in valve:
        for j in valve:
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])


def rec(i, t, remaining, elephant):
    if elephant:
        ans = rec("AA", 26, remaining, False)
    else:
        ans = 0
    for j in remaining:
        next = t - dist[i][j] - 1
        if (next) >= 0:
            ans = max(valve[j] * next + rec(j, next, remaining - {j}, elephant), ans)
    return ans

p = []
for x in valve:
    if valve[x] > 0:
        p.append(x)

a = rec("AA", 26, frozenset(p), True)
print(a)
