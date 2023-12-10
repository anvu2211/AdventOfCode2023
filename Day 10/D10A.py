import queue

f = open("input.txt", "r")
ip = f.read()
#ip = input()

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
resMap = [[-1 for c in line] for line in ip.split("\n")]

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
        targetType = mapp[targetPos[0]][targetPos[1]]
        if opposite[i] in connection[targetType]:
            resMap[pos[0]][pos[1]] = max(resMap[pos[0]][pos[1]], resMap[targetPos[0]][targetPos[1]] + 1)
            if resMap[targetPos[0]][targetPos[1]] == -1:
                fifo_queue.put(targetPos)

fifo_queue.put(startPos)
while not fifo_queue.empty():
    p = fifo_queue.get()
    print(p)
    BFS(p)

res = 0
for row in resMap:
    for value in row:
        res = max(res, value)
print(res)