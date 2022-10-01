#THIS DOESN'T ACTUALLY WORK... I GAVE UP SOME TIME AGO...THERE ARE LIKE A LOT OF PROBLEMS

#location data

class locationData:
    def __init__(self, location, type, name, color, cost, houseCost, numberOfHouses, rentPrices, mortgageAmt, owner, mortgage):
        self.location = location
        self.type = type
        self.name = name
        self.color = color
        self.cost = cost
        self.houseCost = houseCost
        self.numberOfHouses = numberOfHouses
        self.rentPrices = rentPrices
        self.mortgageAmt = mortgageAmt
        self.owner = owner
        self.mortgage = mortgage

filler = locationData("NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", )
one = locationData(1, "GO", "GO", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
two = locationData(2, "property", "Mediterranean Avenue", "brown", 60, 50, 0, [2, 10, 30, 90, 160, 250], 30, "NA", False)
three = locationData(3, "card", "Community Chest", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
four = locationData(4, "property", "Baltic Avenue", "brown", 60, 50, 0, [4, 20, 60, 180, 320, 450], 30, "NA", False)
five = locationData(5, "tax", "Income Tax", "NA", "NA", "NA", "NA", 200, "NA", "NA", "NA")
six = locationData(6, "railroad", "Reading Railroad", "Railroad", 200, "NA", "NA", "NA", 100, "NA", False)
seven = locationData(7, "property", "Oriental Avenue", "lightBlue", 100, 50, 0, [6, 30, 90, 270, 400, 550], 50, "NA", False)
eight = locationData(8, "card", "Chance", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
nine = locationData(9, "property", "Vermont Avenue", "lightBlue", 100, 50, 0, [6, 30, 90, 270, 400, 550], 50, "NA", False)
ten = locationData(10, "property", "Oriental Avenue", "lightBlue", 100, 50, 0, [8, 40, 100, 300, 450, 600], 50, "NA", False)
eleven = locationData(11, "free", "Just Visiting", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
jail = locationData(41, "jail", "Jail", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
twelve = locationData(12, "property", "St. Charles Place", "purple", 140, 100, 0, [10, 50, 150, 450, 625, 750], 70, "NA", False)
thirteen = locationData(13, "company", "Electric Company", "company", 150, "NA", "NA", "NA", 75, "NA", False)
fourteen = locationData(14, "property", "States Avenue", "purple", 140, 100, 0, [10, 50, 150, 450, 625, 750], 70, "NA", False)
fifteen = locationData(15, "property", "Virginia", "purple", 160, 100, 0, [12, 60, 180, 500, 700, 900], 80, "NA", False)
sixteen = locationData(16, "railroad", "Pennsylvania Railroad", "Railroad", 200, "NA", "NA", "NA", 100, "NA", False)
seventeen = locationData(17, "property", "St. James Place", "Orange", 180, 100, 0, [14, 70, 200, 550, 750, 950], 90, "NA", False)
eighteen = locationData(18, "card", "Community Chest", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
nineteen = locationData(19, "property", "Tennessee Avenue", "Orange", 180, 100, 0, [14, 70, 200, 550, 750, 950], 90, "NA", False)
twenty = locationData(20, "property", "New York Avenue", "Orange", 200, 100, 0, [16, 80, 220, 600, 800, 1000], 100, "NA", False)
twentyone = locationData(21, "free", "Free Parking", "NA", "NA", "NA", "NA", "NA", "NA", "NA", False)
twentytwo = locationData(22, "property", "Kentucky Avenue", "Red", 220, 150, 0, [18, 90, 250, 700, 875, 1050], 110, "NA", False)
twentythree = locationData(23, "card", "Chance", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
twentyfour = locationData(24, "property", "Indiana Avenue", "Red", 220, 150, 0, [18, 90, 250, 700, 875, 1050], 110, "NA", False)
twentyfive = locationData(25, "property", "Illinois Avenue", "Red", 240, 150, 0, [20, 100, 300, 750, 925, 1100], 120, "NA", False)
twentysix = locationData(26, "railroad", "B. & O. Railroad", "Railroad", 200, "NA", "NA", "NA", 100, "NA", False)
twentyseven = locationData(27, "property", "Atlantic Avenue", "Yellow", 260, 150, 0, [22, 110, 330, 800, 975, 1150], 130, "NA", False)
twentyeight = locationData(28, "property", "Ventnor Avenue", "Yellow", 260, 150, 0, [22, 110, 330, 800, 975, 1150], 130, "NA", False)
twentynine = locationData(29, "company", "Water Works", "company", 150, "NA", "NA", "NA", 75, "NA", False)
thirty = locationData(30, "property", "Marvin Gardens", "Yellow", 280, 150, 0, [24, 120, 360, 850, 1025, 1200], 140, "NA", False)
thirtyone = locationData(31, "goToJail", "Go to Jail", "NA", "NA", "NA", "NA", "NA", "NA", "NA", False)
thirtytwo = locationData(32, "property", "Pacific Avenue", "Green", 300, 200, 0, [26, 130, 390, 900, 1100, 1275], 150, "NA", False)
thirtythree = locationData(33, "property", "North Carolina Avenue", "Green", 140, 200, 0, [26, 130, 390, 900, 1100, 1275], 150, "NA", False)
thirtyfour = locationData(34, "card", "Community Chest", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
thirtyfive = locationData(35, "property", "Pennsylvania Avenue", "Green", 300, 200, 0, [28, 150, 450, 1000, 1200, 1400], 160, "NA", False)
thirtysix = locationData(36, "railroad", "Short Line", "Railroad", 200, "NA", "NA", "NA", 100, "NA", False)
thirtyseven = locationData(37, "card", "Chance", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
thirtyeight = locationData(38, "property", "Park Place", "Blue", 350, 200, 0, [35, 175, 500, 1100, 1300, 1500,], 175, "NA", False)
thirtynine = locationData(39, "tax", "Luxury Tax", "NA", "NA", "NA", "NA", 100, "NA", "NA", False)
forty = locationData(40, "property", "Boardwalk", "NA", 400, 200, 0, [50, 200, 600, 1400, 1700, 2000], 200, "NA", False)

#location data

#player data

class playerData:
    def __init__(self, balance, house, card, location, railroad, name, company):
        self.balance = balance
        self.house = house
        self.card = card
        self.location = location
        self.railroad = railroad
        self.name = name
        self.company = company

filler = playerData(0,0,0,0,0,0,0)
player1 = playerData(1500, [], "", 0, 0, "", 0)
player2 = playerData(1500, [], "", 0, 0, "", 0)
player3 = playerData(1500, [], "", 0, 0, "", 0)
player4 = playerData(1500, [], "", 0, 0, "", 0)

#player data

#game

#Lets us do this and make a really bad version of monopoly
import random as r
def pboard():
    print("Le board") #I'll get an actually board after I get to actually work

#actions

#pullLocation

pullLocation = [filler, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive, twentysix, twentyseven, twentyeight, twentynine, thirty, thirtyone, thirtytwo, thirtythree, thirtyfour, thirtyfive, thirtysix, thirtyseven, thirtyeight, thirtynine, forty]

#pullLocation

#establish number of players and name
pullName = [filler, player1, player2, player3, player4]

players = int(input("How many players (between 2 and 4): "))

def namePlayers(number):
    if number > players:
        return
    else:
        pullName[number].name = input("Player " + str(number) + ", please enter your name: ")
        namePlayers(number+1)

namePlayers(1)

#establish number of players and name

def mortgage(playerNum):
    array = []
    for x in pullName[playerNum].house:
        if pullLocation[x].mortgage == False:
            array.append(pullLocation[x].name + " (" + str(x) + ")")
    if len(array) == 0:
        print("No more possible houses to mortgage")
        return
    print(array)
    houseNum = int(input(pullName[playerNum].name + ", please chose which house you would like to mortgage (enter the number behind the house name): "))
    pullLocation[houseNum].mortgage = True
    pullName[playerNum].balance += pullLocation[houseNum].mortgageAmt
    print(pullLocation[houseNum].mortgage, pullName[playerNum].balance)
    repeat = input("Would you like to mortgage another property? (y/n): ")
    if repeat == "y":
        mortgage(playerNum)

def startAuction(playerNum, largestBid, ints, passes, array, playerLoc):
    for x in array:
        if x == playerNum:
            if playerNum == players:
                startAuction(1, largestBid, 1, passes, array, playerLoc)
            else: startAuction(playerNum+1, largestBid, 1, passes, array, playerLoc)
    if len(array) + 1 == players:
        print(pullName[playerNum].name + " has won the action. The final price was $" + str(largestBid))
        pullName[playerNum].house.append(playerLoc)
        pullName[playerNum].balance -= largestBid
        pullLocation[playerLoc].owner = playerNum
        return
    if ints == 0:
        print(pullName[playerNum].name + " didn't want to purchuse the property")
        print("Starting Auction")
    bid = input(pullName[playerNum].name + ", please place your bid (Cannot be lower than the 0 or the current higest bid) or say pass: ")
    if bid == "pass":
        array.append(playerNum)
        if playerNum == players:
            startAuction(1, largestBid, 1, passes+1, array, playerLoc)
        else: startAuction(playerNum+1, largestBid, 1, passes+1, array, playerLoc)
    else:
        if int(bid) > pullName[playerNum].balance:
            print("Not enought funds")
            startAuction(1, largestBid, 1, passes, array, playerLoc)
        else:
            if int(bid) < largestBid:
                print("Please bid a larger amount")
                startAuction(playerNum, largestBid, 1, passes, array, playerLoc)
            else:
                if playerNum == players:
                    startAuction(1, int(bid), 1, passes, array, playerLoc)
                else:
                    startAuction(playerNum+1, int(bid), 1, passes, array, playerLoc)

def buyHouse(playerNum, playerLoc, Num):
    decision = 0
    print(pullName[playerNum].balance)
    print(pullLocation[playerLoc].cost)
    if Num == 0: decision = input("No one owns this property yet, would you like to purchuse this property? (y/n): ")
    if decision == "n" and Num != 1:
        startAuction(playerNum, 0, 0, 0, [], playerLoc)
    elif decision == "y" or Num == 1:
        if pullName[playerNum].balance < pullLocation[playerLoc].cost:
            mortDecision = input("You do not have enough funds, would you like to mortgage your property? (y/n): ")
            if mortDecision == "n":
                startAuction(playerNum, 0, 0, 0, [], playerLoc)
            else:
                mortgage(playerNum)
                buyHouse(playerNum, playerLoc, 1)
        else:
            print("You have bought this property!")
            pullName[playerNum].house.append(playerLoc)
            pullName[playerNum].balance -= pullLocation[playerLoc].cost
            pullLocation[playerLoc].owner = playerNum
    return

def buildHouse(playerNum):
    array = []
    for x in pullName[playerNum].house:
        if pullLocation[x].mortgage == False and pullLocation[x].type == "property":
            array.append(pullLocation[x].name + " (" + str(x) + ")" + " (Houses built: " + str(pullLocation[x].numberOfHouses) + ")")
    print(array)
    house = int(input("Which propety would you like to build your house on: "))
    if pullLocation[house].numberOfHouses == 5:
        print(f'You cannot build anymore houses on {pullLocation[house].name}')
        if input("would you like to build a house on another property? y/n") == "y":
            buildHouse(playerNum)
    if pullLocation[house].houseCost > pullName[playerNum].balance:
        print("Not enough funds...")
        if input("Would you like to mortgage something? (y/n): ") == "y":
            mortgage(playerNum)
            buildHouse(playerNum)
    else:
        if pullLocation[house].numberOfHouses == 4:
            pullLocation[house].numberOfHouses += 1
            print(f'Sucess, you have built a hotel for {pullLocation[house].houseCost}')
            if input("would you like to build a house on another property? y/n") == "y":
                buildHouse(playerNum)
        else:
            pullLocation[house].numberOfHouses += 1
            print(f'Sucess, you have built a house for {pullLocation[house].houseCost}')
            if input("would you like to build a house on another property? (y/n): ") == "y":
                buildHouse(playerNum)

def actions(playerNum):
    print("Enter b to build houses")
    decision = input("What actions would you like to preform: ")
    if decision == "b":
        buildHouse(playerNum)
    else:
        return

def locationChecker(playerNum, playerLoc, diceRoll):
    if str(pullLocation[playerLoc].type) == "property" or str(pullLocation[playerLoc].type) == "railroad" or str(pullLocation[playerLoc].type) == "company":
        if pullLocation[playerLoc].owner == "NA":
            buyHouse(playerNum, playerLoc, 0)
        elif pullLocation[playerLoc].owner != playerNum and pullLocation[playerLoc].mortgage == False:
            if str(pullLocation[playerLoc].type) == "property":
                pullName[playerNum].balance -= pullLocation[playerLoc].rentPrices[pullLocation[playerLoc].numberOfHouses]
                pullName[pullLocation[playerLoc].owner].balance += pullLocation[playerLoc].rentPrices[pullLocation[playerLoc].numberOfHouses]
                print(pullName[playerNum].name + " landed on " + pullName[pullLocation[playerLoc].owner].name + " 's property and paid $" + str(pullLocation[playerLoc].rentPrices[pullLocation[playerLoc].numberOfHouses]))
            elif str(pullLocation[playerLoc].type) == "railroad":
                cost = 2**(pullName[pullLocation[playerLoc].owner].railroad-1) * 25
                pullName[playerNum].balance -= cost
                pullName[pullLocation[playerLoc].owner].balance += cost
                print(pullName[playerNum].name + " landed on " + pullName[pullLocation[playerLoc].owner].name + " 's property and paid $" + str(cost))
            elif str(pullLocation[playerLoc].type) == "company":
                companiesOwned = pullName[pullLocation[playerLoc].owner].company
                multiplyer = ["filler", 4, 10]
                pullName[playerNum].balance -= diceRoll * multiplyer[companiesOwned]
                pullName[pullLocation[playerLoc].owner].balance += diceRoll * multiplyer[companiesOwned]
                print(pullName[playerNum].name + " rolled a " + str(diceRoll) + " and paided $" + str(diceRoll * multiplyer[companiesOwned]) + " to " + pullName[pullLocation[playerLoc].owner].name)

    elif str(pullLocation[playerLoc].type) == "tax":
        if pullName[playerNum].balance < pullLocation[playerLoc].rentPrices:
            print("You do not have enough funds to pay your tax, go mortgage some properties")
            mortgage(playerNum)
            locationChecker(playerNum, playerLoc, diceRoll)
        else:
            pullName[playerNum].balance -= pullLocation[playerLoc].rentPrices
            print(pullName[playerNum].name + " landed on " + pullLocation[playerLoc].name + " and paided the bank $" + str(pullLocation[playerLoc].rentPrices))

def diceRoll():
    dice1 = r.randint(1,6)
    dice2 = r.randint(1,6)
    if dice1 == dice2: return [dice1 + dice2, 1]
    else: return [dice1 + dice2, 0]

def gameStart(player, diceInfo, doubleRollC):
    pboard()
    print(pullName[player].name + " rolled a " + str(diceInfo[0]))
    pullName[player].location += int(diceInfo[0]) #updates location
    if pullName[player].location >= 41: pullName[player].location -= 40
    print(pullName[player].name + " landed on " + pullLocation[pullName[player].location].name)
    locationChecker(player, pullName[player].location, diceInfo[0]) #checks location
    if diceInfo[1] == 1: doubleRollC += 1 #adds a counter if the person rolled a double
    if doubleRollC == 3:
        pass #puts the guy in prison... eventually
    actions(player) #the actions that will be placed here eventually
    gameStart(player, diceInfo, doubleRollC)
#actions

#init

gameStart(1, diceRoll(), 0)
