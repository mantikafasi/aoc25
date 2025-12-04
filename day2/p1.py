p1,p2 = 0,0

with open('input.txt') as f:
    for r in f.read().strip().split(","):
        s,e = (int(i) for i in r.split("-"))

        for j in range(s,e + 1):
            f = str(j)
            for k in range(2,len(f) + 1):
                if f[0:int(len(f)/k)]*k == f:
                    p2+=j   
                    break

            if f[0:int(len(f)/2)]*2 == f:p1+=j


print(p1,p2)
