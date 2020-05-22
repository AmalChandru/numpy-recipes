#1. Write a NumPy program to concatenate element-wise two arrays of string.
import numpy as np
x1 = np.array(['Python', 'PHP'], dtype=np.str)
x2 = np.array([' Java', ' C++'], dtype=np.str)
print("Array1:")
print(x1)
print("Array2:")
print(x2)
new_array = np.char.add(x1, x2)
print("new array:")
print(new_array)
#2. Write a NumPy program to repeat all the elements three times of a given array of string
import numpy as np
x1 = np.array(['Python', 'PHP', 'Java', 'C++'], dtype=np.str)
print("Original Array:")
print(x1)
new_array = np.char.multiply(x1, 3)
print("New array:")
print(new_array)
#3. Write a NumPy program to capitalize the first letter, lowercase, uppercase, swapcase, title-case of all the elements of a given array.
import numpy as np
x = np.array(['python', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
capitalized_case = np.char.capitalize(x)
lowered_case = np.char.lower(x)
uppered_case = np.char.upper(x)
swapcased_case = np.char.swapcase(x)
titlecased_case = np.char.title(x)
print("\nCapitalized: ", capitalized_case)
print("Lowered: ", lowered_case)
print("Uppered: ", uppered_case)
print("Swapcased: ", swapcased_case)
print("Titlecased: ", titlecased_case)
#4. Write a NumPy program to make the length of each element 15 of a given array and the string centered / left-justified / right-justified with paddings of _.
import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
centered = np.char.center(x, 15, fillchar='_')
left = np.char.ljust(x, 15, fillchar='_')
right = np.char.rjust(x, 15, fillchar='_')
print("\nCentered =", centered)
print("Left =", left)
print("Right =", right)
#5. Write a NumPy program to insert a space between characters of all the elements of a given array.
import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.join(" ", x)
print(r)
#6. Write a NumPy program to encode all the elements of a given array in cp500 and decode it again.
import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
encoded_char = np.char.encode(x, 'cp500')
decoded_char = np.char.decode(encoded_char,'cp500')
print("\nencoded =", encoded_char)
print("decoded =", decoded_char)
#7. Write a NumPy program to remove the leading and trailing whitespaces of all the elements of a given array.
import numpy as np
x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
print("Original Array:")
print(x)
stripped = np.char.strip(x)
print("\nRemove the leading and trailing whitespaces: ", stripped)
#8. Write a NumPy program to remove the leading whitespaces of all the elements of a given array.
import numpy as np
x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
print("Original Array:")
print(x)
lstripped_char = np.char.lstrip(x)
print("\nRemove the leading whitespaces : ", lstripped_char)
#9. Write a NumPy program to remove the trailing whitespaces of all the elements of a given array.
import numpy as np
x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
print("Original Array:")
print(x)
rstripped_char = np.char.rstrip(x)
print("\nRemove the trailing whitespaces : ", rstripped_char)
#10. Write a NumPy program to split the element of a given array with spaces.
import numpy as np
x = np.array(['Python PHP Java C++'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.split(x)
print("\nSplit the element of the said array with spaces: ")
print(r)
#11. Write a NumPy program to split the element of a given array to multiple lines
import numpy as np
x = np.array(['Python\Exercises, Practice, Solution'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.splitlines(x)
print(r)
#12. Write a NumPy program to make all the elements of a given string to a numeric string of 5 digits with zeros on its left.
import numpy as np
x = np.array(['2', '11', '234', '1234', '12345'], dtype=np.str)
print("\nOriginal Array:")
print(x)
r = np.char.zfill(x, 5)
print("\nNumeric string of 5 digits with zeros:")
print(r)
#13. Write a NumPy program to replace "PHP" with "Python" in the element of a given array.
import numpy as np
x = np.array(['PHP Exercises, Practice, Solution'], dtype=np.str)
print("\nOriginal Array:")
print(x)
r = np.char.replace(x, "PHP", "Python")
print("\nNew array:")
print(r)
#14. Write a NumPy program to test equal, not equal, greater equal, greater and less test of all the elements of two given arrays.
import numpy as np
x1 = np.array(['Hello', 'PHP', 'JS', 'examples', 'html'], dtype=np.str)
x2 = np.array(['Hello', 'php', 'Java', 'examples', 'html'], dtype=np.str)
print("\nArray1:")
print(x1)
print("Array2:")
print(x2)
print("\nEqual test:")
r = np.char.equal(x1, x2)
print(r)
print("\nNot equal test:")
r = np.char.not_equal(x1, x2)
print(r)
print("\nLess equal test:")
r = np.char.less_equal(x1, x2)
print(r)
print("\nGreater equal test:")
r = np.char.greater_equal(x1, x2)
print(r)
print("\nLess test:")
r = np.char.less(x1, x2)
print(r)
#15. Write a NumPy program to count the number of "P" in a given array, element-wise.
import numpy as np
x1 = np.array(['Python', 'PHP', 'JS', 'examples', 'html'], dtype=np.str)
print("\nOriginal Array:")
print(x1)
print("Number of ‘P’:")
r = np.char.count(x1, "P")
print(r)
#16. Write a NumPy program to count the lowest index of "P" in a given array, element-wise.
import numpy as np
x1 = np.array(['Python', 'PHP', 'JS', 'EXAMPLES', 'HTML'], dtype=np.str)
print("\nOriginal Array:")
print(x1)
print("count the lowest index of ‘P’:")
r = np.char.find(x1, "P")
print(r)
#17. Write a NumPy program to check whether each element of a given array is composed of digits only, lower case letters only and upper case letters only.
import numpy as np
x = np.array(['Python', 'PHP', 'JS', 'Examples', 'html5', '5'], dtype=np.str)
print("\nOriginal Array:")
print(x)
r1 = np.char.isdigit(x)
r2 = np.char.islower(x)
r3 = np.char.isupper(x)
print("Digits only =", r1)
print("Lower cases only =", r2)
print("Upper cases only =", r3)
