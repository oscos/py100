"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Vocabulary

Instructions:

    You've been given a list of vocabulary words grouped into sub-lists, by meaning. 
    This is a two-dimensional list or a nested list. Write some code that iterates 
    through and prints all the words, one per line.

    vocabulary = [
        ['happy', 'cheerful', 'merry', 'glad'],
        ['tired', 'sleepy', 'fatigued', 'drained'],
        ['excited', 'eager', 'enthused', 'animated'],
    ]

    # happy
    # cheerful
    # merry
    # glad
    # tired
    # sleepy
    # etc...

Solution:

"""


vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for sublist in vocabulary:
    for word in sublist:
        print(word)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...
