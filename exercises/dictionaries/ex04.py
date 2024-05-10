"""

Created: 05/09/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Dictionaries > What Color?

Instructions:

    Using the following code, select and print the value 'blue' from the car object:

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

if 'color' in car:
    color = car['color']
    print(color)


# Per LS Solution
print(car.get('mileage'))  # => None
print(car.get('gpm', 'N/A'))  # => 'N/A'
