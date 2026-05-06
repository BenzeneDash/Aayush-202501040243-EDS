'''

import pandas as pd

# Take inputs from the user to create a list of numbers
numbers = list(map(int, input().split()))

# Create a Pandas series from the list of numbers

# Grouping by even and odd numbers and calculating the mean
grouped = 

# Display the mean of even and odd numbers with labels
grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]
print("Mean of even and odd numbers:")
print(grouped)
'''
import pandas as pd

# Take inputs from the user to create a list of numbers
numbers = list(map(int, input().split()))

# Create a Pandas series from the list of numbers
s = pd.Series(numbers)

# Grouping by even and odd numbers and calculating the mean
# The lambda function returns True for even and False for odd
grouped = s.groupby(s % 2 == 0).mean()

# Display the mean of even and odd numbers with labels
grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]

# Sort index descending to ensure 'Odd' appears before 'Even' if both exist (matching Test Case 1)
grouped = grouped.sort_index(ascending=False)

print("Mean of even and odd numbers:")
print(grouped)

