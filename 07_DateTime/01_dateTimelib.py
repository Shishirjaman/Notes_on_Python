import datetime

# checking what inside the datetime library
print(dir(datetime))

# creating an datetime object that will get the current datetime (local timezone)
datetime_obj = datetime.datetime.now()
print(datetime_obj)

# creating an datetime object that will get the current date & time in UTC timezone
datetime_obj2 = datetime.datetime.now(datetime.timezone.utc)
print(datetime_obj2)

# creating an object that will store the today's date
date_obj = datetime.date.today()
print(date_obj)

# creating a custom date & time using datetime obj
my_datetime = datetime.datetime(2019, 10, 17, 10, 40, 45)
print(my_datetime)

# Creating a custom date & time with keyword arguments
meeting = datetime.datetime(year=2026, month=11, day=13, hour=15, minute=45)
print(meeting)

# printing year, month, day, hour, minute, second separatly
data = datetime.datetime.now()
year = data.year
month = data.month
day = data.day
hour = data.hour
min = data.minute
sec = data.second
print(year, month, day, hour, min, sec)

# combine date and time using combine() method
meeting_date = datetime.date(2026, 11, 13)
meeting_time = datetime.time(14, 30, 0)
meeting = datetime.datetime.combine(meeting_date, meeting_time)
print(meeting)

# changing any datetime element using replace() method
meeting = datetime.datetime(2026, 11, 13, 14, 30)
updated_meeting = meeting.replace(hour=16, minute=45)
print("Original:", meeting)
print("Updated:", updated_meeting)

# calculating between two data & time
date1 = datetime.datetime(2020, 10, 20) #in datetime if no inserted time means 00:00:00
date2 = datetime.datetime(2024, 1, 31)
duration = date2 - date1
print("Days:", duration.days)
print("Seconds:", duration.seconds)
print("Total seconds:", duration.total_seconds()) # days also converted into seconds and then difference 
print("Total hours:", duration.total_seconds()/3600)