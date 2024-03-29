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
import numpy as np 

data = np.array([1, 2, 3, 4, 5])

# Mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Sum and product of array elements
total = np.sum(data)
product = np.prod(data)

# Sorting
sorted_data = np.sort(data)

'''
3.0
1.4142135623730951
15
120
[1 2 3 4 5]
> 
'''

'''
NumPy broadcasting is a powerful feature that allows NumPy to perform element-wise operations on arrays of different shapes and sizes, without the need for explicitly creating larger arrays to match their shapes. Broadcasting makes it more convenient to work with arrays of different dimensions and simplifies many operations, making your code cleaner and more efficient.
'''
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([10, 20, 30])

result = A + B

# Broadcasting expands B to match the shape of A:
# B becomes [[10, 20, 30], [10, 20, 30]]
# Then, element-wise addition is performed.
'''
[[11 22 33]
 [14 25 36]]

'''

#Scalar array Broadcasting
#The key idea behind broadcasting is to extend smaller arrays to match the shape of larger arrays by implicitly replicating their values along the appropriate dimensions
import numpy as np

scalar = 5
array = np.array([1, 2, 3, 4])
result = scalar * array  
print(result)
'''
[5,10,15,20]
'''

import numpy as np
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([2, 2])
result = array1 * array2  # Broadcasts array2 to [[2, 2], [2, 2]a]
print(result)
'''
[[2 4]
 [6 8]]

'''
