# 1. Write a NumPy program to compute the multiplication of two given matrixes.
import numpy as np

p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the said matrix multiplication:")
print(result1)
# ----------------------------------------------------------------------------------#
# 2. Write a NumPy program to compute the outer product of two given vectors.
import numpy as np

p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result = np.outer(p, q)
print("Outer product of the said two vectors:")
print(result)
# ----------------------------------------------------------------------------------#
# 3. Write a NumPy program to compute the cross product of two given vectors.
import numpy as np

p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)
# ----------------------------------------------------------------------------------#
# 4. Write a NumPy program to compute the determinant of a given square array.
import numpy as np
from numpy import linalg as LA

a = np.array([[1, 0], [1, 2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))
# ----------------------------------------------------------------------------------#
# 5. Write a NumPy program to evaluate Einstein's summation convention of two given multidimensional arrays.
import numpy as np

a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print("Original 1-d arrays:")
print(a)
print(b)
result = np.einsum("n,n", a, b)
print("Einstein’s summation convention of the said arrays:")
print(result)
x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print("Original Higher dimension:")
print(x)
print(y)
result = np.einsum("mk,kn", x, y)
print("Einstein’s summation convention of the said arrays:")
print(result)
# ----------------------------------------------------------------------------------#
# 6. Write a NumPy program to compute the inner product of vectors for 1-D arrays (without complex conjugation) and in higher dimension.
import numpy as np

a = np.array([1, 2, 5])
b = np.array([2, 1, 0])
print("Original 1-d arrays:")
print(a)
print(b)
print
result = np.inner(a, b)
print("Inner product of the said vectors:")
x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print("Higher dimension arrays:")
print(x)
print(y)
result = np.inner(x, y)
print("Inner product of the said vectors:")
print(result)
# ----------------------------------------------------------------------------------#
# 7. Write a NumPy program to compute the eigenvalues and right eigenvectors of a given square array.
import numpy as np

m = np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n", m)
w, v = np.linalg.eig(m)
print("Eigenvalues of the said matrix", w)
print("Eigenvectors of the said matrix", v)
# ----------------------------------------------------------------------------------#
# 8. Write a NumPy program to compute the Kronecker product of two given mulitdimension arrays.
import numpy as np

a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print("Original 1-d arrays:")
print(a)
print(b)
result = np.kron(a, b)
print("Kronecker product of the said arrays:")
print(result)
x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print("Original Higher dimension:")
print(x)
print(y)
result = np.kron(x, y)
print("Kronecker product  of the said arrays:")
print(result)
# ----------------------------------------------------------------------------------#
# 9. Write a NumPy program to compute the condition number of a given matrix.
import numpy as np
from numpy import linalg as LA

a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
print("Original matrix:")
print(a)
print("The condition number of the said matrix:")
print(LA.cond(a))
# ----------------------------------------------------------------------------------#
# 10. Write a NumPy program to find a matrix or vector norm.
import numpy as np

v = np.arange(7)
result = np.linalg.norm(v)
print("Vector norm:")
print(result)
m = np.matrix('1, 2; 3, 4')
result1 = np.linalg.norm(m)
print("Matrix norm:")
print(result1)
# ----------------------------------------------------------------------------------#
# 11. Write a NumPy program to compute the determinant of an array.
import numpy as np

a = np.array([[1, 2], [3, 4]])
print("Original array:")
print(a)
result = np.linalg.det(a)
print("Determinant of the said array:")
print(result)
# ----------------------------------------------------------------------------------#
# 12. Write a NumPy program to compute the inverse of a given matrix.
import numpy as np

m = np.array([[1, 2], [3, 4]])
print("Original matrix:")
print(m)
result = np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)
# ----------------------------------------------------------------------------------#
# 13. Write a NumPy program to calculate the QR decomposition of a given matrix.
import numpy as np

m = np.array([[1, 2], [3, 4]])
print("Original matrix:")
print(m)
result = np.linalg.qr(m)
print("Decomposition of the said matrix:")
print(result)
# ----------------------------------------------------------------------------------#
# 14. Write a NumPy program to compute the condition number of a given matrix.
import numpy as np

m = np.array([[1, 2], [3, 4]])
print("Original matrix:")
print(m)
result = np.linalg.cond(m)
print("Condition number of the said matrix:")
print(result)
# ----------------------------------------------------------------------------------#
# 15. Write a NumPy program to compute the sum of the diagonal element of a given array.
import numpy as np

m = np.arange(6).reshape(2, 3)
print("Original matrix:")
print(m)
result = np.trace(m)
print("Condition number of the said matrix:")
print(result)
# ----------------------------------------------------------------------------------#
# 16. Write a NumPy program to get the lower-triangular L in the Cholesky decomposition of a given array.
import numpy as np

a = np.array([[4, 12, -16], [12, 37, -53], [-16, -53, 98]], dtype=np.int32)
print("Original array:")
print(a)
L = np.linalg.cholesky(a)
print("Lower-trianglular L in the Cholesky decomposition of the said array:")
print(L)
# ----------------------------------------------------------------------------------#
# 17. Write a NumPy program to get the qr factorization of a given array.
import numpy as np

a = np.array([[4, 12, -14], [12, 37, -53], [-14, -53, 98]], dtype=np.int32)
print("Original array:")
print(a)
q, r = np.linalg.qr(a)
print("qr factorization of the said array:")
print("q=\n", q, "\nr=\n", r)
# ----------------------------------------------------------------------------------#
# 18. Write a NumPy program to compute the factor of a given array by Singular Value Decomposition.
import numpy as np

a = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]], dtype=np.float32)
print("Original array:")
print(a)
U, s, V = np.linalg.svd(a, full_matrices=False)
q, r = np.linalg.qr(a)
print("Factor of a given array  by Singular Value Decomposition:")
print("U=\n", U, "\ns=\n", s, "\nV=\n", V)
# ----------------------------------------------------------------------------------#
# 19. Write a NumPy program to calculate the Frobenius norm and the condition number of a given array.
import numpy as np

a = np.arange(1, 10).reshape((3, 3))
print("Original array:")
print(a)
print("Frobenius norm and the condition number:")
print(np.linalg.norm(a, 'fro'))
print(np.linalg.cond(a, 'fro'))
# ----------------------------------------------------------------------------------#
