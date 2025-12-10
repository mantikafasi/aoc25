
import itertools
p1,p2 = 0,0

with open("input.txt") as file:
    machines = [e.strip().split(" ") for e in file.readlines()]
    machineData = []
    for m in machines:
        print(m)
        e = {}
        e["light_diagram"] = [bool(int(i)) for i in m[0][1:-1].replace(".", "0").replace("#", "1")]
        e["joltage"] = [map(int,m[-1][1:-1])]
        e["buttons"] = [[int(e) for e in i[1:-1].split(",")] for i in m[1:-1]]
        machineData.append(e)
    

    for m in machineData:
        state = [False for i in range(len(m["light_diagram"]))]
        
        u = 1
        while True:
            if "result" in m:
                break
            for i in itertools.product(m["buttons"], repeat=u):
                state = [False for i in range(len(m["light_diagram"]))]

                for k in i:
                    for j in k:
                        state[j] = not state[j]
                
                if state == m["light_diagram"] and ("result" not in m or m["result"] > len(i)):
                    m["result"] = len(i)
                    break
            u+=1
        
        p1 += m["result"]

print(p1,p2)