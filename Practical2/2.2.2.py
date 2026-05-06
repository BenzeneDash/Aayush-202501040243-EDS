# Read input (11 space-separated integers)
heights = list(map(int, input().split()))

# Find tallest player
tallest = max(heights)

# Output result
print(tallest)
