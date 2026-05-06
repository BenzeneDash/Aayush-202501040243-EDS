import pandas as pd

file_name = input().strip()

df = pd.read_csv(file_name)

df["FamilySize"] = df["SibSp"] + df["Parch"]
df["IsAlone"] = df["FamilySize"].apply(lambda x: 1 if x == 0 else 0)

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

print(df["Age"].mean())
print(df["Fare"].median())
print(df["Pclass"].value_counts())
print(df["Sex"].value_counts())
print(df["Survived"].value_counts())
print(df["Survived"].mean())
print(df.groupby("Sex")["Survived"].mean())
