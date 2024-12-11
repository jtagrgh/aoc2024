import re
with open('input.txt','r') as f:
    l=''.join(f.readlines())
p=re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)')
s=0
d=True
for m in p.finditer(l):
    g=m.groups()
    if g[2]!=None: d=True
    if g[3]!=None: d=False
    if not d or g[0]==None: continue
    s+=int(g[0])*int(g[1])
print(s)