#Splitting is reverse operation of Joining.
#Joining merges multiple arrays into one and Splitting breaks one array into multiple.
#We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
newArr = np.array_split(arr,2)
print("Split the array in 3 parts:", newArr)
#If the array has less elements than required, it will adjust from the end accordingly.
newArr2 = np.array_split(arr, 6)
print("Adjusting from end:", newArr2)

#If you split an array into 3 arrays, you can access them from the result just like any array element:
print(newArr2[0])
print(newArr2[1])
print(newArr2[2])

#Splitting 2-D Arrays using same method
arr1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
spliting = np.array_split(arr1,3)
print("Spliting 2D array:", spliting)

#Split the 2-D array into two\three 2-D arrays along rows.
spliting2 = np.array_split(arr1,2, axis =1)
print("Spliting 2D arr into three 2D:\n", spliting2)

#An alternate solution is using hsplit() opposite of hstack()
#Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
hor_split = np.hsplit(arr1, 3)
print("Splitting 2D into three 2D:\n", hor_split)


#Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().


