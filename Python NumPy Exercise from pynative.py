# Question 1: Create a 4X2 integer array and Prints its attributes
# Note: The element must be a type of unsigned int16. And print the following Attributes: –
#
# The shape of an array.
# Array dimensions.
# The Length of each element of the array in bytes.
import numpy as np

Array = np.empty([4, 2], dtype=np.uint16)
print("Array Shape is: ", Array.shape)
print("Array dimensions are ", Array.ndim)
print("Length of each element of array in bytes is ", Array.itemsize)
# Question 2: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
import numpy as  np

a = np.arange(100, 200, 10)
b = a.reshape(5, 2)
print(b)
# Question 3: Following is the provided numPy array. return array of items in the third column from all rows
import numpy as np

sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

sampleArray = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

newArray = sampleArray[..., 1]
print(newArray)
# Question 4: Following is the given numpy array return array of odd rows and even columns
import numpy

sampleArray = numpy.array([[3, 6, 9, 12], [15, 18, 21, 24],
                           [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
print("Printing Input Array")
print(sampleArray)

print("\n Printing array of odd rows and even columns")
newArray = sampleArray[::2, 1::2]
print(newArray)
# Question 5: Add the following two NumPy arrays and Modify a result array by calculating the square of each element
# import numpy
#
# arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
# arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])
import numpy

arrayOne = numpy.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = numpy.array([[15, 33, 24], [4, 7, 1]])

resultArray = arrayOne + arrayTwo
print("addition of two arrays is \n")
print(resultArray)

for num in numpy.nditer(resultArray, op_flags=['readwrite']):
    num[...] = num * num
print("\nResult array after calculating the square root of all elements\n")
print(resultArray)
# Question 6: Split the array into four equal-sized sub-arrays
import numpy

print("Creating 8X3 array using numpy.arange")
sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8, 3)
print(sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = numpy.split(sampleArray, 4)
print(subArrays)
# Question 7; Sort following NumPy array
# 7.1- by the second row and
# 7.2-by the second column
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)

sortArrayByRow = sampleArray[:, sampleArray[1, :].argsort()]
print("Sorting Original array by secoond row")
print(sortArrayByRow)

print("Sorting Original array by secoond column")
sortArrayByColumn = sampleArray[sampleArray[:, 1].argsort()]
print(sortArrayByColumn)
# Question 8: Following is the 2-D array. Print max from axis 0 and min from axis 1
# import numpy
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)

minOfAxisOne = numpy.amin(sampleArray, 1)
print("Printing amin Of Axis 1")
print(minOfAxisOne)

maxOfAxisOne = numpy.amax(sampleArray, 0)
print("Printing amax Of Axis 0")
print(maxOfAxisOne)
# Question 9: Following is the input NumPy array delete column two and insert following new column in its place.
# import numpy
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
#
# newColumn = numpy.array([[10,10,10]])
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = numpy.delete(sampleArray, 1, axis=1)
print(sampleArray)

arr = numpy.array([[10, 10, 10]])

print("Array after inserting column 2 on axis 1")
sampleArray = numpy.insert(sampleArray, 1, arr, axis=1)
print(sampleArray)
# Question 10: Create a two 2-D array and Plot it using matplotlib
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = numpy.delete(sampleArray, 1, axis=1)
print(sampleArray)

arr = numpy.array([[10, 10, 10]])

print("Array after inserting column 2 on axis 1")
sampleArray = numpy.insert(sampleArray, 1, arr, axis=1)
print(sampleArray)
