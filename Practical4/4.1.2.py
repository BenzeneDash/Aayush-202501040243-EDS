'''
import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
name = input("New name: ")
age = int(input("New age: "))
df.loc[len(df)] = [name, age]
# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
idx_mod = int(input("Index of row to modify: "))
new_age = int(input("New age: "))
df.at[idx_mod, 'Age'] = new_age
# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
idx_del = int(input("Index of row to delete: "))
df = df.drop(idx_del)
# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
genders = input("Enter genders separated by space: ").split()
df["Gender"] = genders

# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df["Name"] = df["Name"].str.upper()
# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop(columns=["Age"])

# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
'''
import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
name = input("New name: ")
age = int(input("New age: "))
df.loc[len(df)] = [name, age]

print("After adding a row:\n",df)
# print(df)

# Modifying a row
idx_mod = int(input("Index of row to modify: "))
new_age = int(input("New age: "))
df.at[idx_mod, 'Age'] = new_age

print("After modifying a row:")
print(df)

# Deleting a row
idx_del = int(input("Index of row to delete: "))
df = df.drop(idx_del).reset_index(drop=True)

print("After deleting a row:")
print(df)

# Adding a new column
genders = input("Enter genders separated by space: ").split()
df["Gender"] = genders

print("After adding a new column:")
print(df)

# Modifying a column
df["Name"] = df["Name"].str.upper()

print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop(columns=["Age"])

print("After deleting a column:")
print(df)

