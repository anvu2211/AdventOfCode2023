# Manually remove all words in input file first
f = open("input.txt", "r")
ip = f.read()

maps = ip.split("\n\n")[1:]
var = ip.split("\n\n")[0].split()
seed = []
amount = []
for i in range(len(var)):
    if i % 2 == 0:
        seed.append(int(var[i]))
    else:
        amount.append(int(var[i]))
pair = [[]]
for i in range(len(seed)):
    pair[0].append((seed[i], amount[i]))

def check_in_range(id, map): #return next mapping pos, maximmum length
    nearest = 999999999999
    for line in map.split("\n"):
        destination = int(line.split()[0])
        source = int(line.split()[1])
        if source > id and source < nearest:
            nearest = source
        range = int(line.split()[2])
        if id >= source and id <= source + range - 1:
            return destination + (id - source), range - (id - source)
    return id, nearest - id


for i in range(len(maps)):
    pair.append([])
    for source, length in pair[i]:
        while length != 0:
            x, y = check_in_range(source, maps[i])
            if length <= y:
                pair[i+1].append((x, length))
                length = 0
            else:
                length -= y
                pair[i+1].append((x, y))
                source = source + y

res = 999999999999
for x, y in pair[len(pair)-1]:
    res = min(res, x)
print(res)