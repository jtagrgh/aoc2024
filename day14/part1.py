import re
with open('input.txt','r') as f:
    l=f.readlines()
p=re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')
r=[list(map(int,p.match(w).groups())) for w in l]
m,n=103,101
for _ in range(100):
    for x in r:
        x[0]=(x[0]+x[2])%n
        x[1]=(x[1]+x[3])%m
t=[[0,0],[0,0]]
for x in r:
    if x[0]==n//2 or x[1]==m//2:
        continue
    t[x[0]>n//2][x[1]>m//2]+=1
s=1
for x in t:
    for y in x:
        s*=y
print(s)