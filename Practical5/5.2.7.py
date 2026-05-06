import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df.boxplot(column="Age", by="Pclass")
plt.title("Age by Pclass")
plt.suptitle("")
plt.xlabel("Pclass")
plt.ylabel("Age")
plt.show()
