from datetime import datetime,timedelta
birthday=datetime(1998,4,25)
today=datetime.now()
print(f"Today: {today}")
print(f"No of days he/she lived: {today-birthday}")

deathday=datetime(2062,3,28)
print(f"No of days left to live: {deathday-today}")