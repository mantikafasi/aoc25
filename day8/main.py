
import math
import heapq
import itertools

p1,p2 = 0,0
circuits = []
junctionBoxes = []

def is_connected(j1,j2):
    for c in circuits:
        if j1 in c and j2 in c:
            return True
    return False

def merge_circuits(c1,c2):
    if c1 == c2: return
    circuits[c1].extend(circuits[c2])
    circuits.pop(c2)

def find_in_circuit(j1):    
    for i1,c in enumerate(circuits):
        if j1 in c:
            return i1
    return -1

with open("input.txt", "r") as file:
    
    for line in file.readlines():
        junctionBoxes.append([int(i) for i in line.split(",")])    
        circuits.append([junctionBoxes[-1]])
    allResults = []

    for c1, c2 in itertools.combinations(junctionBoxes, 2):
        heapq.heappush(allResults, (math.dist(c1, c2), c1, c2))
        
    allResults.sort(key=lambda x: x[0])
    heapq.heapify(allResults)

    t1 = []

    resIx = 0
    while True:        
        if resIx == 1000:
            circuits.sort(key=lambda x: len(x))
            p1 = len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3])

        _, c1,c2 = heapq.heappop(allResults)

        c2_c_ix = find_in_circuit(c2)
        c1_c_ix = find_in_circuit(c1)

        resIx += 1
        
        merge_circuits(c2_c_ix,c1_c_ix)

        if len(circuits) == 1:
            p2 = c1[0] * c2[0]
            break


print(p1,p2)