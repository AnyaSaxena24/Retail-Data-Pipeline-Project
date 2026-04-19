import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('../output/processed_sales_data.csv')

# Set style
sns.set(style="whitegrid")

# 1. Bar Plot (Product vs Sales)
plt.figure()
sns.barplot(x='product', y='total_sales', data=df)
plt.title("Product vs Total Sales")
plt.xticks(rotation=45)
plt.savefig('../output/bar_chart.png')
plt.close()

# 2. Pie Chart (Category Distribution)
category_data = df.groupby('category')['total_sales'].sum()
plt.figure()
category_data.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Distribution")
plt.savefig('../output/pie_chart.png')
plt.close()

# 3. Line Chart (Sales Trend)
plt.figure()
sns.lineplot(x='order_date', y='total_sales', data=df)
plt.xticks(rotation=45)
plt.title("Sales Trend Over Time")
plt.savefig('../output/line_chart.png')
plt.close()

print("Visualizations created successfully!")