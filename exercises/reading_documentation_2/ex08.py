"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > SyntaxError

Instructions:

    The following code raises a SyntaxError:

    speed_limit = 60
    current_speed = 80

    if current_speed > speed_limit
        print('"People are so bad at driving cars that '
            "computers don\'t have to be that good to be "
            'much better." -- Marc Andreessen')

    What does a SyntaxError indicate? Try running the above code,
    then use the resulting error message to fix the error.

Solution:

    The code raises SyntaxError: expected ':'

    This is because the if statement is missing the colon `:` at the end
    of the line.

"""

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
