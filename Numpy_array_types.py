import numpy as np
#Zeros
arr_z = np.zeros(4)
arr_z1 = np.zeros((3,4))
print("1D Zeros elements array:",arr_z)
print("2D array:\n",arr_z1)

#Ones
arr_o = np.ones(4)
print("One elements array:",arr_o)

#Empty
arr_e = np.empty(4)
print("Empty array:",arr_e)

#Range
arr_r = np.arange(5)
print("Range of the array:",arr_r)

#Diagonal array/identity matrix
arr_d = np.eye(3)
print("Diagonal array:\n",arr_d)
arr_d1 = np.eye(3,4)
print("2D diagonal array:\n",arr_d1)

#Linespace
arr_lp = np.linspace(1, 20,num=5)
print("Line space of the array:",arr_lp)