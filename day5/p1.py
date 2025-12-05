freshIds = set()
p2 = 0

with open("input.txt") as f:
    ranges, numbers = f.read().strip().split("\n\n")
    newRanges = []
    for s in ranges.split("\n"):
        r1,r2 = [int(f) for f in s.split("-")]
        newRanges.append([r1,r2])
        for n in numbers.split("\n"):
            n = int(n)
            if n >= r1 and n <= r2:
                freshIds.add(n)

    ranges = newRanges

    ranges.sort()

    newRanges = [ranges[0]]
    for s,e in ranges[1:]:
        last = newRanges[-1]
        if s <= last[1] + 1:
            newRanges[-1] = [last[0], max(last[1], e)]
        else:
            newRanges.append([s,e])
    


    for s in newRanges:
        r1,r2 = s
        p2 += r2-r1 + 1


print(len(freshIds),p2)