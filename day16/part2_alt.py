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
q=[(0,(s,'r'),((-1,-1),''))]
c={}
p={}
while q:
    t=heappop(q)
    g,k,a=t
    (y,x),d=k
    if l[y][x]=='#':
        continue
    if k not in c or g<c[k]:
        p[k]=set()
        p[k].add(a)
        c[k]=t[0]
    elif t[0]==c[k]:
        p[k].add(a)
    else:
        continue
    heappush(q,(g+1+(0 if d=='d' else 1000),((y+1,x),'d'),k))
    heappush(q,(g+1+(0 if d=='u' else 1000),((y-1,x),'u'),k))
    heappush(q,(g+1+(0 if d=='r' else 1000),((y,x+1),'r'),k))
    heappush(q,(g+1+(0 if d=='l' else 1000),((y,x-1),'l'),k))
h=[(x,c[x]) for x in c if x[0]==e]
f=min(h,key=lambda x: x[1])[0]
r=[]
h=[[f,set(),0,(0,0),0]]
while h:
    n,w,g,d,i=h[-1]
    if i==0:
        h[-1][-1]=1
        if n[0]==s:
            r.append((g,w.copy()))
            h.pop()
            continue
        if n in w:
            continue
        w.add(n)
        for x in p[n]:
            z=(x[0][0]-n[0][0],x[0][1]-n[0][1])
            h.append([x,w,g+1+(0 if z==d else 1000),z,0])
    else:
        w.remove(n)
        h.pop()
r=set(x[0] for y in r for x in y[1])
print(len(r)+1)