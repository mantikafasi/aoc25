p1,p2 = 0,0
with open("input.txt") as f:
    grid = f.readlines()
    beams = []

    for g in grid:
        beams.append(list(map(lambda x: 1 if x == 'S' else 0, g)))
    for y,beam in enumerate(beams):
        for x,count in enumerate(beam):
            try:
                if count == 0:
                    continue
                bottom = grid[y + 1][x]
                if bottom  == "^":
                    p1 += 1
                    beams[y + 1][x + 1] += count
                    beams[y + 1][x - 1] += count
                elif bottom == ".":
                    beams[y + 1][x] += count
            except:
                pass

p2 = sum(beams[-1])

print(p1,p2)