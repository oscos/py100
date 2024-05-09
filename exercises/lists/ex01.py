"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > First Element

Instructions:

    Write a function that returns the first element of a list provided as an argument. For example:

    print(first(['Earth', 'Moon', 'Mars']))  # Earth

    Be sure to handle the case where the input list is empty.

Solution:

    When we attempt to access an element from an empty list, python will raise an IndexError.
    Therefor its good practice to first check for this condition.
    In python, empty lists are falsy.  We can test a list for truthiness to avoid raising an error.

"""


# Solution 1
def first(lst):
    if lst:
        return lst[0]
    else:
        return None


print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # None
