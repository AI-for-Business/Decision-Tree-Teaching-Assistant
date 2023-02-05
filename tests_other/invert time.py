from datetime import datetime, timedelta


d1 = datetime.now()
print(d1)

d2 = d1.strftime("%X")
# d2 = d2 + " hello"
print(d2)

c1 = d2[5]
c2 = d2[6]
c3 = d2[8]
c4 = d2[9]

d2[5] = c3
d2[6] = c4
d2[8] = c1
d2[9] = c2

print(d2)
