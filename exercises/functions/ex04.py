"""

Created: 03/17/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Functions > Squared Number

Instructions:

    Write a function that accepts a single argument, a number, and returns 
    the result of multiplying its argument by an exponent of 2 (also known 
    as squaring the number or raising the number to the power of 2).

    squared_number(3)   # 9

Solution:

"""


def squared(num):
    result = num**2
    return result


print(squared(4))
