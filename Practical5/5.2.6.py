import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df = pd.get_dummies(df, columns=["Embarked"])

survival_by_embarked_q = df.groupby("Embarked_Q")["Survived"].value_counts().unstack(fill_value=0)

survival_by_embarked_q.plot(kind="bar", stacked=True)
plt.title("Survival by Embarked ")
plt.xlabel("Embarked")
plt.ylabel("Count")
plt.legend(["Not Survived", "Survived"])
plt.show()
