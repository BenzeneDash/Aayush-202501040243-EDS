import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
madd = matrix_a+matrix_b
print("Addition (A + B):")
print(madd)
# Subtraction
mdiff = matrix_a-matrix_b
print("Subtraction (A - B):")
print(mdiff)
# Multiplication (element-wise
mmul = matrix_a*matrix_b
print("Element-wise Multiplication (A * B):")
print(mmul)
# Matrix multiplication (dot product)

print("A dot B:")
print(np.dot(matrix_a,matrix_b))
# Transpose
print("Transpose of A:")
print(matrix_a.T)
