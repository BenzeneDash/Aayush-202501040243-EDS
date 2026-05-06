import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df.boxplot(column="Fare", by="Pclass")
plt.title("Fare by Pclass")
plt.suptitle("")
plt.xlabel("Pclass")
plt.ylabel("Fare")
plt.show()
