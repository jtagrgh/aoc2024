with open('input.txt','r') as f:
    l=[int(x) for x in f.readlines()[0].split()]
def dp(k,i,h={}):
    if i==75:
        return 1
    if (k,i) in h:
        return h[(k,i)]
    if k==0:
        v=dp(1,i+1,h)
    else:
        c=str(k)
        if len(c)%2==0:
            m=int(len(c)/2)
            v=dp(int(c[:m]),i+1,h) + dp(int(c[m:]),i+1,h)
        else:
            v=dp(k*2024,i+1,h)
    h[(k,i)]=v
    return v
t=0
for x in l:
    t+=dp(x,0)
print(t)
