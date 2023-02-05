states = ["Rot", "Gelb", "Grün", "Gelb"]
n = 0

for i in range(20):
    print(states[n])
    n += 1
    if n > (len(states)-1):
        n = 0
