"""

Created: 04/13/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Lists > Passcode

Instructions:

    We generated parts of a passcode and now want to combine them into a string. 
    Write some code that returns a string, with each portion of the passcode 
    separated by a hyphen (-).

    passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

    # Write some code here.
    # Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

Solution:

"""

# solution 1
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
result = "-".join(passcode)
print(result)

# solution 2
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
result = ''
for code in passcode:
    result += code + "-"
print(result[:-1])
