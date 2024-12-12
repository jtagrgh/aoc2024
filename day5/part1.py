from math import *
with open('input.txt','r') as f:
    l=f.readlines()
k=l.index('\n')
m=[tuple(map(int,x.strip().split('|'))) for x in l[:k]]
d=[tuple(map(int,x.strip().split(','))) for x in l[k+1:]]
e=0
for w in d:
    u = set(w)
    g={x:set() for x in u}
    h={x:set() for x in u}
    for a,b in m:
        if not(a in u and b in u): continue
        g[a].add(b)
        h[b].add(a)
    r=[k for k in h.keys() if len(h[k]) == 0]
    s=[]
    while r:
        t=r.pop()
        s.append(t)
        for c in g[t]:
            h[c].remove(t)
            if not h[c]:
                r.append(c)
    if w==tuple(s):
        e+=w[ceil(len(w)/2)-1]
print(e)