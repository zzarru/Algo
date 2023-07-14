N = int(input())

card_set = []
for card in range(1, N+1):
    card_set.append(card)

discard_set = []
while len(card_set) != 1:
    discard = card_set[0]
    discard_set.append(discard)
    card_set = card_set[1:]
    top_card = card_set.pop(0)
    card_set.append(top_card)

fin_set = discard_set + card_set

for i in fin_set:
    print(i, end=" ")