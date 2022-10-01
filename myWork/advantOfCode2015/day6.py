grid = []
for i in range(0,1000):
    grid.append([0 for i in range(0,1000)])

def day6pt1(instructions):
    arr = [0,1]
    for i in range(instructions[2] - instructions[0] + 1):
        for j in range(instructions[3] - instructions[1] + 1):
            if instructions[4] == 1:
                grid[i+instructions[0]][j+instructions[1]] = 1
            elif instructions[4] == 0:
                grid[i+instructions[0]][j+instructions[1]] = 0
            else:
                grid[i+instructions[0]][j+instructions[1]] = arr[arr.index(grid[i+instructions[0]][j+instructions[1]])-1]

def day6pt2(instructions):
    for i in range(instructions[2] - instructions[0] + 1):
        for j in range(instructions[3] - instructions[1] + 1):
            if instructions[4] == 1:
                grid[i+instructions[0]][j+instructions[1]] += 1
            elif instructions[4] == 0:
                if grid[i+instructions[0]][j+instructions[1]] != 0:
                    grid[i+instructions[0]][j+instructions[1]] -= 1
            else:
                grid[i+instructions[0]][j+instructions[1]] += 2

file1 = open('day6text.txt', 'r')
lines = file1.readlines()
for line in lines:
    i = line.removesuffix("\n")
    num = i.split(" ")
    if "toggle" in i:
        split = [eval(i) for i in num[1].split(",") + num[3].split(",") + ["-1"]]
        day6pt2(split)
    elif "on" in i:
        split = [eval(i) for i in num[2].split(",") + num[4].split(",") + ["1"]]
        day6pt2(split)
    else:
        split = [eval(i) for i in num[2].split(",") + num[4].split(",") + ["0"]]
        day6pt2(split)

total = 0

for i in grid:
    for j in i:
        total += j
print(total)
