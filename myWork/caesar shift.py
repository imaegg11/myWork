def caesarShift(message, shift):
    string = "abcdefghijklmnopqrstuvwxyz "
    array = [(int(string.index(i)))+1 for i in message]
    coded = [string[(i+shift-1) % 26] if i != 27 else " " for i in array]
    print("".join(coded))
    return "".join(coded)

def unshiftCaesar(coded, shift):
    string = "abcdefghijklmnopqrstuvwxyz "
    array = [(int(string.index(i)))+1 for i in coded]
    uncoded = [string[(i-shift-1) % 26] if i != 27 else " " for i in array]
    print("".join(uncoded))
    return "".join(uncoded)

def bob(coded, shift):
      print("".join(["abcdefghijklmnopqrstuvwxyz "[(i-shift-1) % 26] if i != 27 else " " for i in [(int("abcdefghijklmnopqrstuvwxyz ".index(i)))+1 for i in coded]]))

caesarShift("the temple is coming", 2)
unshiftCaesar("vjg vgorng ku eqokpi", 2)
bob("vjg vgorng ku eqokpi", 2)
