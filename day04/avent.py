f = open("day04/test.txt", "r")
# f = open("day04/input.txt", "r")
lines = f.readlines()

bingo_numbers = lines[0].split(',')
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
        i=0
print(bingo_cards_list)

for number in bingo_numbers:
    for card in bingo_cards_list:
        for row in card:
            print("ROW",row)
        for i in range(5):
            column = [row[i] for row in card]
            print("COLUMN",column)
