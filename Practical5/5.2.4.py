import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

survival_by_gender = df.groupby("Sex")["Survived"].value_counts().unstack()

survival_by_gender.plot(kind="bar", stacked=True)
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(["Not Survived", "Survived"])
plt.show()
