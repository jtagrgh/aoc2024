with open('input.txt','r') as f:
    p=f.readlines()
b=0
for w in p:
    l,r=w.split(': ')
    l=int(l)
    r=list(map(int,r.strip().split()))
    s=[(0,r[0])]
    while s:
        t=s.pop()
        n=t[0]+1
        if n<len(r):
            s.append((n,r[n]+t[1]))
            s.append((n,r[n]*t[1]))
        if t[1]==l and t[0]==len(r)-1:
            b+=l
            break
print(b)