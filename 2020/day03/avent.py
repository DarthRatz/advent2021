import math

# f = open("2020/day03/test.txt", "r")
f = open("2020/day03/input.txt", "r")
lines = f.read().splitlines()

instructions = [line for line in lines]


totals = []
xinc = [1, 3, 5, 7, 1]
yinc = [1, 1, 1, 1, 2]
for i in range(len(xinc)):
    posx, posy = 0, 0
    total = 0
    while posy < len(instructions):
        if (instructions[posy][posx]) == "#":
            total += 1
        posx += xinc[i]
        posy += yinc[i]
        posx %= len(instructions[0])
    print(total)
    totals.append(total)
print(math.prod(totals))
