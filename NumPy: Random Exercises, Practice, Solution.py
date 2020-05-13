# 1. Write a NumPy program to generate five random numbers from the normal distribution.
import numpy as np

x = np.random.normal(size=5)
print(x)
# --------------------------------------------------------------------------------------------------#
# 2. Write a NumPy program to generate six random integers between 10 and 30.
import numpy as np

x = np.random.randint(low=10, high=30, size=6)
print(x)
# --------------------------------------------------------------------------------------------------#
# 3. Write a NumPy program to create a 3x3x3 array with random values
import numpy as np

x = np.random.random((3, 3, 3))
print(x)
# --------------------------------------------------------------------------------------------------#
# 4. Write a NumPy program to create a 5x5 array with random values and find the minimum and maximum values.
import numpy as np

x = np.random.random((5, 5))
print("Original Array:")
print(x)
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)
# --------------------------------------------------------------------------------------------------#
# 5. Write a NumPy program to create a random 10x4 array and extract the first five rows of the array and store them into a variable.
import numpy as np

x = np.random.rand(10, 4)
print("Original array: ")
print(x)
y = x[:5, :]
print("First 5 rows of the above array:")
print(y)
# --------------------------------------------------------------------------------------------------#
# 6. Write a NumPy program to shuffle numbers between 0 and 10 (inclusive)
import numpy as np

x = np.arange(10)
np.random.shuffle(x)
print(x)
print("Same result using permutation():")
print(np.random.permutation(10))
# --------------------------------------------------------------------------------------------------#
# 7. Write a NumPy program to normalize a 3x3 random matrix.
import numpy as np

x = np.random.random((3, 3))
print("Original Array:")
print(x)
xmax, xmin = x.max(), x.min()
x = (x - xmin) / (xmax - xmin)
print("After normalization:")
print(x)
# --------------------------------------------------------------------------------------------------#
# 8. Write a NumPy program to create a random vector of size 10 and sort it.
import numpy as np

x = np.random.random(10)
print("Original array:")
print(x)
x.sort()
print("Sorted array:")
print(x)
# --------------------------------------------------------------------------------------------------#
# 9. Write a NumPy program to find the nearest value from a given value in an array.
import numpy as np

x = np.random.uniform(1, 12, 5)
v = 4
n = x.flat[np.abs(x - v).argmin()]
print(n)
# --------------------------------------------------------------------------------------------------#
# 10. Write a NumPy program to check two random arrays are equal or not.
import numpy as np

x = np.random.randint(0, 2, 6)
print("First array:")
print(x)
y = np.random.randint(0, 2, 6)
print("Second array:")
print(y)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(x, y)
print(array_equal)
# --------------------------------------------------------------------------------------------------#
