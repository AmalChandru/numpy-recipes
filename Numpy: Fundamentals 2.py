#21. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
import numpy as np
v = np.linspace(10, 49, 5)
print("Length 10 with values evenly distributed between 5 and 50:")
print(v)
#22. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
import numpy as np
x = np.arange(20)
print("Original vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)
#23. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
import numpy as np
x = np.random.randint(0, 11, 5)
print("Vector of length 5 filled with arbitrary integers from 0 to 10:")
print(x)
#24. Write a NumPy program to multiply the values of two given vectors.
import numpy as np
x = np.array([1, 8, 3, 5])
print("Vector-1")
print(x)
y= np.random.randint(0, 11, 4)
print("Vector-2")
print(y)
result = x * y
print("Multiply the values of two said vectors:")
print(result)
#25. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
import numpy as np
m= np.arange(10,22).reshape((3, 4))
print(m)
#26. Write a NumPy program to find the number of rows and columns of a given matrix.
import numpy as np
m= np.arange(10,22).reshape((3, 4))
print("Original matrix:")
print(m)
print("Number of rows and columns of the said matrix:")
print(m.shape)
#27. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
import numpy as np
x = np.eye(3)
print(x)
#28. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
import numpy as np
x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)
#29. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
import numpy as np
x = np.diag([1, 2, 3, 4, 5])
print(x)
#30. Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
import numpy as np
x = np.zeros((4, 4))
x[::2, 1::2] = 1
x[1::2, ::2] = 1
print(x)
#31. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
import numpy as np
x = np.random.random((3, 3, 3))
print(x)
#32. Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.
import numpy as np
x = np.array([[0,1],[2,3]])
print("Original array:")
print(x)
print("Sum of all elements:")
print(np.sum(x))
print("Sum of each column:")
print(np.sum(x, axis=0))
print("Sum of each row:")
print(np.sum(x, axis=1))
#33. Write a NumPy program to compute the inner product of two given vectors.
import numpy as np
x = np.array([4, 5])
y = np.array([7, 10])
print("Original vectors:")
print(x)
print(y)
print("Inner product of said vectors:")
print(np.dot(x, y))
#34. Write a NumPy program to add a vector to each row of a given matrix.
import numpy as np
m = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 1, 0])
print("Original vector:")
print(v)
print("Original matrix:")
print(m)
result = np.empty_like(m)
for i in range(4):
  result[i, :] = m[i, :] + v
print("\nAfter adding the vector v to each row of the matrix m:")
print(result)
#35. Write a NumPy program to save a given array to a binary file .
import numpy as np
import os
a = np.arange(20)
np.save('temp_arra.npy', a)
print("Check if 'temp_arra.npy' exists or not?")
if os.path.exists('temp_arra.npy'):
    x2 = np.load('temp_arra.npy')
    print(np.array_equal(a, x2))
#36. Write a NumPy program to save two given arrays into a single file in compressed format (.npz format) and load it
import numpy as np
import os
x = np.arange(10)
y = np.arange(11, 20)
print("Original arrays:")
print(x)
print(y)
np.savez('temp_arra.npz', x=x, y=y)
print("Load arrays from the 'temp_arra.npz' file:")
with np.load('temp_arra.npz') as data:
    x2 = data['x']
    y2 = data['y']
    print(x2)
    print(y2)
#37. Write a NumPy program to save a given array to a text file and load it.
import numpy as np
import os
x = np.arange(12).reshape(4, 3)
print("Original array:")
print(x)
header = 'col1 col2 col3'
np.savetxt('temp.txt', x, fmt="%d", header=header)
print("After loading, content of the text file:")
result = np.loadtxt('temp.txt')
print(result)
#38. Write a NumPy program to convert a given array into bytes, and load it as array.
import numpy as np
import os
a = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
print(a)
a_bytes = a.tostring()
a2 = np.fromstring(a_bytes, dtype=a.dtype)
print("After loading, content of the text file:")
print(a2)
print(np.array_equal(a, a2))
#39. Write a NumPy program to convert a given array into a list and then convert it into a list again.
import numpy as np
a = [[1, 2], [3, 4]]
x = np.array(a)
a2 = x.tolist()
print(a == a2)
#40. Write a NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib.
import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.2)
y = np.sin(x)
print("Plot the points using matplotlib:")
plt.plot(x, y)
plt.show()
