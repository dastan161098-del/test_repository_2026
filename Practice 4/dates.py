#1
import datetime

x = datetime.datetime.now()
print(x)

#2
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#3
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#4
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#EXERCISES
#1
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("5 days ago:", new_date)

#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("Original:", now)
print("Without microseconds:", without_microseconds)

#4
from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 12, 0, 0)

difference = date2 - date1

print("Difference in seconds:", difference.total_seconds())