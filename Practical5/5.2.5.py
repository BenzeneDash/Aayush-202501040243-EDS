import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

survival_by_pclass = df.groupby("Pclass")["Survived"].value_counts().unstack(fill_value=0)

survival_by_pclass.plot(kind="bar", stacked=True)
plt.title("Survival by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.legend(["Not Survived", "Survived"])
plt.show()
