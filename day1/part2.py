l=[l.strip().split() for l in open('input.txt', 'r').readlines()]
a=sorted([int(x[0]) for x in l])
b=sorted([int(x[1]) for x in l])
f={x:0 for x in a+b}
for n in b:
    f[n] += 1
r=sum(x*f[x] for x in a)
print(r)