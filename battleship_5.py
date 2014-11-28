'''
What could be better:
    - what if the guesses are not valid ints?
    - let them know if it's a near miss (a la Sub Search)?
    - variable-sized grid?
    - variable number of _ships?
    - show location of ship when player loses?
'''
from random import randint
from __builtin__ import int
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


def mark_ship_positions(_board, force_lowercase=True):
    '''
    Marks the position of each ship in _board, but only if it has not
    already been marked (by being sunk).
    '''
    for ship in _ships:
        if _board[ship[0]][ship[1]] == _board_initial_char:
            marker = best_effort_abbreviation(_ships[ship])
            if force_lowercase:
                marker = marker.lower()
            _board[ship[0]][ship[1]] = marker


def random_row(_board):
    return randint(0, len(_board) - 1)


def random_col(_board):
    return randint(0, len(_board[0]) - 1)


def place_ship(_board, _ship_name, _ships):
    _ship_placed = False
    while not _ship_placed:
        ship_row = random_row(_board)
        ship_col = random_col(_board)
        if not ((ship_row, ship_col)) in _ships:
            _ships[(ship_row, ship_col)] = _ship_name
            _ship_placed = True


def trim_leading_noise(the_string):
    noise_words = ['the', 'a', 'an', 'this', 'these', 'those', 'some', 'my']
    trim_string = the_string

    if ' ' in the_string:
        space_index = the_string.index(' ')
        if the_string[:space_index].lower() in noise_words:
            trim_string = the_string[(space_index + 1):]

    return(trim_string)


def best_effort_abbreviation(the_string):

    best_effort = trim_leading_noise(the_string)[0]

    if best_effort == _board_initial_char:
        best_effort = "!"

    return(best_effort)


# main:
_debug = True
_board_initial_char = "O"
_ships_count = getIntFromUser("How many ships? ", 1, 6)
_noise_words = ['the', 'a', 'an', 'this', 'these', 'those', 'some']

_good_geometry = False
while not _good_geometry:

    _rows = getIntFromUser("How many rows? ", 1, 10)
    _cols = getIntFromUser("How many columns? ", 1, 15)

    if _rows * _cols >= _ships_count:
        _good_geometry = True
    else:
        print("Error: you must make a _board big enough to hold your _ships!")

_turns = getIntFromUser("How many turns? ", 1, 20)

_board = []
for x in range(_rows):
    _board.append([_board_initial_char] * _cols)

print("")
_ships = {}
for ship in range(_ships_count):
    _ship_name_good = False
    while not _ship_name_good:
        _ship_name = raw_input("What do you want to name ship number {}? "
                               .format(ship + 1))
        if len(_ship_name) > 0:
            _ship_name_good = True

    place_ship(_board, _ship_name, _ships)

if _debug:
    print(_ships)

print("\nLet's play Battleship!\n")

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
_ships_sunk = 0
for turn in range(_turns):

    print("")
    print_board(_board)
    print("")
    print("Turn {0}".format(turn + 1))
    print("")

    _guess_row = getIntFromUser("Guess Row: ", 1, _rows) - 1
    _guess_col = getIntFromUser("Guess Column: ", 1, _cols) - 1

    if ((_guess_row < 0 or _guess_row > _rows - 1) or
            (_guess_col < 0 or _guess_col > _cols - 1)):
        print("Oops, that's not even in the ocean.")
    elif _board[_guess_row][_guess_col] != _board_initial_char:
        print("You guessed that one already.")
    elif (_guess_row, _guess_col) in _ships:
        _ship_name = _ships[(_guess_row, _guess_col)]
        _ship_trim_name = trim_leading_noise(_ship_name)
        if _ship_trim_name == _ship_name:
            _ship_name = "my " + _ship_name
        print("You sunk {}!".format(_ship_name))
        _marker = best_effort_abbreviation(_ship_name).upper()
        _board[_guess_row][_guess_col] = _marker

        _ships_sunk += 1

    else:
        print("You missed!")
        _board[_guess_row][_guess_col] = "X"

    if turn == _turns - 1 or _ships_sunk == _ships_count:
        print("")
        print("Game Over")
        if _ships_sunk == _ships_count:
            print("Congratulations! You win!")
            print("")
            break
        else:
            print("You poor sap - lost again, did you?")
        print("")

mark_ship_positions(_board, True)
print_board(_board)
