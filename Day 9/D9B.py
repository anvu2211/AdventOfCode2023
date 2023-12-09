f = open("input.txt", "r")
ip = f.read()
#ip = input()


def check(nums):
    for i in nums:
        if i != 0:
            return False
    return True
def cal(nums):
    nums = [int(x) for x in nums]
    ss = [nums]
    level = 0
    while not check(ss[level]):
        ss.append([])
        for i in range(len(ss[level])-1):
            ss[level+1].append(ss[level][i+1]-ss[level][i])
        level += 1
    res = 0
    for i in ss:
        res += i[-1]
    return res

result = 0
for line in ip.split("\n"):
    print(cal(line.split()[::-1]))
    result += cal(line.split()[::-1])
print(result)