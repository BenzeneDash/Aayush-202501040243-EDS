import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df["Survived"].value_counts().sort_index().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()
