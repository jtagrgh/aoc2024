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
        if not r:
            continue
        s=set((y-1,x) for y,x in r if (y-1,x) not in r)
        q=0
        while s:
            q+=1
            f=[s.pop()]
            while f:
                y,x=f.pop()
                if (k:=(y,x-1)) in s:
                    s.remove(k)
                    f.append(k)
                if (k:=(y,x+1)) in s:
                    s.remove(k)
                    f.append(k)
        s=set((y+1,x) for y,x in r if (y+1,x) not in r)
        while s:
            q+=1
            f=[s.pop()]
            while f:
                y,x=f.pop()
                if (k:=(y,x-1)) in s:
                    s.remove(k)
                    f.append(k)
                if (k:=(y,x+1)) in s:
                    s.remove(k)
                    f.append(k)
        s=set((y,x+1) for y,x in r if (y,x+1) not in r)
        while s:
            q+=1
            f=[s.pop()]
            while f:
                y,x=f.pop()
                if (k:=(y-1,x)) in s:
                    s.remove(k)
                    f.append(k)
                if (k:=(y+1,x)) in s:
                    s.remove(k)
                    f.append(k)
        s=set((y,x-1) for y,x in r if (y,x-1) not in r)
        while s:
            q+=1
            f=[s.pop()]
            while f:
                y,x=f.pop()
                if (k:=(y-1,x)) in s:
                    s.remove(k)
                    f.append(k)
                if (k:=(y+1,x)) in s:
                    s.remove(k)
                    f.append(k)
        g+=q*len(r)
print(g)
