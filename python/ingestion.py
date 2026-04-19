from transformation import load_data, clean_data, transform_data, validate_data, save_data

df = load_data('../data/sales_data.csv')

df = clean_data(df)

df = transform_data(df)

df = validate_data(df)

save_data(df, '../output/processed_sales_data.csv')