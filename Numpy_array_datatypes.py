#NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
import numpy as np
# int 8 to 64 : 'i'
arr = np.array([0, 100, 5])
print("Type of the array:", arr.dtype) #np using 'dtype' for represent data types

# 'U' unicode string
arr1 = np.array(["apple","banana","cherry"])
print("String type called:",arr1.dtype)

#Creating Arrays With a Defined Data Type: using dtype as a argument for expected d-type
arr2 = np.array([10,99,200], dtype = np.uint8)
print("NumPy array of unsigned 8-bit integers",arr2)

#Create an array with data type string: one character string representaion
arr3 = np.array([1,2,3,4,5], dtype='S') # you can use: dtype = 'f'/'i'
print("Representing string type:",arr3)

#Converting Data Type on Existing Arrays
#The 'astype()' function creates a copy of the array, and allows you to specify the data type as a parameter.
arr4 = np.array([1.2, 3.4, 0.75])
newarr = arr4.astype("int")
print("Converted float as a int:",newarr)
print(newarr.dtype)

#Change data type from integer to boolean:
arr5 = np.array([1, 0, 3, 100])
newarr1 = arr5.astype(bool)
print("Checking booleans:",newarr1)
print(newarr1)

#dtype = timedelta64: is a data type used to represent time durations or time intervals
import numpy as np

# Creating timedelta objects
delta1 = np.timedelta64(5, 'D')  # 5 days
delta2 = np.timedelta64(3, 'h')  # 3 hours
delta3 = np.timedelta64(30, 'm')  # 30 minutes
delta4 = np.timedelta64(150, 's')  # 150 seconds
print("How musch day timedate:",delta1)

#calculating the difference between two dates or adding a certain time duration to a date.
result1 = delta1 + delta2  # Adding timedelta objects
result2 = delta3 - delta4  # Subtracting timedelta objects
result3 = delta1 * 2       # Multiplying a timedelta by a scalar
print("how musch hours bro:",result1)
print("How much days after multiply:",result3)




#Date & time data type: dtype = datetime64()
datetime_with_tz = np.datetime64('2023-09-21T15:30:00-0500', 's')
print("Date & time for spesific time zone:",datetime_with_tz)

#dtype = object: object data type is a generic data type that can hold any Python object. 
#dtype = unicode:  Unicode is a character encoding standard that provides a unique code point for every character

