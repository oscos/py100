"""

Created: 05/09/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Dictionaries > Checking Key Existence

Instructions:

    Check whether the keys 'name' and 'grade' exist in the following dictionary:

    student = {
        'id': 123,
        'grade': 'B',
    }

Solution:

"""

student = {
    'id': 123,
    'grade': 'B',
}

# solution 1
if 'grade' in student:
    print(True)
else:
    print(False)

if 'name' in student:
    print(True)
else:
    print(False)


# LS Solution
print('grade' in student)
print('name' in student)
