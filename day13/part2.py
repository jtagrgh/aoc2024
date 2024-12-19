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
    q[-1].append([int(y)+10000000000000 for y in p[1].match(x[2]).groups()])
t=0
for z in q:
    x1,x2,x3=[x[0] for x in z]
    y1,y2,y3=[x[1] for x in z]
    b=(x1*y3-x3*y1)/(x1*y2-x2*y1)
    a=(x3-b*x2)/x1
    if b%1==0 and a%1==0:
        t+=b+3*a
print(int(t))