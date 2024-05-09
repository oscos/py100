"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Equality

Instructions:

    Predict the output of the code shown below. When you run the code, 
    do you see what you expected? Why or why not?

    list1 = [2, 6, 4]
    list2 = [2, 6, 4]

    print(list1 == list2)


Solution:

    The `==` operator returns `True` if the two list literals being compared
    have the same elements in the same order. Otherwise it returns `False`.

    The `is` operator returns `True` if the two list literals being compared 
    are the same object in memory. Otherwise it returns `False`.

"""

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)  # True
print(list1 is list2)  # False
