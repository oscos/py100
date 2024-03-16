"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Take Two

Instructions:

    Write a for loop that iterates over the integers from 1 to 100 and 
    prints the result of multiplying each integer by 2.

Solution:

    To loop over the integers 1 to 100, we can use the `range` built-in function
    within a `for` loop. The `range` function takes three integer arguments:
    `start`, `stop`, and `step`.  
    If the `start` argument is ommited, it defaults to 1.  
    If the `step` argument is ommited, it defaults to 1.  
    Note, that `start` argument is inclusive, and the `stop` argument is exclusive.
"""

for i in range(1, 101):
    product = i * 2
    print(product)
