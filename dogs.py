'''
dogs.py

Created on Jan 20, 2015

@author: cleonard
'''

petID = (0, 1)
petName = ("Gypsie", "Pocahontas")
petType = ("Kind of a dachsund", "Finnicky cat")
petGender = "Female"
petSize = "XS"
petOwnerPrimaryFirstName = "Margie"
petOwnerPrimaryLastName = "Leonard"
petOwnerOtherFirstName = "Chris"
petOwnerOtherLastName = "Leonard"


gypsie = {
    "petName": "Gypsie",
    "petType": "Awesome",
    "lastRabiesShot": "2014-11-05",
    "OwnerFirstName": "Margie",
    "OwnerLastName": "Leonard"
    }

poco = {
    "petName": "Pocahontas",
    "petType": "Kitty cat",
    "OwnerFirstName": "Margie",
    "OwnerLastName": "Leonard"
    }


def getPetAttribute(pet, attributeName):
    try:
        return(pet[attributeName])
    except:
        return("Invalid attribute name {0}.".format(attributeName))


print(getPetAttribute(gypsie, "petName"))
print(getPetAttribute(poco, "petType"))
print(getPetAttribute(poco, "lastRabiesShot"))

