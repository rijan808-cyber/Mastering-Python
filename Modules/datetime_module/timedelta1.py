from datetime import datetime,timedelta
today=datetime.now()
future=today+timedelta(days=7)
print(future)
print(f"Today: {today}")
print(f"The day after 7 days is {future}")

past=today-timedelta(days=3)
print(f"The time before 3 days is {past}")
print(f"Date before 100 days: {today-timedelta(days=100)}")

print(f"Replace year: {today.replace(year=3025)}")
