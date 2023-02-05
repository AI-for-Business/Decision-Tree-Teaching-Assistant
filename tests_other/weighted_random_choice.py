# Requires installation of NumPy
from numpy.random import choice

candidates = ["Alpha", "Beta", "Gamma"]
weightings = [0.85, 0.05, 0.10]

# Counter
alpha = 0
beta = 0
gamma = 0

for n in range(100):
    x = str(choice(candidates, 1, p=weightings))
    # print(x)
    if x == "['Alpha']":
        alpha = alpha + 1
    if x == "['Beta']":
        beta += 1
    if x == "['Gamma']":
        gamma += 1

print(alpha)
print(beta)
print(gamma)
