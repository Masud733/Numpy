#Sorting means putting elements in an ordered sequence. sort() method will sorted
import numpy as np
arr = np.array([3,0,1,2])
#sorted = np.sort(arr)
#print("the sorted array:", arr)
print("The sorted array is:",np.sort(arr))

#Sorting array string according to alphabet
arr1 = np.array(["Banana", "Apple", "Cherry"])
print("The sorted array string:", np.sort(arr1))

#sort boolean array
arr2 = np.array([True,False,True,False])
print("sorting this booleans:",np.sort(arr2))

#Sorting a 2-D Array
arr3 = np.array([[4,2,1,3],[5,6,8,7]])
print("Sorted the 2D array:\n", np.sort(arr3))


