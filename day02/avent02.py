# f = open("day02/test02.txt", "r")
f = open("day02/input02.txt", "r")
lines = f.readlines()

instructions = [tuple(line.split()) for line in lines]

horizontal = 0
aim = 0
depth = 0
for instruction in instructions:
    if instruction[0] == "forward":
        horizontal += int(instruction[1])
        depth += int(instruction[1]) * aim
    if instruction[0] == "down":
        aim += int(instruction[1])
    if instruction[0] == "up":
        aim -= int(instruction[1])

print(depth)
print(horizontal)
print(depth * horizontal)
