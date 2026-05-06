import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

colors = df["Survived"].map({0: "red", 1: "blue"})

plt.scatter(df["Age"], df["Fare"], c=colors)
plt.title("Age vs. Fare by Survival")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
