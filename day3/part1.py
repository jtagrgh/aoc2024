import re
with open('input.txt','r') as f:
    l=''.join(f.readlines())
p=re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
s=0
for m in p.finditer(l):
    n=list(map(int,m.groups()))
    s+=n[0]*n[1]
print(s)