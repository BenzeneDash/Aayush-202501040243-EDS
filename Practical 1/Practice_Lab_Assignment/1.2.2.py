def fibonacci(n):
    # Base cases: return 0 for the first term and 1 for the second term
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    # Recursive step: sum of the two preceding terms
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
for i in range(1, n + 1):
    print(fibonacci(i), end=" ")

