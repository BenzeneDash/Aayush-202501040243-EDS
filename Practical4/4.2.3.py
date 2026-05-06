import pandas as pd

file_name = input().strip()

df = pd.read_csv(file_name)

city_sales = df.groupby("City")["Quantity"].sum()

best_city = city_sales.idxmax()

print(f"City sold the most products: {best_city}")
