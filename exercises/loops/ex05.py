"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Looping over List Elements

Instructions:

Using the code below as a starting point, write a while loop that prints 
the elements of lst at each index and terminates after printing the last 
element of the list.

lst = [1, 3, 7, 15]
index = 0

Solution:

"""

lst = [1, 3, 7, 15]
index = 0

print("Using a while loop")
while index < len(lst):
    print(f"index {index}: => {lst[index]}")
    index += 1


# Further exploration:
# What would the code output if lst is empty? Why is that?
"""
If `lst` is empty, the while loop would not execute with no output.  
This is because `while` loop only executes
when the condition is `True`.  Since len(lst) returns `0`, the condition
`index < len(lst)` returns `False` and the loop terminitates without 
printing anything.
"""
