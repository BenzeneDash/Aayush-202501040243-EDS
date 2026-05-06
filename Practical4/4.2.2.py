import pandas as pd

file_name = input().strip()

df = pd.read_csv(file_name)

product_sales = df.groupby("Product")["Quantity"].sum()

best_product = product_sales.idxmax()
total_quantity = product_sales.max()

print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {total_quantity}")
