import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('../sql/retail.db')

# Query 1: Total Sales
query1 = "SELECT SUM(total_sales) AS total_revenue FROM sales;"
df1 = pd.read_sql(query1, conn)
print("\nTotal Revenue:")
print(df1)

# Query 2: Top Product
query2 = """
SELECT product, SUM(total_sales) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 1;
"""
df2 = pd.read_sql(query2, conn)
print("\nTop Selling Product:")
print(df2)

# Query 3: City-wise Sales
query3 = """
SELECT city, SUM(total_sales) AS revenue
FROM sales
GROUP BY city;
"""
df3 = pd.read_sql(query3, conn)
print("\nCity-wise Sales:")
print(df3)

conn.close()
