"""

Created: 04/05/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Functions > LInternationalization 2

Instructions:

Building on your solutions from the previous exercises, write a function 
local_greet that takes a locale as input, and returns a greeting. The 
locale lets us greet people from different countries appropriately, 
even when they share a common language, for example:

Solution:

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

Distinguish greetings for English speaking countries like the US, UK, 
Canada, or Australia in your implementation, and feel free to fall 
back on the language-specific greetings in all other cases, for example:

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

When implementing local_greet, make sure you re-use your extract_language, 
extract_region, and greet functions from the previous exercises.

If you're interested, you can find a list of locales here 
[https://www.localeplanet.com/icu/iso639.html].

"""


def greet(lang):
    match lang:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'


def extract_language(str):
    first_part = str.split('_')[0]
    return first_part


def extract_region(str):
    return str.split('_')[1].split('.')[0]


def local_greet(str):
    language = extract_language(str)
    region = extract_region(str)

    if language == 'fr':
        return greet(language)
    else:
        if region == 'US':
            return 'Hey!'
        elif region == 'GB':
            return 'Hello'
        elif region == 'AU':
            return 'Howdy'


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
