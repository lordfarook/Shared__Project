def my_list():j
    first_line = [' ',' ',' ']
    second_line = [' ',' ',' ']
    third_line = [' ',' ',' ']
    return [first_line, second_line, third_line]

first_line, second_line, third_line = my_list()

def ball(first_line, second_line, third_line):
    line_question = int(input("What line would you like to pick (1-3)? "))
    index_question = int(input("What is you index (0-2)? "))
    value_question = input("What is you sign (x or o)? ")
    if line_question == 1:
        first_line[index_question] = value_question
    elif line_question == 2:
        second_line[index_question] = value_question
    elif line_question == 3:
        third_line[index_question] = value_question
    return [first_line, second_line, third_line]

def winning_condition(first_line, second_line, third_line):
    board = [first_line, second_line, third_line]
    white_list = ['x','o']
    for letter in white_list:
        #Vertical
        for indx in range(0, 3):
            if (board[0][indx] == board[1][indx] == board[2][indx] == letter):
                return f'vertical {letter} winning'

        #Horizontal
        for indx in range(0, 3):
            if (board[indx] == board[indx] == board[indx] == letter):
                return f'horizontal {letter} winning'

        #diagonal
        if (board[0][0] == board[1][1] == board[2][2] == letter):
            return f'diagonal {letter} winning'
        elif (board[0][2] == board[1][1] == board[2][0] == letter):
            return f'diagonal {letter} winning'

    return "Nobody won"

while True:
    print(f"Your current board: \n{first_line}\n{second_line}\n{third_line}")
    first_line, second_line, third_line = ball(first_line, second_line, third_line)

    shortcut = winning_condition(first_line, second_line, third_line)
    if "winning" in shortcut:
        print(f"Your current board: \n{first_line}\n{second_line}\n{third_line}")
        print(shortcut)
        break