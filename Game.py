from copy import deepcopy
from time import time

board = ["_","_","_","_","_","_","_","_","_"]

print(board[0],board[1],board[2])
print(board[3],board[4],board[5])
print(board[6],board[7],board[8])

def winCondition(board, i):
    win = [[board[0],board[1],board[2]],[board[3],board[4],board[5]],[board[6],board[7],board[8]],
           [board[0],board[3],board[6]], [board[1],board[4],board[7]], [board[2],board[5],board[8]],
           [board[0],board[4],board[8]], [board[2],board[4],board[6]]
           ]
    if([i,i,i] in win):
        return 1
    else:
        return -1

def draw(board):
    for i in board:
        if (i == "_"):
            return False
    return True

def playerTurn(board, pos):
    board[pos] = "X"

def validMove(board,i):
    if(board[i]=="_"):
        return True
    return False

def generateNode(board,symbol):
    node = []
    count=0
    if(winCondition(board,symbol)!= -1):
        return winCondition(board,symbol)

    if(draw(board)==True):
        return 0

    newSymbol = "X"
    if(symbol=='X'):
        newSymbol = "O"
    sumlist = 0
    for i in range(9):
        if(i=='_'):
            node.append(deepcopy(board))
            node[count][i] = symbol
            count +=1
            sumlist += generateNode(node[count],newSymbol)
    return sumlist

def stopWin(board):

    for i in range(3):
        if(board[i] == 'X' and board[i+3] == 'X' and board[i+6]=="_"):
            board[i+6]="O"
            return board

        if (board[i] == 'X' and board[i + 6] == 'X' and board[i + 3] == "_"):
            board[i + 3] = "O"
            return board

        if (board[i+6] == 'X' and board[i+3] == 'X' and board[i] == "_"):
            board[i] = "O"
            return board

    ###################################
    if(board[0]=="X" and board[4]=="X" and board[8]=="_"):
        board[8]="O"
        print ("yo0")
        return board

    if(board[8]=="X" and board[4]=="X" and board[0]=="_"):
        board[0]="O"
        return board

    if(board[0]=="X" and board[8]=="X" and board[4]=="_"):
        board[4]="O"
        return board

    if (board[2] == "X" and board[4] == "X" and board[6] == "_"):
        board[6] = "O"
        return board

    if (board[6] == "X" and board[4] == "X" and board[2] == "_"):
        board[2] = "O"
        return board

    if (board[2] == "X" and board[6] == "X" and board[4] == "_"):
        board[4] = "O"
        return board
    #####################################
    for x in range(0,9,3):
        if(board[x]=="X" and board[x+1]=="X" and board[x+2]=="_"):
            board[x+2]="O"
            return board

        if(board[x]=="X" and board[x+2]=="X" and board[x+1]=="_"):
            board[x+1]="O"
            return board

        if(board[x+1]=="X" and board[x+2]=="X" and board[x]=="_"):
            board[x]="O"
            return board
    return board

def maxlist(board,symbol):
    node = []
    count = 0

    temp = deepcopy(board)

    if (winCondition(board, symbol) != -1):
        return winCondition(board, symbol)

    if (draw(board) == True):
        return 0

    b = stopWin(board)
    board = b
    if(temp!=b):
        return b

    newSymbol = "X"
    if (symbol == 'X'):
        newSymbol = "O"
    sumlist = []
    iList= []
    for i in range(9):
        if (board[i] == '_'):
            node.append(deepcopy(board))
            node[count][i] = symbol
            sumlist.append(generateNode(node[count], newSymbol))
            iList.append(i)
            count += 1

    a = minList(sumlist)
    board[iList[a]] = "O"
    return board

def minList(iList):
    min = iList[0]
    minpos=0
    count=0
    for i in iList:
        if (i<min):
            min = i
            minpos = count
        count+=1

    return minpos


def solve(board):
    while(draw(board)==False):
        move = int(input("enter position for x: "))
        if(validMove(board,move)):
            a = time()
            playerTurn(board,move)
            print(board[0], board[1], board[2])
            print(board[3], board[4], board[5])
            print(board[6], board[7], board[8])

            if (draw(board)):
                print("Draw")
                break

            board = maxlist(board, "O")

            if(winCondition(board,"O")==1):
                print("Computer Won")
                print(board[0], board[1], board[2])
                print(board[3], board[4], board[5])
                print(board[6], board[7], board[8])
                break

            print("########################")

            # board = maxlist(board,"O")
            print(board[0], board[1], board[2])
            print(board[3], board[4], board[5])
            print(board[6], board[7], board[8])
            b = time()
            print(b - a)

        # board = maxlist(board,"O")
        # print(board[0], board[1], board[2])
        # print(board[3], board[4], board[5])
        # print(board[6], board[7], board[8])

solve(board)