import pandas as pd

def preprocess_data(df):
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Sort data by date
    df = df.sort_values(by='date')
    
    # Check missing values
    print("\nMissing Values:\n", df.isnull().sum())
    
    # Handle missing values (if any)
    df = df.dropna()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Reset index
    df = df.reset_index(drop=True)
    
    print("\nData after cleaning:")
    print(df.head())
    
    return df