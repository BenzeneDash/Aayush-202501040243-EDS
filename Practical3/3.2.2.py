import numpy as np

# Input matrices
print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

# Perform horizontal stacking (hstack)
a = np.hstack((arr1,arr2))
print("Horizontal Stack:")
print(a)
# Perform vertical stacking (vstack)
b = np.vstack((arr1,arr2))
print("Vertical Stack:")
print(b)
