from math import *

boardSize = 3
board = []
currentPlayer = 0
playerSymbols = ["X","O"]

def generateBoard():
  for rowIndex in range(boardSize):
    row = []
    for columnIndex in range(boardSize):
      row.insert(columnIndex, -1)
    
    board.insert(rowIndex, row)

def startTurn():
  winner = -1
  draw = False

  global currentPlayer

  print(playerSymbols[currentPlayer] + "'s turn.")
  selectedLocation = int(input())
  row, column = getRowAndColumn(selectedLocation)

  if board[row][column] < 0:
    board[row][column] = currentPlayer
    winner = checkForWin()
    draw = isBoardFull()
    currentPlayer = (currentPlayer + 1) % len(playerSymbols)
  else:
    print("")
    print("Spot is already taken!")
  
  print("")
  printBoard()

  return winner, draw

def getRowAndColumn(location):
  column = abs((location - 1) % boardSize)
  row = abs((boardSize - ceil(location / boardSize)) % boardSize)
  
  return row, column

def printBoard():
  for row in board:
    rowString = ""
    for column in row:
      if column == -1:
        rowString += "-"
      else:
        rowString += playerSymbols[column]
    
    print(rowString)

def checkForWin():
  global currentPlayer

  win = -1

  # Horizontal Win
  for rowIndex in range(boardSize):
    lastSpaceNumber = -1
    horizontalWin = True
    for columnIndex in range(boardSize):
      spaceNumber = board[rowIndex][columnIndex]
      if spaceNumber < 0 or (lastSpaceNumber > -1 and lastSpaceNumber != spaceNumber):
        horizontalWin = False
        break

      lastSpaceNumber = spaceNumber
    if horizontalWin == True:
      win = currentPlayer
      break
  
  # Vertical Win
  for columnIndex in range(boardSize):
    lastSpaceNumber = -1
    verticalWin = True
    for rowIndex in range(boardSize):
      spaceNumber = board[rowIndex][columnIndex]
      if spaceNumber < 0 or (lastSpaceNumber > -1 and lastSpaceNumber != spaceNumber):
        verticalWin = False
        break

      lastSpaceNumber = spaceNumber
    if verticalWin == True:
      win = currentPlayer
      break
  
  # Diagonal Win (Top Left to Bottom Right)
  lastSpaceNumber = -1
  diagnoalWin = True
  for diagonalIndex in range(boardSize):
    spaceNumber = board[diagonalIndex][diagonalIndex]
    if spaceNumber < 0 or (lastSpaceNumber > -1 and lastSpaceNumber != spaceNumber):
      diagnoalWin = False
      break

    lastSpaceNumber = spaceNumber
  if diagnoalWin == True:
    win = currentPlayer
  
  # Diagonal Win (Bottom Left to Top Right)
  lastSpaceNumber = -1
  diagnoalWin = True
  for diagonalIndex in range(boardSize):
    spaceNumber = board[boardSize - diagonalIndex - 1][diagonalIndex]
    if spaceNumber < 0 or (lastSpaceNumber > -1 and lastSpaceNumber != spaceNumber):
      diagnoalWin = False
      break

    lastSpaceNumber = spaceNumber
  if diagnoalWin == True:
    win = currentPlayer
  
  return win

def isBoardFull():
  isFull = True
  for row in board:
    for column in row:
      if column < 0:
        isFull = False
  
  return isFull

generateBoard()
while True:
  winner, draw = startTurn()
  print("")
  if winner > -1:
    print(playerSymbols[winner] + " has won!")
    break
  if draw == True:
    print("Draw!")
    break