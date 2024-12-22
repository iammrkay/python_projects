import os
from icecream import ic
board = list()
col = list()
row = list()

def display_board():
    for col in range(3):
        row1 = []
        for row in range(3):
            #print("0",end = "  ")
            row1.insert(row,"")
        #print("\n")
        board.append(row1)

def displayboard(board):
    print("---------- ")    
    for i in range(3):
        print(board[i],end="")
        print("\n")

key = {
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

users = ["x","o"]

#print(key.get(value))
def board_update(value,user):    
    cordinate = key.get(value)    
    print("the values selected is ",cordinate)
    i = cordinate[0]
    j = cordinate[-1]

    if board[i][j] == "x" or board[i][j] == "o":
        print("position is already occupied")
    else:
        board[i][j]=user           

def switch(user):
    if user == "x":
        user = "o"
    elif user == "o":
        user = "x"  
    return user  

def Verify_board(board):    
    if (board[0][0] ==board[0][1] == board[0][2] == "x" or board[0][0] ==board[0][1] == board[0][2] == "o" ):
        print("you won")
    elif (board[1][0] ==board[1][1] == board[1][2]== "x" or board[1][0] ==board[1][1] == board[1][2]== "o" ):
        print("you won")
    elif (board[2][0] ==board[2][1] == board[2][2]== "x" or board[2][0] ==board[2][1] == board[2][2] == "o" ):
        print("you won")
    elif (board[0][0] ==board[1][0] == board[2][0]== "x" or board[0][0] ==board[1][0] == board[2][0]== "o" ):
        print("you won")
    elif (board[0][1] ==board[1][1] == board[2][1]== "x" or board[0][1] ==board[1][1] == board[2][1] == "o" ):
        print("you won")
    elif (board[0][2] ==board[1][2] == board[2][2]== "x" or board[0][2] ==board[1][2] == board[2][2]== "o" ):
        print("you won")
    elif (board[0][0] ==board[1][1] == board[2][2] == "x" or board[0][0] ==board[1][1] == board[2][2]  == "o"):
        print("you won")
    elif (board[0][2] ==board[1][1] == board[2][0] == "x" or board[0][2] ==board[1][1] == board[2][0] == "o"):
        print("you won")    

def verify_borad1(board):
    array1 = [board[0][0],board[0][1],board[0][2]]
    array2 = [board[1][0],board[1][1],board[1][2]]
    array3 = [board[2][0],board[2][1],board[2][2]]
    count = 0
    for x in range(len(array1)):        
        if "x" == array1[x]:
            count = count +1
        if count ==3:
            print("You WON")
            

display_board()
is_running = True
user = "x"
while is_running: 
    
    value = int(input("select a number  "))
    if value == 0:        
        break 
    elif value >=10:
        print("select any number between 1 to 9")        
    else:
        user = switch(user)
        board_update(value,user)
        displayboard(board)
        Verify_board(board)
        #verify_borad1(board)

#ic(board)