"""
  Created: 03/06/2024
  Updated:
  Launch School - Intro to Python
  PY100 - Python Basics > Reading Documentation 1 > Right Justifying Strings

  Instructions:

  Use the Python documentation for the str class to determine which method can be used to right justify a str object.

  Solution:

  str.rjust(width[, fillchar])¶
  Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).

"""

original_string = "Python" 
width_padding = 10 
fill_character = '*' 
right_justified_string = original_string.rjust(width_padding)
right_justified_string_with_character_padding = original_string.rjust(width_padding, fill_character)

print(f"original_string: '{original_string}'")
print(f"right_justified_string: '{right_justified_string}'")
print(f"right_justified_string_with_character_padding: '{right_justified_string_with_character_padding}'")
