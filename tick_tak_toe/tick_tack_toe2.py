import os
from icecream import ic
board = []
keys = {
    7 : (0,0),
    8 : (0,1),
    9 : (0,2),
    4 : (1,0),
    5 : (1,1),
    6 : (1,2),
    1 : (2,0),
    2 : (2,1),
    3 : (2,2)    
    }

def _board():
    for i in range(3):
        row = []
        for j in range(3):
            row.insert(j,"")
        board.append(row)
        
def _insert(val,user):

    cordinates = keys.get(int(val))
    i = cordinates[0]
    j = cordinates[-1]
  
    if board[i][j] == "X" or board[i][j] == "O":
        print("position is already occupied")
    else:
        board[i][j]=user
               
def switch(user):
    if user == "O":
        user ="X"
    elif user == "X":
        user = "O"
    return user

def display_board():
    for i in range(3):
        print(board[i], end = "")
        print("\n")
        
def Verify_board(board,user):    
    if (board[0][0] ==board[0][1] == board[0][2] == "X" or board[0][0] ==board[0][1] == board[0][2] == "O" ):
        print( user ," won")
        exit()
    elif (board[1][0] ==board[1][1] == board[1][2]== "X" or board[1][0] ==board[1][1] == board[1][2]== "O" ):
        print( user ," won")
        exit()
    elif (board[2][0] ==board[2][1] == board[2][2]== "X" or board[2][0] ==board[2][1] == board[2][2] == "O" ):
        print( user ," won")
        exit()
    elif (board[0][0] ==board[1][0] == board[2][0]== "X" or board[0][0] ==board[1][0] == board[2][0]== "O" ):
        print( user ," won")
        exit()
    elif (board[0][1] ==board[1][1] == board[2][1]== "X" or board[0][1] ==board[1][1] == board[2][1] == "O" ):
        print( user ," won")
        exit()
    elif (board[0][2] ==board[1][2] == board[2][2]== "X" or board[0][2] ==board[1][2] == board[2][2]== "O" ):
        print( user ," won")
        exit()
    elif (board[0][0] ==board[1][1] == board[2][2] == "X" or board[0][0] ==board[1][1] == board[2][2]  == "O"):
        print( user ," won")
        exit()
    elif (board[0][2] ==board[1][1] == board[2][0] == "X" or board[0][2] ==board[1][1] == board[2][0] == "O"):
        print( user ," won")
        exit()  

def tick_tack_toe():
    print("welcome to tick tack toe")
    is_running = 1
    user = "O"
    _board()
    display_board()
    while is_running == 1:
        
        val = input("enter any number between 1 to 9: ")        
        if val.isalpha() == True:
            print("incorrect value select the correct value")
        elif int(val) >=10:
            print("the value is greater that 10 ")
        elif int(val) == 0:
            exit()
        else:                        
            os.system('cls')
            user = switch(user)
            _insert(val,user)
            display_board()            
            Verify_board(board,user)
           
tick_tack_toe()