#Binomial distribution is a descrete distribution
#Given 10 trials for coin toss generate 10 data points:
# Visualization of Binomial Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()