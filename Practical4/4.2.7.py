import pandas as pd

file_name = input().strip()

df = pd.read_csv(file_name)

df["FamilySize"] = df["SibSp"] + df["Parch"]
df["IsAlone"] = df["FamilySize"].apply(lambda x: 1 if x == 0 else 0)

df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

print(df.groupby("Pclass")["Survived"].mean())
print(df.groupby("Embarked_S")["Survived"].mean())
print(df.groupby("FamilySize")["Survived"].mean())
print(df.groupby("IsAlone")["Survived"].mean())
print(df.groupby("Pclass")["Fare"].mean())
print(df.groupby("Pclass")["Age"].mean())
print(df.groupby("Survived")["Age"].mean())
print(df.groupby("Survived")["Fare"].mean())
print(df[df["Survived"] == 1]["Pclass"].value_counts())
print(df[df["Survived"] == 0]["Pclass"].value_counts())
