def mg(fn):
    with open(fn,'r') as f:
        l=[x.strip() for x in f.readlines()]
    g={}
    for w in l[l.index('')+1:]:
        x=w.split(' -> ')
        g[x[0]]=x[1]
    return g
g1=mg('fixed_input.txt')
g0=mg('input.txt')
s=[]
for k in g1:
    if g1[k]!=g0[k]:
        s.append(g1[k])
print(','.join(sorted(s)))
