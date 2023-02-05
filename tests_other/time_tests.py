from datetime import datetime, timedelta
from time import sleep


d1 = datetime.now()
# print(d1.year)
# print(d1.month)
# print(d1.day)
# print(d1.hour)
# print(d1.minute)
# print(d1.second)

print("d1: ", d1)
sleep(0.1)
d2 = datetime.now()
print("d2: ", d2)
delta = d2-d1

# print("====")
# print("delta: ", delta)

print("====")
time_added = timedelta(weeks=7, days=8, hours=5, minutes=40, seconds=10)
d3 = d2 + time_added
print("d3: ", d3)

# print("====")
# x = d3.replace(hour=8, minute=0)
# print(x)

# print("====")
# n1 = datetime.now()
# n2 = n1.replace(hour=8, minute=0, second=0, microsecond=0)
# print(n2)


