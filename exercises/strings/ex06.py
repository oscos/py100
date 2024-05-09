"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Is Empty?

Instructions:

    Write a function that checks whether a string is empty or not. For example:

    print(is_empty('mars'))  # False
    print(is_empty('  '))    # False
    print(is_empty(''))      # True

Solution:
    Empty strings are considered falsy

"""


def is_empty(str):
    result = False
    if not str:
        result = True
    return result


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True


# LS Solution:
def ls_is_empty(s):
    return not s
