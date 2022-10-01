def sort(e):
    return e[0]
def ctc(message, key):
    array = [[i] for i in key]
    for i in range(len(message.replace(" ","")) + len(message.replace(" ", "")) % len(key)):
        num  = i % len(key)
        try:
            array[num].append(message.replace(" ","")[i])
        except: array[num].append(" ")
    array.sort(key=sort)
    coded = ""
    for x in range(len(key)): del array[x][0]
    for i in range(len(message.replace(" ", "")) + len(key)):
        try:
            num = i % len(key)
            coded += array[num][0]
            del array[num][0]
        except:
            pass
    print(coded)
    return coded

def unctc(coded, key):
    keySort = [i for i in key]
    keySort.sort()
    array = [[] for i in key]
    for i in range(len(coded)):
        num  = i % len(key)
        array[num].append(coded[i])
    decoded = []
    decodedString = ""
    for i in key:
        num = keySort.index(i)
        decoded.append(array[num])
        del array[num]
        del keySort[num]
    for i in range(len(coded)+len(key)):
        try:
            num = i % len(key)
            decodedString += decoded[num][0]
            del decoded[num][0]
        except: pass
    print(decodedString)
ctc("hello my friend and this is john", "hack")
unctc("elhlmyofiernanddhitssjion h", "hack")
