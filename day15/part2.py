with open('input.txt','r') as f:
    l=f.readlines()
m=[list(x.strip()) for x in l[:l.index('\n')]]
s=''.join([x.strip() for x in l[l.index('\n')+1:]])
for y in reversed(range(len(m))):
    for x in reversed(range(len(m[0]))):
        z=m[y][x]
        m[y][x]='##' if z=='#' else '[]' if z=='O' else '..' if z=='.' else '@.'
m=[list(''.join(x)) for x in m]
p=(0,0)
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x]=='@':
            p=(y,x)
def dfs(y,x,d,m):
    if m[y][x]=='.':
        return True
    elif m[y][x]=='#':
        return False
    else:
        z=m[y+d[0]][x+d[1]]
        v=dfs(y+d[0],x+d[1],d,m)
        if d[0]!=0 and z in '[]':
            v=v and dfs(y+d[0],x+d[1]+(1 if z=='[' else -1),d,m)
        if v:
            m[y+d[0]][x+d[1]],m[y][x]=m[y][x],m[y+d[0]][x+d[1]]
        return v
for z in s:
    d=(1,0) if z=='v' else (-1,0) if z=='^' else (0,1) if z=='>' else (0,-1)
    m_=[list(x) for x in m]
    if dfs(p[0],p[1],d,m_):
        m=m_
        p=(p[0]+d[0],p[1]+d[1])
t=0
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x]=='[':
            t+=y*100+x
print(t)