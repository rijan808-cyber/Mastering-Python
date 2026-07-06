#  Birthday Calculator
from datetime import datetime
from dateutil.relativedelta import relativedelta
birthday=datetime(2008,6,14)
today=datetime.now()
print(f"Person age: {today.year-birthday.year} years")
age=relativedelta(today,birthday)
print(f"Age: {age.years} Years, {age.months} Months, {age.days} Days")