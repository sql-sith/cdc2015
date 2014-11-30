'''
Battleship: a one-player Python implementation of the classic board game.
Author: sql.sith
'''
from random import randint
from reportlab.lib.validators import isInt
import re
import sys
import os


def get_int_from_user(prompt, min, max):

    done = False
    while not done:
        the_string = raw_input(prompt)
        if isInt(the_string):
            the_int = int(the_string)
            if the_int >= min and the_int <= max:
                done = True
            else:
                print('Error - the integer must be between {} and {}!'
                      .format(min, max))
        else:
            print('{} is not an integer. Please try again.'.format(the_string))

    return(the_int)


def print_board(board):
    print "     1   2   3   4   5   6   7   8   9  10"
    print "    --- --- --- --- --- --- --- --- --- ---"
    for row in range(len(board)):
        sys.stdout.write(chr(ord("A") + row) + " |  " + "   ".join(board[row]) + "          ")
        if row in (0, 2, 9):
            sys.stdout.write("=".center(30, "="))
        elif row == 1:
            sys.stdout.write("==" + "Turn # {0}".format(_turns).center(26) + "==")
        elif row in (3, 8):
            sys.stdout.write("==" + " ".center(26) + "==")
        elif row == 4:
            sys.stdout.write("==" + "Hits: {0}".format(_hits).center(26) + "==")
        elif row == 5:
            sys.stdout.write("==" + "Misses: {0} / {1}".format(_misses, _misses_allowed).center(26) + "==")
        elif row == 6:
            sys.stdout.write("==" + "Mistakes: {0}".format(_mistakes).center(26) + "==")
        elif row == 7:
            sys.stdout.write("==" + "Sunk: {0} / {1}".format(_ships_sunk, _ships_count).center(26) + "==")
        sys.stdout.write("\n")


def mark_ship_positions(board, ships, force_lowercase=True):
    '''
    Marks the position of each ship in board, but only if it has not
    already been marked (by being sunk).
    '''
    for ship in ships:
        for position in ship["Positions"]:
            row = position[0]
            col = position[1]

            if board[row][col] == _board_initial_char:
                marker = ship["Abbreviation"]
                if force_lowercase:
                    marker = marker.lower()
                board[row][col] = marker


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def place_ship(board, ship):
    ship_placed = False
    max_row_if_vertical = len(board) - ship["Length"]
    max_row_if_horizontal = len(board) - 1
    max_col_if_vertical = len(board[0]) - 1
    max_col_if_horizontal = len(board[0]) - ship["Length"]
    occupied_positions = []
    
    for s in _ships:
        occupied_positions += s["Positions"]
            
    while not ship_placed:
        collision = False
        
        if randint(0, 1) == 0:
            horizontal = True
        else:
            horizontal = False
            
        if horizontal:
            fixed_coordinate = randint(0, max_row_if_horizontal)
            variable_coordinate_start = randint(0, max_col_if_horizontal)
        else:
            fixed_coordinate = randint(0, max_col_if_vertical)
            variable_coordinate_start = randint(0, max_row_if_vertical)
            
        ship["Positions"] = []
        for x in range(ship["Length"]):
            variable_coordinate = variable_coordinate_start + x
            if horizontal:
                coords = (fixed_coordinate, variable_coordinate)
            else:
                coords = (variable_coordinate, fixed_coordinate)
                
            if coords in occupied_positions:
                collision = True
                break
            else:
                ship["Positions"] += [coords]

        if not collision:
            ship_placed = True
    
    if _debug:  
        print ship
        print max_row_if_vertical
        print max_col_if_horizontal
        print ship["Positions"]


def trim_leading_noise(the_string):
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


def hit(row, col):
    for ship in _ships:
        if (row, col) in ship["Positions"]:
            return(ship)

    # return None for a miss:
    return(None)


def sunk(ship):
    all_hit = True
    for position in ship["Positions"]:
        if _board[position[0]][position[1]] != ship["Abbreviation"].upper():
            all_hit = False
            break
    return(all_hit)

def clear_console():
    if 'TERM' in os.environ:
        os.system('cls' if os.name=='nt' else 'clear')
    else:
        print("\n" * 50)


# main:
_debug = False
_board_initial_char = "O"
_board_missed_char = "X"
_noise_words = ['the', 'a', 'an', 'this', 'these', 'those', 'some']
_ships_sunk = 0
_misses = 0
_hits = 0
_mistakes = 0
_turns = 0
_guess_prompt = "Your guess? "
_guess_regex = "^([a-jA-J])-?(10|[1-9])$"
_rows = 10
_cols = 10

_board = []
for x in range(_rows):
    _board.append([_board_initial_char] * _cols)

_ships = [ { "Name" : "Aircraft Carrier", "Length" : 5, "Abbreviation" : "a", "Positions" : []},
           { "Name" : "Battleship", "Length" : 4, "Abbreviation" : "b", "Positions" : []},
           { "Name" : "Cruiser", "Length" : 3, "Abbreviation" : "c", "Positions" : []},
           { "Name" : "Destroyer", "Length" : 2, "Abbreviation" : "d", "Positions" : []},
           { "Name" : "Submarine", "Length" : 3, "Abbreviation" : "s", "Positions" : []}
           ]  
_ships_count = len(_ships)

for ship in _ships:
    place_ship(_board, ship)

if _debug:
    for ship in _ships:
        print(ship)
    mark_ship_positions(_board, _ships, True)

if not _debug:
    clear_console()

print("Let's play Battleship!\n")
print("")
_misses_allowed = get_int_from_user("How many misses allowed? ", 10, 50)  

while _misses < _misses_allowed and _ships_sunk < _ships_count:
    _turns += 1
    
    print("")
    print_board(_board)
    print("")
    print("Turn {0}".format(_turns)) 
    print("")

    # get user's guess:
    _guess_match = None
    while _guess_match is None:
        _guess_input = raw_input(_guess_prompt)
        _guess_match = re.match(_guess_regex, _guess_input)
        if _guess_match is None:
            print("Please enter your guess in the format A-1 or A1.")
            print("")
    
    _guess_row = ord(_guess_match.group(1).upper()) - ord("A") # maps A -> 0, B -> 1, etc.
    _guess_col = int(_guess_match.group(2)) - 1 # should never fail, per validation
    
    if not _debug:
        clear_console()

    if _debug:
        print("You guessed {0:s}, which maps to row {1:d} and column {2:d}.".format(_guess_input, _guess_row, _guess_col))
    
    # first case should not happen per validation, but leaving it in just in case:
    if ((_guess_row < 0 or _guess_row > _rows - 1) or
            (_guess_col < 0 or _guess_col > _cols - 1)):
        print("Oops, that's not even in the ocean.")
        _mistakes += 1
    elif _board[_guess_row][_guess_col] not in(_board_initial_char, _board[_guess_row][_guess_col].lower()):
        print("You guessed that one already.")
        _mistakes += 1
    else:
        _ship_hit = hit(_guess_row, _guess_col)
        if _ship_hit is None:
            print("You missed!")
            _board[_guess_row][_guess_col] = "X"
            _misses += 1
        else:
            _ship_name = _ship_hit["Name"]
            _board[_guess_row][_guess_col] = _ship_hit["Abbreviation"].upper()
            
            if sunk(_ship_hit):
                print("You sunk my {}!".format(_ship_name))
                _ships_sunk += 1
            else:
                print("Hit - {}.".format(_ship_name))
            _hits += 1

    if _misses == _misses_allowed or _ships_sunk == _ships_count:
        print("")
        print("Game Over")
        if _ships_sunk == _ships_count:
            print("Congratulations - you won!!!")
        else:
            print("You poor sap - lost again, did you?")
        print("")

mark_ship_positions(_board, _ships, True)
print_board(_board)
print("")
