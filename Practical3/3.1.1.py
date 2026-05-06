import numpy as np

rows,cols=map(int, input().split())
elements=[ ]
for _ in range(rows):
	elements.extend(map(int, input().split()))
array=np.array(elements).reshape(rows,cols)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)
