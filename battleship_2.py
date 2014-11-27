'''
What could be better:
    - what if the guesses are not valid ints?
    - let them know if it's a near miss (a la Sub Search)?
    - variable-sized grid?
    - variable number of ships?
    - show location of ship when player loses?
'''
from random import randint
_rows = 6
_cols = 8
_turns = int(raw_input("How many turns? "))

_board = []
_debug = True

for x in range(_rows):
    _board.append(["O"] * _cols)


def print_board(_board):
    for row in _board:
        print(" ".join(row))


def random_row(_board):
    return randint(0, len(_board) - 1)


def random_col(_board):
    return randint(0, len(_board[0]) - 1)

print("Let's play Battleship!")
print_board(_board)

ship_row = random_row(_board)
ship_col = random_col(_board)

if _debug:
    print("Ship location: {0}.{1}"
          .format(ship_row, ship_col))

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(_turns):
    print("")
    print("Turn {0}\n".format(turn + 1))

    _guess_row = int(raw_input("Guess Row: "))
    _guess_col = int(raw_input("Guess Col: "))

    if _guess_row == ship_row and _guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if ((_guess_row < 0 or _guess_row > _rows - 1) or
                (_guess_col < 0 or _guess_col > _cols - 1)):
            print("Oops, that's not even in the ocean.")
        elif(_board[_guess_row][_guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            _board[_guess_row][_guess_col] = "X"
        if turn == 3:
            print("Game Over")

        print("")
        print_board(_board)
