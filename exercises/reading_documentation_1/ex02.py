"""
  Created: 03/06/2024
  Updated:
  Launch School - Intro to Python
  PY100 - Python Basics > Reading Documentation 1 > Finding Documentation
  Instructions:

  Instructions:

  Determine whether Python has a method to lowercase a string, for example converting 'Aloha, World!' into 'aloha, world!.

  Solution:

  https://docs.python.org/3/library/stdtypes.html#str.lower

  str.lower()
  Return a copy of the string with all the cased characters [4] converted to lowercase.

  The lowercasing algorithm used is described in section 3.13 ‘Default Case Folding’ of the Unicode Standard.
"""

greeting = 'Aloha, World!'
print(greeting.lower())
