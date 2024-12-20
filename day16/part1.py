from heapq import *
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
q=[(0,s,'r')]
d=((1,0,'d'),(-1,0,'u'),(0,1,'r'),(0,-1,'l'))
v=set()
while q:
    t=heappop(q)
    v.add(t[1])
    if t[1]==e:
        print(t[0])
        break
    for z in d:
        y=t[1][0]+z[0]
        x=t[1][1]+z[1]
        if l[y][x]!='#' and (y,x) not in v:
            w=1+(0 if t[2]==z[2] else 1000)
            heappush(q,(t[0]+w,(y,x),z[2]))