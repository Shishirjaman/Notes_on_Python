'''
Date format code

%Y	Year (4 digits)	                                => 2026
%y	Year (2 digits)	                                => 26
%m	Month number (01-12)	                        => 11
%B	Full month name	                                => November
%b	Abbreviated month name	                        => Nov
%d	Day of the month (01-31)	                    => 14
%j	Day of the year (001-366)	                    => 318
%A	Full weekday name	                            => Saturday
%a	Abbreviated weekday name	                    => Sat
%w	Weekday number (Sunday = 0)	                    => 6
%u	Weekday number (Monday = 1)	                    => 6
%U	Week number of the year (Sunday as first day)   => 45
%W	Week number of the year (Monday as first day)   => 45
%V	ISO week number (01-53)                         => 46
%G	ISO week-based year                             => 2026

Time format code

%H	Hour in 24-hour format (00-23)	    =>18
%I	Hour in 12-hour format (01-12)	    =>06
%M	Minute (00-59)	                    =>45
%S	Second (00-59)	                    =>30
%f	Microsecond (6 digits)	            =>123456
%p	AM or PM	                        =>PM

Time zone format code

%z	UTC offset	            => -0500
%Z	Time zone name	        => EST, UTC

Common formatting shortcuts

%c	Locale's date and time representation	    => Sat Nov 14 18:45:30 2026
%x	Locale's date representation	            => 11/14/26
%X	Locale's time representation	            => 18:45:30
%%	A literal percent sign	                    => %
'''

from datetime import datetime

# Create a datetime object
now = datetime(2026, 11, 14, 14, 30, 45)

# Convert datetime into a formatted string
formatted_date = now.strftime("%d-%m-%Y")
print(formatted_date)
print(type(formatted_date)) # Check the data type

# all type of string conversion of datetime
now = datetime(2026, 11, 14, 14, 30, 45)

print(now.strftime("%d %B %Y"))
print(now.strftime("%A"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%Y/%m/%d %H:%M:%S"))