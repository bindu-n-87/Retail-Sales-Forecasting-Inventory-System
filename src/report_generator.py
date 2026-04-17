import pandas as pd
import os

os.makedirs("outputs", exist_ok=True)

def generate_report(df):

    # -----------------------------
    # 1. Forecast Summary
    # -----------------------------
    forecast_summary = df.groupby("date")[["sales", "forecast"]].sum().reset_index()
    forecast_summary.to_csv("outputs/forecast_summary.csv", index=False)

    # -----------------------------
    # 2. Inventory Report
    # -----------------------------
    inventory_report = df[[
        "date",
        "product_id",
        "store_id",
        "current_stock",
        "reorder_point",
        "reorder_flag"
    ]]

    inventory_report.to_csv("outputs/inventory_report.csv", index=False)

    # -----------------------------
    # 3. Business Insights Summary
    # -----------------------------
    total_sales = df["sales"].sum()
    total_forecast = df["forecast"].sum()
    reorder_days = df["reorder_flag"].sum()

    summary = {
        "Total Sales": [total_sales],
        "Total Forecasted Sales": [total_forecast],
        "Reorder Alerts Count": [reorder_days]
    }

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv("outputs/business_summary.csv", index=False)

    print("\nREPORT GENERATED SUCCESSFULLY")
    print(summary_df)

    return summary_df