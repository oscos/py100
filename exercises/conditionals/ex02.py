"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Yes? No? Part 1

Instructions:

The code provided below randomly initializes random_number to either 0 or 1 
each time it is executed.

Write an if statement that prints Yes! if random_number is 1, and No. 
if random_number is 0.

import random
random_number = random.randint(0, 1)

Solution:

"""

import random
random_number = random.randint(0, 1)

print(f"random_number is: {random_number}")

if random_number:
    print("Yes!")
else:
    print("No.")
