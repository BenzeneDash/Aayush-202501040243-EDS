import pandas as pd
from itertools import combinations
from collections import Counter

file_name = input().strip()

df = pd.read_csv(file_name)

pair_counts = Counter()

for _, group in df.groupby("Date"):
    products = sorted(group["Product"].unique())
    for pair in combinations(products, 2):
        pair_counts[pair] += 1

max_count = max(pair_counts.values())

for pair, count in sorted(pair_counts.items()):
    if count == max_count:
        print(f"{pair[0]} and {pair[1]}: {count} times")
