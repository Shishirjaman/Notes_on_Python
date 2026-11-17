# importing date from datetime
from datetime import date

# creating a custom date using date sublibrary from datetime library
day = 25
month = 9
year = 2026
my_date = date(year, month, day)
print(my_date)

# from 31st dec 1969 we can get the date by specifying the seconds of time in timestamp
my_timestamp = date.fromtimestamp(0)
print(my_timestamp)

my_timestamp = date.fromtimestamp(5002393473)
print(my_timestamp)

# getting year, month and day seperately from date
my_date = date.today()
my_year = my_date.year
my_month = my_date.month
my_day = my_date.day
print(my_year , my_month, my_day)

# Creating a custom date with keyword arguments
meeting = date(year=2026, month=11, day=13)
print(meeting)

# changing any date element using replace() method
meeting = date(2026, 11, 13)
updated_meeting = meeting.replace(month=10, day=25)
print("Original:", meeting)
print("Updated:", updated_meeting)

# finding difference between two days
start_date = date(2026, 11, 13)
end_date = date(2026, 12, 25)

difference = end_date - start_date
print(difference)
print(difference.days)