import itertools
from shapely.geometry.polygon import Polygon
p2 = 0

with open("input.txt", "r") as file:
    maxLen = 0
    
    tiles = []
    for line in file.readlines():
        tiles.append([int(i) for i in line.strip().split(",")])
        if max(tiles[-1]) > maxLen:
            maxLen = max(tiles[-1])

    maxSize = 0


    polygon = Polygon(tiles)

    newTiles = []
    for tx,ty in tiles:
        for dx,dy in [(1,1), (0,1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (0,-1)]:
            newTiles.append([tx+dy,ty+dy])

    tiles.extend(newTiles)

    for c1,c2 in itertools.combinations(tiles,2):
        size = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

        if size < maxSize:
            continue

        possible = True
        s,e = (c1[0], c2[0]) if c2[0]>c1[0] else (c2[0], c1[0])

        if not polygon.contains_properly(Polygon([c1,c2,(c1[0],c2[1]),(c2[0],c1[1])])):
            continue

        if possible:
            maxSize = size

    print(maxSize)
    print(p2)