"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Style Guide

Instructions:

    In the following code snippet, find all violations of the PEP8 style guide. 
    Rewrite it so that it conforms with the guide

    ```python code

    iceCreamDensity=10

    while iceCreamDensity>0 :
        print('Drip...')
        iceCreamDensity-=1

    print('The ice cream melted.')

    ```


Solution:

    1. variables should use the snake_case naming convention
    2. Always surround these binary operators with a single space on either side: 
       - assignment (=), augmented assignment (+=, -= etc.), 
       - comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), 
       - Booleans (and, or, not).
    3. Avoid extraneous whitespace in the following situations:
       - Immediately inside parentheses, brackets or braces:
       - Between a trailing comma and a following close parenthesis
       - Immediately before a comma, semicolon, or colon:


"""

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')
