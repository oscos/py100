"""

Created: 03/17/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Loops > Match-Case

Instructions:

Examine the code shown below. Without running it, determine what it will print. 
If you're not sure, refer to our Python book.

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

Solution:

"""

print("The code will print 'neigh'")
print("")

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')
