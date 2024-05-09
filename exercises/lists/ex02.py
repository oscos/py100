"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Last Element

Instructions:

    Write a function that returns the last element of a list provided as an argument. 
    
    For example:

    print(last(['Earth', 'Moon', 'Mars']))  # Mars

    Be sure to handle the case where the input list is empty.

Solution:

    When we attempt to access an element from an empty list, python will raise an IndexError.
    Therefor its good practice to first check for this condition.
    In python, empty lists are falsy.  We can test a list for truthiness to avoid raising an error.

"""


def last(lst):
    if lst:
        return lst[-1]
    else:
        return None


print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))  # None
