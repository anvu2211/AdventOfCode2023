import sys
from math import gcd

f = open("input.txt", "r")
ip = f.read()
#ip = input()

instruction = ip.split("\n\n")[0]
mapp = ip.split("\n\n")[1]

def lcm(xs):
  res = 1
  for x in xs:
    res = (x*res)//gcd(x,res)
  return res

dict = {}
pos = []
def create_map(m):
    for line in m.split("\n"):
        node = line.split("=")[0][:-1]
        if node[2] == 'A' and node not in pos:
            pos.append(node)
        l = line.split("=")[1][2:5]
        r = line.split("=")[1][-4:-1]
        dict[node] = (l,r)
iii = create_map(mapp)

#print(len(pos))


def check_stop(listt):
    for i in listt:
        if i[2] != 'Z':
            return False
    return True

step = 0
res = []
inspection = [[]for i in range(6)]
while step < 1000000:
    for i in instruction:
        step += 1
        for j in range(len(pos)):
            if i == 'L':
                pos[j] = dict[pos[j]][0]
            else:
                pos[j] = dict[pos[j]][1]
            if pos[j][2] == 'Z':
                inspection[j].append(step)
        if check_stop(pos):
            print(step)
            sys.exit()
res = []
for i in range(6):
    res.append(inspection[i][0])

print(lcm(res))