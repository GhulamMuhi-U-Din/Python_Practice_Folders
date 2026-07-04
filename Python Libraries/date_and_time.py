# =============================
# datetime library
# =============================

# for current date and time

from datetime import datetime

current = datetime.now()

print(current)

# for current date only

from datetime import date

today = date.today()

print(today)

# for current time only

from datetime import datetime

current_time = datetime.now().time()

print(current_time)

# for individual components

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# for creating your own date

from datetime import datetime

birthday = datetime(1975, 4, 10)

print(birthday)

# for formatting date

from datetime import datetime

today = datetime.now()

print(today.strftime("%d/%m/%Y"))

# important syntax

# | Code | Meaning         | Example |
# | ---- | --------------- | ------- |
# | `%d` | Day             | 04      |
# | `%m` | Month           | 07      |
# | `%Y` | Year (4 digits) | 2026    |
# | `%y` | Year (2 digits) | 26      |
# | `%H` | Hour (24-hour)  | 18      |
# | `%M` | Minutes         | 45      |
# | `%S` | Seconds         | 30      |