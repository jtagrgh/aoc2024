from heapq import *
from itertools import pairwise
with open('input.txt','r') as f:
    l=[x.strip() for x in f.readlines()]
s=(0,0)
e=(0,0)
for y in range(len(l)):
    for x in range(len(l[0])):
        z=l[y][x]
        if z=='S':
            s=(y,x)
        elif z=='E':
            e=(y,x)
q=[(0,s,'r',(-1,-1))]
c={}
p={}
while q:
    t=heappop(q)
    if l[t[1][0]][t[1][1]]=='#':
        continue
    if t[1] not in c or t[0]<c[t[1]]-1001:
        p[t[1]]=set()
        p[t[1]].add(t[3])
        c[t[1]]=t[0]
    elif t[0]<=c[t[1]]+1000:
        p[t[1]].add(t[3])
    else:
        continue
    heappush(q,(t[0]+1+(0 if t[2]=='d' else 1000),(t[1][0]+1,t[1][1]),'d',t[1]))
    heappush(q,(t[0]+1+(0 if t[2]=='u' else 1000),(t[1][0]-1,t[1][1]),'u',t[1]))
    heappush(q,(t[0]+1+(0 if t[2]=='r' else 1000),(t[1][0],t[1][1]+1),'r',t[1]))
    heappush(q,(t[0]+1+(0 if t[2]=='l' else 1000),(t[1][0],t[1][1]-1),'l',t[1]))
for k in p:
    p[k]=list(p[k])
r=[]
def dfs(n,c,w,d):
    global r
    if n==s and d!=(0,-1):
        c+=1000
    if n==(-1,-1):
        r.append((c,w.copy()))
        return
    if n in w:
        return
    w.add(n)
    for x in p[n]:
        z=(x[0]-n[0],x[1]-n[1])
        dfs(x,c+1+(0 if z==d else 1000),w,z)
    w.remove(n)
dfs(e,0,set(),(0,0))
r=[x[1] for x in r if x[0]==min(r,key=lambda y: y[0])[0]]
r=set(x for y in r for x in y)
print(len(r))
