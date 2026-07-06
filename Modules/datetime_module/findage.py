#  Birthday Calculator
from datetime import datetime
birthday=datetime(1992,4,25)
today=datetime.now()
print(f"Person age: {today.year-birthday.year} years{today.day-birthday.day} days")