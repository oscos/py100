"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Check Prefix

Instructions:

    Write a function that checks whether a string starts with a specific prefix.

    print(starts_with("launch", "la"))   # True
    print(starts_with("school", "sah"))  # False
    print(starts_with("school", "sch"))  # True

Solution:

"""


# Solution 1
def starts_with(str1, str2):
    return str1.startswith(str2)


# Solution 2
def starts_with(str1, str2):
    substring_length = len(str2)
    return str1[:substring_length] == str2


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
