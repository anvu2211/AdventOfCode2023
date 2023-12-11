f = open("input.txt", "r")
ip = f.read()
#ip = input()

def expandGalaxy(mapp):
    rows = mapp.split("\n")
    length = len(rows[0])
    i = 0
    while i < len(rows):
        if "#" not in rows[i]:
            rows.insert(i + 1, '.'*length)
            i += 1
        i += 1
    #mapp = "\n".join(rows)

    i = 0
    while i < len(rows[0]):
        column = [row[i] for row in rows]
        if "#" not in column:
            for n, row in enumerate(rows):
                l = [c for c in row]
                l.insert(i+1, '.')
                rows[n] = ''.join(l)
            i += 1
        i += 1
    return "\n".join(rows)

ip = expandGalaxy(ip)

galaxies = []

for i, row in enumerate(ip.split("\n")):
    for j, content in enumerate(row):
        if content == "#":
            galaxies.append((i, j))

def calculateDistance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

res = 0
for i in range(len(galaxies)):
    j = i + 1
    while(j < len(galaxies)):
        res += calculateDistance(galaxies[i], galaxies[j])
        j += 1

print(res)