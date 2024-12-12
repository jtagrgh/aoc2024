with open('input.txt','r') as f:
    p=[list(x.strip()) for x in f.readlines()]
for j in range(len(p[0])):
    for i in range(len(p)):
        if p[i][j]=='^':
            s=(j,i)
d=[(0,-1),(1,0),(0,1),(-1,0)]
k=0
while True:
    n=(s[0]+d[k][0],s[1]+d[k][1])
    if not(0<=n[0]<len(p[0]) and 0<=n[1]<len(p)):
        break
    if p[n[1]][n[0]]=='#':
        k=(k+1)%len(d)
        continue
    p[s[1]][s[0]]='X'
    s=n
print(sum(x=='X' for w in p for x in w)+1)