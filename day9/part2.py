with open('input.txt','r') as f:
    l=[int(x) for x in f.readlines()[0].strip()]
b=list(l)
i=1
j=len(l)-1 if len(l)%2!=0 else len(l)-2
f=[[] for _ in l]
while j>=0:
    for i in range(1,j,2):
        if l[i]>=l[j]:
            f[i].append((j/2,l[j]))
            l[i]-=l[j]
            l[j]=0
            break
    j-=2
for i in range(0,len(l),2):
    if l[i]!=0:
        f[i].append((i/2,l[i]))
    else:
        f[i].append((0,b[i]))
for i in range(1,len(l),2):
    if l[i]!=0:
        f[i].append((0,l[i]))
t=0
i=0
for x in f:
    for y in x:
        for z in range(y[1]):
            t+=i*y[0]
            i+=1
print(t)
