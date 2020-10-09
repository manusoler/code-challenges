import os
from utils.decorators import timer
"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def get_day_of_week(year, month, day):
    ## THIS COULD BE DONE WITH DATETIME LIBRARY
    FIRST_YEAR, DAYS_PER_YEAR = 1900, 365
    dow = {0:'Monday', 1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    # Days in month
    dim = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # Numbers of days since FIRST_YEAR
    num_leaps = 0
    for y in range(FIRST_YEAR, year):
        if (y % 100 == 0 and y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
            num_leaps += 1
    n_days = (year - FIRST_YEAR) * DAYS_PER_YEAR + num_leaps

    # Number of days since January
    for m in range(1, month):
        n_days += dim[m]
        # February has 29 if leap year
        if (m == 2 and ((year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0))):
            n_days += 1
    
    # Number of days since 1st day of month
    n_days += day - 1

    return dow[n_days % 7]

def counting_sundays(from_year, to_year):
    sundays = 0
    for y in range(from_year, to_year+1):
        for m in range(1,13):
            sundays += 1 if get_day_of_week(y, m, 1) == "Sunday" else 0
    return sundays

@timer
def main():
    print(counting_sundays(1901,2000))

if __name__ == "__main__":
    main()