import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train_model(df):
    
    # Features (X)
    features = [
        'day',
        'month',
        'dayofweek',
        'lag_1',
        'lag_7',
        'lag_30',
        'rolling_mean_7',
        'rolling_mean_30'
    ]
    
    X = df[features]
    y = df['sales']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )
    
    # Model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    print("\nModel Training Completed")
    
    return model

def forecast(model, df):
    
    features = [
        'day',
        'month',
        'dayofweek',
        'lag_1',
        'lag_7',
        'lag_30',
        'rolling_mean_7',
        'rolling_mean_30'
    ]
    
    df['forecast'] = model.predict(df[features])
    
    print("\nForecasting Completed")
    print(df[['date', 'sales', 'forecast']].head())
    
    return df
