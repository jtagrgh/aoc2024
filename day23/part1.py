from collections import defaultdict
from itertools import combinations
with open('input.txt','r') as f:
    l=[x.strip().split('-') for x in f.readlines()]
g=defaultdict(lambda: set())
for u,v in l:
    g[u].add(v)
    g[v].add(u)
t=0
for x in combinations(g.keys(),3):
    if not any(y[0]=='t' for y in x):
        continue
    if x[0] not in g[x[1]] or x[0] not in g[x[2]]:
        continue
    if x[1] not in g[x[0]] or x[1] not in g[x[2]]:
        continue
    if x[2] not in g[x[0]] or x[2] not in g[x[1]]:
        continue
    t+=1
print(t)
