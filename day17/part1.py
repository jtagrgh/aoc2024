import re
p=re.compile(r'Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([\d,]+)')
with open('input.txt','r') as f:
    l=f.read()
a,b,c,p=p.match(l).groups()
a,b,c=map(int,(a,b,c))
p=[int(x) for x in p.split(',')]
i=0
r=[]
while i<len(p)-1:
    x,y=p[i],p[i+1]
    z=a if y==4 else b if y==5 else c if y==6 else y
    # print(f'x:{x} y:{y} z:{z} a:{a} b:{b} c:{c}')
    # print(r)
    # input()
    if x==0:
        a=int((a/2**z)%2**32)
    elif x==1:
        b=int(b^y)
    elif x==2:
        b=int(z%2**3)
    elif x==3 and a:
        i=y
        continue
    elif x==4:
        b=int(b^c)
    elif x==5:
        r.append(z%2**3)
    elif x==6:
        b=int((a/2**z)%2**32)
    elif x==7:
        c=int((a/2**z)%2**32)
    i+=2
print(','.join(map(str,r)))