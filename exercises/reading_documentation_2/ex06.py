"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Argument Signatures

Instructions:

    How many arguments does the str.join method expect? 
    What happens if you call it with fewer or more arguments?

Solution:

Invoking join with too many or without any arguments will raise a TypeError.

Definition from Python Docs

Return a string which is the concatenation of the strings in iterable.
A TypeError will be raised if there are any non-string values in iterable,
including bytes objects. The separator between elements is the string
providing this method.

https://docs.python.org/3/
Library Reference - https://docs.python.org/3/library/index.html
Text Sequence Type — str - https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
str.join(iterable) - https://docs.python.org/3/library/stdtypes.html#str.join

"""

letters = "abc"
print(" ".join(letters))
