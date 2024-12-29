from itertools import pairwise
with open('input.txt','r') as f:
    l=[int(x.strip()) for x in f.readlines()]
p=lambda x,n: (x^n)%16777216
v={}
for n in l:
    s=[]
    for _ in range(2000):
        n=p(n*64,n)
        n=p(int(n/32),n)
        n=p(n*2048,n)
        s.append(n)
    vp={}
    s=[x%10 for x in s]
    d=[y-x for x,y in pairwise(s)]
    for i in reversed(range(4,len(d)+1)):
        vp[tuple(d[i-4:i])]=s[i]
    for k in vp:
        if k not in v:
            v[k]=[]
        v[k].append(vp[k])
mk=max(v,key=lambda k: sum(v[k]))
r=sum(v[mk])
print(r)
