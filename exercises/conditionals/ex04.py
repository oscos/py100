"""

Created: 03/15/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Check the Weather, Part 1

Instructions:

Initialize a variable weather with a string value being
 'sunny', 'rainy', or whatever weather condition you choose. 
 Then, write an if statement that prints:

It's a beautiful day! if weather's value is 'sunny'
Grab your umbrella. if weather's value is 'rainy'
Let's stay inside. if weather's value is anything else
Test your code with different values for weather.

Solution:

"""
import random
random_number = random.randint(0, 2)

weather_list = ['sunny', 'rainy', 'snowy']

weather = weather_list[random_number]

print(f"The weather's value is: {weather}")
print("")
if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")
