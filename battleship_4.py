'''
What could be better:
    - what if the guesses are not valid ints?
    - let them know if it's a near miss (a la Sub Search)?
    - variable-sized grid?
    - variable number of ships?
    - show location of ship when player loses?
'''
from random import randint
from reportlab.lib.validators import isInt


def getIntFromUser(prompt, _min, _max):

    done = False
    while not done:
        the_string = raw_input(prompt)
        if isInt(the_string):
            the_int = int(the_string)
            if the_int >= _min and the_int <= _max:
                done = True
            else:
                print('Error - the integer must be between {} and {}!'
                      .format(_min, _max))
        else:
            print('{} is not an integer. Please try again.'.format(the_string))

    return(the_int)


def print_board(_board):
    for row in _board:
        print(" ".join(row))


def random_row(_board):
    return randint(0, len(_board) - 1)


def random_col(_board):
    return randint(0, len(_board[0]) - 1)


_rows = getIntFromUser("How many rows? ", 1, 10)
_cols = getIntFromUser("How many columns? ", 1, 15)
_turns = getIntFromUser("How many turns? ", 1, 20)

_board = []
_debug = True

for x in range(_rows):
    _board.append(["O"] * _cols)


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

    _guess_row = getIntFromUser("Guess Row: ", 1, _rows) - 1
    _guess_col = getIntFromUser("Guess Column: ", 1, _cols) - 1

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
        if turn == _turns - 1:
            print("Game Over")

        print("")
        print_board(_board)
