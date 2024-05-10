"""

Created: 05/09/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Dictionaries > Labeled Numbers

Instructions:

    Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.

    numbers = {
        'high':   100,
        'medium': 50,
        'low':    10,
    }

    A high number is 100.
    A medium number is 50.
    A low number is 10.

Solution:

Key Concepts:
    When using dictionary.items(), you will need 
    to use tuple unpacking.  This is similar to 
    multiple or parallel Assigment in Ruby
    The number of variables on the right must equal
    the number on the left.

    tup = (2, 3)

    # here we unpack the tuple referenced by `tup` into the variables `num1` and `num2`
    num1, num2 = tup 

"""

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for k, v in numbers.items():
    print(f"A {k} number is {v}.")
