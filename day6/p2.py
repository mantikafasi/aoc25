p1,p2 = 0,0

with open("input.txt") as f:
    lines = f.readlines()
    symbols = lines[-1].split()
    r = list(zip(*lines[:-1]))

    si = 0
    turkiye = 0
    for k in r:
        joined = "".join(k).strip()
        if joined == "": 
            si+=1
            p2 += turkiye
            turkiye = 0
            continue
        joined = int(joined)
        if symbols[si] == '*':
            if turkiye == 0:
                turkiye = joined
            else:
                turkiye*=joined
        elif symbols[si] == '+':
            turkiye+=joined
print(p1,p2)