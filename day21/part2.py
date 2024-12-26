from collections import deque
from itertools import product,pairwise
g={
    (0,0):'7',
    (0,1):'8',
    (0,2):'9',
    (1,0):'4',
    (1,1):'5',
    (1,2):'6',
    (2,0):'1',
    (2,1):'2',
    (2,2):'3',
    (3,1):'0',
    (3,2):'A',
}
h={
    (0,1):'^',
    (0,2):'A',
    (1,0):'<',
    (1,1):'v',
    (1,2):'>'
}
def dm(g):
    p={}
    for k in g:
        a={}
        c={}
        q=deque()
        v=set()
        q.append((k,(-1,-1),0))
        while q:
            t,b,j=q.popleft()
            if t not in g or (t in c and j>c[t]):
                continue
            elif t not in c:
                c[t]=j
                a[t]=set()
            a[t].add(b)
            q.append(((t[0]+1,t[1]),t,j+1))
            q.append(((t[0]-1,t[1]),t,j+1))
            q.append(((t[0],t[1]+1),t,j+1))
            q.append(((t[0],t[1]-1),t,j+1))
        d={}
        def dfs(n,z,p):
            if n==(-1,-1):
                z.append(p.copy())
                return
            p.append(n)
            for m in a[n]:
                dfs(m,z,p)
            p.pop()
        for x in a:
            z=[]
            dfs(x,z,[])
            sk=[]
            for w in z:
                s=''
                for u,v in pairwise(reversed(w)):
                    e=(v[0]-u[0],v[1]-u[1])
                    s+='>' if e[1]==1 else '<' if e[1]==-1 else '^' if e[0]==-1 else 'v'
                sk.append(s)
            # bsk=min(sk,key=lambda x: sum(1 for y in pairwise(x) if y[0]!=y[1]))
            d[g[x]]=sk
        p[g[k]]=d
    return p

gm=dm(g)
hm=dm(h)

mem={}
def dfs(seq,md,cd):
    if cd==md:
        return len(seq)
    seq='A'+seq
    k=(seq,md,cd)
    if k in mem:
        return mem[k]
    t=0
    for a,b in pairwise(seq):
        ssq=gm[a][b] if cd==0 else hm[a][b]
        ssq=[sq+'A' for sq in ssq]
        t+=min(dfs(sq,md,cd+1) for sq in ssq)
    mem[k]=t
    return t

with open('input.txt','r') as f:
    l=[x.strip() for x in f.readlines()]

t=0
for w in l:
    print(w)
    n=int(''.join(x for x in w if x.isdigit()))
    m=dfs(w,26,0)
    t+=(n*m)
print(t)
