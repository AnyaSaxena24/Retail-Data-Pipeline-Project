<<<<<<< HEAD
from transformation import load_data, clean_data, transform_data, validate_data, save_data

df = load_data('../data/sales_data.csv')

df = clean_data(df)

df = transform_data(df)

df = validate_data(df)

=======
from transformation import load_data, clean_data, transform_data, validate_data, save_data

df = load_data('../data/sales_data.csv')

df = clean_data(df)

df = transform_data(df)

df = validate_data(df)

>>>>>>> 0ba55a4fda3736f5faf58da868efe97116708868
save_data(df, '../output/processed_sales_data.csv')