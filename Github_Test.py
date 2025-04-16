def make_grid():
    grid = [
        [' ', ' ', ' '],  # row 0
        [' ', ' ', ' '],  # row 1
        [' ', ' ', ' ']   # row 2
    ]
    return grid

my_grid = make_grid()

# Access the middle cell (row 1, col 1)
print(my_grid[1][1])  # → ' '

# Change a cell value
my_grid[0][0] = 'X'
