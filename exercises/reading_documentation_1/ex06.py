"""

Created: 03/08/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Finding Index

Instructions:

    Given a list: 
    
    fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

    How would you determine the index of the fruit "cherry" in this list?

    Refer to the official Python documentation on lists to assist with your answer.

Solution:

    You can use the `index` list method to return the first occurance of the specified value.  
    
    Note: If the value is not found within the list, the `index` list method will 
    raise a `ValueError`. Therefore, its often a good idea to wrap the code inside a 
    try/catch statement.

    You can find information on this by navigating over to: 
    https://docs.python.org/3/library/stdtypes.html#list 

    Locate the Common link:

    HERE: https://docs.python.org/3/library/stdtypes.html#typesseq-common

    OR HERE: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

"""

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

try:
    fruit_selection = 'cherry'
    fruit_selection_index = fruits.index(fruit_selection)
    print(f"The index for {fruit_selection} is {fruit_selection_index}")
except ValueError:
    print(f"{fruit_selection} was not found")
