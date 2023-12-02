f = open("input.txt", "r")
ip = f.read()
#ip = input()

def getRGB(line):
    r, g, b = 0, 0, 0
    words = line.split()
    for i, word in enumerate(words):
        word = word[:-1]
        if word == "red":
            r = max(r, int(words[i-1]))
        if word == "green":
            g = max(g, int(words[i-1]))
        if word == "blue":
            b = max(b, int(words[i-1]))
    return r, g, b
def getID(line):
    return int(line.split()[1][:-1])

res = 0
for line in ip.split(sep="\n"):
    line += ';'
    id = getID(line)
    r, g, b = getRGB(line)
    res += r*g*b
print(res)