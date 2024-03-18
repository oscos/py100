"""

Created: 03/1/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Are we moving?

Instructions:

    Determine what the following code snippet prints. First solve it in 
    your head or on paper, then run it in your Python environment to check 
    the result.

    speed = 0
    acceleration = 24
    braking_force = 19
    is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
    print(is_moving)

    Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

Solution:

@TODO: Privide Explanation.

Key Points: 
`0` is false, meaning it will evaluate to `False`
`and` has greater precedence than `<`
`and` logical operator requires both `acceleration` and `(speed > 0 or acceleration > 0)`
to evaluate to `True`
`or` logical operator requires that only `speed` or `accelartion > 0` to evaluate to `True`
`parenthesis` has greater precenence than `and` and `or`.

"""

print("The code will print `True`")

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)
