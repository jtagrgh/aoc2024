with open('input.txt','r') as f:
    l=f.readlines()
m=[list(x.strip()) for x in l[:l.index('\n')]]
s=''.join([x.strip() for x in l[l.index('\n')+1:]])
p=(0,0)
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x]=='@':
            p=(y,x)
def dfs(y,x,d):
    global m
    if m[y][x]=='.':
        return True
    elif m[y][x]=='#':
        return False
    else:
        v=dfs(y+d[0],x+d[1],d)
        if v:
            m[y+d[0]][x+d[1]],m[y][x]=m[y][x],m[y+d[0]][x+d[1]]
        return v
for z in s:
    d=(1,0) if z=='v' else (-1,0) if z=='^' else (0,1) if z=='>' else (0,-1)
    p=(p[0]+d[0],p[1]+d[1]) if dfs(p[0],p[1],d) else p
t=0
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x]=='O':
            t+=y*100+x
print(t)