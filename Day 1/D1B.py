characterised_digit = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
reversed_characterised_digit = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]

def find_digit(line , pos , module):
    l = len(line)
    if module == 1:
        for i in range(9):
            for j in range(len(characterised_digit[i])):
                if pos + j >= l:
                    break
                if line[pos+j] != characterised_digit[i][j]:
                    break
                if j == len(characterised_digit[i]) - 1:
                    return i + 1
    if module == 2:
        for i in range(9):
            for j in range(len(reversed_characterised_digit[i])):
                if pos - j < 0:
                    break
                if line[pos-j] != reversed_characterised_digit[i][j]:
                    break
                if j == len(characterised_digit[i]) - 1:
                    return i + 1
    return -1
f = open("../Day 2/input.txt", "r")
ip = f.read()
#ip = input()
total = 0
for line in ip.split():
    val = 0
    for i, c in enumerate(line):
        if c.isdigit():
            val += int(c)*10
            break
        if  (x:=find_digit(line, i, 1)) != -1:
            val += x*10
            break
    for i, c in enumerate(reversed(line)):
        if c.isdigit():
            val += int(c)
            break
        if (x:=find_digit(line, len(line) - i - 1, 2)) != -1:
            val += x
            break
    total += val
print(total)