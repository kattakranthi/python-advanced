#linspace
#vstack
#hstack
import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Create an array of zeros
zeros_array = np.zeros((3, 4))  # 3 rows, 4 columns

# Create an array of ones
ones_array = np.ones((2, 3))    # 2 rows, 3 columns


print(arr1d)
print(arr2d)
print(zeros_array)
print(ones_array)


arr = np.array([1, 2, 3, 4, 5])

# Basic arithmetic operations
addition = arr + 10
subtraction = arr - 2
multiplication = arr * 3
division = arr / 2

print(addition)
print(subtraction)
print(multiplication)
print(division)


arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[2])  # Access element at index 2

# Slicing
print(arr[1:4])  # Elements from index 1 to 3 (excluding 4)
print(arr[:3])   # Elements from the beginning to index 2
print(arr[2:])   # Elements from index 2 to the end
