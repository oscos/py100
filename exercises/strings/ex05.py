"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Contains Character

Instructions:

    Write code that checks whether the string char_sequence contains the character x.

Solution:
     Use the `in` keyword which allows us to search for character or substring
     in iterables such as string and list

"""

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

flag = False
for letter in char_sequence:
    if letter.casefold() == 'x'.casefold():
        flag = True
print(flag)


# LS solution:
print('x' in char_sequence)   # True

# Note that the in statement can iterate through the entire string without having
# to specifically iterate one by one.
