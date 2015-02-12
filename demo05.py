'''
Created on Dec 23, 2014

@author: cleonard
'''
from reportlab.lib.validators import isInt


def is_prime(num):
    retval = True
    bad_input = False

    # check that num is integer >= 0
    if isInt(num):
        num = int(num)
    else:
        bad_input = True

    if not bad_input:
        if num < 0:
            bad_input = True

    if bad_input:
        e = Exception("Bad argument detected. " +
                      "Please pass in a non-negative integer.")
        raise(e)
    # =======================================================================
    # if num <= 3:
    #     return(num >= 2)
    # =======================================================================

    if num in (0, 1):
        retval = False
    elif num == 2:
        retval = True
    elif num % 2 == 0:
        retval = False
    else:
        for factor in range(3, int(num ** 0.5) + 1, 2):
            if num % factor == 0:
                retval = False
                break

    return(retval)


global _debug
_debug = True

if __name__ == '__main__':
    print("Gimme a number*, bub.")
    print("")
    prime_candidate = raw_input("* but it had better be a non-negative integer! ")

    p = is_prime(prime_candidate)

    print("{0} is prime: {1}".format(prime_candidate, p))
