import random

def display(): #prints row and column numbers
    i = 1
    while i <= 6:
        if i == 6:
            print ((" "*9), i, sep="")
            i += 1
        else:
            print ((" "*9), i, sep="", end="")
            i += 1

    num = 1
    i = 1
    while i <= 60:
        if i == 60:
            num = 0
            print (num,sep="")
        elif num == 10:
            num = 0
            print (num,end="")
        else:
            print (num,end="")
        num += 1
        i += 1

def board(ship,prob):

    board = []
    row = 1
    probability = prob
    ships = ship

    while row <= 20:
        rowBoard = []
        column = 1
        while column <= 60:
            surprise = random.choice(probability)
            if ship == 0:
                rowBoard.append(0)
                column += 1
            else:
                if surprise >= 1 and surprise <= 4 and surprise in rowBoard:
                    column = column
                else:
                    if surprise == 0:
                        rowBoard.append(surprise)
                        column += 1
                    else:
                        if surprise >= 1 and surprise <= 4:
                            for i in range(5):
                                rowBoard.append(surprise)
                        column += 5
                        ship -= 1

        board.append(rowBoard)
        row += 1

####################display time########################
    displayBoard = []

    for i in range(20):
        displayBoard.append(["#"]*60)

    booms = 1
    shipCounter = 0
    while booms <= 15:
        if shipCounter == 5:
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            print ("You've sunk my battleship!")
            attempts = booms
            return attempts
            booms = 16
        else:
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            try:
                userRow, userCol = map(int, input("Enter row and col: ").split())              
                if userRow < 1 or userRow > 20 or userCol < 1 or userCol > 60:
                    print ("Sorry, this ocean isn't that big.")
                    continue
            except ValueError:
                print("Sorry, I don't understand that.")
                continue
            else:
                booms += 1
                bombed = board[userRow-1][userCol-1]
                if ships == 80:
                    if bombed == 5:
                        print ("You've already bombed that ship.")
                    else:
                        if bombed == 6:
                            print ("You've already know there isn't a ship there.")
                        else:
                            if bombed >= 1 and bombed <= 4:
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 5
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"

                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "
                                
                elif ships == 50:
                    if bombed == 4:
                        print ("You've already bombed that ship.")
                    else:
                        if bombed == 5:
                            print ("You've already know there isn't a ship there.")
                        else:
                            if bombed >= 1 and bombed <= 3:
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 4
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"
                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "
                                
                elif ships == 20:
                    if board[userRow-1][userCol-1] == 2: 
                        print ("You've already bombed that ship.")
                    else:
                        if board[userRow-1][userCol-1] == 3:
                            print ("You already know there isn't a ship there.")
                        else:
                            if board[userRow-1][userCol-1] == 1: #if position chosen == 1 in board
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = [] #initialize index list to use for display board
                                for n, i in enumerate(board[userRow-1]): #for the row specificed by user in board list
                                        if i == 1:
                                            shipIndex.append(board[userRow-1].index(i))
                                            board[userRow-1][n] = 2
                                            for i in shipIndex:
                                                displayBoard[userRow-1][n] = "O"
                        
                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "

    if attempts >= 13 and attempts <= 15:
        print ("You are a novice.")
    elif attempts >=10 and attempts <= 12:
        print ("Not bad.")
    elif attempts < 10:
        print ("You have the talent!") #should there be some extra feature for this
    else:
        print ("You've no luck today, try again.")


p1 = '''
Welcome to Battleship!
Please select a difficulty mode:
Beginner = 1
Intermediate = 2
Advanced = 3
'''
print (p1)

x = int(input("Mode: "))
if x == 1:
    board(80, [0,1,0,2,0,3,0,4,0])
elif x ==2:
    board(50,[0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,3,0,0,0] )
else:
    board(20,[0,0,0,1,0,0,0,0,0,0,0,0])
    
    
