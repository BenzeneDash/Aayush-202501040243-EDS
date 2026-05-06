import pandas as pd

file_name = input().strip()

df = pd.read_csv(file_name)

df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

print(df[df["Survived"] == 1]["Sex"].value_counts())
print(df[df["Survived"] == 0]["Sex"].value_counts())
print(df[df["Survived"] == 1]["Embarked_S"].value_counts())
print(df[df["Survived"] == 0]["Embarked_S"].value_counts())

children = df[df["Age"] < 18]
adults = df[df["Age"] >= 18]

print(children["Survived"].mean())
print(adults["Survived"].mean())

print(df[df["Survived"] == 1]["Age"].median())
print(df[df["Survived"] == 0]["Age"].median())
print(df[df["Survived"] == 1]["Fare"].median())
print(df[df["Survived"] == 0]["Fare"].median())
