import pandas as pd

def create_features(df):
    
    # Ensure date is datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Sort for time-series consistency
    df = df.sort_values('date')
    
    # ----------------------------
    # TIME FEATURES
    # ----------------------------
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofweek'] = df['date'].dt.dayofweek
    
    # ----------------------------
    # LAG FEATURES (VERY IMPORTANT)
    # ----------------------------
    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)
    df['lag_30'] = df['sales'].shift(30)
    
    # ----------------------------
    # ROLLING FEATURES
    # ----------------------------
    df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()
    df['rolling_mean_30'] = df['sales'].rolling(window=30).mean()
    
    # Drop NaN values created by lagging
    df = df.dropna()
    
    print("\nFeature Engineering Completed")
    print(df.head())
    
    return df