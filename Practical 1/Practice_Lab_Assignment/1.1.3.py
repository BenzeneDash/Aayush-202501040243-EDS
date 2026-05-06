from datetime import date


# Input
y1, m1, d1 = map(int, input().split('-'))
y2, m2, d2 = map(int, input().split('-'))

# Create date objects
date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

# Calculate difference
difference = (date2 - date1).days

# Output
print(difference)
