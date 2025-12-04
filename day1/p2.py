l,r,k = 50,0,0
with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        c = line[0]
        n = int(line[1:])
        p=l
        if c == "R":
            for _i in range(n):
                l -= 1
                if l < 0:
                    l = 99
                if l == 0:
                    r += 1
        elif c == "L":
            for _i in range(n):
                l += 1
                if l > 99:
                    l = 0
                if l == 0:
                    r += 1


print(r,k)