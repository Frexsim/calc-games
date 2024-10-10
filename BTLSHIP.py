players = 2
boardSize = 10
boats = 10
generalSymbols = {
    "placed": "#",
    "sunken": "X",
    "sunkenByYou": "+"
}
playerSymbols = ["1", "2"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

boards = []

def generateBoards():
    for playerNumber in range(players):
        playerBoard = []
        for x in range(boardSize):
            row = []
            for y in range(boardSize):
                row.insert(y, -1)
            
            playerBoard.insert(x, row)
        
        boards.insert(playerNumber, playerBoard)

def parseCoordinate(coordinate: str):
    coordinate = coordinate.capitalize()

    xString = coordinate[0]
    if (xString in alphabet) == False: return False, None, None
    if alphabet.index(xString) >= boardSize: return False, None, None
    x = alphabet.index(xString)

    yString = coordinate.removeprefix(xString)
    if yString.isdigit() != True: return False, None, None
    if int(yString) >= boardSize: return False, None, None
    y = int(yString)

    return True, x, y

def startBoatPlacing():
    for playerIndex in range(players):
        playerBoard = boards[playerIndex]

        boatNumber = 0
        while True:
            printBoard(playerIndex)

            success, x, y = parseCoordinate(input("(Player " + str(playerIndex) + "'s board) " + "Placing Boat " + str(boatNumber) + "/" + str(boats) + ": "))
            if success == False:
                print("Invalid Coordinates.")
            else:
                if playerBoard[y][x] == -1:
                    playerBoard[y][x] = -2
                    boatNumber += 1
                else:
                    print("There is already a boat there!")
            
            if boatNumber > boats:
                break

def printBoard(playerNumber):
    playerBoard = boards[playerNumber]

    horizontalCoordinates = " "
    for x in range(boardSize):
        horizontalCoordinates += alphabet[x]
    print(horizontalCoordinates)

    for rowIndex in range(boardSize):
        rowString = str(rowIndex)
        for columnIndex in range(boardSize):
            pointValue = playerBoard[rowIndex][columnIndex]
            if pointValue == -2:
                rowString += generalSymbols["placed"]
            elif pointValue >= 0:
                if pointValue != playerNumber:
                    rowString += generalSymbols["sunken"]
                elif pointValue == playerNumber:
                    rowString += generalSymbols["sunkenByYou"]
            else:
                rowString += "-"
        print(rowString)

generateBoards()
startBoatPlacing()