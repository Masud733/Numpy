#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
import numpy as np
#Slice elements from index 1 to index 5 from the following array:
arr = np.array([1,2,3,4,5,6,7])
print(arr[0:4]) # first element bade porer elemet theke last porjonto

#Slice elements from index 4 to the end of the array:
arr1 = np.array([10,20,30,40,50])
print("Slice array 30 to end:", arr1[2: ])## Slice the array from index 2 (30) to the end
#Slice elements from the beginning to index 4
print("Slice array beggining to 40:",arr1[ :4])

#Slice from the index 3 from the end to index 1 from the end:
arr2 = np.array([1,2,3,4,5,6,7])
print("Index 3 from end to index 1 from end:",arr2[-3:-1])

#Use the step value to determine the step of the slicing:
arr3 = np.array([1,2,3,4,5,6,7,8,9])
print("Determine step value between 1 to 7:",arr3[1:7:2])#The stride of 2 indicates that it will skip the next element

#Return every other element from the entire array:
arr4 = np.array([1,3,5,7,8,4])
print(":: colons work like:",arr4[::2])#2 is work like step or stride

#Slicing 2-D array
#From the second element, slice elements from index 1 to index 4
arr5 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("From 2nd row slice 1 to 4:",arr5[1, 1:4]) #1:4 - includes columns 1, 2, and 3.

#From both elements, return index 2 from column:
arr6 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Enter element from given range within 3rd col:", arr6[0:2, 2])

