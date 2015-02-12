'''
advanced-topics-01.py - code to illustrate topics we discussed last week.
Created on Jan 19, 2015

@author: cleonard
'''
import csv

global contactList
contactList = []

# Data Structure Iteration:
def load_sample_data():
    strInput = None
    global contactList
    
    with open('./us-500.csv', 'rU') as f:
        csv_reader = csv.reader(f, quotechar='"')
        for row in csv_reader:
            # throw away header row:
            if csv_reader.line_num == 1: continue  # @ignorePep8
            contactList.append({"first_name": row[0],
                                "last_name": row[1],
                                "city": row[4]
                                })
    
load_sample_data()
print contactList

targetField = raw_input("What field should I search for? ")
targetValue = raw_input("What string should I search for in {0}? ".format(targetField))

for 
        
# List Comprehension:

# Lambda Expressions:

# Bitwise Operators:
