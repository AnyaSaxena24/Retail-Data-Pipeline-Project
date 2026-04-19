from transformation import load_data, clean_data, transform_data, validate_data, save_data

# Step 1: Load data
df = load_data('../data/sales_data.csv')

# Step 2: Clean data
df = clean_data(df)

# Step 3: Transform data
df = transform_data(df)

# Step 4: Validate data
df = validate_data(df)

# Step 5: Save processed data
save_data(df, '../output/processed_sales_data.csv')

print("Pipeline executed successfully!")