m=[[0 for _ in range(30)] for _ in range(30)]
c=(len(m)//2,len(m[0])//2)
for a in range(5):
    for b in range(5-a):
        m[c[0]+a][c[1]+b]=1
        m[c[0]-a][c[1]+b]=1
        m[c[0]+a][c[1]-b]=1
        m[c[0]-a][c[1]-b]=1

for y in range(len(m)):
    for x in range(len(m[0])):
        print(m[y][x],end='')
    print()