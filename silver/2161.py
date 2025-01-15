cards = []
popped_cards = []

for i in range(int(input())):
    cards.append(i+1)

while cards != []:
    try:
        popped_one = cards[0]
        cards = cards[1:]
        popped_cards.append(popped_one)

        popped_one = cards[0]
        cards = cards[1:]
        cards.append(popped_one)
    except IndexError:
        break

print(*popped_cards)


