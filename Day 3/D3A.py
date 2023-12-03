f = open("input.txt", "r")
ip = f.read()
#ip = input()

w = len(ip.split()[0])
h = len(ip.split())
result = 0

def check_adjacent(map, x, y):
    pos_x = [-1, -1, -1, 0, 0, 1, 1, 1]
    pos_y = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        if x+pos_x[i] >= 0 and y+pos_y[i] >= 0 and x+pos_x[i] < h and y+pos_y[i] < w and (not map[x+pos_x[i]][y+pos_y[i]].isdigit()) and not map[x+pos_x[i]][y+pos_y[i]] == '.':
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
    print(res , x , y , check_adjacent(map, x, y))
    return res

ar = [['0']*w for i in range(h)]
for i in range(h):
    for j in range(w):
        ar[i][j] = ip.split()[i][j]

for i in range(h):
    for j in range(w):
        if ar[i][j].isdigit() and (j == 0 or not ar[i][j-1].isdigit()):
            #print(i, j)
            result += find_number(ar, i, j)

print(result)