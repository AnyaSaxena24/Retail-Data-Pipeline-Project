import pandas as pd
import sqlite3

df = pd.read_csv('../output/processed_sales_data.csv')

conn = sqlite3.connect('../sql/retail.db')

df.to_sql('sales', conn, if_exists='replace', index=False)

print("Data loaded into database!")

print("\nTotal Revenue:")
query1 = "SELECT SUM(total_sales) FROM sales"
print(pd.read_sql(query1, conn))

print("\nTop Selling Product:")
query2 = """
SELECT product, SUM(quantity) as total_qty
FROM sales
GROUP BY product
ORDER BY total_qty DESC
LIMIT 1
"""
print(pd.read_sql(query2, conn))

print("\nCity-wise Revenue:")
query3 = """
SELECT city, SUM(total_sales) as revenue
FROM sales
GROUP BY city
"""
print(pd.read_sql(query3, conn))

conn.close()