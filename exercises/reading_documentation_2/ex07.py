"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Find Substring

Instructions:

    Using the official Python documentation, can you determine how to 
    check whether a string contains a specific substring?

Solution:

    To check if sub is a substring or not, use the `in` operator:

    6.10.2. Membership test operations 
    - https://docs.python.org/3/reference/expressions.html#membership-test-operations

"""

substring = "fragilistic"
string = "supercalifragilisticexpialidocious"
result = substring in string

print(
    f"It\'s {result} that the string '{string}' contains the substring '{substring}'.")
