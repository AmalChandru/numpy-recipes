# 1.Write a NumPy program to get the numpy version and show numpy build configuration.
import numpy as np

print(np.__version__)
print(np.show_config())
# 2. Write a NumPy program to  get help on the add function.
import numpy as np

print(np.info(np.add))
# 3. Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np

x = np.array([1, 2, 3, 4])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
x = np.array([0, 1, 2, 3])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
# 4. Write a NumPy program to test whether any of the elements of a given array is non-zero.
import numpy as np

x = np.array([1, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))
x = np.array([0, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))
# 5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
import numpy as np

a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))
# 6. Write a NumPy program to test element-wise for positive or negative infinity.
import numpy as np

a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for positive or negative infinity:")
print(np.isinf(a))
# 7. Write a NumPy program to test element-wise for NaN of a given array.
import numpy as np

a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for NaN:")
print(np.isnan(a))
# 8. Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.
import numpy as np

a = np.array([1 + 1j, 1 + 0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))
# 9. Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.
import numpy as np

print("Test if two arrays are element-wise equal within a tolerance:")
print(np.allclose([1e10, 1e-7], [1.00001e10, 1e-8]))
print(np.allclose([1e10, 1e-8], [1.00001e10, 1e-9]))
print(np.allclose([1e10, 1e-8], [1.0001e10, 1e-9]))
print(np.allclose([1.0, np.nan], [1.0, np.nan]))
print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True))
# 10. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays
import numpy as np

x = np.array([3, 5])
y = np.array([2, 5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")
print(np.less_equal(x, y))
# 11. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays
import numpy as np

x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("Original numbers:")
print(x)
print(y)
print("Comparison - equal:")
print(np.equal(x, y))
print("Comparison - equal within a tolerance:")
print(np.allclose(x, y))
# 12. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array
import numpy as np

X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))
# 13. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
import numpy as np

array = np.zeros(10)
print("An array of 10 zeros:")
print(array)
array = np.ones(10)
print("An array of 10 ones:")
print(array)
array = np.ones(10) * 5
print("An array of 10 fives:")
print(array)
# 14. Write a NumPy program to create an array of the integers from 30 to70.
import numpy as np

array = np.arange(30, 71)
print("Array of the integers from 30 to70")
print(array)
# 15. Write a NumPy program to create an array of all the even integers from 30 to 70.
import numpy as np

array = np.arange(30, 71, 2)
print("Array of all the even integers from 30 to 70")
print(array)
# 16. Write a NumPy program to create a 3x3 identity matrix.
import numpy as np

array_2D = np.identity(3)
print('3x3 matrix:')
print(array_2D)
# 17. Write a NumPy program to generate a random number between 0 and 1.
import numpy as np

rand_num = np.random.normal(0, 1, 1)
print("Random number between 0 and 1:")
print(rand_num)
# 18. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
import numpy as np

rand_num = np.random.normal(0, 1, 15)
print("15 random numbers from a standard normal distribution:")
print(rand_num)
# 19. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np

v = np.arange(15, 55)
print("Original vector:")
print(v)
print("All values except the first and last of the said vector:")
print(v[1:-1])
# 20. Write a NumPy program to create a 3X4 array using and iterate over it.
import numpy as np

a = np.arange(10, 22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
    print(x, end=" ")
# 20. Write a NumPy program to create a 3X4 array using and iterate over it.
import numpy as np

a = np.arange(10, 22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
    print(x, end=" ")
