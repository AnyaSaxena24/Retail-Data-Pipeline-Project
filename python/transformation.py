<<<<<<< HEAD
import pandas as pd

def load_data(path):
    """Load CSV data"""
    df = pd.read_csv(path)
    print("Data loaded successfully")
    return df


def clean_data(df):
    """Handle missing values"""
    df = df.dropna()
    print("Data cleaned")
    return df


def transform_data(df):
    """Create new features"""
    df['total_sales'] = df['quantity'] * df['price']
    print("Transformation complete")
    return df


def validate_data(df):
    """Basic validation checks"""
    if (df['quantity'] < 0).any():
        print("Warning: Negative quantity found")
    if (df['price'] < 0).any():
        print("Warning: Negative price found")
    print("Validation done")
    return df


def save_data(df, path):
    """Save processed data"""
    df.to_csv(path, index=False)
=======
import pandas as pd

def load_data(path):
    """Load CSV data"""
    df = pd.read_csv(path)
    print("Data loaded successfully")
    return df


def clean_data(df):
    """Handle missing values"""
    df = df.dropna()
    print("Data cleaned")
    return df


def transform_data(df):
    """Create new features"""
    df['total_sales'] = df['quantity'] * df['price']
    print("Transformation complete")
    return df


def validate_data(df):
    """Basic validation checks"""
    if (df['quantity'] < 0).any():
        print("Warning: Negative quantity found")
    if (df['price'] < 0).any():
        print("Warning: Negative price found")
    print("Validation done")
    return df


def save_data(df, path):
    """Save processed data"""
    df.to_csv(path, index=False)
>>>>>>> 0ba55a4fda3736f5faf58da868efe97116708868
    print("Data saved successfully")