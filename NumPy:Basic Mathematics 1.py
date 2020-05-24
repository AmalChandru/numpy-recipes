#1. Write a NumPy program to add, subtract, multiply, divide arguments element-wise.
import numpy as np
print("Add:")
print(np.add(1.0, 4.0))
print("Subtract:")
print(np.subtract(1.0, 4.0))
print("Multiply:")
print(np.multiply(1.0, 4.0))
print("Divide:")
print(np.divide(1.0, 4.0))
#2. Write a NumPy program to compute logarithm of the sum of exponentiations of the inputs, sum of exponentiations of the inputs in base-2.
import numpy as np
l1 = np.log(1e-50)
l2 = np.log(2.5e-50)
print("Logarithm of the sum of exponentiations:")
print(np.logaddexp(l1, l2))
print("Logarithm of the sum of exponentiations of the inputs in base-2:")
print(np.logaddexp2(l1, l2))
#3. Write a NumPy program to get true division of the element-wise array inputs.
import numpy as np
x = np.arange(10)
print("Original array:")
print(x)
print("Division of the array inputs, element-wise:")
print(np.true_divide(x, 3))
#4. Write a NumPy program to get the largest integer smaller or equal to the division of the inputs.
import numpy as np
x = [1., 2., 3., 4.]
print("Original array:")
print(x)
print("Largest integer smaller or equal to the division of the inputs:")
print(np.floor_divide(x, 1.5))
#5. Write a NumPy program to get the powers of an array values element-wise.
import numpy as np
x = np.arange(7)
print("Original array")
print(x)
print("First array elements raised to powers from second array, element-wise:")
print(np.power(x, 3))
#6. Write a NumPy program to get the element-wise remainder of an array of division.
import numpy as np
x = np.arange(7)
print("Original array:")
print(x)
print("Element-wise remainder of division:")
print(np.remainder(x, 5))
#7. Write a NumPy program to calculate the absolute value element-wise.
import numpy as np
x = np.array([-10.2, 122.2, .20])
print("Original array:")
print(x)
print("Element-wise absolute value:")
print(np.absolute(x))
#8. Write a NumPy program to round array elements to the given number of decimals.
import numpy as np
x = np.round([1.45, 1.50, 1.55])
print(x)
x = np.round([0.28, .50, .64], decimals=1)
print(x)
x = np.round([.5, 1.5, 2.5, 3.5, 4.5]) # rounds to nearest even value
print(x)
#9. Write a NumPy program to round elements of the array to the nearest integer.
import numpy as np
x = np.array([-.7, -1.5, -1.7, 0.3, 1.5, 1.8, 2.0])
print("Original array:")
print(x)
x = np.rint(x)
print("Round elements of the array to the nearest integer:")
print(x)
#10. Write a NumPy program to get the floor, ceiling and truncated values of the elements of a numpy array.
import numpy as np
x = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 1.8, 2.0])
print("Original array:")
print(x)
print("Floor values of the above array elements:")
print(np.floor(x))
print("Ceil values of the above array elements:")
print(np.ceil(x))
print("Truncated values of the above array elements:")
print(np.trunc(x))
#11. Write a NumPy program to multiply a 5x3 matrix by a 3x2 matrix and create a real matrix product.
import numpy as np
x = np.random.random((5,3))
print("First array:")
print(x)
y = np.random.random((3,2))
print("Second array:")
print(y)
z = np.dot(x, y)
print("Dot product of two arrays:")
print(z)
#12. Write a NumPy program to multiply a matrix by another matrix of complex numbers and create a new matrix of complex numbers.
import numpy as np
x = np.array([1+2j,3+4j])
print("First array:")
print(x)
y = np.array([5+6j,7+8j])
print("Second array:")
print(y)
z = np.vdot(x, y)
print("Product of above two arrays:")
print(z)
#13. Write a NumPy program to create an inner product of two arrays.
import numpy as np
x = np.arange(24).reshape((2,3,4))
print("Array x:")
print(x)
print("Array y:")
y = np.arange(4)
print(y)
print("Inner of x and y arrays:")
print(np.inner(x, y))
#14. Write a NumPy program to generate inner, outer, and cross products of matrices and vectors.
import numpy as np
x = np.array([1, 4, 0], float)
y = np.array([2, 2, 1], float)
print("Matrices and vectors.")
print("x:")
print(x)
print("y:")
print(y)
print("Inner product of x and y:")
print(np.inner(x, y))
print("Outer product of x and y:")
print(np.outer(x, y))
print("Cross product of x and y:")
print(np.cross(x, y))
#15. Write a NumPy program to generate a matrix product of two arrays.
import numpy as np
x = [[1, 0], [1, 1]]
y = [[3, 1], [2, 2]]
print("Matrices and vectors.")
print("x:")
print(x)
print("y:")
print(y)
print("Matrix product of above two arrays:")
print(np.matmul(x, y))
#16. Write a NumPy program to find the roots of the following polynomials.
import numpy as np
print("Roots of the first polynomial:")
print(np.roots([1, -2, 1]))
print("Roots of the second polynomial:")
print(np.roots([1, -12, 10, 7, -10]))
#17. Write a NumPy program to compute the following polynomial values
import numpy as np
print("Polynomial value when x = 2:")
print(np.polyval([1, -2, 1], 2))
print("Polynomial value when x = 3:")
print(np.polyval([1, -12, 10, 7, -10], 3))
#19. Write a NumPy program to calculate mean across dimension, in a 2D numpy array.
import numpy as np
x = np.array([[10, 30], [20, 60]])
print("Original array:")
print(x)
print("Mean of each column:")
print(x.mean(axis=0))
print("Mean of each row:")
print(x.mean(axis=1))
#20. Write a NumPy program to create a random array with 1000 elements and compute the average, variance, standard deviation of the array elements.
import numpy as np
x = np.random.randn(1000)
print("Average of the array elements:")
mean = x.mean()
print(mean)
print("Standard deviation of the array elements:")
std = x.std()
print(std)
print("Variance of the array elements:")
var = x.var()
print(var)
