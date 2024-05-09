"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Ignoring Case

Instructions:

    Using the following code, compare the value of name with the string 'RoGeR' 
    while ignoring the case of both strings. Print true if the values are the same; 
    print false if they aren't. Next, perform a case-insensitive comparison between 
    the value of name and the string 'DAVE'.

Solution:

"""

my_string = 'RoGeR'
name = 'Roger'

if my_string == name:
    print(True)
else:
    print(False)

# using lower()
if my_string.lower() == name.lower():
    print(True)
else:
    print(False)

# more comprehensive approach than lower() or upper()
if my_string.casefold() == name.casefold():
    print(True)
else:
    print(False)
