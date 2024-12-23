from collections import deque
n=71
with open('input.txt','r') as f:
   l=f.readlines()
l=[tuple(map(int,x.strip().split(','))) for x in l]
s=set([(x[1],x[0]) for x in l[:1024]])
a={}
q=deque()
q.append(((0,0),(-1,-1)))
while q:
    t=q.popleft()
    if not(0<=t[0][0]<n) or not(0<=t[0][1]<n) or t[0] in s or t[0] in a:
        continue
    a[t[0]]=t[1]
    if t[0]==(n-1,n-1):
        break
    q.append(((t[0][0]+1,t[0][1]),t[0]))
    q.append(((t[0][0]-1,t[0][1]),t[0]))
    q.append(((t[0][0],t[0][1]+1),t[0]))
    q.append(((t[0][0],t[0][1]-1),t[0]))
x=(n-1,n-1)
k=-1
while x!=(-1,-1):
    k+=1
    x=a[x]
print(k)
