l,r,k = 50,0,0
with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        c = line[0]
        n = int(line[1:])
        p=l
        if c == "R":
            l -= n
        elif c == "L":
            l += n
        print("L", l)
        if l<0:
            k+=int(-(l/100)) + 1
            # print(-(l//100))
            l%=100
            
        if l>99:
            k+=int((l)/100) - 1
            l%=100

            
        if l==0:r+=1

# GAVE UP THIS METHOD ON PART 2

print(r,k)