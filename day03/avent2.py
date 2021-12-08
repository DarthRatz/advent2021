# f = open("day03/test.txt", "r")
f = open("day03/input.txt", "r")
lines = f.readlines()

instructions = [str(line).strip() for line in lines]


def common(transpose):
    most_common = ""
    least_common = ""
    for bits in transpose:
        one = bits.count("1")
        zero = bits.count("0")
        if one >= zero:
            most_common += "1"
            least_common += "0"
        if zero > one:
            most_common += "0"
            least_common += "1"
    return most_common, least_common


oxygen = instructions.copy()
pos = 0
while len(oxygen) > 1:
    transpose = []
    for ins in range(len(oxygen[0])):
        temp_string = "".join(i[ins] for i in oxygen)
        transpose.append(temp_string)

    most_common, least_common = common(transpose)
    oxygen[:] = [x for x in oxygen if x[pos] == most_common[pos]]
    pos += 1
print(oxygen)

carbon = instructions.copy()
pos = 0
while len(carbon) > 1:
    transpose = []
    for ins in range(len(carbon[0])):
        temp_string = "".join(i[ins] for i in carbon)
        transpose.append(temp_string)

    most_common, least_common = common(transpose)
    carbon[:] = [x for x in carbon if x[pos] == least_common[pos]]
    pos += 1
print(carbon)

print(int(oxygen[0], base=2) * int(carbon[0], base=2))
