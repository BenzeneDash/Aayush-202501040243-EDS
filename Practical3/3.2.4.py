import numpy as np

def array_operations(A, B):

	# Convert A and B to NumPy arrays
	arr1 = np.array(A)
	arr2 = np.array(B)
	# Arithmetic Operations
	sum_result = arr1+arr2
	diff_result = arr1-arr2
	prod_result = arr1*arr2

	# Statistical Operations
	mean_A = np.mean(arr1)
	median_A = np.median(arr1)
	std_dev_A = np.std(arr1)

	# Bitwise Operations
	and_result = arr1 & arr2
	or_result = arr1 | arr2
	xor_result = arr1^arr2

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  # Elements of array A
B = list(map(int, input().split()))  # Elements of array B
array_operations(A, B)
