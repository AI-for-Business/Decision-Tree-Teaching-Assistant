import random as r

ex_list = ["a", "b", "c", "d", "e"]
count = 20

for j in range(count):
    n = r.randrange(0, len(ex_list))
    print(ex_list[n])
