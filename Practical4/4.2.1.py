import pandas as pd

file_name = input().strip()

df = pd.read_csv(file_name)

df["Date"] = pd.to_datetime(df["Date"])
df["Sales"] = df["Quantity"] * df["Price"]
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Sales"].sum()

best_month = monthly_sales.idxmax()
best_sales = monthly_sales.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${best_sales:.2f}")
