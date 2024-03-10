"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > String Formatting

Instructions:

    Python offers multiple ways to format strings. The str.format method is a popular method, 
    but since Python 3.6, a new way called f-strings (formatted string literals) was introduced. 
    F-strings offer a concise way to embed expressions inside string literals.

    Given the following variables:

    name = "Victor"
    profession = "programmer"

    How can you print the string Hello, Victor. You are a programmer. using the str.format method? 
    You should fill in the name and profession in a string literal that contains the rest of the text.
    How can you achieve the same result using an f-string?

    Refer to the Python documentation on Format String Syntax and Formatted string literals for guidance.


Solution Using Format String Syntax (str.format):

    The str.format method is used to format strings.  It does this by subsituting placeholders, 
    represented by `{}` within the string with actual values. it does this by invoking the `format()` 
    method where the arguments are listed in sequential order, onto the string containing the 
    placeholders `{}`.

    Here is the actual definition from the Python Docs:

    Format strings contain “replacement fields” surrounded by curly braces {}. Anything that is not 
    contained in braces is considered literal text, which is copied unchanged to the output. If you 
    need to include a brace character in the literal text, it can be escaped by doubling: {{ and }}.

    string — Common string operations - https://docs.python.org/3/library/string.html#format-string-syntax

    Format String Syntax - https://docs.python.org/3/library/string.html#format-string-syntax


Solution Using String Literals (f-string):

    f-strings allow you to insert the value of a variable or expression directly into a string. 

    Here is the actual definition from the Python Docs:

    New in version 3.6.

    A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. 
    These strings may contain replacement fields, which are expressions delimited by curly braces {}. 
    While other string literals always have a constant value, formatted strings are really 
    expressions evaluated at run time.

    2. Lexical analysis - https://docs.python.org/3/reference/lexical_analysis.html#lexical-analysis

    2.4. Literals - https://docs.python.org/3/reference/lexical_analysis.html#literals

    2.4.3. f-strings - https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals


"""


name = "Victor"
profession = "programmer"

print("Print using the str.format method:")
print("Hello, {0}. You are a {1}.".format(name, profession))

print("")

print("Print using an f-string:")
print(f"Hello, {name}. You are a {profession}.")
