import os
import random
from icecream import ic
board = list()
count = 0

def randomizer():
    value = []
    c = 1
    for i in range(25):
        value.insert(i ,c)
        c = c + 1
    value = random.sample(value, len(value))
    return value
value = randomizer()

for i in range(5):
    row = []
    for j in range(5):
        row.insert(j,value[count])
        count = count +1
    board.append(row)

def display_board():
    for i in range(0,5):
        for j in range(0,5):
            print(board[i][j],end="\t")
        print("\n")

def update_board(val):
   for i in range(5):
        for j in range(5):
            if board[i][j] == val:
                board[i][j] = "X" 

def verify(board):
    k = 0
    l = 0
    m = 0
    n = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == "X":
                k = k + 1
                                
    for i in range(5):
        for j in range(5):
            if board[j][i] == "X":
                l = l + 1
    for i in range(5):
        for j in range(1 , 5 , -1):
            if board[i][j] == "X":
                n = n + 1

    for i in range(5):
        if board[i][i]== "X":
            m = m + 1
  
    if k == 5 or l == 5 or m == 5 or n == 5:
        ic("bingo")
        exit()

is_running = 1
print("welcome to BINGOO!!")
display_board()
while is_running == 1:
    val = input("enter the value ")    
    if val == ".":
        is_running =0
        exit()
    elif val.isalpha() == True:
        print("Please enter a valid number")
    elif val.isnumeric()== True:
        val = int(val)
        if val >=100:
            print("please select a number between 1 to 99")
        else:                        
            update_board(val)
            display_board()
            verify(board)
            
            
            
            
            
            
            


