"""
Shows one way to implement a solution to Challenge Exercise 4 (simple calculator)

@author: sql.sith
date: Nov 11, 2014
"""

import sys


def calc_this(int1, op, int2):
    if op == "+":
        return int1 + int2
    elif op == "-":
        return int1 - int2
    elif op == "*":
        return int1 * int2
    elif op == "/":
        return float(int1) / float(int2)
    else:
        _INVALID_OPERATOR = "Invalid operator: " + op
        raise(Exception(_INVALID_OPERATOR))


_debug = False

print("Goal 1\n")

if sys.version_info.major < 3:
    input = raw_input

typedInput = input("Enter an arithmetic problem in the form INT1 OPERATOR INT2: ")

# the easy way:
splitInput = typedInput.split()
print(calc_this(int(splitInput[0]), splitInput[1], int(splitInput[2])))
