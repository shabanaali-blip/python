from datetime import datetime,timedelta
n=datetime.now()
t=n.time()
print("Current Time: ",t)
today=datetime.today()
day=today-timedelta(5)
print("Five days before today is : ",day)
print("Yesterday : ",today-timedelta(1))
print("Current date : ",today)
print("Tomorrow : ",today+timedelta(1))
print("Next 5 days: ")
for i in range(1,6):
    t=today+timedelta(i)
    print(t)

sec=n+timedelta(0,5)
print("After 5 Seconds:",sec.time())
