"""

Created: 03/1/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Check the Weather, Part 2

Instructions:

Take your code from the previous Check the Weather exercise 
and rewrite it as a match-case statement. Feel free to add 
more cases besides 'sunny' and 'rainy'.

Solution:

"""

import random
random_number = random.randint(0, 2)

weather_list = ['sunny', 'rainy', 'snowy']

weather = weather_list[random_number]

print(f"The weather's value is: {weather}")
print("")

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside.")
