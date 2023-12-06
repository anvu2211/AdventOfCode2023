f = open("input.txt", "r")
ip = f.read()
#ip = input()

t = ip.split("\n")[0].split()[1:]
d = ip.split("\n")[1].split()[1:]

def cal(t, d):
    res = 0
    for i in range(t):
        if (t - i)*i > d:
            res += 1
    return res

result = 1
for i in range(len(t)):
    result *= cal(int(t[i]) , int(d[i]))
print(result)