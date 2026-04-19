import sqlite3

# Connect to database
conn = sqlite3.connect('../sql/retail.db')
cursor = conn.cursor()

# Drop tables if exist (clean rerun)
cursor.execute("DROP TABLE IF EXISTS sales_fact")
cursor.execute("DROP TABLE IF EXISTS product_dim")
cursor.execute("DROP TABLE IF EXISTS city_dim")
cursor.execute("DROP TABLE IF EXISTS date_dim")

# Create dimension tables
cursor.execute("""
CREATE TABLE product_dim AS
SELECT DISTINCT product, category FROM sales;
""")

cursor.execute("""
CREATE TABLE city_dim AS
SELECT DISTINCT city FROM sales;
""")

cursor.execute("""
CREATE TABLE date_dim AS
SELECT DISTINCT order_date FROM sales;
""")

# Create fact table
cursor.execute("""
CREATE TABLE sales_fact AS
SELECT order_id, order_date, city, product, total_sales
FROM sales;
""")

conn.commit()
conn.close()

print("Star schema created successfully!")