"""
One implementation of a solution to the rusty_calculator challenge.
Created on Feb 10, 2015

@author: sql.sith
"""


def answer(instring):
    """ calculate and return answer for arithmetic stored in instring.
        instring will hold integers, + and * symbols only.
    """
    digits = '0123456789'
    star = '*'
    plus = '+'

    retval = ''
    held_stars = 0
    held_plusses = 0

    for c in instring:
        if c in digits:
            # always print digits immediately, since we want largest
            # lexicographical string, and since we know that all
            # numbers are single-digit, and that the digit strings
            # are larger than the other two possible characters
            # (which are "+" and "*"):
            #
            # notice also that since the instring has infix notation,
            # the final character will be a digit:
            retval += c
        elif c == star:
            # glob the stars together to go at the end of each
            # multiplicative term:
            held_stars += 1
        elif c == plus:
            # glob the plusses together for the very end of the retval...
            held_plusses += 1
            # ...but print stars when you find a plus, since plusses will
            # separate multiplicative terms:
            for _ in range(held_stars):
                retval += star
            held_stars = 0

    # at the end, we may have stars, which we need to print first to make
    # the RPN notation evaluate correctly:
    for _ in range(held_stars):
        retval += star

    # at the end, we may have plusses, which we need to print last to make
    # the RPN notation evaluate correctly:
    for _ in range(held_plusses):
        retval += plus

    # note: at the end, we will not have digits, since they will always be
    # immediately printed to the retval.
    return retval


print(answer('2+3*2'))
print(answer('2*4*3+9*3+5'))
