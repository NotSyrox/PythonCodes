# all ai too hard 
from datetime import datetime

now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)

time_left = new_year - now

days = time_left.days
hours = time_left.seconds // 3600
minutes = (time_left.seconds % 3600) // 60

print(f"{days} days, {hours} hours, {minutes} minutes until New Year!")
