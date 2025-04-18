#Next step is not letting a sign be at the same time at one cell
#Really understanding the logic of game_state

def Board():
    board = [[' ',' ',' '],  #[0] - row 1
             [' ',' ',' '],  #[1] - row 2
             [' ',' ',' ']]  #[2] - row 3
    return board

board = Board()
def row(board):
    for raw in board:
        print(raw)

game_state = {'chosen_path': None, 'count': 0}

def Sign(board, game_state):
    x_list = ['x','o','x','o','x','o','x','o','x']
    o_list = ['o','x','o','x','o','x','o','x','o']
    lst = [0, 1, 2]
    available_signs = ['x', 'o']
    if board == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]:
        sign = input("What is going to be your sign? [ x or o ] ")
        while sign not in available_signs:
            print("Please choose either x or o!")
            sign = input("What is your sign? [ x or o ] ")
        if sign == 'x':
            game_state['chosen_path'] = x_list
        else:
            game_state['chosen_path'] = o_list

    sign = game_state['chosen_path'][game_state['count']]

    row = int(input("What is going to be your row? (1-3) ")) - 1     # 1 -> [0]
    while row not in lst:
        print("Please choose value from (1-3)")
        row = int(input("What is going to be your row? (1-3) ")) - 1
    col = int(input("What is going to be your col? (1-3) ")) - 1     # 1 -> [0]
    while col not in lst:
        print("Please choose value from (1-3)")
        col = int(input("What is going to be your col? (1-3) ")) - 1



    board[row][col] = sign
    game_state['count'] += 1
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
    game_state = {'chosen_path': None, 'count': 0}
    flag = True
    while flag:
        print(f"Your current board:")
        row(board)
        board = Sign(board, game_state)

        result = Winning_Condition(board)
        if "No one is Winning" not in result:
            print(f"Congratulations {result}:")
            row(board)
            print("Game Over!")
            flag = False


Gameplay(board)




