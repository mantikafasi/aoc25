import math


p1,p2 = 0,0
u = set()
with open('input.txt') as f:
    for r in f.read().strip().split(","):
        s, sl, e, el = (v for i in r.split("-") for v in (int(i), len(i)))
        for l in range(1,int(el/2) + 1):
            for k in range(10**(l-1),10**l):
                for f in range(max(sl,2),el + 1):
                    d = int(math.log10(k)) + 1
                    n = k * (10**(d * (f//l)) - 1) // (10**d - 1)
                    if n >= s and n <= e:
                        if l == f/2:
                            p1+=n
                        if n not in u:
                            p2+=n
                        u.add(n)
print(p1,p2)

# 28146997880 40028128307