with open('input.txt','r') as f:
    l=[x.strip() for x in f.readlines()]
t=0
for i in range(len(l[0])-2):
    for j in range(len(l)-2):
        c1=''.join(l[i+n][j+n] for n in range(3))
        c2=''.join(l[i+2-n][j+n] for n in range(3))
        t+=all((w=='MAS' or w=='SAM') for w in (c1,c2))
print(t)