# importing timedelta from datetime
from datetime import timedelta, date, datetime

# creating a custom duration using timedelta
duration = timedelta(
                    days=20,
                    seconds=40,
                    microseconds=230,
                    milliseconds=2350,
                    minutes=30,
                    hours=10,
                    weeks=5
                )

print(duration)
print(duration.total_seconds())

# Adding timedelta to a date
today = date(2026, 11, 13)
duration = timedelta(days=10) #duration of 10 days
future_date = today + duration
print(future_date)

start_date = date(2026, 11, 13)
future_date = start_date + timedelta(weeks=2) # add 2 weeks
print(future_date)

# Subtracking timedelta from a date
today = date(2026, 11, 13)
previous_date = today - timedelta(days=7) # Subtract 7 days
print(previous_date)

# Adding and subtracting timedelta from datetime
meeting = datetime(2026, 11, 13, 14, 30)
new_meeting = meeting + timedelta(hours=3) # Add 3 hours
print(new_meeting)

new_meeting = meeting - timedelta(weeks=3) # subtract 3 weeks
print(new_meeting)