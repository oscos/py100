"""

Created: 05/09/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Dictionaries > Divided by Two

Instructions:

    Use a for loop to iterate over the numbers dictionary and return a list 
    containing each number divided by 2 as an integer. The result should be 
    truncated to an integer. Assign the returned list to a variable named 
    half_numbers and print its value using print.

    numbers = {
        'high':   100,
        'medium': 50,
        'low':    25,
    }

    Expected Result: [50, 25, 12]

Solution:

"""

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}


# Solution 1:
half_numbers = []
for number in numbers:
    half_numbers.append(numbers[number] // 2)
print(half_numbers)

# Solution 2:
half_numbers = []
for number in numbers.values():
    half_numbers.append(number // 2)
print(half_numbers)

# Solution 3:
half_numbers = [number // 2 for number in numbers.values()]
print(half_numbers)
