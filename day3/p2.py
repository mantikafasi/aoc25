p1,p2 = 0,0

with open("input.txt") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        joltagearr = [int(c) for c in line]

        l = 0
        while len(joltagearr) > 12:
            if len(joltagearr) < l + 2:
                break
            if joltagearr[l] < joltagearr[l + 1]:
                joltagearr.pop(l)
                l = 0
            else:
                l += 1
            
        t = 0
        for i in range(12):
            t*=10
            t+=joltagearr[i]
        p2 += t
print(p2)