from colorama import Fore,init
import random
init(autoreset=True)
board=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
def print_board():
    board1=f'{board[0][0]} | {board[0][1]} | {board[0][2]}\n'
    sep1='---------\n'
    board2=f'{board[1][0]} | {board[1][1]} | {board[1][2]}\n'
    sep2='---------\n'
    board3=f'{board[2][0]} | {board[2][1]} | {board[2][2]}'
    return board1+sep1+board2+sep2+board3
def choice():
    chce=input(f"{Fore.BLUE}What's your choice X/O:")
    if chce.upper()=='X':
        return chce.upper()
    elif chce.upper()=='O':
        return chce.upper()
    elif chce.upper()=='EXIT':
        exit()
    else:
        print(f'{Fore.RED}Please enter only X/O')
        choice()
def player_turn(choice):
    col=input(f'{Fore.BLUE}Enter coulumn:')
    row=input(f'{Fore.BLUE}Enter row:')
    for i in range(0,len(board)):
        for j in range(0,i):
            if board[i][j]=='X' or board[i][j]=='O':
                player_turn(choice)
    if col.isdigit() and len(col)==1 and int(col)<=3 and int(col)>0 and row.isdigit() and len(row)==1 and int(row)<=3 and int(row)>0:
        print(f'{Fore.GREEN}valid statement')
        board[int(col)-1][int(row)-1]=choice
        return [int(col)-1,int(row)-1]
    else:
        player_turn()
def is_won(bd,choice):
    if (bd[0][0] and bd[0][1] and bd[0][2])==choice:
        return True
    elif (bd[1][0] and bd[1][1] and bd[1][2])==choice:
        return True
    elif (bd[2][0] and bd[2][1] and bd[2][2])==choice:
        return True
    elif (bd[0][0] and bd[1][1] and bd[2][2])==choice:
        return True
    elif (bd[0][2] and bd[1][1] and bd[2][0])==choice:
        return True
    elif (bd[0][0] and bd[1][0] and bd[2][0])==choice:
        return True
    elif (bd[0][1] and bd[1][1] and bd[2][1])==choice:
        return True
    elif (bd[0][2] and bd[1][2] and bd[2][2])==choice:
        return True
    return False
def is_winning(chce):
    abc=board.copy()
    for i in range(len(board)):
        for j in range(i):
            abc[i][j]==chce
            print(is_won(board,chce))
            if is_won(board,chce):
                return [i,j]
def bot_turn(bd,player):
    choice_col=[]
    choice_row=[]
    for i in range(0,len(bd)):
        for j in range(0,len(bd)):
            if bd[i][j]=='X' or bd[i][j]=='O':
                pass
            else:
                choice_col.append(i)
                choice_row.append(j)
    row=random.choices(choice_col)
    col=random.choices(choice_row)
    bt=''
    if player=='X':
        bt='O'
    elif player=='O':
        bt='X'
    board[col[0]][row[0]]=bt
    print(is_winning(player))
    return print_board()
abc=choice()
while True:
    print(player_turn(abc))
    print(bot_turn(board,abc))