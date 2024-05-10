"""

Created: 05/09/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Dictionaries > Broken Odometer

Instructions:

    Using the following code, delete the 'mileage' key and its associated value from car.

    car = {
        'type':    'sedan',
        'color':   'blue',
        'mileage': 80_000,
        'year':    2003,
    }

Solution:

"""


car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

# # Solution 1
# if 'mileage' in car:
#     del car['mileage']

# print(car)

# Solution 2
# https://docs.python.org/3/library/stdtypes.html#typesmapping
# https://www.w3schools.com/python/ref_dictionary_pop.asp
car.pop('mileage', None)
print(car)
