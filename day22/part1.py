with open('input.txt','r') as f:
    l=[int(x.strip()) for x in f.readlines()]
p=lambda x,n: (x^n)%16777216
t=0
for n in l:
    for _ in range(2000):
        n=p(n*64,n)
        n=p(int(n/32),n)
        n=p(n*2048,n)
    t+=n
print(t)
