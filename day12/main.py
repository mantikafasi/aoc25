
p1, p2 = 0, 0
with open("input.txt", "r") as file:
    presentSizes = []

    for i in range(6):
        file.readline()

        x = [file.readline().strip() for _ in range(3)]
        e = 0
        for a in x:
            e += a.count("#")
        presentSizes.append(e)
        file.readline()

    while True:
        l = file.readline().strip().split(":")
        if l == [""]:
            break

        regionsize = [int(i) for i in l[0].split("x")]
        if sum([presentSizes[i]*j for i, j in enumerate([int(i) for i in l[1].strip().split(" ")])]) < regionsize[0] * regionsize[1]:
            p1 += 1

print(p1)
