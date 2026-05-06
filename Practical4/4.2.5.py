import pandas as pd

file_name = input().strip()

df = pd.read_csv(file_name)

print(df.head())
print()

print(df.tail())
print()

print(df.shape)

print(df.info())

print(df.describe())
print()

print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop("Cabin", axis=1)
df["FamilySize"] = df["SibSp"] + df["Parch"]
