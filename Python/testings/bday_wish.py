import datetime, bday_messages

today = datetime.date.today()
nextBday = datetime.date(2026,6,17)
days_away = nextBday - today

if today == nextBday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')