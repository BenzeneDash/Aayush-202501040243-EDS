import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df.boxplot(column="Age", by="Survived")
plt.title("Age by Survival")
plt.suptitle("")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()
