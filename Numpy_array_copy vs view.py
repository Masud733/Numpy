#create a copy using the copy() method or the np.copy() function. Its create a completely new array with its own data in memory. 
import numpy as np
arr = np.array([1,2,3,4,5])
arr_copy = arr.copy()
arr_copy[0] = 99
print("The original array:",arr)
print("The copy array:",arr_copy) #The copy SHOULD NOT be affected by the changes made to the original array.

#Array View: provides a different "view" of the existing data, Slicing, indexing, and reshaping operations.
arr1 = np.array([1, 2, 3, 4])
arr_view = arr1[2:4]
arr_view[0] = 99

print("The copy array:",arr1)       
print("Array view after slicing:",arr_view)  

#Make a view, change the view, and display both arrays:
arr2 = np.array([10,20,30,40])
arr_v = arr2.view()
arr_v[3] = 999
print("The main array view:",arr2)
print("Change view:",arr_v)

#Every NumPy array has the attribute base that returns None if the array owns the data.
#Otherwise, the base  attribute refers to the original object.
x = arr2.copy() #owns data
y = arr2.view()
print("Its owns data:",x.base)
print("Its dose not own data:",y.base)

