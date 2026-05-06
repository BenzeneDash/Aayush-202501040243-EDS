import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

plt.scatter(df["Age"], df["Fare"])
plt.title("Age vs. Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
