import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# 1. Bar Plot - Pclass Distribution
pclass_counts = df["Pclass"].value_counts().sort_index()
axes[0, 0].bar(pclass_counts.index, pclass_counts.values, color="skyblue")
axes[0, 0].set_title("Passenger Class Distribution")
axes[0, 0].set_xlabel("Pclass")
axes[0, 0].set_ylabel("Count")

# 2. Pie Chart - Gender Distribution
gender_counts = df["Gender"].value_counts()
axes[0, 1].pie(
    gender_counts.values,
    labels=gender_counts.index,
    colors=["lightblue", "lightcoral"],
    autopct="%1.1f%%"
)
axes[0, 1].set_title("Gender Distribution")

# 3. Histogram - Age Distribution
axes[1, 0].hist(df["Age"].dropna(), bins=8, color="lightgreen", edgecolor="black")
axes[1, 0].set_title("Age Distribution")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Frequency")

# 4. Bar Plot - Survival Count
survival_counts = df["Survived"].value_counts().sort_index()
axes[1, 1].bar(survival_counts.index, survival_counts.values, color=["lightcoral", "lightblue"])
axes[1, 1].set_title("Survival Count")
axes[1, 1].set_xlabel("Survived (0 = No, 1 = Yes)")
axes[1, 1].set_ylabel("Count")

# 5. Scatter Plot - Fare vs Age
axes[2, 0].scatter(df["Age"], df["Fare"], color="orange")
axes[2, 0].set_title("Fare vs Age")
axes[2, 0].set_xlabel("Age")
axes[2, 0].set_ylabel("Fare")

# Hide the unused subplot
axes[2, 1].axis("off")

plt.tight_layout()
plt.show()
