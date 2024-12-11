with open('input.txt','r') as f:
    l=[x.strip() for x in f.readlines()]
t=0
for i in range(len(l)):
    for j in range(len(l)-3):
        w=l[i][j:j+4]
        t+=(w=='XMAS')+(w=='SAMX')
for i in range(len(l)-3):
    for j in range(len(l)-3):
        w=''.join(l[i+n][j+n] for n in range(4))
        t+=(w=='XMAS')+(w=='SAMX')
for i in range(3,len(l)):
    for j in range(len(l)-3):
        w=''.join(l[i-n][j+n] for n in range(4))
        t+=(w=='XMAS')+(w=='SAMX')
for i in range(0,len(l)-3):
    for j in range(len(l)):
        w=''.join(l[i+n][j] for n in range(4))
        t+=(w=='XMAS')+(w=='SAMX')
print(t)