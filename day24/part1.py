with open('input.txt','r') as f:
   l=[x.strip() for x in f.readlines()]
xor=lambda a,b: int((a and not(b)) or (not(a) and b))
g={}
h={}
for x in l[:l.index('')]:
    t=x.split(': ')
    h[t[0]]=int(t[1])
for x in l[l.index('')+1:]:
    t=x.split(' ')
    g[t[4]]=(t[1],t[0],t[2])
def dfs(n):
    if n in h:
        return h[n]
    t,a,b=g[n]
    if t=='AND':
        r=dfs(a) and dfs(b)
    elif t=='OR':
        r=dfs(a) or dfs(b)
    elif t=='XOR':
        r=xor(dfs(a),dfs(b))
    h[n]=r
    return r
for x in g.keys():
    dfs(x)
ks=sorted([k for k in h.keys() if k[0]=='z'])
vs=[int(h[k]) for k in ks]
r=0
for i,n in enumerate(vs):
    r+=n*2**i
print(r)
