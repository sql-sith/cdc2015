
# For part 2, this is important:
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#
# This also is helpful:
# https://docs.python.org/2/howto/regex.html 
from datetime import datetime
import re

print('Trying with % format operator first...\n')

print('Trying to print:\n2014-1-2 3:04:05 AM')
my_datetime = datetime(2014, 1, 2, 3, 4, 5)
if my_datetime.hour < 12:
    sAMPM = 'AM'
else:
    sAMPM = 'PM'
print("%02d-%01d-%01d %01d:%02d:%02d %s\n" % (
    my_datetime.year,
    my_datetime.month,
    my_datetime.day,
    my_datetime.hour % 12,
    my_datetime.minute,
    my_datetime.second,
    sAMPM))

print('Let\'s verify that this works with PM hours...')
print('Trying to print:\n2014-1-2 3:04:05 PM')
my_datetime = datetime(2014, 1, 2, 15, 4, 5)
if my_datetime.hour < 12:
    sAMPM = 'AM'
else:
    sAMPM = 'PM'
print("%02d-%01d-%01d %01d:%02d:%02d %s\n" % (
    my_datetime.year,
    my_datetime.month,
    my_datetime.day,
    my_datetime.hour % 12,
    my_datetime.minute,
    my_datetime.second,
    sAMPM))

print("That works, but it's a little clunky.\n")
print("Here's a more concise way, if you allow the leading zeros:")
print(my_datetime.strftime("%Y-%m-%d %I:%M:%S %p\n"))
print("Here's a hack that gets rid of the leading zeros, but it works in Linux only!")
print(my_datetime.strftime("%Y-%-m-%-d %-I:%M:%S %p\n"))
print("And here is an answer that uses pattern-based (regex-based) replacement:")
p = re.compile('( |-)0')
print(p.sub('\\1', my_datetime.strftime("%Y-%m-%d %I:%M:%S %p")))
print("   or ...")
print(p.sub(r'\1', my_datetime.strftime("%Y-%m-%d %I:%M:%S %p")))
