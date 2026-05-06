import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

plt.hist(df["Age"].dropna(), bins=30, edgecolor="k")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()
