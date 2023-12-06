f = open("input.txt", "r")
ip = f.read()
total = 0
for line in ip.split():
    val = 0
    for i in line:
        if i.isdigit():
            val += int(i)*10
            break
    for i in reversed(line):
        if i.isdigit():
            val += int(i)
            break
    total += val
print(total)