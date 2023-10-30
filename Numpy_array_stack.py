#In NumPy, you can join arrays using various stacking functions. 
import numpy as np
#stack function create a new array taking column value
arr11 = np.array([1,2,3,4])
arr22 = np.array([5,6,8,9])
arr_stk = np.stack((arr11,arr22),axis =1)
print("The array stack is:\n",arr_stk)

#1.Vertical Stack (numpy.vstack): This function stacks arrays vertically along the first axis (rows). The arrays being stacked must have the same number of columns.
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([10,20,30,40])
v_stack = np.vstack((arr1,arr2))
print("The vertical stack is:\n", v_stack)

#2.Horizontal Stack (numpy.hstack): This function stacks arrays horizontally along the second axis (columns). The arrays being stacked must have the same number of rows.
arr3 = np.array([1,2,3])
arr4 = np.array([10,20,30])
h_stack = np.hstack((arr3, arr4))
print("The horizontal stack creating row:\n",h_stack)

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6]])
# Horizontal stack
result = np.hstack((array1, array2.T))  # Transpose array2 to match rows with array1, array2.T becomes [[5], [6]].
print("Transpose array with array1 is :\n",result)

#dstack() to stack along height, which is the same as depth.
arr5 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
arr6 = np.array([[[10,11,12],[13,14,15],[16,17,18]]])
d_stack = np.dstack((arr5,arr6)) # It concatenates them along the last dimension, combining corresponding 2D arrays from array1 and array2 into a new 3D array.
print("Concatenete last dim into depth stack:\n",d_stack)
