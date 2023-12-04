f = open("input.txt", "r")
ip = f.read()
#ip = input()

numCard = len(ip.split("\n"))
cardCount = [1 for i in range(numCard)]

def amount_win(card):
    notID = line.split(":")[1]
    win = notID.split("|")[0].split()
    own = notID.split("|")[1].split()
    amount = 0
    for i in own:
        if i in win:
            amount += 1
    return amount

for i,line in enumerate(ip.split("\n")):
    amount = amount_win(line)
    #print(i , "win", amount)
    if amount > 0:
        for j in range(amount):
            if i + j + 1 < numCard:
                cardCount[i+j+1] += cardCount[i]
    #print(cardCount)

res = 0
for i in cardCount:
    res += i
print(res)