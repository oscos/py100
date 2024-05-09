"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Count Substrings

Instructions:

    Write a function that counts the number of occurrences of a substring in a string.

Solution:

"lemon lemon lemon"
 0   5 # lemon
  1    6 # emon_
   2    7 # mon_l
    3    8
     4    9
      5    10
       6    11
        7    12
         8    13
          9    14
           10    15
            11    16
             12    17
"""


# Solution 1:
def count_substrings(str1, str2):
    return str1.count(str2)


# Solution 2:
def count_substrings(string, substring):
    counter = 0

    string_length = len(string)
    substring_length = len(substring)

    # print(string_length, substring_length)
    for i in range(string_length - substring_length + 1):
        # print(i, i+substring_length)
        current_substring = string[i:i+substring_length]
        # print(current_substring)
        if current_substring == substring:
            counter += 1
    return counter


print(count_substrings("lemon lemon lemon", "lemon"))  # 3
print(count_substrings("laLAlaLA", "la"))  # 2
print(count_substrings("launch", "uno"))  # 0
