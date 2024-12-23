import sys
sys.setrecursionlimit(10**6)
with open('input.txt','r') as f:
    l=f.readlines()
p=l[0].strip().split(", ")
m=[x.strip() for x in l[2:]]
c={}
def dfs(i,w):
    if i==len(w):
        return 1
    if i>len(w):
        return 0
    d=w[i:]
    if d in c:
        return c[d]
    f=[x for x in p if all(y==z for y,z in zip(x,d))]
    r=0
    for a in f:
        r+=dfs(i+len(a),w)
    c[d]=r
    return r
r=(dfs(0,w) for w in m)
print(sum(r))
