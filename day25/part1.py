from itertools import product
with open('input.txt','r') as f:
    l=[x.split('\n') for x in (f.read()+'\n').split('\n\n')]
k=[x for x in l if x[0]=='#####']
k=[[sum(c=='#' for c in w)-1 for w in zip(*x)] for x in k]
m=[x for x in l if x[-1]=='#####']
m=[[sum(c=='#' for c in w)-1 for w in zip(*x)] for x in m]
t=0
for x,y in product(k,m):
    t+=all(a+b<=5 for a,b in zip(x,y))
print(t)
