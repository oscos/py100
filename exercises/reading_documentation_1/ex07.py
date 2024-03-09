"""

Created: 03/08/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Out Of Bounds

Instructions:

    What happens if we take the list ['fish', 'and', 'chips'] and try to access 
    the element at index position 10? First try to determine what will happen by 
    consulting the documentation, then verify your understanding in the Python REPL

Solution:

    The code raises the error: IndexError: list index out of range. 
    This occurs when the given index is invalid.

"""

meal = ['fish', 'and', 'chips']
word = meal[10]
print(word)
