'''
Implements various math functions using basic arithmetic and estimation.

Created on Dec 16, 2014

@author: cleonard
'''
from reportlab.lib.validators import isNumber, isInt
from decimal import Decimal, getcontext
from __builtin__ import abs, True
import re
from datetime import datetime


tolerance = Decimal('0.000000001')


def is_prime_miller_rabin(n, _precision_for_huge_n=16):
    '''
        This is a re-arranged version of the code available at
        http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python.
        The only reason it's rearranged is to make it easier to put
        in our debug timers.
    '''
    retval = None

    if _debug: start = datetime.now()  # @IgnorePep8

    _known_primes = [2, 3]

    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  # n  is definitely composite

    if n in _known_primes or n in (0, 1):
        retval = True
    elif any((n % p) == 0 for p in _known_primes):
        retval = False
    else:
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
    if retval is None:
        # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
        if n < 1373653:
            retval = not any(_try_composite(a, d, n, s)
                             for a in (2, 3))
        elif n < 25326001:
            retval = not any(_try_composite(a, d, n, s)
                             for a in (2, 3, 5))
        elif n < 118670087467:
            if n == 3215031751:
                retval = False
            else:
                retval = not any(_try_composite(a, d, n, s)
                                 for a in (2, 3, 5, 7))
        elif n < 2152302898747:
            retval = not any(_try_composite(a, d, n, s)
                             for a in (2, 3, 5, 7, 11))
        elif n < 3474749660383:
            retval = not any(_try_composite(a, d, n, s)
                             for a in (2, 3, 5, 7, 11, 13))
        elif n < 341550071728321:
            retval = not any(_try_composite(a, d, n, s)
                             for a in (2, 3, 5, 7, 11, 13, 17))
        # otherwise
        else:
            retval = not any(_try_composite(a, d, n, s)
                             for a in _known_primes[:_precision_for_huge_n])

    if _debug: stop = datetime.now()  # @IgnorePep8
    if _debug: print(stop-start)  # @IgnorePep8
    return(retval)


def is_prime_wiki(num):
    '''
        This is an implementation given in (and explained by) Wikipedia at
        https://en.wikipedia.org/wiki/Primality_test#Python_implementation.
        It is slightly modified to allow timing inside the function if _debug
        is True.
    '''
    retval = None  # @UnusedVariable

    if _debug: start = datetime.now()  # @IgnorePep8

    if num <= 3:
        retval = (num >= 2)  # @UnusedVariable
    elif num % 2 == 0 or num % 3 == 0:
        retval = False  # @UnusedVariable
    else:
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                retval = False  # @UnusedVariable
        if retval is None:
            retval = True

    if _debug:
        stop = datetime.now()
        print(stop-start)

    return(retval)


def is_prime_regex(num):
    '''
        Unbelievably (OK, maybe just surprisingly), you can detect prime
        numbers by creating a string whose members are all the character "1"
        and which has a length equal to the number you are testing, and then
        running a clever regular expression on that string.

        There is a nice explanation of how this works at this URL:
            http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
    '''
    s = "1" * num

    if _debug: start = datetime.now()  # @IgnorePep8
    m = re.search(r'^1?$|^(11+?)\1+$', s)
    if _debug: stop = datetime.now()  # @IgnorePep8
    if _debug: print(stop-start)  # @IgnorePep8

    if m:
        return(False)
    else:
        return(True)


def is_prime_naive_division(num):
    # if not isInt(num): raise _NON_INTEGER_ARG  # @IgnorePep8
    if num < 0: raise _NEGATIVE_ARG  # @IgnorePep8

    if _debug: start = datetime.now()  # @IgnorePep8

    if num in (0, 1): return(False)  # @IgnorePep8

    trial = 2
    is_prime = True

    while is_prime and (trial * trial <= num):
        is_prime = not (num % trial == 0)
        trial += 1

    if _debug: stop = datetime.now()  # @IgnorePep8
    if _debug: print(stop-start)  # @IgnorePep8

    return(is_prime)


def square_root_newton(num, precision=None):
    '''
        See http://mathworld.wolfram.com/NewtonsIteration.html for details.
        See https://mitpress.mit.edu/sicp/full-text/sicp/book/node12.html
            for another discussion of the same algorithm.

        Notice that it is possible to have values for num and precision
            which will result in an infinite loop, due to not being able to
            get "close enough" to the correct answer, as specified by the
            global tolerance variable. This implementation merely detects
            this situation and raises _NO_SOLUTION_FOUND if it occurs.
    '''

    if isInt(precision):
        getcontext().prec = precision

    if not isNumber(num):
        raise(_NON_NUMERIC_ARG)

    target = abs(Decimal(str(num)))
    this_guess = Decimal('1')
    guesses = 0

    while abs(this_guess * this_guess - target) > tolerance:
        guesses += 1
        if _debug: print(this_guess)  # @IgnorePep8
        prior_guess = this_guess
        this_guess = Decimal('0.5') * (this_guess + target/this_guess)
        if this_guess == prior_guess:
            raise(_NO_SOLUTION_FOUND)

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

global _NON_INTEGER_ARG
_NON_INTEGER_ARG = Exception('Non-integer argument detected.' +
                             'Please pass only integer arguments.')

global _NEGATIVE_ARG
_NEGATIVE_ARG = Exception('Negative argument detected.' +
                          'Please pass only non-negative arguments.')


if __name__ == "__main__":
    square = Decimal('48')

    # =======================================================================
    # try:
    #     root = square_root(square)
    #     print(root)
    #     print(root * root)
    # except Exception as e:
    #     print(e)
    # =======================================================================

    # =======================================================================
    # try:
    #     root = square_root_newton(square, precision=38)
    #     print(root)
    #     print(root * root)
    # except Exception as e:
    #     print(e)
    # =======================================================================

    try:
        # prime_big_trial = 10876570039
        # prime_big_trial = 100000000001
        # mersenne primes will make the naive algorithm have a bad day.
        # see https://primes.utm.edu/mersenne/index.html
        prime_big_trial = 2**57885161-1
        prime_loop_trial_count = 0
        _perform_regex_big_trial = False
        _perform_naive_big_trial = False
        _perform_wiki_big_trial = False

        print("")
        print("##### Starting regex tests:")

        _debug = False
        for i in range(prime_loop_trial_count):
            negator = ""
            if not is_prime_regex(i):
                negator = "not "
            print("The number {0} is {1}prime."
                  .format(i, negator))
        _debug = True

        if _perform_regex_big_trial:
            negator = ""
            if not is_prime_regex(prime_big_trial):
                negator = "not "
            print ("The number {0} is {1}prime."
                   .format(prime_big_trial, negator))

        print("")
        print("##### Starting naive tests:")
        _debug = False
        for i in range(prime_loop_trial_count):
            negator = ""
            if not is_prime_naive_division(i):
                negator = "not "
            print("The number {0} is {1}prime."
                  .format(i, negator))
        _debug = True

        if _perform_naive_big_trial:
            negator = ""
            if not is_prime_naive_division(prime_big_trial):
                negator = "not "
            print ("The number {0} is {1}prime."
                   .format(prime_big_trial, negator))

        print("")
        print("##### Starting wiki tests:")

        _debug = False
        for i in range(prime_loop_trial_count):
            negator = ""
            if not is_prime_wiki(i):
                negator = "not "
            print("The number {0} is {1}prime."
                  .format(i, negator))
        _debug = True

        if _perform_wiki_big_trial:
            negator = ""
            if not is_prime_wiki(prime_big_trial):
                negator = "not "
            print ("The number {0} is {1}prime."
                   .format(prime_big_trial, negator))

        print("")
        print("##### Starting Miller-Rabin tests:")

        _debug = False
        for i in range(prime_loop_trial_count):
            negator = ""
            if not is_prime_miller_rabin(i):
                negator = "not "
            print("The number {0} is {1}prime."
                  .format(i, negator))
        _debug = True

        negator = ""
        if not is_prime_miller_rabin(prime_big_trial):
            negator = "not "
        print ("The number {0} is {1}prime."
               .format(prime_big_trial, negator))

    except Exception as e:
        print(e)
