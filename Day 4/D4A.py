f = open("input.txt", "r")
ip = f.read()
#ip = input()

def calculate_point(amount):
    if amount == 0:
        return 0
    else:
        return 2**(amount-1)

def amount_win(card):
    notID = line.split(":")[1]
    win = notID.split("|")[0].split()
    own = notID.split("|")[1].split()
    amount = 0
    for i in own:
        if i in win:
            amount += 1
    return amount

res = 0
for line in ip.split("\n"):
    amount = amount_win(line)
    res += calculate_point(amount)
print(res)