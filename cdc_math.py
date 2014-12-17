'''
Implements various math functions using basic arithmetic and estimation.

Created on Dec 16, 2014

@author: cleonard
'''
from reportlab.lib.validators import isNumber
from decimal import Decimal
from __builtin__ import abs

tolerance = Decimal('0.00000000000000001')


def square_root_newton(num):
    '''
        See http://mathworld.wolfram.com/NewtonsIteration.html for details.
        See https://mitpress.mit.edu/sicp/full-text/sicp/book/node12.html
            for another discussion of the same algorithm.
    '''

    if not isNumber(num):
        raise(_NON_NUMERIC_ARG)

    target = abs(Decimal(str(num)))
    this_guess = Decimal('1')
    guesses = 0

    while abs(this_guess * this_guess - target) > tolerance:
        guesses += 1
        if _debug: print(this_guess)  # @IgnorePep8
        this_guess = Decimal('0.5') * (this_guess + target/this_guess)

    if _debug:
        accuracy = abs(this_guess * this_guess - target)
        print('Guesses: {0}; final_guess: {1}; accuracy: {2}'
              .format(guesses, this_guess, accuracy))  # @IgnorePep8

    if not (this_guess * this_guess - target) <= tolerance:
            raise(_NO_SOLUTION_FOUND)

    return(this_guess)


def square_root(num):
    if not isNumber(num):
        raise(_NON_NUMERIC_ARG)

    target = abs(Decimal(str(num)))
    guesses = 0
    guess = Decimal('0')

    while abs(guess * guess - target) > tolerance:
        guesses += 1
        guess += tolerance
        if guess * guess > target:
            if _debug: print(guesses)  # @IgnorePep8
            if _debug: print(guess)  # @IgnorePep8
            raise(_NO_SOLUTION_FOUND)

    if _debug: print(guesses)  # @IgnorePep8
    return(guess)

global _debug
_debug = True

global _NON_NUMERIC_ARG
_NON_NUMERIC_ARG = Exception('Non-numeric argument detected.' +
                             'Please pass only numeric arguments.')

global _NO_SOLUTION_FOUND
_NO_SOLUTION_FOUND = Exception('No solution found. Cry me a river.')


if __name__ == "__main__":
    square = 1001293847612398

    #===========================================================================
    # try:
    #     root = square_root(square)
    #     print(root)
    #     print(root * root)
    # except Exception as e:
    #     print(e)
    #===========================================================================

    try:
        root = square_root_newton(square)
        print(root)
        print(root * root)
    except Exception as e:
        print(e)
