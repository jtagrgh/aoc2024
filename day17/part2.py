import re
from z3 import *
p=re.compile(r'Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([\d,]+)')
with open('input.txt','r') as f:
    l=f.read()
p=p.match(l).groups()[-1]
p=[int(x) for x in p.split(',')]
r=[x*3 for x in range(len(p))]
a=BitVec('a',48)
c=[((LShR(a,y)&0b111^0b101^(LShR(LShR(a,y),(LShR(a,y)&0b111^0b001))))&0b111)==x for x,y in zip(p,r)]
solve(c)