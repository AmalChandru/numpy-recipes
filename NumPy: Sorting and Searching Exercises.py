#1. Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array.
import numpy as np
a = np.array([[10,40],[30,20]])
print("Original array:")
print(a)
print("Sort the array along the first axis:")
print(np.sort(a, axis=0))
print("Sort the array along the last axis:")
print(np.sort(a))
print("Sort the flattened array:")
print(np.sort(a, axis=None))
#2. Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort the array on height.
import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))
#3. Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort by class, then height if class are equal
import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by class, then height if class are equal:")
print(np.sort(students, order=['class', 'height']))
#4. Write a NumPy program to sort the student id with increasing height of the students from given students id and height. Print the integer indices that describes the sort order by multiple columns and the sorted data.
import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
#Sort by studen_id then by student_height
indices = np.lexsort((student_id, student_height))
print("Sorted indices:")
print(indices)
print("Sorted data:")
for n in indices:
  print(student_id[n], student_height[n])
#5. Write a NumPy program to get the indices of the sorted elements of a given array.
import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
print("Original array:")
print(student_id)
i = np.argsort(student_id)
print("Indices of the sorted elements of a given array:")
print(i)
#6. Write a NumPy program to sort a given complex array using the real part first, then the imaginary part
import numpy as np
complex_num = [1 + 2j, 3 - 1j, 3 - 2j, 4 - 3j, 3 + 5j]
print("Original array:")
print(complex_num)
print("\nSorted a given complex array using the real part first, then the imaginary part.")
print(np.sort_complex(complex_num))
#7. Write a NumPy program to partition a given array in a specified position and move all the smaller elements values to the left of the partition, and the remaining values to the right, in arbitrary order (based on random choice).

import numpy as np
nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])
print("Original array:")
print(nums)
print("\nAfter partitioning on 4 the position:")
print(np.partition(nums, 4))
#8. Write a NumPy program to sort the specified number of elements from beginning of a given array.
import numpy as np
nums =  np.random.rand(10)
print("Original array:")
print(nums)
print("\nSorted first 5 elements:")
print(nums[np.argpartition(nums,range(5))])