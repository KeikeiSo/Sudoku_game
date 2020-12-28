from copy import deepcopy
from create_sudoku import generate, empty


# helper functions
def find_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return (-1, -1)

def valid(n, i, j, sudoku):
    # check row
    row = sudoku[i]
    for r in row:
        if r == n:
            return False
    # check column
    for c in range(9):
        if sudoku[c][j] == n:
            return False

    # check box
    boxposx = (i // 3)*3
    boxposy = (j // 3)*3
    for x in range(boxposx, boxposx+3):
        for y in range(boxposy, boxposy+3):
            if sudoku[x][y] == n:
                return False

    return True
    
# the solver function
def solve(sudoku):
    x, y = find_empty(sudoku)
    if x == y == -1:
        return True
    else:
        for i in range(1, 10):
            if valid(i, x, y, sudoku):
                sudoku[x][y] = i
                if solve(sudoku):
                    return True
                sudoku[x][y] = 0
    return False

"""
# main:
# generate a sudoku
board = generate()

sudoku = deepcopy(board)
empty(sudoku, 50)

# print the solution and sudoku
for line in board:
    print(line)

print()

for line in sudoku:
    print(line)

print()

# print the solver's solution
solve(sudoku)

for line in sudoku:
    print(line)
"""
            
        


