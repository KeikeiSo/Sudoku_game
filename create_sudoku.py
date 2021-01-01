from random import sample

# define base variable
base = 3
side = base * base

# define helper functions


def shuffle(s):
    return sample(s, len(s))


def pattern(r, c):
    return (base * (r % base) + r // base + c) % side

# define function generate


def generate():
    # get a sequence of 0, 1, 2
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    return [[nums[pattern(r, c)] for c in cols] for r in rows]

# define function empty


def empty(board, empties):
    squares = side * side
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0


def create_sudoku(n):
    board = generate()
    empty(board, n)
    return board


"""
# main
for line in create_sudoku():
    print(line)
"""
