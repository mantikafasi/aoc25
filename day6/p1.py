p1,p2 = 0,0

import math

with open("input.txt") as f:
    lines = f.readlines()

    symbols = lines[-1].strip().split()

    numbers = [list(map(int, line.split())) for line in lines[:-1]]

    for i,s in enumerate(symbols):
        r = 0
        for j,k in enumerate(numbers):
            if r == 0: r = k[i];continue
            if s == '*':
                r*=k[i]
            elif s == '+':
                r+=k[i]

        p1+=r
print(p1,p2)