import numpy as np

#Random number: rand() between 0,1
rand = np.random.rand(4)
rand2 = np.random.rand(3,4)
print("Random numbers array:",rand)
print("2D Random numbers array:\n",rand2)

#Random number: randn() close to 0 or nagative or positive value
randn = np.random.randn(4)
print("Random values 0,-or + like that:",randn)

#Random floats: randf()
randf = np.random.ranf(4)
print("Random float values:",randf)

#Random values between two range: randint(min,max,total_values)
randint = np.random.randint(5,20,5)
print("Random 5 values between 5-20 like that:",randint)





