"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Filter

Instructions:

    Count the number of elements in scores that are 100 or above.

    scores = [96, 47, 113, 89, 100, 102]

Solution:
    while I used a counter along with a for loop, list expressions are considered more readable. 
    However, when first learning how loops work, list comprehensions are harder to grasp in my opinion. 
    Having everything in one line make it harder to see what is going on and troubleshoot.

    list comprehension has three components [expression, item in iterator, filtering condition]

"""


# # Solution 1
scores = [96, 47, 113, 89, 100, 102]
counter = 0
for score in scores:
    if score >= 100:
        counter += 1

print(counter)


# Solution 2 - list comprehension
scores2 = [96, 47, 113, 89, 100, 102]
score_counter2 = [score for score in scores2 if score >= 100]
print(score_counter2)
print(len(score_counter2))

# My own problems to understand drill down list comprehensions better:

# Solution 3 - list comprehension with additional criteria
# to find even numbers
scores3 = [96, 47, 113, 89, 100, 102, 103, 104, 105, 110]
score_counter3 = [
    score for score in scores3 if score >= 100 and score % 2 == 0]
print(score_counter3)
print(len(score_counter3))


# Solution 3 - list comprehension with additional criteria
# to find even numbers and double the result
scores4 = [96, 47, 113, 89, 100, 102, 103, 104, 105, 110]
score_counter4 = [
    score * 2 for score in scores4 if score >= 100 and score % 2 == 0]
print(score_counter4)
print(len(score_counter4))


# Solution 4 - list comprehension with additional criteria
# to find even numbers and triple the result by passing
# the result of the iterator to a `triple` function.

def triple(int):
    return int * 3


scores5 = [96, 47, 113, 89, 100, 102, 103, 104, 105, 110]
score_counter5 = [
    triple(score) for score in scores5 if score >= 100 and score % 2 == 0]
print(score_counter5)
print(len(score_counter5))
