'''
Created on 14 Oct 2017
@author: Vlad Ciobanu
@student ID: C15716369
'''

def readInput(minR, maxR):
    option = -1
    while not (minR <= option and option <= maxR):
        optionTmp = input("* You can choose the grid size to be between {0} and {1}:".format(minR, maxR))

        if len(optionTmp) > 0 and isSafeInt(optionTmp):
            option = int(optionTmp)
        else:
            print("Number out of bounds")
    return option

def readSafeInt():
    tmpRead = "null"
    while not isSafeInt(tmpRead):
        print("Please enter a number: ")
        inp = input()
        if isSafeInt(inp):
            tmpRead = int(inp)
        else:
            print("Provided input is not a number.")
    return tmpRead

def isSafeInt(N):
    try:
        int(N)
        return True
    except Exception:
        return False    

print("            === Welcome to my Tic Tac Toe Game ===    ")
print()
print("* This is a multiplayer game where 3 players must participate. *")
print("* Player 1 is X, Player2 is 0, Player 3 is -                   *")
print("****************************************************************")
print("* Good luck!                                                   *")
print("* And lets play :D                                             *")
print("****************************************************************")
print("* Please enter the board size.                                 *")
size = readInput(5, 10)
board = [" " for i in range(100)]

def print_board():
    current = 0
    maxLength = len(str(size * size))
    for i in range(0, size):
        for j in range(0, size):
            current += 1
            numOfSpaces = maxLength - len(str(current)) + 1
            print(" " + board[current - 1], end='')
            for k in range(0, numOfSpaces):
                print(" ", end='')
            print(str(current) + "| ", end='')
            
        print()
        for k in range(0, size):
            numOfSpaces = maxLength - len(str(current)) + 1
            print("--", end='')
            for k1 in range(0, numOfSpaces):
                print("-", end='')
            for k2 in range(0, len(str(current))):
                print("-", end='')
            
            if k == (size - 1):
                print("|", end='')
            else:
                print("|-", end='')
        print()

print_board()

def player_move(symbol):
    validatePick = "null"
    
    if symbol == "X":
        number = 1
    elif symbol == "0":
        number = 2
    elif symbol == "-":
        number = 3
    print(" ")        
    print("It's your turn player {}".format(number) + ": Enter your pick from (1-{}):".format(size * size))    
    
    while not isSafeInt(validatePick):
        print("Please enter a number: ")
        pick = input()        
        if isSafeInt(pick):
            validatePick = pick
            break
        else:
            print("Provided input is not a number.")            

    pick = int(validatePick)  
    
    if board[pick - 1] != " ":
        while board[pick - 1] != " ":
            pick = int(input("Wrong pick, this space is taken! Try again with a different pick: ").strip())
            print(is_draw())
    board[pick - 1] = symbol    

def is_victory(symbol):
    for j in range(0, size - 2):
        for i in range(0, size - 2):
            boardTMP = [" " for i in range(9)]
            boardTMP[0] = board[i + j * size]
            boardTMP[1] = board[i + j * size + 1]
            boardTMP[2] = board[i + j * size + 2]
            boardTMP[3] = board[i + j * size + size]
            boardTMP[4] = board[i + j * size + size + 1]
            boardTMP[5] = board[i + j * size + size + 2]
            boardTMP[6] = board[i + j * size + size * 2]
            boardTMP[7] = board[i + j * size + size * 2 + 1]
            boardTMP[8] = board[i + j * size + size * 2 + 2]
            
            if(boardTMP[0] == symbol and boardTMP[1] == symbol and boardTMP[2] == symbol) or\
            (boardTMP[3] == symbol and boardTMP[4] == symbol and boardTMP[5] == symbol) or\
            (boardTMP[6] == symbol and boardTMP[7] == symbol and boardTMP[8] == symbol) or\
            (boardTMP[0] == symbol and boardTMP[3] == symbol and boardTMP[6] == symbol) or\
            (boardTMP[1] == symbol and boardTMP[4] == symbol and boardTMP[7] == symbol) or\
            (boardTMP[2] == symbol and boardTMP[5] == symbol and boardTMP[8] == symbol) or\
            (boardTMP[0] == symbol and boardTMP[4] == symbol and boardTMP[8] == symbol) or\
            (boardTMP[2] == symbol and boardTMP[4] == symbol and boardTMP[6] == symbol):
                return True
    return False
            
def is_draw():
    if " " not in board[:size*size]:
        return True
    else:
        return False

while True:
   
        player_move("X")
        print_board()
        if is_victory("X"):
            print("Player 1 wins! Congratulations!")
            print(is_draw())
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move("0")
        print_board()
        if is_victory("0"):
            print_board()
            print("Player 2 wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move("-")
        print_board()
        if is_victory("-"):
            print_board()
            print("Player 3 wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break