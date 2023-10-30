#Iterating means going through elements one by one.
#As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
    print("Iterate elemet one by one:", x) #same as 1D
    
#terate on the elements of the following 3-D array:
arr1 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for x in arr1:
    print("Iterate 3D array:\n", x)
    
#To return the actual values, the scalars, we have to iterate the arrays in each dimension.
arr2 = np.array([[[1,2,3,4],[5,6,7,8],[10,20,30,40]]])
for x in arr2:
    for y in x:
        for z in y:
            print("The actual values & the scalers:", z)



# Create a 2D NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Get the shape of the array (dimensions)
shape = arr.shape

# Iterate through each dimension
for i in range(shape[0]):  # Loop through rows
    for j in range(shape[1]):  # Loop through columns
        # Access and process the individual scalar value
        value = arr[i, j]
        print(f"Element at row {i}, column {j} is {value}")


