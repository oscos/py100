"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Date

Instructions:

    Using the datetime module in Python, how would you obtain the current date and time?

Solution:

    https://www.python.org/doc/

    Python Docs - https://docs.python.org/3/

    Library Reference - https://docs.python.org/3/library/index.html

    The Python Standard Library - https://docs.python.org/3/library/index.html#the-python-standard-library

    Date Types - https://docs.python.org/3/library/datatypes.html

    datetime — Basic date and time types - https://docs.python.org/3/library/datetime.html

"""

from datetime import datetime

current_datetime = datetime.now()
print(f"The current date and time is: {current_datetime}")
