'''
Shows one way to implement a solution to Challenge Exercise 4
(simple calculator)

@author: sql.sith
'''


def calcThis(float1=None,
             op1=None,
             float2=None,
             op2=None,
             float3=None):

    # handle cases with two operators:
    if op2 in ('*', '/'):
        partialResult = calcThis(float2, op2, float3)
        return(calcThis(float1, op1, partialResult))
    elif op2 in ('+', '-'):
        partialResult = calcThis(float1, op1, float2)
        return(calcThis(partialResult, op2, float3))
    # handle cases with one operator:
    elif op2 is not None:
        _INVALID_OPERATOR2 = "Invalid operator: " + op2
        raise(Exception(_INVALID_OPERATOR2))
    elif op1 == "+":
        return(float1 + float2)
    elif op1 == "-":
        return(float1 - float2)
    elif op1 == "*":
        return(float1 * float2)
    elif op1 == "/":
        return(float1 / float2)
    else:
        _INVALID_OPERATOR = "Invalid operator: " + op1
        raise(Exception(_INVALID_OPERATOR))

# main:
_debug = False

print("Goals 1 through 4\n")
typedInput = raw_input("Enter an arithmetic problem in the form " +
                       "INT1 OPERATOR INT2 \n" +
                       "    or in the form " +
                       "INT1 OPERATOR1 INT2 OPERATOR2 INT3: ")

# initialize variables:
firstNumberString = ""
secondNumberString = ""
thirdNumberString = ""
firstOperator = None
secondOperator = None
firstNumber = None
secondNumber = None
thirdNumber = None


# parse everything, another hard way:

for ch in typedInput:
    # skip whitespace:
    if ch in (" ", "\t"):
        # this will go back to the top of the loop:
        continue
    # detect operators:
    elif ch in ("+", "-", "*", "/"):
        if firstOperator is None:
            firstOperator = ch
        else:
            secondOperator = ch
    # if we get to this else, we should be reading a number:
    else:
        if firstOperator is None:
            firstNumberString += ch
        elif secondOperator is None:
            secondNumberString += ch
        else:
            thirdNumberString += ch

firstNumber = float(firstNumberString)
secondNumber = float(secondNumberString)

if thirdNumberString == "":
    thirdNumber = None
else:
    thirdNumber = float(thirdNumberString)

if _debug:
    print("firstNumber: " + str(firstNumber))
    print("firstOperator: " + firstOperator)
    print("secondNumber: " + str(secondNumber))
    print("secondOperator: " + secondOperator)
    print("thirdNumber: " + str(thirdNumber))

result = calcThis(firstNumber, firstOperator, secondNumber,
                  secondOperator, thirdNumber)
