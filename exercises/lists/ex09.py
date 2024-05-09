"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Travel

Instructions:

    The destinations list contains a list of travel destinations.

    
    destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                    'Rome', 'Aruba', 'Paris', 'Bora Bora',
                    'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                    'New York City']

    Write a function that, without using the built-in in operator, 
    checks whether a specific destination is included within destinations. 
    For example: When checking whether 'Barcelona' is contained in destinations, 
    the expected output is True, whereas the expected output for 'Nashville' is False.


    contains('Barcelona', destinations)  # True
    contains('Nashville', destinations)  # False

Solution:

"""


def contains(item, alist):
    counter = len(alist)
    flag = False
    while counter > 0:
        current_element = (alist[counter - 1])
        if current_element == item:
            flag = True
        counter -= 1
    return flag


destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']


print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
