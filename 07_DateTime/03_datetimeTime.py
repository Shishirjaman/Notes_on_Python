# importing time from datetime
from datetime import time, datetime
# creating custom time using time
sec = 25
min = 9
hour = 20
my_time = time(hour, min, sec)
print(my_time)

# getting hour, minute and seconds seperately from datetime object
my_time = datetime.now().time()
my_hour = my_time.hour
my_min = my_time.minute
my_sec = my_time.second
print(my_hour , my_min, my_sec)

# Creating a custom time with keyword arguments
meeting = time(hour=20, minute=11, second=13)
print(meeting)

# changing any time element using replace() method
meeting = time(15, 11, 13)
updated_meeting = meeting.replace(hour=10, minute=25)
print("Original:", meeting)
print("Updated:", updated_meeting)