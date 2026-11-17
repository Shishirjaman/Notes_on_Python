from datetime import datetime, timedelta

# converting a date string into a datetime oject
date_string = "14-11-2026"
converted_date = datetime.strptime(date_string, "%d-%m-%Y") # format must need to match the string
print(converted_date)
print(type(converted_date)) # Check the data type

# another format of date string converting into a datetime object
date_string = "2026/11/14"
converted_date = datetime.strptime(date_string, "%Y/%m/%d")
print(converted_date)

# parsing date and time string together into a datetime object
date_string = "14-11-2026 02:30 PM"
converted_datetime = datetime.strptime(date_string, "%d-%m-%Y %I:%M %p")
print(converted_datetime)

# parsing date and time string (24H format) together into a datetime object
date_string = "2026-12-25 18:45:30"
result = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(result)

# strptime() and timedelta combined operation
booking_date = "14-11-2026"
converted_date = datetime.strptime(booking_date, "%d-%m-%Y")
future_date = converted_date + timedelta(days=7)
print(future_date.strftime("%d %B %Y"))