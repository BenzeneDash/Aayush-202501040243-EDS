import pandas as pd

# Read the data from the file
df = pd.read_csv("studentdata.txt", sep="\t")

# Display first five rows
print("First five rows:")
print(df.head())

# Calculate average age
avg_age = df["Age"].mean()
print(f"Average age: {avg_age:.2f}")

# Filter students with grade up to B
filtered_df = df[df["Grade"].isin(["A", "B"])]
print("Students with a grade up to B")
print(filtered_df)
