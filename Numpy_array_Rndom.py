#Random means something that can not be predicted logically.Pseudo Random and True Random.
#NumPy offers the random module to work with random numbers.
from numpy import random
Random_int = random.randint(100)
print(Random_int)
Random_float= random.rand()
print(Random_float)

#Generate Random Number From Array: choice() method alow for take random one number
x = random.choice([10,22,3,4,5,23,1])
print("Randomly choice a nimber:", x)
 
#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
twodarr = random.choice((3,5,7,9), size =(3,5)) #size( for shape)
print(twodarr)