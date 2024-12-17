from collections import defaultdict
with open('input.txt','r') as f:
    l=[x.strip() for x in f.readlines()]
v=set()
m,n=len(l),len(l[0])
g=0
for i in range(m):
    for j in range(n):
        s=[(i,j)]
        r=set()
        while s:
            t=s.pop()
            if t in v:
                continue
            else:
                v.add(t)
                r.add(t)
            y,x=t
            h=l[y][x]
            if y-1>=0 and l[y-1][x]==h:
                s.append((y-1,x))
            if y+1<m and l[y+1][x]==h:
                s.append((y+1,x))
            if x-1>=0 and l[y][x-1]==h:
                s.append((y,x-1))
            if x+1<n and l[y][x+1]==h:
                s.append((y,x+1))
        e=defaultdict(lambda: 0)
        for y,x in r:
            e[(y-1,x)]+=1
            e[(y+1,x)]+=1
            e[(y,x-1)]+=1
            e[(y,x+1)]+=1
        for k in r:
            if k in e:
                del e[k]
        p=sum(e.values())
        g+=p*len(r)
print(g)
