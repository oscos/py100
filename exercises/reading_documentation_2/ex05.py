"""

Created: 03/10/2024
Updated:
Launch School - Intro to Python
PY100 - Python Basics > Reading Documentation 1 > Which Year is This?

Instructions:

    The Python documentation for the datetime module provides two attributes to
    retrieve the year from a date or datetime object: year and isocalendar.

Solution:

    Using year returns only a year object.
    Using isocalendar returns a tuple containing year, week number, and weekday.

"""

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

print(f"Using year: {today.year}")
print(f"Using isocalendar year: {today.isocalendar()}")
