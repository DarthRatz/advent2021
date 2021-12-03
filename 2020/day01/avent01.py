# f = open("2020/day01/test01.txt", "r")
f = open("2020/day01/input01.txt", "r")
lines = f.read().splitlines()

numbers = [int(line) for line in lines]

for number in numbers:
    for num in numbers:
        if num + number == 2020:
            print(num * number)
        for n in numbers:
            if n + num + number == 2020:
                print(n * num * number)
