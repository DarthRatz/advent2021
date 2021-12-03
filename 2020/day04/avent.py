f = open("2020/day04/test.txt", "r")
f = open("2020/day04/input.txt", "r")
lines = f.read().splitlines()

instructions = [line for line in lines]

passports = []
p1 = {}
for ins in instructions:
    for i in ins.split():
        p1[i.split(":")[0]] = i.split(":")[1]
    if ins == "":
        passports.append(p1)
        p1 = {}

for passport in passports:
    for valids in ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]:
        try:
            passport[valids]
        except:
            print(f"Missing: {valids} from {passport}")
            passports.remove(passport)
            break

print(len(passports))
