#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
#The NumPy Random module provides two methods for this: shuffle() and permutation().
from numpy import random
import numpy as np
arr = np.array([1,2,3,4,5])
random.shuffle(arr) #makes changes to the original array.
print(arr)

#Generating Permutation of Arrays
arr1 = np.array([1,2,3,4,5,6,7])
print(random.permutation(arr1)) #The permutation() method returns a re-arranged array

