"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Strings > Capitalize Words

Instructions:

    Write code that capitalizes the words in the string 'launch school tech & talk', 
    so that you get the string 'Launch School Tech & Talk'.

Solution:

"""


# Solution 1
# def capitalize_string(string):
#     return my_string.title()


# Solution 2
def capitalize_string(string):
    result = []

    word_list = string.split()
    # print(word_list)
    for word in word_list:
        # print(word)
        word_cap = word.capitalize()
        # print(word_cap)
        result.append(word_cap)

    return " ".join(result)


my_string = 'launch school tech & talk'
print(capitalize_string(my_string))
print(capitalize_string(my_string) == my_string.title())
