"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Is Empty or Blank?

Instructions:

    Write an is_empty_or_blank function to determine whether a string 
    is either empty or consists entirely of spaces. For example:


    print(is_empty_or_blank('mars'))  # False
    print(is_empty_or_blank('  '))    # True
    print(is_empty_or_blank(''))      # True
    
Solution:
    You can use python's logical operator `or`
    Python will search the conditions for the first truthy value
    so even if the first part of statement evaluates to False,
    python will search other part of the statement.

"""


def is_empty_or_blank(str):
    return not str or str.isspace()


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True


# LS Solution

# def is_empty_or_blank(s):
#     return s.strip(' ') == ''

# def is_empty_or_blank(s):
#     return len(s.strip(' ')) == 0

# def is_empty_or_blank(s):
#     return not s.strip(' ')
