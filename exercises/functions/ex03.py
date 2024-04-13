"""

Created: 03/17/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Functions > Cite the Author

Instructions:

Let's generalize the function from the previous exercise. Implement a function 
named cite that takes two string arguments: the author of the quote and what 
they said. It then prints the quote, as shown below.


cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

Solution:

"""


def cite(author, quote):
    print(f'{author} said: "{quote}"')


cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."
