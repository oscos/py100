"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Checking items off the grocery list

Instructions:

We have a grocery list. As we check off items on that list, 
we want to remove them from the list.

Write code that removes the items from grocery_list, one by one, 
until it is empty. If you print the elements you remove, 
the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.

print(grocery_list)

Expected output:
    paprika
    tofu
    garlic
    quinoa
    carrots
    broccoli
    hummus
    []

Solution:

    pop()  # removes last item in list
    pop(0) # removes first item in list

"""

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Solution 1
while grocery_list:  # making use of the fact that an empty list is falsy
    item = grocery_list.pop(0)
    # print(grocery_list)
    print(item)

print(grocery_list)

# Solution 2
grocery_list_copy = grocery_list.copy()

for item in grocery_list_copy:
    print(item)
    grocery_list.remove(item)

print(grocery_list)
