import numpy as np

#access the 1st and 2nd elemets
arr = np.array([1,2,3,4,5])
print(arr[0],arr[1])

#Get third and fourth elements from the following array and add them.
arr1 = np.array([1,2,4,5,6])
print(arr1[2]+arr1[3])

#Access the element on the 2nd row, 3rd column:
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print("3rd elemt of the 2ndst row:",arr2[1,2])

#Access the element on the first row, second column:
arr_e = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr_e[0, 1])

#To access elements from 3-D array
arr_3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("Access the third element of the second array of the first array:",arr_3[0,1,2])

#Negative Indexing:Use negative indexing to access an array from the end.
#1: This is the first index,-1: This is the second index, and it's a negative index. Negative indices count from the end of the array. -1 refers to the last element of the selected row (the second row in this case).
arr_4 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("last element from the 2nd dim:",arr_4[1,-1])
