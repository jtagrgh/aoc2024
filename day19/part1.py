import sys
sys.setrecursionlimit(10**6)
with open('input.txt','r') as f:
    l=f.readlines()
p=l[0].strip().split(", ")
m=[x.strip() for x in l[2:]]
def dfs(i,w):
    if i==len(w):
        return True
    if i>len(w):
        return False
    d=w[i:]
    f=[x for x in p if all(y==z for y,z in zip(x,d))]
    for a in f:
        if dfs(i+len(a),w):
            return True
    return False
r=sum(dfs(0,w) for w in m)
print(r)