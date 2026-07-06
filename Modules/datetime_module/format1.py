from datetime import datetime
today=datetime.now()
date_format1=today.strftime(f"%d /%B /%Y (%a)")
time_format1=today.strftime(f"%I:%M:%S %p")
print(today.strftime(f"%d/%B/%Y"))
print(today)
print(date_format1)
print(time_format1)