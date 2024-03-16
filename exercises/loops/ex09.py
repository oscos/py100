"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Finding Nemo

Instructions:

Loop over the elements of the fish_list list below, logging each one. 
Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

Solution:

Note: The code should print `Nemo`, then exit program.

"""

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

print("Using for loop:")
for fish in fish_list:
    print(fish)

    if fish == 'Nemo':
        break

# Further Exploration:

# Can you achieve the same result using a while loop?
# What would the code look like?

print("")

print("Using while loop:")
counter = 0
while counter < len(fish_list):
    current_element = fish_list[counter]
    print(current_element)

    if current_element == 'Nemo':
        break

    counter += 1
