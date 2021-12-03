# f = open("day03/test.txt", "r")
f = open("day03/input.txt", "r")
lines = f.readlines()

instructions = [str(line) for line in lines]

transpose = []

for ins in range(len(instructions[0])):
    temp_string = "".join(i[ins] for i in instructions)
    transpose.append(temp_string)

transpose.pop()
# print(transpose)

most_common = ""
least_common = ""
for bits in transpose:
    one = bits.count("1")
    zero = bits.count("0")
    if one > zero:
        most_common += "1"
        least_common += "0"
    if zero > one:
        most_common += "0"
        least_common += "1"

gamma_rate = int(most_common, base=2)
epsilon_rate = int(least_common, base=2)
print(gamma_rate * epsilon_rate)
