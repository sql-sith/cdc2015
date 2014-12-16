'''
Shows a way to complete the challenge exercises for week 3. Well, two ways, actually.
Author: Chris Leonard
'''

sName = "Chris Leonard"
iShoeSize = 12
fChildCount = 4.0
bMarried = True
 
#===============================================================================
# print(dir())
# print(locals())
# print(globals())
#===============================================================================
var = dict(locals())
 
for v in var:
    if v[0:2] <> '__':
        print v
        print eval(v)
        print type(eval(v)).__name__
        print ''

# here's a way to do it using list comprehension:
for x in [x for x in set(locals()) if x[0:2] <> '__']:
    print x
    print eval(x)
    print type(eval(x)).__name__
    print ""

maxIndex = var.__len__()

for i in range(maxIndex):
    print var.keys()[i]
    print var.values()[i]
    print type(var.values()[i]).__name__
    print ""
        