import numpy as np
import pandas as pd

def calculate_inventory(df):
    
    lead_time = 5  # days (assumption)
    
    # Use forecast as demand
    demand = df['forecast']
    
    # -------------------------
    # SAFETY STOCK
    # -------------------------
    demand_std = np.std(demand)
    safety_stock = 1.65 * demand_std
    
    # -------------------------
    # REORDER POINT
    # -------------------------
    avg_demand = np.mean(demand)
    
    reorder_point = (avg_demand * lead_time) + safety_stock
    
    # -------------------------
    # INVENTORY DECISION LOGIC
    # -------------------------
    df['safety_stock'] = safety_stock
    df['reorder_point'] = reorder_point
    
    # Simulated current stock
    df['current_stock'] = df['forecast'] + np.random.randint(-20, 20, size=len(df))
    
    # Reorder signal
    df['reorder_flag'] = df['current_stock'] < reorder_point
    
    print("\nInventory Optimization Completed")
    print(df[['date', 'current_stock', 'reorder_point', 'reorder_flag']].head())
    
    return df