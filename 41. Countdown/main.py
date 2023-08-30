# Countdown 🎂
# Main 🎂

import datetime
from datetime import date

import bday_messages

today = datetime.date.today()
my_next_birthday = datetime.date(2023, 8, 30)
time_difference = my_next_birthday - today
days_away = time_difference.days

if my_next_birthday == today:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")