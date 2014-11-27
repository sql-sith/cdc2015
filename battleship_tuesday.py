'''
What could be better:
    - what if the guesses are not valid ints?
    - let them know if it's a near miss (a la Sub Search)?
    - variable-sized grid?
    - variable number of ships?
    - show location of ship when player loses?
'''
from random import randint
_ROWS = 6
_COLS = 8

_board = []
_debug = True

for x in range(_ROWS):
    _board.append(["O"] * _COLS)


def print_board(_board):
    for row in _board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(_board)


def random_row(_board):
    return randint(0, _ROWS - 1)


def random_col(_board):
    return randint(0, _COLS - 1)

ship_row = random_row(_board)
ship_col = random_col(_board)

if _debug:
    print("Ship location: ({0},{1})"
          .format(ship_row, ship_col))

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print("")
    print("Turn {0}\n".format(turn + 1))
    # print "Turn", turn + 1
    _guess_row = int(raw_input("Guess Row:"))
    _guess_col = int(raw_input("Guess Col:"))

    if _guess_row == ship_row and _guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if ((_guess_row < 0 or _guess_row > 4) or
                (_guess_col < 0 or _guess_col > 4)):
            print("Oops, that's not even in the ocean.")
        elif(_board[_guess_row][_guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            _board[_guess_row][_guess_col] = "X"
        if turn == 3:
            print("Game Over")
        # Print (turn + 1) here!
        print("")
        print_board(_board)
