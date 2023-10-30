#The array object in NumPy is called ndarray.
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
arr1 = np.array(42) #0-D array
arr2 = np.array([1,2,3,4,5,6])#1-D array
arr3 = np.array([[1,2,3,4],[5,6,7,8]])#2-D array containing two arrays 
arr4 = np.array([[[1,2,3],[4,5,6],[7,8,9],[1,2,3]]])#3-D array that has 2-D arrays (matrices) as its elements
print(arr1.ndim)
print(arr4.ndim)

#Higher Dimention: Create an array with 5 dimensions and verify that it has 5 dimensions:
import numpy as np
arr5 = np.array([1,2,3,4], ndmin=5) 
print(arr5)
print("Number of dimensions:", arr5.ndim)

#ndim (Attribute):integer indicating how many dimensions the array has.
import numpy as np
arr_1 = np.array([1,2,3])
arr_2 = np.array([[1,2,3],[4,5,6]])
print(arr_1.ndim)
print(arr_2.ndim)
#ndmin (Parameter):ndmin to the desired minimum number of dimensions
arr_min = np.array([10,20,30],ndmin=2)
print(arr_min)
print(arr_min.ndim)