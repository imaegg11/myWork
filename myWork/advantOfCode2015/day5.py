def day5pt1(string):
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        return 0
    vowelCount = 0
    vowels = "aeiou"
    doubleCount = 0
    for i in range(len(string)):
        try:
            j = string[i]
            if j in vowels:
                vowelCount += 1
            if j == string[i+1]:
                doubleCount += 1
        except:
            continue
    if vowelCount >= 3 and doubleCount > 0:
        return 1
    else:
        return 0

glob = []
other = []

def day5pt2(string):
    array = []
    yes = 0
    for i in range(len(string)-1):
        if string[i] + string[i+1] in array[:-1]:
            yes = 1
            break
        else:
            array.append(string[i] + string[i+1])

    for i in range(len(string)-2):
        if string[i] == string[i+2] and yes == 1:
            return 1
    return 0

file1 = open('day5text.txt', 'r')
lines = file1.readlines()
total = 0
for i in lines:
    total += int(day5pt2(i.removesuffix("\n")))
print(total)
