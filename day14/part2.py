import re
from time import sleep
with open('input.txt','r') as f:
    l=f.readlines()
p=re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')
r=[list(map(int,p.match(w).groups())) for w in l]
m,n=103,101
i=0
while True:
    d=sum((x[0]-n/2)**2+x[1]-m//2 for x in r)
    if d<200000:
        g=[[0 for _ in range(n)] for _ in range(m)]
        for x in r:
            g[x[1]][x[0]]='*'
        for y in range(m):
            for x in range(n):
                z=g[y][x]
                print(z if z else '.', end='')
            print()
        print(i)
        input()
    i+=1
    for x in r:
        x[0]=(x[0]+x[2])%n
        x[1]=(x[1]+x[3])%m
