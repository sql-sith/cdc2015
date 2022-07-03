"""
Shows one way to implement a solution to Challenge Exercise 4 (simple calculator)

@author: sql.sith
"""

from sys import version_info

if version_info.major < 3:
    input = raw_input


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
        print("The only operators supported are: +-/*")
        raise(Exception(_INVALID_OPERATOR))


_debug = False

print("Goal 1\n")

typedInput = input("Enter an arithmetic problem in the form INT1 OPERATOR INT2: ")
# typedInputSaved = typedInput

# get the first number, one hard way (there are several):
firstNumberString = ""

for ch in typedInput:
    if ch != " ":
        firstNumberString += ch
    else:
        # this exits the loop:
        break
firstNumber = int(firstNumberString)

# trim the first number and the first space:
typedInput = typedInput[len(firstNumberString) + 1:]

operator = typedInput[:1]

# trim operator and second space: 
typedInput = typedInput[2:]

# what's left is the second number:
secondNumber = int(typedInput)

if _debug:
    print("firstNumber: " + str(firstNumber))
    print("operator: " + operator)
    print("secondNumber: " + str(secondNumber))

print (calc_this(firstNumber, operator, secondNumber))
