with open('input.txt','r') as f:
    l=[int(x) for x in f.readlines()[0].split()]
for _ in range(25):
    n=[]
    for i in range(len(l)):
        if l[i]==0:
            l[i]=1
        else:
            c=str(l[i])
            if len(c)%2==0:
                m=int(len(c)/2)
                l[i]=int(c[:m])
                n.append(int(c[m:]))
            else:
                l[i]*=2024
    l.extend(n)
print(len(l))
