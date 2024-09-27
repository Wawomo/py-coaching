#date module
import datetime
from datetime import timedelta

today = datetime.datetime.now()
print(today)

print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

#create a date object
yearsAgo = datetime.date(1994, 6, 25)
print(yearsAgo)
yearsAgo = datetime.datetime(1994, 6,25,12,54,6)
print(yearsAgo)

print(today.strftime("%a %d %b %Y, %H:%M %p"))
"""
timedelta allows
seconds, minutes, hours,days
"""

oneWeekFromNow = today + timedelta(weeks=1)
print(oneWeekFromNow)
print(oneWeekFromNow.strftime("%a %d %b %Y, %H:%M "))
#I is for 12 hour format while H is for 24 hr format

fiveDaysAgo = today + timedelta(days=-5)
print(fiveDaysAgo)
print(fiveDaysAgo.strftime("%a %d %b %Y, %I:%M %p"))

constTime = datetime.time(12,30,00)
print(constTime)
