# -*- coding: utf-8 -*-
"""

Tic-tac-toe

Created on Fri May 22 22:43:40 2020

@author: Mr Spence
"""

def board_draw(board):
    line_down="     |     |     "
    line_setup1=line_down
    line_setup2=line_down
    line_setup3=line_down
    line_cross="-----------------"
    
    a=list(line_setup1)
    a[2]=board[0]
    a[8]=board[1]
    a[14]=board[2]
    b=""
    for i in list(range(0,len(a))):
        b=b+a[i]
    line_setup1=b
    
    a=list(line_setup2)
    a[2]=board[3]
    a[8]=board[4]
    a[14]=board[5]
    b=""
    for i in list(range(0,len(a))):
        b=b+a[i]
    line_setup2=b
    
    a=list(line_setup3)
    a[2]=board[6]
    a[8]=board[7]
    a[14]=board[8]
    b=""
    for i in list(range(0,len(a))):
        b=b+a[i]
    line_setup3=b
    
    board_sketch=line_down + "\n" + line_setup1 + "\n" + line_down + "\n" + line_cross + "\n" + line_down + "\n" + line_setup2 + "\n" + line_down + "\n" + line_cross + "\n" + line_down + "\n" + line_setup3 + "\n" + line_down
    return board_sketch          
 
def start_game():
    XO="a"
    while XO not in ["X","O","x","o",0]:
        XO=input("Would you like to be Os or Xs (Write X or O): ")
        if XO not in ["X","O","x","o",0]:
            print("This is not a valid answer")
        else:
            if XO in ["X","x"]:
                XTurn=1
            else:
                XTurn=0
            print("Let's start the game! \n")
            board=["1","2","3","4","5","6","7","8","9",]
            board_sketch=board_draw(board)
            print("The board looks like: \n" + board_sketch + "\nYou need to enter the number you wish to put your marker when prompted")
    return XTurn
  
def play_turn(XTurn,board):
    available=[]
    x=1
    for i in board:
        if i==" ":
            available.append(x)
        x=x+1
    print(available)
    a=0
    while a not in available:
        a=0
        print(board_draw(board))
        if XTurn==1:
            a=input("Where would you like your marker? (X): ")
        elif XTurn==0:
            a=input("Where would you like your marker? (O): ")
        if a.isdigit():
            a=int(a)
        else:
            print("This is not a valid entry")
    if XTurn==1:
        board[a-1]="X"
    elif XTurn==0:
        board[a-1]="O"
        
    return(board)

def check_win(board):
    Win=0
    
    if board[0]=="X" and board[1]=="X" and board[2]=="X":
        Win=1
        print("X Wins")
    elif board[3]=="X" and board[4]=="X" and board[5]=="X":
        Win=1
        print("X Wins")
    elif board[6]=="X" and board[7]=="X" and board[8]=="X":
        Win=1
        print("X Wins")
    elif board[0]=="X" and board[3]=="X" and board[6]=="X":
        Win=1
        print("X Wins")
    elif board[1]=="X" and board[4]=="X" and board[7]=="X":
        Win=1
        print("X Wins")
    elif board[2]=="X" and board[5]=="X" and board[8]=="X":
        Win=1
        print("X Wins")
    elif board[0]=="X" and board[4]=="X" and board[8]=="X":
        Win=1
        print("X Wins")
    elif board[2]=="X" and board[4]=="X" and board[6]=="X":
        Win=1
        print("X Wins")

    if board[0]=="O" and board[1]=="O" and board[2]=="O":
        Win=2
        print("O Wins")
    elif board[3]=="O" and board[4]=="O" and board[5]=="O":
        Win=2
        print("O Wins")
    elif board[6]=="O" and board[7]=="O" and board[8]=="O":
        Win=2
        print("O Wins")
    elif board[0]=="O" and board[3]=="O" and board[6]=="O":
        Win=2
        print("O Wins")
    elif board[1]=="O" and board[4]=="O" and board[7]=="O":
        Win=2
        print("O Wins")
    elif board[2]=="O" and board[5]=="O" and board[8]=="O":
        Win=2
        print("O Wins")
    elif board[0]=="O" and board[4]=="O" and board[8]=="O":
        Win=2
        print("O Wins")
    elif board[2]=="O" and board[4]=="O" and board[6]=="O":
        Win=2
        print("O Wins")
        
    if " " not in board:
        Win=3
        
    
    
    return(Win)


def game_frame():
    Win=0
    XTurn=start_game()
    board=[" "," "," "," "," "," "," "," "," ",]
    
    a=input("Ready to begin? Y/N: ")
    if a in ["Y","y"]:
        while Win==0:
            board=play_turn(XTurn,board)
            Win=check_win(board)
            
            XTurn=int((XTurn+1)%2)
        
        if Win==1 or Win==2 or Win==3:
            board_sketch=board_draw(board)
            print(board_sketch)
            if Win==1:
                print("Well played X!")
            elif Win==2:
                print("Well played O!")
            elif Win==3:
                print("It's a draw")
            replay=input("Want to play again? Y/N: ")
            if replay in ["Y","y"]:
                game_frame()
        
            
    else:
        print("Okay!")

game_frame()
    
    
    
    