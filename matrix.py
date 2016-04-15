import numpy as np
import scipy
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
print(A)
print(linalg.inv(A))
print(scipy.linalg.solve(A, b))
print(A.dot(scipy.linalg.solve(A, b)))
print(A.dot(linalg.inv(A)))  # double check
print(A)
A.
