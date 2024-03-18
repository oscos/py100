"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Yes? No? Part 2 (conditional expression)

Instructions:

Rewrite your code from the previous exercise to use a ternary expression.

Solution:

"""


import random
random_number = random.randint(0, 1)

print(f"random_number is: {random_number}")

print("Yes!" if random_number else "No.")
