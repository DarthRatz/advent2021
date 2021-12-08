# f = open("day04/test.txt", "r")
f = open("day04/input.txt", "r")
lines = f.readlines()

bingo_numbers = lines[0].split(",")
bingo_numbers = list(map(int, bingo_numbers))

bingo_card = [[0] * 5 for i in range(5)]
bingo_cards_list = []

i = 0
for instructions in lines:
    if len(instructions) == 15:
        bingo_card[i] = instructions.split()
        i += 1
    elif bingo_card != [[0] * 5 for i in range(5)]:
        bingo_cards_list.append(bingo_card.copy())
        bingo_card = [[0] * 5 for i in range(5)]
        i = 0
# print(bingo_cards_list)

numbers_called = []
winning_numbers = []
winning_card = []

for number in bingo_numbers:
    numbers_called.append(number)
    found = False
    for card in list(bingo_cards_list):
        for row in card:
            fiveinarow = 0
            for digit in row:
                for num in numbers_called:
                    if int(digit) == num:
                        fiveinarow += 1
                        if fiveinarow >= 5:
                            winning_card = card.copy()
                            winning_numbers = numbers_called.copy()
                            bingo_cards_list.remove(card)
                            found = True
        if not found:
            for i in range(5):
                column = [row[i] for row in card]
                fiveinarow = 0
                for digit in column:
                    for num in numbers_called:
                        if int(digit) == num:
                            fiveinarow += 1
                            if fiveinarow >= 5:
                                winning_card = card.copy()
                                winning_numbers = numbers_called.copy()
                                bingo_cards_list.remove(card)

flatten_list = sum(winning_card, [])
flatten_list = list(map(int, flatten_list))
l3 = [x for x in flatten_list if x not in winning_numbers]
total = sum(int(digit) for digit in l3)
print(total)
last_number = int(winning_numbers.pop())
print(last_number)
print("FINAL SCORE: ", total * last_number)
