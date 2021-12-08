# f = open("day04/test.txt", "r")
f = open("day04/input.txt", "r")
lines = f.readlines()

bingo_numbers = lines[0].split(",")
# for number in bingo_numbers:
#     print("int(number)")

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
winning_card = []
winning_card_found = False

for number in bingo_numbers:
    numbers_called.append(number)
    for card in bingo_cards_list:
        for row in card:
            fiveinarow = 0
            for digit in row:
                for num in numbers_called:
                    if digit == num:
                        fiveinarow += 1
                        if fiveinarow == 5:
                            print("ROW: ", row)
                            winning_card = card
                            winning_card_found = True
        for i in range(5):
            column = [row[i] for row in card]
            fiveinarow = 0
            for digit in column:
                for num in numbers_called:
                    if digit == num:
                        fiveinarow += 1
                        if fiveinarow == 5:
                            print("COLUMN: ", column)
                            winning_card = card
                            winning_card_found = True
    if winning_card_found:
        break


print(winning_card, numbers_called)
flatten_list = sum(winning_card, [])
l3 = [x for x in flatten_list if x not in numbers_called]
total = sum(int(digit) for digit in l3)
print(total)
last_number = int(numbers_called.pop())
print(last_number)
print("FINAL SCORE: ", total * last_number)
