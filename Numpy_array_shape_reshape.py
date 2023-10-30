#The shape of an array is the number of elements in each dimension.
#NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print("The shape of 2D array:", arr.shape)

#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr1 = np.array([10,20,30,40], ndmin=5)
print("The main 2d array:\n", arr)
print("verify that first 3 dim has size 1 and last dim has value 4:",arr1.shape)

array = np.array([1,2,3,4,5,6,7,8])
revers_arr = array[::-1]
print("Reverse this array:", revers_arr)
