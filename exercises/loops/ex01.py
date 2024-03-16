"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Loop and Print

Instructions:

    Add some code inside the following for loop to print the current value 
    of num on each iteration. Before you execute the code: What sequence 
    of numbers do you expect to be printed?

    for num in range(0, 11, 2):
        pass # include your code here

Solution:

    We can use the `print()` statement to print the current value of num 
    on each iteration. 

    The code will print the numbers from 0 to 10 (inclusive), incrementing 
    by two on each iteration.

    The range function generates a sequence staring from the first numeric
    argument `0` (inclusive), and stopping before reaching the second numeric 
    argument `11` (exclusive), and incrementing by the third argument `2` on 
    each iteration. 

"""

for num in range(0, 11, 2):
    # pass # include your code here
    print(num)  # 0, 2, 4, 6, 8, 10
