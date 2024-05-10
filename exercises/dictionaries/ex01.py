"""

Created: 05/08/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Dictionaries > 

Instructions:

    Create a dictionary that contains the following data, and assign it to a variable named car.

    type	color	mileage
    sedan	blue	80000


Solution:

KeyPoints: 
    while we can use many types as dictionary keys (strings, numbers, booleans, floats, and tuples), 
    they should be immutable and hashable.

    Any hashable type is immutable, but not all immutable types are hashable
    i.e. tuple is immutable but if it contains a list, it is not hashable.
            this is becuase lists are mutable
"""

car = {
    "type": "sedan",
    "color": "blue",
    "mileage": "80_000",
}

print(car)
