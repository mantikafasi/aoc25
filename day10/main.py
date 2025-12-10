from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, value
p1, p2 = 0, 0

with open("input.txt") as file:
    
    machines = [e.strip().split(" ") for e in file.readlines()]

    machineData = []

    for m in machines:
        print(m)
        e = {}
        e["light_diagram"] = [bool(int(i)) for i in m[0][1:-1].replace(".", "0").replace("#", "1")]
        e["joltage"] = [int(i) for i in m[-1][1:-1].split(",")]
        e["buttons"] = [[int(e) for e in i[1:-1].split(",")] for i in m[1:-1]]
        machineData.append(e)

    for m in machineData:
        prob = LpProblem("",LpMinimize)
        
        button_vars = [LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(len(m["buttons"]))]
        
        prob += lpSum(button_vars)
        
        for j in range(len(m["joltage"])):
            jbuttons = [button_vars[b] for b in range(len(m["buttons"])) if j in m["buttons"][b]]
            if jbuttons: prob += lpSum(jbuttons) == m["joltage"][j]
        
        prob.solve()
        
        if LpStatus[prob.status] == 'Optimal':
            p1 += sum((value(var) or 0) for var in button_vars)
        else:
            print("exploded")

print(p1, p2)