from collections import deque
with open('test_input.txt','r') as f:
    l=[x.strip() for x in f.readlines()]
g={}
for x in l[l.index('')+1:]:
    y=x.split(' ')
    g[y[4]]=(y[0],y[1],y[2])
q=deque()
q.append('z03')
q.append(None)
while len(q)>1:
    t=q.popleft()
    if t==None:
        print()
        q.append(None)
        continue
    print(t,end=' ')
    if t in g:
        q.append(g[t][0])
        q.append(g[t][1])
        q.append(g[t][2])
print()
