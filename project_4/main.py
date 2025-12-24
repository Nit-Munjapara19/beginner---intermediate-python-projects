board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentplayer = "X"
winner = None
gamerunning = True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerinput(board):
    a=int(input("Enter number between 1 to 9 : "))  
    if a>=1 and a<=9 and board[a-1]=="-":
        board[a-1] = currentplayer
    else:
        switchplayer()
        print("Oops something is worng")
         
def checkhorizontle(board):
    global winner
    if board[0] == board[1] == board[2]  and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]  and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]  and board[7] != "-":
        winner = board[6]
        return True

def checkrow(board):
    global winner
    if board[0] == board[3] == board[6]  and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]  and board[4] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]  and board[5] != "-":
        winner = board[2]
        return True

def checkdi(board):
    global winner
    if board[0]==board[4]==board[8] and board[4] != "-":
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6] and board[4] != "-":
        winner = board[2]
        return True
    
def checktie(board):
    if "-" not in board:
        printboard(board)
        print("It's a Tie!")
        gamerunning = False

def checkwin():
    global gamerunning
    if checkhorizontle(board) or checkrow(board) or checkdi(board):      
        print(f"The winner is {winner}") 
        gamerunning = False 


def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"          

while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
