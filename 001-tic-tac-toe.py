import os

clear = lambda: os.system('cls')
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
numcells = 3
players = ["x", "o"]
initPlayer = 0

def initGame():
    clear()
    printBoard(initPlayer)
    selectColumn(0)

def selectGamer(current):
    current += 1
    return 0 if current > len(players) - 1 else current

def selectColumn(currentPlayer):
    print('Enter COLUMN between 1 and 3:')
    column = int(input()) - 1
    if column >= numcells:
        print('ERROR: Column selected doesnt exist')
        selectColumn(currentPlayer)
    selectRow(column, currentPlayer)

def selectRow(column, currentPlayer):
    print('Enter ROW between 1 and 3:')
    row = int(input()) - 1
    if row >= numcells:
        print('ERROR: row selected doesnt exist')
        selectRow(column, currentPlayer)
    verify(column, row, currentPlayer)

def verify(column, row, currentPlayer):
    if board[column][row] != " ":
        print("ERROR: The cell is already taken")
        selectColumn(currentPlayer)
    else:
        board[column][row] = players[currentPlayer]
        clear()
        printBoard(selectGamer(currentPlayer))
    
def printBoard(currentPlayer):
    print(boardHeader())
    print(":                            :")
    print(":      > Player: " + str(currentPlayer + 1) + " (" + str(players[currentPlayer])  + ")       :")
    print(":                            :")
    print(":                            :")
    for x in range(len(board)):
        strRow = ':       '
        for y in range(len(board[x])):
            strRow += "| " + board[x][y] + " "
        strRow += "|        :"
        print(strRow)
        print(":       -------------        :")
    print(":                            :")
    print(":                            :")
    print("::::::::::::::::::::::::::::::")
    print("")
    selectColumn(currentPlayer)

def boardHeader():
    return"::::::::::::::::::::::::::::::\n:::       TIC TAC TOE      :::\n::::::::::::::::::::::::::::::"

initGame()

