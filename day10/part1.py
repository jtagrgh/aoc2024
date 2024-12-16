with open('input.txt','r') as f:
    l=[[int(x) for x in w.strip()] for w in f.readlines()]
m=len(l)
n=len(l[0])
f=[[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if l[i][j]!=0:
            continue
        s=[(i,j)]
        h=set()
        while s:
            y,x=s.pop()
            if l[y][x]==9 and (y,x) not in h:
                f[i][j]+=1
                h.add((y,x))
                continue
            v=l[y][x]
            if y-1>=0 and l[y-1][x]==v+1:
                s.append((y-1,x))
            if y+1<m and l[y+1][x]==v+1:
                s.append((y+1,x))
            if x-1>=0 and l[y][x-1]==v+1:
                s.append((y,x-1))
            if x+1<n and l[y][x+1]==v+1:
                s.append((y,x+1))
t=sum(x for w in f for x in w)
print(t)
