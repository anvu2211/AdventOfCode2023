f = open("input.txt", "r")
ip = f.read()
#ip = input()

mul = 1000000
rowGaps = []
colGaps = []

def expandGalaxy(mapp):
    rows = mapp.split("\n")
    length = len(rows[0])
    i = 0
    while i < len(rows):
        if "#" not in rows[i]:
            rowGaps.append(i)
        i += 1
    #mapp = "\n".join(rows)

    i = 0
    while i < len(rows[0]):
        column = [row[i] for row in rows]
        if "#" not in column:
            colGaps.append(i)
        i += 1

expandGalaxy(ip)
galaxies = []
print(rowGaps)
print(colGaps)

for i, row in enumerate(ip.split("\n")):
    for j, content in enumerate(row):
        if content == "#":
            galaxies.append((i, j))

def calculateDistance(p1, p2):
    res = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    for i in rowGaps:
        if (p1[0] < i and i < p2[0]) or (p2[0] < i and i < p1[0]):
            res += mul - 1
    for i in colGaps:
        if (p1[1] < i and i < p2[1]) or (p2[1] < i and i < p1[1]):
            res += mul - 1
    return res

res = 0
for i in range(len(galaxies)):
    j = i + 1
    while(j < len(galaxies)):
        res += calculateDistance(galaxies[i], galaxies[j])
        j += 1

print(res)