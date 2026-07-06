from datetime import datetime
today=datetime.now()
print(datetime.timestamp(today))
print(datetime.fromtimestamp(datetime.timestamp(today)))
print(datetime.fromtimestamp(1783323326))