'''
Implementation of "Persons of Interest" challenge question.

Created on Feb 9, 2015.
@author: sql.sith (chris leonard)
'''
from datetime import date
import pickle
from os.path import os


class Person(object):
    # class variables would go here
    species = 'Homo sapiens'

    # ========================================================================
    # def __init__(self, first_name, last_name, email_address, city,
    #              state_or_province, country, birth_date):
    #
    # yeah, that would work, but the following is easier.
    # see also args/kwargs discussed at
    #     https://docs.python.org/dev/tutorial/controlflow.html
    #     (searh for * and ** on that page)
    # ========================================================================
    def __init__(self, **kwargs):

        try:
            self.first_name = kwargs["first_name"]
            self.last_name = kwargs["last_name"]
            self.email_address = kwargs["email_address"]
            self.city = kwargs["city"]
            self.state_or_province = kwargs["state_or_province"]
            self.country = kwargs["country"]
            self.birth_date = kwargs["birth_date"]
        except KeyError:
            __REQUIRED_ARGS_MISSING = Exception(
                'You must supply all required parameters ' +
                '(first_name, last_name, email_address, city,' +
                'state_or_province, country, birth_date).')
            raise(__REQUIRED_ARGS_MISSING)

    def get_formatted_name(self):
        return(self.first_name + ' ' + self.last_name)

    def get_age(self):
        today = date.today()
        if (today.month > self.birth_date.month or
            (today.month == self.birth_date.month and
             today.day >= self.birth_date.day)):
            return(today.year - self.birth_date.year)
        else:
            return(today.year - self.birth_date.year - 1)

    def has_email_address(self):
        if self.email_address is None:
            return False
        else:
            return True

    def get_species(self):
        return(self.species)

# main:
line = '-' * 50
file_name = 'people.dat'

if __name__ == '__main__':
    grandpaColeman = Person(
        first_name='Charles',
        last_name='Coleman',
        email_address=None,
        city='Bertram',
        state_or_province='IA',
        country='US',
        birth_date=date(1889, 12, 25))

    chris = Person(
        first_name='Chris',
        last_name='Leonard',
        email_address='chris@databaseguy.com',
        city='Cedar Rapids',
        state_or_province='IA',
        country='US',
        birth_date=date(1964, 12, 25))

    people = [chris, grandpaColeman]

    # open file for binary write mode:
    f = open(file_name, 'wb')
    print('File opened for writing.')

    # we'll add up the size of each IO in calculated_file_size:
    calculated_file_size = 0

    print('Here is some information about our people:')
    print(line)
    for person in people:
        # basic info dump:
        print(person.get_formatted_name())
        print(person.has_email_address())
        print(person.get_age())
        print(line)

        # formatted info dump:
        if person.has_email_address():
            email_possession = ' has '
        else:
            email_possession = ' does not have '
        msg = (person.get_formatted_name() + ' is ' + str(person.get_age()) +
               ' years old and' + email_possession + 'an email address.')
        print(msg)
        print('Also, {0} is a member of the species "{1}".'
              .format(person.first_name, person.get_species()))

        # store record into our file:
        pickle.dump(person, f, 2)
        calculated_file_size += len(pickle.dumps(person, 2))
        print(line)

    # close the file so we can open it to read it:
    f.close()
    print('File closed.')
    print(line)

    # Get actual file size from the OS:
    actual_file_size = os.path.getsize(file_name)
    print('File size calculated by program is {0} bytes.'
          .format(calculated_file_size))
    print('Actual file size reported by OS is {0} bytes.'
          .format(actual_file_size))

    print(line)

    # reset the people list:
    people = []
    f = open(file_name, 'rb')
    print('File opened for reading and people list emptied.')
    print(line)

    while True:
        try:
            person = pickle.load(f)
            people.append(person)
        except (EOFError):
            break

    for person in people:
        print(person.get_formatted_name())

    print(line)
    f.close()
    print('File closed.')
