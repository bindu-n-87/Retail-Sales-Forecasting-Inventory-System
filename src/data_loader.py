import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    
    dates = pd.date_range(start="2023-01-01", periods=365)
    
    stores = [1, 2, 3]
    products = [101, 102, 103, 104]
    categories = {
        101: "Dairy",
        102: "Beverages",
        103: "Snacks",
        104: "Groceries"
    }
    
    data = []
    
    for date in dates:
        for store in stores:
            for product in products:
                
                base_demand = np.random.randint(20, 100)
                
                # Seasonality (weekly pattern)
                seasonal = 10 * np.sin(2 * np.pi * date.dayofyear / 7)
                
                # Trend (slight increase)
                trend = 0.05 * (date.dayofyear)
                
                # Random noise
                noise = np.random.normal(0, 5)
                
                sales = max(0, int(base_demand + seasonal + trend + noise))
                
                price = np.random.uniform(10, 100)
                
                data.append([
                    date,
                    store,
                    product,
                    categories[product],
                    sales,
                    round(price, 2)
                ])
    
    df = pd.DataFrame(data, columns=[
        "date", "store_id", "product_id", "category", "sales", "price"
    ])
    
    return df

def load_data():
    df = generate_data()
    return df
