p1,p2 = 0,0

with open("input.txt") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        prev = 0
        maxjoltage = 0

        for i,c in enumerate(line):
            c = int(c)
            if i != len(line)-1 and c > maxjoltage:
                maxjoltage = c
                prev = 0
                continue
        
            if c > prev and maxjoltage != 0:
                prev = c    
        p1 += maxjoltage* 10 + prev

print(p1,p2)
