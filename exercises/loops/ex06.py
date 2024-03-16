"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Greet Your Friends

Instructions:

Your friends just showed up! Given the following list of names, 
use a for loop to greet each friend individually.

friends = ['Sarah', 'John', 'Hannah', 'Dave']

Expected output:

Hello, Sarah!
Hello, John!
Hello, Hannah!
Hello, Dave!

Solution:

Note: The `in` operator is a membership operator that tests whether a specified 
value is a member of a sequence.  It yields `True` if the value is 
found within the given sequence, otherwise it yields `False`

There is also `not in` membership operator.

"""
friends = ['Sarah', 'John', 'Hannah', 'Dave']

# options 1:
print("Using `range`:")
for i in range(len(friends)):
    print(f"Hello, {friends[i]}!")

print("")
print("Using `in`:")
for friend in friends:
    print(f"Hello, {friend}!")
