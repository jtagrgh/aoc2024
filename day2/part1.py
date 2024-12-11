l=[list(map(int, x.strip().split())) for x in open('input.txt','r')]
s=0
for r in l:
    d=r[0]>r[1]
    c=True
    for n,m in zip(r[1:],r[:-1]):
        if not((m>n)==d):
            c=False
            break
        if not(1 <= abs(m-n) <= 3):
            c=False
            break
    s+=c

print(s)