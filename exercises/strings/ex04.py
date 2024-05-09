"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Multiline String

Instructions:
    
    How can you assign the following rhyme to a single variable while preserving the line break?

    A pirate I was meant to be!
    Trim the sails and roam the sea!

Solution:

"""

my_string = '''A pirate I was meant to be!
Trim the sails and roam the sea!'''
print("Using \''' triple single qoutes:")
print(my_string)

print("")

my_other_string = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'
print("Using \\n espace sequence:")
print(my_other_string)
