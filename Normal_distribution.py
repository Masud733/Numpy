#The Normal Distribution is one of the most important distributions.
#It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
#It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
#Use the random.normal() method to get a Normal Data Distribution.
#It has three parameters:
from numpy import random
x = random.normal(size=(2, 3))
print("Generate a random normal distribution of size 2x3:",x)

#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
y = random.normal(loc = 1, scale = 2, size=(2,3))
print(y)