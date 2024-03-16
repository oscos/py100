"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > TypeError

Instructions:

    The following code raises a TypeError:

    tweet = 'Woohoo! :-)'

    if len(tweet) > 140:
        print('Tweet is too long!')

    length_of_tweet = len(tweet + 5)

    What does a TypeError indicate? Try running the above code,
    then use the resulting error message to determine exactly 
    what is wrong. (You don't have to fix this code.)

Solution:

    The TypeError is raised because you can not concatenate
    an object of type `str` with an object of type `int`.

    TypeError: can only concatenate str (not "int") to str

"""

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)
