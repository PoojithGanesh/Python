#Write a python program to find number of weak days in given month and year and find the date of first monday.
from datetime import datetime 
import calendar
month, year = 10, 2024
cal = calendar.Calendar()
wee = [0] * 7
mon = None
for day, wd in cal.itermonthdays2(year, month):
    if day:
        wee[wd] += 1
        if wd == 0 and mon is None:
            mon = datetime(year, month, day)
totalweekdays = sum(wee[:5]) 
print(f"Total number of weekdays: {totalweekdays}")
print(f"Date of the first Monday: {mon.strftime('%Y-%m-%d') if mon else 'None'}")
