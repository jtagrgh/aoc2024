import re
p=[re.compile(r'.*X\+(\d+), Y\+(\d+)'),
   re.compile(r'.*X=(\d+), Y=(\d+)')]
with open('input.txt','r') as f:
    l=f.readlines()
m=[[]]
for w in l:
    if w=='\n':
        m.append([])
    else:
        m[-1].append(w)
q=[]
for x in m:
    q.append([])
    q[-1].append([int(y) for y in p[0].match(x[0]).groups()])
    q[-1].append([int(y) for y in p[0].match(x[1]).groups()])
    q[-1].append([int(y) for y in p[1].match(x[2]).groups()])
b=[]
for z in q:
    b.append(float('inf'))
    for i in range(1, 201):
        for j in range(1, 201):
            x=i*z[0][0]+j*z[1][0]
            y=i*z[0][1]+j*z[1][1]
            if x==z[2][0] and y==z[2][1]:
                b[-1]=min(b[-1],i*3+j)
print(sum(x for x in b if x!=float('inf')))