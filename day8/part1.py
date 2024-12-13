with open('input.txt','r') as f:
    p=[x.strip() for x in f.readlines()]
f={}
for i in range(len(p)):
    for j in range(len(p[0])):
        v=p[i][j]
        if v=='.':
            continue
        if v not in f:
            f[v]=[]
        f[v].append((i,j))
v=set()
for k in f:
    for i in range(len(f[k])):
        for j in range(len(f[k])):
            if i==j:continue
            n=(2*f[k][j][0]-f[k][i][0],2*f[k][j][1]-f[k][i][1])
            if 0<=n[0]<len(p) and 0<=n[1]<len(p[0]) and n not in v:
                v.add(n)
print(len(v))
