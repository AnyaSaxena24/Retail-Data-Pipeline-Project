CREATE TABLE product_dim (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    category TEXT
);

CREATE TABLE city_dim (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT
);

CREATE TABLE date_dim (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT
);

CREATE TABLE sales_fact (
    order_id INTEGER,
    date_id INTEGER,
    product_id INTEGER,
    city_id INTEGER,
    quantity INTEGER,
    total_sales REAL
);