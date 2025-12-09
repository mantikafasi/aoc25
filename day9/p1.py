import itertools
import numpy as np

with open("input.txt", "r") as file:
    tiles = []
    for line in file.readlines():
        tiles.append([int(i) for i in line.strip().split(",")])

    maxSize = 0

    for c1,c2 in itertools.combinations(tiles,2):
        size = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

        if size > maxSize:
            print(c1,c2 )
            maxSize = size

    
    print(maxSize)
