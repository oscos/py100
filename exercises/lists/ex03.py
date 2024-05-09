"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Add + Delete

Instructions:

    We are given the following list of energy sources.

    energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

    Write some code to remove 'fossil' from the list, 
    then add 'geothermal' to the end of the list.

Solution:

"""

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# Solution 1
# When we attempt to access an element that does not exists in a list,
# python will raise an ValueError. Therefor its good practice to first
# check for this condition using the `in` keyword.

if 'fossil' in energy:
    energy.remove('fossil')

energy.append('geothermal')
print(energy)

"""

# Solution 2
if 'fossil' in energy:
    fossil_index = energy.index('fossil')
del energy[fossil_index]
print(energy)

# # Solution 3
if 'fossil' in energy:
    fossil_index = energy.index('fossil')
energy.pop(fossil_index)
print(energy)

# Solution 4 - Does not mutate original list.
if 'fossil' in energy:
    fossil_index = energy.index('fossil')
print(energy[:fossil_index]) # => []
print(energy[fossil_index + 1:]) # => ['solar', 'wind', 'tidal', 'fusion']
new_list = energy[:fossil_index] + energy[fossil_index + 1:]
print(new_list)

"""
