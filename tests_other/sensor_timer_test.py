import random
from datetime import datetime, timedelta


class Sensor:
    def __init__(self, name):
        self.Name = name

    def activate(self, time):
        print(self.Name, time)
        pass


s1 = Sensor("s1")
s2 = Sensor("s2")
s3 = Sensor("s3")
s4 = Sensor("s4")
s5 = Sensor("s5")
s6 = Sensor("s6")


# Sensors = [s1]
# Sensors = [s1, s2]
# Sensors = [s1, s2, s3]
# Sensors = [s1, s2, s3, s4]
# Sensors = [s1, s2, s3, s4, s5]
Sensors = [s1, s2, s3, s4, s5, s6]


duration = timedelta(minutes=60)
d1 = datetime.now()
d2 = d1.replace(hour=8, minute=0, second=0, microsecond=0)
d3 = d2 + duration


if len(Sensors) == 1:
    dur2 = duration / 2
    d4 = d2 + dur2
    Sensors[0].activate(d4)
elif len(Sensors) == 2:
    d4 = duration / 3
    start = d2 + d4
    for s in Sensors:
        s.activate(start)
        start = start + d4
else:
    start = d2
    d4 = duration / (len(Sensors)-1)
    for s in Sensors:
        # s.activate(start)
        start = start + d4


timers = []
ls = len(Sensors)-1
for i in range(ls):
    n = random.randrange(0, duration.total_seconds(), 1)
    dif = timedelta(seconds=n)
    dx = d2 + dif
    timers.append(dx)

timers.sort()

print("===========")
print("Variant 1:")
for j in range(ls):
    Sensors[j].activate(timers[j])

print("===========")
print("Variant 2:")
usl = random.sample(Sensors, len(Sensors))
for j in range(ls):
    usl[j].activate(timers[j])
