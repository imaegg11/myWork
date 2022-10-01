import random
word = random.choice(open("G:\Alex\Coding\words_alpha.txt").readlines()).removesuffix("\n")
array = []
hidArray = []
guesses = 11
location = []

for x in word:
    array.append(x)
    hidArray.append("*")

while guesses != 0:
    user = str(input(str(hidArray) + "\nGuess the letter: "))

    if user in array:
        for x in range(len(array)):
            if user is array[x]:
                location.append(x)

        for x in range(len(location)):
            del hidArray[int(location[x])]
            hidArray.insert(int(location[x]), user)

        location.clear()

    else:
        if guesses != 2:
            guesses-= 1
            print("You have " + str(guesses-1) + " attempts left")
        else:
            guesses-=2
            print("Game Over, the word was " + str(word))

    y = str("".join(hidArray))
    if y == word:
        print("You got it, the word was " + str(word))
        break

if str(input("Do you want to play again?\n")) == "yes":
    import Hangman.py
