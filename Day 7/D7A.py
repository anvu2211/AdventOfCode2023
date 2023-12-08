f = open("input.txt", "r")
ip = f.read()
#ip = input()

cardRank = {
    'A' : 0,
    'K' : 1,
    'Q' : 2,
    'J' : 3,
    'T' : 4,
    '9' : 5,
    '8' : 6,
    '7' : 7,
    '6' : 8,
    '5' : 9,
    '4' : 10,
    '3' : 11,
    '2' : 12,
}

def type(cards):
    dict = {}
    for card in cards:
        dict[card] = dict.get(card, 0) + 1
    counts = list(dict.values())
    if len(counts) == 1:
        return 1
    if len(counts) == 2:
        if 4 in counts:
            return 2
        else:
            return 3
    if 3 in counts:
        return 4
    if len(counts) == 3 and 1 in counts:
        return 5
    if 2 in counts:
        return 6
    if len(counts) == 5:
        return 7


def compare_hand(cards1, cards2): #true if 1st is bigger
    if type(cards1) < type(cards2):
        return True
    elif type(cards1) > type(cards2):
        return False
    else:
        for i in range(5):
            if cardRank[cards1[i]] > cardRank[cards2[i]]:
                return True
            elif cardRank[cards1[i]] < cardRank[cards2[i]]:
                return False
    return True

def turn_to_val(cards):
    res = 0
    res += type(cards)
    res *= 100
    for i in range(5):
        res += cardRank[cards[i]]
        res *= 100
    return res

hands = []

for line in ip.split("\n"):
    cards, bid = line.split()
    hands.append((cards, int(bid)))

sorted_hands = sorted(hands, key=lambda x: turn_to_val(x[0]), reverse=True)
res = 0
for i in range(len(sorted_hands)):
    res += sorted_hands[i][1]*(i+1)
print(res)


