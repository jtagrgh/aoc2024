from collections import defaultdict
from itertools import combinations
with open('input.txt','r') as f:
    l=[x.strip().split('-') for x in f.readlines()]
g=defaultdict(lambda: set())
for u,v in l:
    g[u].add(v)
    g[v].add(u)
c={}
b=tuple()
def dfs(n,s):
    global b
    k=tuple(sorted(list(s)+[n]))
    if k in c:
        return c[k]
    if not(s<=g[n]):
        return 0
    s.add(n)
    m=1+max(dfs(x,s) for x in g[n]-s)
    if len(k)>len(b):
        b=tuple(k)
    s.remove(n)
    c[k]=m
    return m
t=max(dfs(x,set()) for x in g.keys())
print(','.join(b))
