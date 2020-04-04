import numpy as np
import random as rd
import time

def player():
    global board
    print("\nPlayer turn")
    while True:
        select = int(input("\nSelect : "))
        if(board[select-1] =='X' or board[select-1] =='O'): print("\nTry again\n")
        elif(select in range(1,10)):
            board[select-1] = 'X'
            break
    return board

def computer():
    print("\nComputer turn")
    global board
    global move
    choose = rd.choice(move)
    board[choose] = 'O'
    return board
    
def print_board():
    print("\n")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("\n")
    

def check():
    global board
    global running
    if (np.all(board[0:3]=='X')==True 
        or np.all(board[3:6]=='X')==True 
        or np.all(board[6:9]=='X')==True
        or np.all(board[0] == 'X' and board[3]=='X' and board[6]=='X')==True
        or np.all(board[1] == 'X' and board[4]=='X' and board[7]=='X')==True
        or np.all(board[2] == 'X' and board[5]=='X' and board[8]=='X')==True
        or np.all(board[0] == 'X' and board[4]=='X' and board[8]=='X')==True
        or np.all(board[2] == 'X' and board[4]=='X' and board[6]=='X')==True):
        print("\nPlayer wins")
        running = False

    elif (np.all(board[0:3]=='O')==True 
        or np.all(board[3:6]=='O')==True 
        or np.all(board[6:9]=='O')==True
        or np.all(board[0] == 'O' and board[3]=='O' and board[6]=='O')==True
        or np.all(board[1] == 'O' and board[4]=='O' and board[7]=='O')==True
        or np.all(board[2] == 'O' and board[5]=='O' and board[8]=='O')==True
        or np.all(board[0] == 'O' and board[4]=='O' and board[8]=='O')==True
        or np.all(board[2] == 'O' and board[4]=='O' and board[6]=='O')==True):
        print("\nComputer wins")
        running = False

    elif(np.all(board != '_' ) == True ):
        print("\nDraw")
        running = False
        
    return running
    
def best():
    global move
    global board
    if(board[0]=='_' and board[1]=='O' and board[2]=='O'):move.append(0)
    elif(board[0]=='O' and board[1]=='_' and board[2]=='O'):move.append(1)
    elif(board[0]=='O' and board[1]=='O' and board[2]=='_'):move.append(2)
    elif(board[3]=='_' and board[4]=='O' and board[5]=='O'):move.append(3)
    elif(board[3]=='O' and board[4]=='_' and board[5]=='O'):move.append(4)
    elif(board[3]=='O' and board[4]=='O' and board[5]=='_'):move.append(5)
    elif(board[6]=='_' and board[7]=='O' and board[8]=='O'):move.append(6)
    elif(board[6]=='O' and board[7]=='_' and board[8]=='O'):move.append(7)
    elif(board[6]=='O' and board[7]=='O' and board[8]=='_'):move.append(8)
    elif(board[0]=='_' and board[4]=='O' and board[8]=='O'):move.append(0)
    elif(board[0]=='O' and board[4]=='_' and board[8]=='O'):move.append(4)
    elif(board[0]=='O' and board[4]=='O' and board[8]=='_'):move.append(8)    
    elif(board[2]=='_' and board[4]=='O' and board[6]=='O'):move.append(2)
    elif(board[2]=='O' and board[4]=='_' and board[6]=='O'):move.append(4)
    elif(board[2]=='O' and board[4]=='O' and board[6]=='_'):move.append(6)
    elif(board[0]=='_' and board[3]=='O' and board[6]=='O'):move.append(0)
    elif(board[0]=='O' and board[3]=='_' and board[6]=='O'):move.append(3)
    elif(board[0]=='O' and board[3]=='O' and board[6]=='_'):move.append(6)
    elif(board[1]=='_' and board[4]=='O' and board[7]=='O'):move.append(1)
    elif(board[1]=='O' and board[4]=='_' and board[7]=='O'):move.append(4)
    elif(board[1]=='O' and board[4]=='O' and board[7]=='_'):move.append(7)
    elif(board[2]=='_' and board[5]=='O' and board[8]=='O'):move.append(2)
    elif(board[2]=='O' and board[5]=='_' and board[8]=='O'):move.append(5)
    elif(board[2]=='O' and board[5]=='O' and board[8]=='_'):move.append(8)
    
    elif(board[0]=='_' and board[1]=='X' and board[2]=='X'):move.append(0)
    elif(board[0]=='X' and board[1]=='_' and board[2]=='X'):move.append(1)
    elif(board[0]=='X' and board[1]=='X' and board[2]=='_'):move.append(2)
    elif(board[3]=='_' and board[4]=='X' and board[5]=='X'):move.append(3)
    elif(board[3]=='X' and board[4]=='_' and board[5]=='X'):move.append(4)
    elif(board[3]=='X' and board[4]=='X' and board[5]=='_'):move.append(5)
    elif(board[6]=='_' and board[7]=='X' and board[8]=='X'):move.append(6)
    elif(board[6]=='X' and board[7]=='_' and board[8]=='X'):move.append(7)
    elif(board[6]=='X' and board[7]=='X' and board[8]=='_'):move.append(8)
    elif(board[0]=='_' and board[4]=='X' and board[8]=='X'):move.append(0)
    elif(board[0]=='X' and board[4]=='_' and board[8]=='X'):move.append(4)
    elif(board[0]=='X' and board[4]=='X' and board[8]=='_'):move.append(8)    
    elif(board[2]=='_' and board[4]=='X' and board[6]=='X'):move.append(2)
    elif(board[2]=='X' and board[4]=='_' and board[6]=='X'):move.append(4)
    elif(board[2]=='X' and board[4]=='X' and board[6]=='_'):move.append(6)
    elif(board[0]=='_' and board[3]=='X' and board[6]=='X'):move.append(0)
    elif(board[0]=='X' and board[3]=='_' and board[6]=='X'):move.append(3)
    elif(board[0]=='X' and board[3]=='X' and board[6]=='_'):move.append(6)
    elif(board[1]=='_' and board[4]=='X' and board[7]=='X'):move.append(1)
    elif(board[1]=='X' and board[4]=='_' and board[7]=='X'):move.append(4)
    elif(board[1]=='X' and board[4]=='X' and board[7]=='_'):move.append(7)
    elif(board[2]=='_' and board[5]=='X' and board[8]=='X'):move.append(2)
    elif(board[2]=='X' and board[5]=='_' and board[8]=='X'):move.append(5)
    elif(board[2]=='X' and board[5]=='X' and board[8]=='_'):move.append(8)
    elif(board[0]=='_' or board[2]=='_'or board[6]=='_'or board[8]=='_' ):
        for i in [0,2,6,8]:
            if(board[i]=='_'): move.append(i)
    elif(board[4]=='_'):move.append(4)            
    else:
        for i in [1,3,5,7]:
            if board[i] == '_' : move.append(i)

    return move

    

board = np.array(['_','_','_',
                   '_','_','_',
                   '_','_','_'])
