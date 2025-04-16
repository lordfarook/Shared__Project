def Board():
    board = [[' ',' ',' '],  #[0] - row 1
             [' ',' ',' '],  #[1] - row 2
             [' ',' ',' ']]  #[2] - row 3
    return board

def Sign(board):
    row = int(input("What is going to be your row? (1-3)")) - 1
    col = int(input("What is going to be your row? (1-3)"))

