with open('input.txt','r') as f:
    l=[x.strip() for x in f.readlines()]
for y in range(len(l)):
    for x in range(len(l[0])):
        if l[y][x]=='S':
            s=(y,x)
        if l[y][x]=='E':
            e=(y,x)
f={}
k=0
x=s
while True:
    f[x]=k
    if x==e:
        break
    k+=1
    q=True
    for y in ((x[0]+1,x[1]),(x[0]-1,x[1]),(x[0],x[1]+1),(x[0],x[1]-1)):
        if l[y[0]][y[1]] in '.SE' and y not in f:
            x=y
            q=False
            break
    if q:
        break
g={}
k=0
x=e
while True:
    g[x]=k
    if x==s:
        break
    k+=1
    q=True
    for y in ((x[0]+1,x[1]),(x[0]-1,x[1]),(x[0],x[1]+1),(x[0],x[1]-1)):
        if l[y[0]][y[1]] in '.SE' and y not in g:
            x=y
            q=False
            break
    if q:
        break
m={}
for y in range(len(l)):
    for x in range(len(l[0])):
        v=l[y][x]
        if v not in ('.SE'):
            continue
        z=(y,x)
        for n in ((y+2,x),(y-2,x),(y,x+2),(y,x-2)):
            if not(0<=n[0]<len(l)) or not(0<=n[1]<len(l[0])) or l[n[0]][n[1]] not in '.SE':
                continue
            m[(z,n)]=f[z]+g[n]+2
c=[(k,m[k]) for k in m if g[s]-m[k]>=100]
print(len(c))
