"""
You are given the following information, but you may prefer to do
some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on
    a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

def leap_year(year):
    """
    Return 1 if year is a leap year
    """
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return 1
    return 0

def nb_days_month(month, year):
    """
    Return the number of days for the month in the year
    """
    if (month == 1):
        return 28 + leap_year(year)
    elif month in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    else:
        return 30

def nb_sundays_on_first():
    """
    Return the number Sundays that fell on the first of the month during 
    the twentieth century
    """

    #    days_str = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    nb_days     = 1
    nb_saturday = 0

    # Compute the number of days in 1900
    for month in range(12):
        nb_days += nb_days_month(month, 1900)

    # For every year from 1901 to 2000
    for year in range(1901, 2001):
        for month in range(12):
            if (nb_days % 7 == 6):
                nb_saturday +=1

            nb_days += nb_days_month(month, year)

    return nb_saturday

if __name__ == '__main__':
    res = nb_sundays_on_first()
    print(res)