#Joining means putting contents of two or more arrays in a single array.
#We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. 
#If axis is not explicitly passed, it is taken as 0.
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr = np.concatenate((arr1,arr2))
print("Joining two array:",arr)

#Along with the axisin 2D array
arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[10,20,30],[40,50,60]])
arr_con = np.concatenate((arr3,arr4), axis=1)
print("Joining 2D array with exis one:\n",arr_con)




 