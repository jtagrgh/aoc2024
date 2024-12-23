n=71
with open('input.txt','r') as f:
   l=f.readlines()
l=[tuple(map(int,x.strip().split(','))) for x in l]
s=set()
for i in range(len(l)):
    s.add(l[i])
    q=[]
    v=set()
    q.append((0,0))
    while q:
        t=q.pop()
        if not(0<=t[0]<n) or not(0<=t[1]<n) or t in s or t in v:
            continue
        v.add(t)
        q.append((t[0]+1,t[1]))
        q.append((t[0]-1,t[1]))
        q.append((t[0],t[1]+1))
        q.append((t[0],t[1]-1))
    if (n-1,n-1) not in v:
        print(l[i])
        break
