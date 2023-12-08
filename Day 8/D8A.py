import sys

f = open("input.txt", "r")
ip = f.read()
#ip = input()

instruction = ip.split("\n\n")[0]
mapp = ip.split("\n\n")[1]

dict = {}
def create_map(m):
    for line in m.split("\n"):
        node = line.split("=")[0][:-1]
        l = line.split("=")[1][2:5]
        r = line.split("=")[1][-4:-1]
        dict[node] = (l,r)

iii = create_map(mapp)
pos = 'AAA'
step = 0
while True:
    for i in instruction:
        step += 1
        if i == 'L':
            pos = dict[pos][0]
        else:
            pos = dict[pos][1]
        if pos == 'ZZZ':
            print(step)
            sys.exit()
