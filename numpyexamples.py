#linspace
#vstack
#hstack
import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

zeros_arr = np.zeros(5)  # Creates a 1D array of 5 zeros
print(zeros_arr)

arr = np.array([10, 20, 30, 40, 50])
element = arr[2]  # Access the third element (zero-based index)
print(element)

# Create an array of zeros
zeros_array = np.zeros((3, 4))  # 3 rows, 4 columns

arr = np.array([10, 20, 30, 40, 50])
slice = arr[1:4]  # Get elements from index 1 (inclusive) to 4 (exclusive)
print(slice)

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

import numpy as np
#Transposing a 2D matrix 
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Transpose the matrix
transposed_matrix = np.transpose(matrix)

# Alternatively, you can also use the .T attribute
# transposed_matrix = matrix.T

print("Original Matrix:")
print(matrix)
print("Transposed Matrix:")
print(transposed_matrix)

'''
Output:
Original Matrix:
[[1 2 3]
 [4 5 6]]
Transposed Matrix:
[[1 4]
 [2 5]
 [3 6]]
'''
