import pandas as pd
import sqlite3

# Load processed data
df = pd.read_csv('../output/processed_sales_data.csv')

conn = sqlite3.connect('../sql/retail.db')
cursor = conn.cursor()

with open('../sql/star_schema.sql', 'r') as f:
    cursor.executescript(f.read())

products = df[['product', 'category']].drop_duplicates()
products.to_sql('product_dim', conn, if_exists='append', index=False)

cities = df[['city']].drop_duplicates()
cities.to_sql('city_dim', conn, if_exists='append', index=False)

dates = df[['order_date']].drop_duplicates()
dates.to_sql('date_dim', conn, if_exists='append', index=False)

product_dim = pd.read_sql('SELECT * FROM product_dim', conn)
city_dim = pd.read_sql('SELECT * FROM city_dim', conn)
date_dim = pd.read_sql('SELECT * FROM date_dim', conn)

df = df.merge(product_dim, on=['product', 'category'])
df = df.merge(city_dim, on='city')
df = df.merge(date_dim, on='order_date')

fact_df = df[['order_id', 'date_id', 'product_id', 'city_id', 'quantity', 'total_sales']]

fact_df.to_sql('sales_fact', conn, if_exists='append', index=False)

print("Star schema created successfully!")

conn.close()