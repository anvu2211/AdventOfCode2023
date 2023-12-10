import queue

f = open("input.txt", "r")
ip = f.read()
#ip = input()

ip = str("\n"+'|'*len(ip.split("\n")[0])+"\n").join(ip.split("\n"))
ip = "\n".join(['-'.join(line) for line in ip.split("\n")])

direction = {"up": (-1, 0), "down": (1,0), "l": (0,-1), "r": (0,1)}
connection = {
    "|": ("up", "down"),
    "-": ("l", "r"),
    "L": ("up", "r"),
    "J": ("up", "l"),
    "7": ("l", "down"),
    "F": ("r", "down"),
    "S": ("l", "r", "up", "down"),
    ".": (),
}

opposite = {
    "l": "r",
    "r": "l",
    "up": "down",
    "down": "up",
}

def isExist(i, j, l, h):
    if i < 0 or j < 0:
        return False
    if i >= h or j >= l:
        return False
    return True


mapp = [[c for c in line] for line in ip.split("\n")]
initialMap = mapp
resMap = [[-1 for c in line] for line in ip.split("\n")]
length = len(resMap[0])
height = len(resMap)

startPos = -1
for i, line in enumerate(mapp):
    for j, c in enumerate(line):
        if c == "S":
            startPos = (i, j)
resMap[startPos[0]][startPos[1]] = 0

fifo_queue = queue.Queue()
def BFS(pos):
    pipeType = mapp[pos[0]][pos[1]]
    connections = connection[pipeType]
    for i in connections:
        targetPos = (pos[0] + direction[i][0], pos[1] + direction[i][1])
        if isExist(targetPos[0], targetPos[1], length, height ) == False:
            continue
        targetType = mapp[targetPos[0]][targetPos[1]]
        if opposite[i] in connection[targetType]:
            resMap[pos[0]][pos[1]] = max(resMap[pos[0]][pos[1]], resMap[targetPos[0]][targetPos[1]] + 1)
            if resMap[targetPos[0]][targetPos[1]] == -1:
                resMap[targetPos[0]][targetPos[1]] = 0
                fifo_queue.put(targetPos)

fifo_queue.put(startPos)
while not fifo_queue.empty():
    p = fifo_queue.get()
    BFS(p)

for i, row in enumerate(resMap):
    for j, value in enumerate(row):
        if value == -1:
            resMap[i][j] = 'S'
        else:
            resMap[i][j] = '.'
mapp = resMap
resMap = [[-1 for c in line] for line in ip.split("\n")]

for i, row in enumerate(mapp):
    for j, value in enumerate(row):
        if i == 0 or i == height-1 or j == 0 or j == length - 1:
            if value == "S" and resMap[i][j] == -1:
                resMap[i][j] = 0
                fifo_queue.put((i,j))
                while not fifo_queue.empty():
                    p = fifo_queue.get()
                    BFS(p)

res = 0
for i, row in enumerate(resMap):
    for j, value in enumerate(row):
        if value == -1 and mapp[i][j] == "S" and i % 2 == 0 and j % 2 == 0:
            res += 1
print(res)