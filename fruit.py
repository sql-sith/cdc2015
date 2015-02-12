'''
Created on Jan 20, 2015

@author: cleonard
'''


class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, _name, _color, _flavor, _poisonous):
        self.name = _name
        self.color = _color
        self.flavor = _flavor
        self.poisonous = _poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
print(len(lemon.color))