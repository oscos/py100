"""

Created: 04/05/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Functions > Transformation

Instructions:

Use Python's string methods on the string 'Captain Ruby' 
to create a string with the value 'Captain Python'.

Solution:

"""

captain_name = 'Captain Ruby'
method_one = captain_name.replace('Ruby', 'Python')
print(f"Using str.replace method: {method_one}")
print('')


captain_name = 'Captain Ruby'
method_two = captain_name[0:8] + 'Python'
print(f"Using slicing method: {method_two}")
print('')


captain_name = 'Captain Ruby'
method_three = captain_name.split()[0] + ' Python'
print(f"Using str.split method: {method_three}")
print('')
