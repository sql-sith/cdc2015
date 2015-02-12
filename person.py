'''
An implementation of the "Persons of Interest" challenge exercise.
Created on Feb 10, 2015

@author: sql.sith
'''

from datetime import date


class Person(object):

    species = 'Homo sapiens'

    def __init__(self, first_name, last_name, city, state_or_province,
                 country, birth_date, email_address):

        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state_or_province = state_or_province
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address

    def has_email_address(self):
        if self.email_address is None:
            return(False)
        else:
            return(True)

    def get_formatted_name(self):
        return(self.first_name + ' ' + self.last_name)

    def get_age(self):
        today = date.today()
        age = None

        if today.month > self.birth_date.month:
            age = today.year - self.birth_date.year
        elif today.month < self.birth_date.month:
            age = today.year - self.birth_date.year - 1
        else:  # same month
            if today.day >= self.birth_date.day:
                age = today.year - self.birth_date.year
            else:  # same month, but no birthday yet
                age = today.year - self.birth_date.year - 1

        return(age)

# main
chris = Person('Chris', 'Leonard', 'Cedar Rapids', 'IA',
               'US', date(1964, 12, 25), 'chris@databaseguy.com')
charlie = Person('Charles', 'Coleman', 'Bertram', 'IA',
                 'US', date(1889, 12, 25), None)

print(chris.get_formatted_name())
print(chris.has_email_address())
print(chris.get_age())

print(charlie.get_formatted_name())
print(charlie.has_email_address())
print(charlie.get_age())

print("Chris is a {0}.".format(Person.species))
