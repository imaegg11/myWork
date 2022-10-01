import hashlib, threading

def day4pt1(secretKey):
    hash = ""
    count = 1
    while hash[0:5] != "00000":
        string = secretKey + str(count)
        temp = hashlib.md5(string.encode())
        hash = temp.hexdigest()
        count += 1
    return count-1

def day4pt2(secretKey):
    hash = ""
    count = 1
    while hash[0:6] != "000000":
        string = secretKey + str(count)
        temp = hashlib.md5(string.encode())
        hash = temp.hexdigest()
        count += 1
    return count-1

print(day4pt2("bgvyzdsv"))
