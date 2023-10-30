#NumPy, which stands for "Numerical Python",Python library for numerical and scientific computing.
#Creating Arrays: NumPy allows you to create arrays,These arrays can be used to store and manipulate data efficiently  using numpy.array().
import numpy as np
#as np: This part of the line specifies an alias for the imported library. By using as np, you are creating a shorter and more convenient way to refer to the numpy librar
data = [1,2,3,4,5]
arr = np.array(data)
print(arr)

#mathematical operations
data2 = np.array([10,20,30])
mean = np.mean(data2) #calculate the mean (average)
print(int(mean))
std_dev = np.std(data2) #standard deviation of the values in the data array
print(std_dev) #σ = √(Σ(xi - μ)² / N)
#Array Indexing and Slicing
data = np.array([2,4,6,8])
print(data[0])
print(data[1:3])
#Array Broadcasting: operation on array in diffrerent shape
data3 = np.array([1,2,3,4,5])
scalar = 2
result = data3 * scalar
print("Result after broadcusting:",result)
#Aggregation and Reduction such as sum , means and statical calculation
data4 = np.array([[1,2,3],[4,5,6]])
row_sum = np.sum(data4, axis=0)#axis=0 refers to the rows (vertical axis)
print(row_sum)#row_sum = [1+4, 2+5, 3+6] = [5, 7, 9]
#comperison or logicak expression
comp = data3[data3 > 2]
print(comp)
#Liner algebra: Linear Algebra: NumPy includes functions for linear algebra operations, such as matrix multiplication, eigenvalue calculations, and solving linear equations, which are essential for many data analysis tasks.
import numpy as np
matrics_a = np.array([[1,2],[3,4]])
matrics_b = np.array([[5,6],[7,8]])
mat_mul = np.dot(matrics_a,matrics_b)
print("Matrics multiplication:",mat_mul)