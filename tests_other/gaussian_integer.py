import numpy

mu = 250
sigma = 1


# for i in range(20):
n = numpy.random.normal(mu, sigma, 1).round(0)
x = n % 1
print(x)
y = x * 1000
print(y)

