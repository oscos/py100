"""

Created: 03/08/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Checking Data Types

Instructions:

    Referring to the official Python documentation, how would you identify 
    the data type of the following values?

    23.5
    'Call me Ishmael.'
    False
    0
    None

Solution:

    The type() function returns an object’s type or class (which is an object itself).

    3. Data model 
    https://docs.python.org/3/reference/datamodel.html#data-model

    3.1. Objects, values and types¶
    https://docs.python.org/3/reference/datamodel.html#objects-values-and-types

"""

print(f"The type for value: 23.5 is {type(23.5 )}")
print(f"The type for value: 'Call me Ishmael.' is {type('Call me Ishmael.')}")
print(f"The type for value: False is {type(False)}")
print(f"The type for value: 0 is {type(0)}")
print(f"The type for value: None is {type(None)}")
