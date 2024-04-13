"""

Created: 04/05/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Functions > Locale Part 1

Instructions:
Write a function that extracts the language code from a locale. 
A locale is a combination of a language code, a region, and usually 
also a character set, e.g en_US.UTF-8.

Solution:

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

"""


def extract_language(str):
    first_part = str.split('_')[0]
    return first_part


print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko
