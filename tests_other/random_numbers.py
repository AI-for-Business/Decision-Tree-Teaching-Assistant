from numpy import random
import random as r

min_val = 0
max_val = 10

c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0

count = 1000000

for j in range(count):
    y = r.randrange(min_val, max_val)
    if y == 0:
        c0 += 1
    if y == 1:
        c1 += 1
    if y == 2:
        c2 += 1
    if y == 3:
        c3 += 1
    if y == 4:
        c4 += 1
    if y == 5:
        c5 += 1
    if y == 6:
        c6 += 1
    if y == 7:
        c7 += 1
    if y == 8:
        c8 += 1
    if y == 9:
        c9 += 1

print(c0)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)
print("++++")
a = count/10  # average results per option
i1 = (min([c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]))
i2 = (max([c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]))
d1 = (i1-a)/a
d2 = (i2-a)/a
print(i1, " ::: ", d1)
print(i2, " ::: ", d2)
