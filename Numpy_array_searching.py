#You can search an array for a certain value using where() method and return the indexes that get a match.
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
search = np.where(arr ==5)
print("Find the indexes where the value is 5:", search)

#Find the indexes where the values are even:
find_even = np.where(arr%2 == 0)
print("The even numbers from the array:", find_even)

#Find the indexes where the values are odd:
find_odd = np.where(arr%2 == 1)
print("The odd numbers from the array:", find_odd)

#Search Sorted: There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
#Find the indexes where the value 7 should be inserted:
arr1 = np.array([1,5,2,10])
Sorter = np.searchsorted(arr1, 2)
print("Value 2 should be inserted in:", Sorter)

#Search From the Right Side: By default the left most index is returned, but we can give side='right' to return the right most index instead.
search_right = np.searchsorted(arr1, 5, side = 'right')
print("Starting from the right for where 5 should be inserted:", search_right)

#Multiple Values: To search for more than one value, use an array in searchsorted() the specified values.
arr2 = np.array([1,3,5,7])
search_mul = np.searchsorted(arr2, [2,4,6])
print("Find the indexes for this list:", search_mul)
