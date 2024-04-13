"""

Created: 04/05/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Functions > Locale Part 2

Instructions:

Similar to the previous exercise, write a function that extracts the 
region code from a locale. For example:

Solution:

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

"""


def extract_region(str):
    return str.split('_')[1].split('.')[0]


print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR
