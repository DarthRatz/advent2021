# f = open("2020/day02/test.txt", "r")
f = open("2020/day02/input.txt", "r")
lines = f.read().splitlines()

instructions = [str(line) for line in lines]

total = 0
total2 = 0
for instruction in instructions:
    values, key, password = instruction.split()
    count = password.count(key[0])
    lower, higher = values.split("-")
    if count >= int(lower) and count <= int(higher):
        total += 1
    if {password[int(lower) - 1] == key[0]} ^ {password[int(higher) - 1] == key[0]}:
        total2 += 1

print(total)
print(total2)
