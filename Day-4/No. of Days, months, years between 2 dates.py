import datetime
a=datetime.datetime.now()
x=datetime.datetime(2018, 6, 1)
c=(a-x)
days=c.days
years=days//365
months=(days%365)//30
remaining_days=(days%365)%30
print("Years:",years)
print("Months:",months)
print("Days:",remaining_days)
