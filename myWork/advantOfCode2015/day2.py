def day2pt1(equation):
    dimension = equation.split("x")
    for i in range(len(dimension)):
        dimension[i] = int(dimension[i])
    dimension.sort()
    l = dimension[0]
    w = dimension[1]
    h = dimension[2]
    return 2*l*w + 2*w*h + 2*h*l + l*w

def day2pt2(equation):
    dimension = equation.split("x")
    for i in range(len(dimension)):
        dimension[i] = int(dimension[i])
    dimension.sort()
    l = dimension[0]
    w = dimension[1]
    h = dimension[2]
    return 2*l + 2*w + l*w*h

file1 = open('day2text.txt', 'r')
lines = file1.readlines()
total = 0
for i in lines:
    total += day2pt2(i)
print(total)
