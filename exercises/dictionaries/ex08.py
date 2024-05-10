"""

Created: 05/09/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Dictionaries > Which Collection?

Instructions:

    Rewrite car as a nested list containing the same key/value pairs.

    car = {
        'type':  'sedan',
        'color': 'blue',
        'year':  2003,
    }

Solution:

"""

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

car_list = [[k, v] for k, v in car.items()]

# print(car_list)
# print(car_list[0])
print(car_list[0][1])

# car_list = [
#     ['type', 'sedan'],
#     ['color', 'blue'],
#     ['year', 2003],
# ]
# print(car_list)
