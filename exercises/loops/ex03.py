"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Triple Greeting

Instructions:

    Write a loop that prints the value of the greeting variable three times.

    greeting = 'Aloha!'

Solution:

"""

greeting = 'Aloha!'

print("Using for loop:")
for _ in range(3):
    print(greeting)

print("")

print("Using while loop:")
counter = 0
while counter < 3:
    print(greeting)
    counter += 1
