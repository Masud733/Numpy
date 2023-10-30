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
print("how musch day and hours bro:",result1)
print("How much days after multiply:",result3)


import numpy as np

# Creating a datetime array
dates = np.array(['2023-09-21', '2023-09-22', '2023-09-23'], dtype='datetime64')

# Adding a timedelta to the datetime array
new_dates = dates + np.timedelta64(7, 'D')

# Computing the time difference between two datetime arrays
time_diff = new_dates - dates
print(time_diff)