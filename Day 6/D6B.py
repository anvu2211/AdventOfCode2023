import math

f = open("input.txt", "r")
ip = f.read()
#ip = input()

t = ip.split("\n")[0].replace(" ","").split(":")[1:]
d = ip.split("\n")[1].replace(" ","").split(":")[1:]

def cal(t, d):
    x1 = ((t-math.sqrt(t*t - 4*d))/2)
    x2 = (t+math.sqrt(t*t - 4*d))/2
    return math.floor(x1), math.ceil(x2)

for i in range(len(t)):
    x1, x2 = cal(int(t[i]), int(d[i]))
    print(x2-x1-1)