boardSize = 10
boats = 2
generalSymbols = {
    "empty": "-",
    "placed": "#",
    "missed": "X",
    "sunken": "S"
}
playerSymbols = ["1", "2"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

boards = []

def generateBoards():
    for playerNumber in range(len(playerSymbols)):
        playerBoard = []
        for x in range(boardSize):
            row = []
            for y in range(boardSize):
                row.insert(y, {
                    "hasBoat": False,
                    "sunkenBy": -1
                })
            
            playerBoard.insert(x, row)
        
        boards.insert(playerNumber, playerBoard)

def parseCoordinate(coordinate: str):
    coordinate = coordinate.capitalize()

    if len(coordinate) <= 0: return False, None, None

    xString = coordinate[0]
    if (xString in alphabet) == False: return False, None, None
    if alphabet.index(xString) >= boardSize: return False, None, None
    x = alphabet.index(xString)

    yString = coordinate.removeprefix(xString)
    if yString.isdigit() != True: return False, None, None
    if int(yString) >= boardSize: return False, None, None
    y = int(yString)

    return True, x, y

def printBoard(boardOwner, requester):
    playerBoard = boards[boardOwner]

    horizontalCoordinates = " "
    for x in range(boardSize):
        horizontalCoordinates += alphabet[x]
    print(horizontalCoordinates)

    for rowIndex in range(boardSize):
        rowString = str(rowIndex)
        for columnIndex in range(boardSize):
            pointValue = playerBoard[rowIndex][columnIndex]
            if boardOwner == requester:
                if pointValue["hasBoat"] == True:
                    if pointValue["sunkenBy"] <= -1:
                        rowString += generalSymbols["placed"]
                    else:
                        rowString += playerSymbols[pointValue["sunkenBy"]]
                else:
                    if pointValue["sunkenBy"] <= -1:
                        rowString += generalSymbols["empty"]
                    else:
                        rowString += playerSymbols[pointValue["sunkenBy"]]
            else:
                if pointValue["sunkenBy"] == requester:
                    if pointValue["hasBoat"] == True:
                        rowString += generalSymbols["sunken"]
                    else:
                        rowString += generalSymbols["missed"]
                else:
                    rowString += generalSymbols["empty"]

        print(rowString)

def startBoatPlacing():
    for playerNumber in range(len(playerSymbols)):
        playerBoard = boards[playerNumber]

        boatNumber = 1
        while True:
            printBoard(playerNumber, playerNumber)

            success, x, y = parseCoordinate(input("(Player " + str(playerSymbols[playerNumber]) + "'s board) " + "Placing Boat " + str(boatNumber) + "/" + str(boats) + ": "))
            if success == False:
                print("Invalid coordinates.")
            else:
                if playerBoard[y][x]["hasBoat"] == False:
                    playerBoard[y][x]["hasBoat"] = True
                    boatNumber += 1
                else:
                    print("There is already a boat there!")
            
            if boatNumber > boats:
                break

def startTurn(playerNumber):
    playerToAttackNumber = 0
    while True:
        if playerToAttackNumber > len(playerSymbols): break
        if playerToAttackNumber == playerNumber: playerToAttackNumber += 1; continue

        printBoard(playerToAttackNumber, playerNumber)
        success, x, y = parseCoordinate(input("(Player " + str(playerSymbols[playerNumber]) + "'s turn) " + "Attacking " + "Player" + str(playerSymbols[playerToAttackNumber]) + ": "))
        if success == False:
            print("Invalid coordinates.")
        else:
            if boards[playerToAttackNumber][y][x]["sunkenBy"] == playerNumber:
                print("Already sunken!")
            else:
                boards[playerToAttackNumber][y][x]["sunkenBy"] = playerNumber
            
            if boards[playerToAttackNumber][y][x]["hasBoat"] == False:
                break

generateBoards()
startBoatPlacing()

currentPlayer = 0
while True:
    startTurn(currentPlayer)

    currentPlayer = (currentPlayer + 1) % len(playerSymbols)