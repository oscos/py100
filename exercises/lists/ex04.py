"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Alphabet

Instructions:

    Split the string alphabet into a list of characters.

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

Solution:
    While you would think the split('') method would work, however
     this will simply raises a ValueError: Empty seperator
     because `split()` needs an actual delimiter as an argument to work
     and `''` is not a delimiter.
    Instead you can simple wrap the string with a list constructor `list()`

"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet_list = list(alphabet)

print(alphabet_list)
