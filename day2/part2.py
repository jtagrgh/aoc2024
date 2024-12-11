l=[list(map(int, x.strip().split())) for x in open('input.txt','r')]
s=0
for r in l:
    for i in range(len(r)):
        d=-1
        g=True
        for j in range(len(r)):
            if j==i: continue
            k=j+2 if j+1==i else j+1
            if k>=len(r):
                break
            d=d if d!=-1 else r[k]>r[j]
            if (r[k]>r[j])!=d or not(1<=abs(r[k]-r[j])<=3):
                g=False
                break
        if g:
            s+=1
            break
print(s)