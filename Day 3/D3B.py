f = open("input.txt", "r")
ip = f.read()
#ip = input()

w = len(ip.split()[0])
h = len(ip.split())
result = 0

pos_x = [-1, -1, -1, 0, 0, 1, 1, 1]
pos_y = [-1, 0, 1, -1, 1, -1, 0, 1]
def check_adjacent(map, x, y):
    for i in range(8):
        if x+pos_x[i] >= 0 and y+pos_y[i] >= 0 and x+pos_x[i] < h and y+pos_y[i] < w:
            if (not map[x+pos_x[i]][y+pos_y[i]].isdigit()) and not map[x+pos_x[i]][y+pos_y[i]] == '.':
                return True
    return False
def find_number(map, x, y):
    res = 0
    adj = False
    while map[x][y].isdigit():
        if check_adjacent(map , x , y):
            adj = True
        res = res*10+int(map[x][y])
        if y + 1 >= w or (not map[x][y+1].isdigit()):
            break
        else:
            y += 1
    if adj == False:
        res = 0
    print(res , x , y , adj)
    return res

ar = [['0']*w for i in range(h)]
for i in range(h):
    for j in range(w):
        ar[i][j] = ip.split()[i][j]

# for i in range(h):
#     for j in range(w):
#         if ar[i][j].isdigit() and (j == 0 or not ar[i][j-1].isdigit()):
#             #print(i, j)
#             result += find_number(ar, i, j)

island_map = [['0']*w for i in range(h)]
island_position = []
count = 0
for i in range(h):
    for j in range(w):
        if ar[i][j].isdigit():
            if j == 0 or not ar[i][j-1].isdigit():
                count += 1
                island_map[i][j] = count
                island_position.append((i,j))
            else:
                island_map[i][j] = island_map[i][j-1]
        else:
            island_map[i][j] = 0

for x in range(h):
    for y in range(w):
        if ar[x][y] == '*':
            listt = []
            for i in range(8):
                if x+pos_x[i] >= 0 and y+pos_y[i] >= 0 and x+pos_x[i] < h and y+pos_y[i] < w:
                    if island_map[x+pos_x[i]][y+pos_y[i]] != 0 and island_map[x+pos_x[i]][y+pos_y[i]] not in listt:
                        listt.append(island_map[x+pos_x[i]][y+pos_y[i]])
            if len(listt) == 2:
                x1, y1 = island_position[listt[0]-1]
                val1 = find_number(ar, x1, y1)
                x2, y2 = island_position[listt[1]-1]
                val2 = find_number(ar, x2, y2)
                result += val1*val2
                print(val1 , " x ", val2)
print(result)