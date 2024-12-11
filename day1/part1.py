l=[l.strip().split() for l in open('input.txt', 'r').readlines()]
a=sorted([int(x[0]) for x in l])
b=sorted([int(x[1]) for x in l])
r=sum(abs(x-y) for x,y in zip(a,b))
print(r)