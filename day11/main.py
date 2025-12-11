from functools import cache
p1, p2 = 0, 0
connectionMap = {}
allPossibleWays = {}

@cache
def findAllPossibleWays(start, target, hasdac, hasfft):
    r = 0

    for target in connectionMap[start]:
        if target == "out":
            if hasdac and hasfft:
                r += 1
        else:
            r += findAllPossibleWays(target, "out", hasdac or target ==
                                     "dac", hasfft or target == "fft")
    return r


with open("input.txt", "r") as file:

    for i in file.readlines():
        connectionMap[i.split(":")[0]] = i.split(":")[1].strip().split(" ")

    p1 = findAllPossibleWays("you", "out", True, True)
    p2 = findAllPossibleWays("svr", "out", False, False)
print(p1, p2)
