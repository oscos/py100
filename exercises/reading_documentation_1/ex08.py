"""

Created: 03/08/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Large Numbers

Instructions:

    Using the Python documentation, determine how you can write large numbers
    in a way that makes them easier to read.

Solution:

    Underscores can be used to group digits for enhanced readability.
    They are ignored for determining the numeric value of the literal.

    Documentation: 

    2.4.5. Integer literals
    https://docs.python.org/3/reference/lexical_analysis.html#integer-literals

Further Exploration:

    Is it okay to write 1_987_654_321 as 19_87_65_4321?

Further Exploratio Solution:

    Yes, it is. The underscores are for readability and do not impact the 
    literal value.
"""
NUMBER1 = 987_654_321
print(f"The integer literal 987_654_321 will print as: {NUMBER1}")


NUMBER2 = 19_87_65_4321
print(f"The integer literal 19_87_65_4321 will print as: {NUMBER2}")
