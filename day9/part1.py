with open('input.txt','r') as f:
    l=[int(x) for x in f.readlines()[0].strip()]
i=1
j=len(l)-1 if len(l)%2!=0 else len(l)-2
f=[[] for _ in l]
while i<j:
    if l[i]>=l[j]:
        f[i].append((j,l[j]))
        l[i]-=l[j]
        l[j]=0
        j-=2
    else:
        f[i].append((j,l[i]))
        l[j]-=l[i]
        l[i]=0
        i+=2
for i,n in list(enumerate(l))[::2]:
    if n:
        f[i].append((i,n))
t=0
i=0
for x in f:
    for y in x:
        for j in range(y[1]):
            z=i*(y[0]/2)
            t+=z
            i+=1
print(t)
