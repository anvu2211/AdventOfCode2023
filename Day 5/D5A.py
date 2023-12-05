# Manually remove all words in input file first
f = open("input.txt", "r")
ip = f.read()

def check_in_range(id, map):
    for line in map.split("\n"):
        destination = int(line.split()[0])
        source = int(line.split()[1])
        range = int(line.split()[2])
        if id >= source and id <= source + range - 1:
            return destination + (id - source)
    return id


var = ip.split("\n\n")[0].split()

for paragraph in ip.split("\n\n")[1:]:
    for i, val in enumerate(var):
        val = int(val)
        var[i] = check_in_range(val, paragraph)

res = 999999999999
for i in var:
    if res > i:
        res = i
print(res)
