b = ["-","-","-",
    "-","-","-",
    "-","-","-"]
print(b[0] + b[1] + b[2] + "\n" + b[3] + b[4] + b[5] + "\n" + b[6] + b[7] + b[8])

def findWinner(a):
    if a == "X":
        print("player 1 is the winner")
        if input("Do you want to play again: ") == "yes": import TicTacToe.py
    else:
        print("player 2 is the winner")
        if input("Do you want to play again: ") == "yes": import TicTacToe.py

def playerTurn(a):

    if b[0] == b[1] == b[2] and b[0] != "-": findWinner(b[0])
    if b[3] == b[4] == b[5] and b[4] != "-": findWinner(b[4])
    if b[6] == b[7] == b[8] and b[8] != "-": findWinner(b[8])
    if b[0] == b[3] == b[6] and b[0] != "-": findWinner(b[0])
    if b[1] == b[4] == b[7] and b[4] != "-": findWinner(b[4])
    if b[2] == b[5] == b[8] and b[8] != "-": findWinner(b[8])
    if b[0] == b[4] == b[8] and b[0] != "-": findWinner(b[0])
    if b[2] == b[4] == b[6] and b[6] != "-": findWinner(b[6])

    number = 0
    for x in b:
        if x != "-": number += 1
    if number == 9:
        print("It is a draw!")
        if input("Do you want to play again: ") == "yes": import TicTacToe.py

    if a % 2 != 0:
        user = int(input("Player 1 turn: "))
        if b[user - 1] == "-":
            b[user - 1] = "X"
            print(b[0] + b[1] + b[2] + "\n" + b[3] + b[4] + b[5] + "\n" + b[6] + b[7] + b[8])
            playerTurn(a+1)
        else:
            print("This spot is occupied, try again")
            playerTurn(a)
    else:
        user = int(input("Player 2 turn: "))
        if b[user - 1] == "-":
            b[user - 1] = "O"
            print(b[0] + b[1] + b[2] + "\n" + b[3] + b[4] + b[5] + "\n" + b[6] + b[7] + b[8])
            playerTurn(a+1)
        else:
            print("This spot is occupied, try again")
            playerTurn(a)
playerTurn(1)
