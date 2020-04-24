import time
from datetime import datetime

dt = datetime(2018, 1, 1)
dt = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())


dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

print(dt)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m/%d"))

print(dt2 > dt1)
