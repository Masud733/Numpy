#Getting some elements out of an existing array and creating a new array out of them is called filtering.
#In NumPy, you filter an array using a boolean index list.
import numpy as np
arr = np.array([10,11,44,99,75])
x = [True, False, True, True, False]
new_arr = arr[x]
print("Included this elements using True:", new_arr)

#Create a filter array that will return only values higher than 44:
filter_arr = arr> 44
new_arr = arr[filter_arr]
print("Filtering selements using condition:",new_arr)
print("Filtering with booleans:",filter_arr)

#Create a filter array that will return only even elements from the original array:
filtering_even = arr%2 ==0
newarr = arr[filtering_even]
print("The ven values fron the array:",newarr)

#Create a filter array that will return only values higher than 42:
original_array = np.array([44,45,50,78,99,10,100])
filtered_array = []

for value in original_array:
    if value > 45:
        filtered_array.append(value)

filtarr = np.array(filtered_array)
print("Filter the higher values:", filtarr)

#Create a filter array that will return only even elements from the original array:
originalarr = np.array([3,4,5,6,7,10,11,12])
filtered_arr1 = []
for elements in originalarr:
    if elements %2 ==0:
        filtered_arr1.append(True)
    else:
        filtered_arr1.append(False)
newarr = np.array(filtered_arr1)
print("Filtered even numbers:", filtered_arr1)
print(newarr)
        
    