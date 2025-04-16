def Board():
    board = [[' ',' ',' '],  #[0] - row 1
             [' ',' ',' '],  #[1] - row 2
             [' ',' ',' ']]  #[2] - row 3
    return board

board = Board()
def row(board):
    for raw in board:
        print(raw)

def Sign(board):
    lst = [0, 1, 2]
    available_signs = ['x', 'o']
    row = int(input("What is going to be your row? (1-3) ")) - 1     # 1 -> [0]
    while row not in lst:
        print("Please choose value from (1-3)")
        row = int(input("What is going to be your row? (1-3) ")) - 1
    col = int(input("What is going to be your col? (1-3) ")) - 1     # 1 -> [0]
    while col not in lst:
        print("Please choose value from (1-3)")
        col = int(input("What is going to be your col? (1-3) ")) - 1
    sign = input("What is your sign? [ x or o ] ")
    while sign not in available_signs:
        print("Please choose either x or o!")
        sign = input("What is your sign? [ x or o ] ")


    board[row][col] = sign
    return board

def Winning_Condition(board):
    available_signs = ['x','o']
    for check_x_o in available_signs:
        for indx in range(0,3):
            #vertical
            if all(place == check_x_o for place in board[indx]):
                return f"vertical {check_x_o} Winning"
            #horizontal
            elif all(board[i][indx] == check_x_o for i in range(0,3)):
                return f"horizontal {check_x_o} Winning"

        #diagonal
        if all(board[i][i] == check_x_o for i in range(0,3)):
            return f"diagonal {check_x_o} Winning"
        elif all(board[i][-i-1] == check_x_o for i in range(0,3)):
            return f"diagonal {check_x_o} Winning"

    return "No one is Winning"

def Gameplay(board):
    flag = True
    while flag:
        print(f"Your current board:")
        row(board)
        board = Sign(board)

        result = Winning_Condition(board)
        if "No one is Winning" not in result:
            print(f"Congratulations {result}:")
            row(board)
            flag = False


Gameplay(board)




