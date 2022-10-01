import random
word,location,guesses = random.choice(open("G:\Alex\Coding\words_alpha.txt").readlines()).removesuffix("\n"), [], 11
array,hidArray = [x for x in word], ["*" for i in word]


while guesses != 0:
    user = input(' '.join(hidArray) + "\nGuess the letter: ")
    if user in array:
        location = [x for x in range(len(array)) if user is array[x]]
        for x in location: hidArray[x] = user
        location.clear()
    else:
        if guesses != 2:
            guesses-= 1
            print("You have " + str(guesses-1) + " attempts left")
        else:
            guesses-=2
            print("Game Over, the word was " + str(word))
    if str("".join(hidArray)) == word:
        print("You got it, the word was " + str(word) + " with " + str(guesses) + " remaining")
        break
if str(input("Do you want to play again?\n")) == "yes": import Hangman.py
