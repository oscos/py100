"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Loop on Command

Instructions:

Modify the following code so the loop continues iterating until 
the user inputs 'yes'.

while True:
    print('Should I stop looping?')
    answer = input()

Solution:

"""

while True:
    print('Should I stop looping?')
    answer = input()

    if answer == 'Yes':
        break

    print("Enter 'Yes' to exit loop.")
