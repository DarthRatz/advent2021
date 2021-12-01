f = open("input01.txt", "r")
lines = f.read().splitlines()

numbers = [int(line) for line in lines]
threeMeasure = [
    numbers[i] + numbers[i + 1] + numbers[i + 2] for i in range(len(numbers) - 2)
]

total = 0
priorNumber = 0
for number in threeMeasure:
    if number > priorNumber:
        total += 1
    priorNumber = number
total -= 1
print(total)
