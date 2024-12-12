with open('input.txt','r') as f:
    p=[list(x.strip()) for x in f.readlines()]
for j in range(len(p[0])):
    for i in range(len(p)):
        if p[i][j]=='^':
            s0=(j,i)
d=[(0,-1),(1,0),(0,1),(-1,0)]
k=0
s=s0
while True:
    n=(s[0]+d[k][0],s[1]+d[k][1])
    p[s[1]][s[0]]='X'
    if not(0<=n[0]<len(p[0]) and 0<=n[1]<len(p)):
        break
    if p[n[1]][n[0]]=='#':
        k=(k+1)%len(d)
        continue
    s=n
t=0
b=[[c if c!='X' else '.' for c in w] for w in p]
for i in range(len(p)):
    for j in range(len(p[0])):
        if p[i][j]!='X' or (i,j)==s0:
            continue
        b[i][j]='#'
        k=0
        s=s0
        o=False
        q=s
        v=set()
        while True:
            n=(s[0]+d[k][0],s[1]+d[k][1])
            if not(0<=n[0]<len(b[0]) and 0<=n[1]<len(b)):
                break
            if (s[0],s[1],k) in v:
                o=True
                break
            v.add((s[0],s[1],k))
            if b[n[1]][n[0]]=='#':
                k=(k+1)%len(d)
                continue
            s=n
        t+=o
        b[i][j]='X'
print(t)
