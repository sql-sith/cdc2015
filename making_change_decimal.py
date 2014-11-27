'''
Shows a solution for the challenge exercise asking you to calculate change. 
Created on Oct 29, 2014

@author: chris
'''

from math import trunc
from reportlab.lib.validators import isNumber
from decimal import *

raw_transaction_amount = raw_input("What is the cost of the sale? ")
if isNumber(raw_transaction_amount):
    transaction_amount = Decimal(raw_transaction_amount).quantize(Decimal('0.01'))
    if Decimal(raw_transaction_amount) <> transaction_amount:
        print("No funny money allowed! Let's round to a sane number.")
    print ("OK, so that's %.2f for the sale." % transaction_amount)
else:
    print("Yeah, that's not even a number. I give up.")
    exit(1)

print("")

raw_cash_amount = raw_input("How much cash was tendered? ")
if isNumber(raw_cash_amount):
    cash_amount = Decimal(raw_cash_amount).quantize(Decimal('.01'))
    if Decimal(raw_cash_amount) <> cash_amount:
        print("Really??!? They gave you THAT??!?\n" +
              "I am going to pretend things were a bit more normal.")
    print("That's %.2f for the cash tendered." % cash_amount)
else:
    print("Srsly? That can't be right. I'm outta here.")
    exit(2)

print("")

change_required = cash_amount - transaction_amount
if change_required < 0:
    print("Sorry to tell you this, but they stiffed you. Keep what you got, and call it good.")
    exit(3)
else:
    print("That means I need to figure out how to come up with %.2f in change.\n" % change_required)
    print("Hmm, let me think...")

# how many $20 bills?
twenties = trunc(change_required / Decimal('20'))
change_required -= twenties * Decimal('20')

# how many $10 bills?
tens = trunc(change_required / Decimal('10'))
change_required -= tens * Decimal('10')

# how many $5 bills?
fives = trunc(change_required / Decimal('5'))
change_required -= fives * Decimal('5')

# how many $1 bills?
ones = trunc(change_required / Decimal('1'))
change_required -= ones

# how many quarters?
quarters = trunc(change_required / Decimal('0.25'))
change_required -= quarters * Decimal('0.25')

# how many dimes?
dimes = trunc(change_required / Decimal('0.10'))
change_required -= dimes * Decimal('0.10')

# how many nickels?
nickels = trunc(change_required / Decimal('0.05'))
change_required -= nickels * Decimal('0.05')

# finally, how many pennies
pennies = trunc(change_required / Decimal('0.01'))
change_required -= pennies * Decimal('0.01')

print("")
print("I think I have it!\n")
print(("To make %.2f in change from a sale of %.2f when %.2f was tendered,\n" +
        "use the following currency:") % (cash_amount - transaction_amount, transaction_amount, cash_amount))
print("")

if twenties > 0:
    if twenties > 1:
        currency = "20-dollar bills"
    else:
        currency = "20-dollar bill"
    print("\t%d %s" % (twenties, currency))

if tens > 0:
    if tens > 1:
        currency = "10-dollar bills"
    else:
        currency = "10-dollar bill"
    print("\t%d %s" % (tens, currency))

if fives > 0:
    if fives > 1:
        currency = "5-dollar bills"
    else:
        currency = "5-dollar bill"
    print("\t%d %s" % (fives, currency))

if ones > 0:
    if ones > 1:
        currency = "1-dollar bills"
    else:
        currency = "1-dollar bill"
    print("\t%d %s" % (ones, currency))

if quarters > 0:
    if quarters > 1:
        currency = "quarters"
    else:
        currency = "quarter"
    print("\t%d %s" % (quarters, currency))

if dimes > 0:
    if dimes > 1:
        currency = "dimes"
    else:
        currency = "dime"
    print("\t%d %s" % (dimes, currency))

if nickels > 0:
    if nickels > 1:
        currency = "nickels"
    else:
        currency = "nickel"
    print("\t%d %s" % (nickels, currency))

if pennies > 0:
    if pennies > 1:
        currency = "pennies"
    else:
        currency = "penny"
    print("\t%d %s" % (pennies, currency))
