'''
Shows a solution for the challenge exercise asking you to calculate change. 
Created on Oct 29, 2014

@author: chris

bug test cases:
- case PI: sale=3.14159265359, tendered=123.4567
- case PIRROUNDED: sale=3.14, tendered=123.46
- case SODA: sale=1.35, tendered=1.50
'''

from math import trunc
from reportlab.lib.validators import isNumber

raw_transaction_amount = raw_input("What is the cost of the sale? ")

# debug: step into isNumber() ?
if isNumber(raw_transaction_amount):
    literal_transaction_amount = float(raw_transaction_amount)
    transaction_amount = round(literal_transaction_amount, 2)
    if literal_transaction_amount <> transaction_amount:
        print("No funny money allowed! Let's round to a sane number.")
    print ("OK, so that's %.2f for the sale." % transaction_amount)
else:
    print("Yeah, that's not even a number. I give up.")
    exit(1)

print("")

raw_cash_amount = raw_input("How much cash was tendered? ")
if isNumber(raw_cash_amount):
    literal_cash_amount = float(raw_cash_amount)
    cash_amount = round(literal_cash_amount, 2)
    if literal_cash_amount <> cash_amount:
        print("Really??!? They gave you THAT??!? " +
              "I am going to pretend things were a bit more normal.")
    print("That's %.2f for the cash tendered." % cash_amount)
else:
    print("Srsly? That can't be right. I'm outta here.")
    exit(2)

print("")

change_required = cash_amount - transaction_amount
if change_required < 0:
    print("Sorry to tell you this, but they stiffed you.\n"+
          "Keep what you got, and call it good, or call the police.")
    exit(3)
else:
    print("That means I need to figure out how to come up with %.2f in change.\n" % change_required)
    print("Hmm, let me think...")

# how many $20 bills?
twenties = trunc(change_required / 20)
change_required -= twenties * 20

# how many $10 bills?
tens = trunc(change_required / 10)
change_required -= tens * 10

# how many $5 bills?
fives = trunc(change_required / 5)
change_required -= fives * 5

# how many $1 bills?
ones = trunc(change_required / 1)
change_required -= ones

# how many quarters?
quarters = trunc(change_required / 0.25)
change_required -= quarters * 0.25

# how many dimes?
dimes = trunc(change_required / 0.10)
change_required -= dimes * 0.10

# how many nickels?
nickels = trunc(change_required / 0.05)
change_required -= nickels * 0.05

# finally, how many pennies
pennies = trunc(change_required / 0.01)
change_required -= pennies * 0.01

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
