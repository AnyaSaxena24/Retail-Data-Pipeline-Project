import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title(" Retail Data Dashboard")

# Load data
df = pd.read_csv('../output/processed_sales_data.csv')

st.subheader("Dataset Preview")
st.dataframe(df)

# --- Product Sales ---
st.subheader("Sales by Product")
product_sales = df.groupby('product')['total_sales'].sum()
st.bar_chart(product_sales)

# --- City Sales ---
st.subheader("Sales by City")
city_sales = df.groupby('city')['total_sales'].sum()
st.bar_chart(city_sales)

# --- Category Pie Chart ---
st.subheader("Category Distribution")
fig1, ax1 = plt.subplots()
df.groupby('category')['total_sales'].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax1)
st.pyplot(fig1)

# --- Sales Trend ---
st.subheader("Sales Trend")
fig2, ax2 = plt.subplots()
sns.lineplot(x='order_date', y='total_sales', data=df, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)