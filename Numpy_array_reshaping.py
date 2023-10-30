#Reshaping means change the elemets or giving a new shape of an array
#By reshaping we can add or remove dimensions or change number of elements in each dimension.
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape = arr.reshape(4,3)
print("Reshaping 1D to 2D:\n",reshape)

#Reshape From 1-D to 3-D
#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
reshape2 = arr.reshape(2,3,2) # create 2 array matrix within 3D array with 2 elemets
print("Reshape 1D from 3D:\n",reshape2)

#Check if the returned array is a copy or a view:
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr2.reshape(2, 4).base)

#Unknown Dimension: You are allowed to have one "unknown" dimension. pass -1 as the value
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr3.reshape(2, 2, -1)# '-1' Numpy will count it as a number for you
print("Convert 1D arr with 8 elem to 3D arr with 2x2 elem:\n",newarr)

#Flattening the arrays: Flattening array means converting a multidimensional array into a 1D array.
arr4 =np.array([[1,2,3,4],[10,20,30,40]])
flatten = arr4.reshape(-1)
print("Flattening the 2D array into 1:",flatten)