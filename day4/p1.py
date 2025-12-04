p1,p2,grid,le = 0,0,[],0

def run():
    global grid
    grid2 = [row[:] for row in grid]
    r = 0
    for i in range(le):
        for j in range(le):
            if grid[i][j] != '@': continue
            count = 0
            for (x,y) in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1, 1), (1, -1)]:
                if 0 <= (i + x) < le and 0 <= (j + y) < le and grid[(i + x)][(j + y)] == '@':
                    count+=1
            if count < 4:
                r += 1
                grid2[i][j] = '.'
    
    grid = grid2
    return r


with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]
    le = len(grid)

    p1 = run()
    p2+=p1

    while True:
        r = run()
        p2 += r
        if r == 0:
            break

print(p1,p2)