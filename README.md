# Retail Sales Forecasting & Inventory Optimization System

## Project Overview

The **Retail Sales Forecasting & Inventory Optimization System** is an end-to-end machine learning project designed to simulate a real-world retail analytics pipeline.

It predicts future sales using historical patterns and optimizes inventory levels using statistical business rules such as **Safety Stock** and **Reorder Point**.

This project is built using **synthetic retail data** to simulate real-world scenarios similar to companies like Amazon, Walmart, Flipkart, D-Mart, and Reliance Retail.

---

## Problem Statement

Retail businesses face major challenges such as:

- Stockouts (lost sales opportunities)
- Overstocking (increased storage cost)
- Poor demand forecasting
- Inefficient inventory planning

This project solves these problems by:

✔ Predicting future sales demand  
✔ Optimizing inventory levels  
✔ Generating reorder alerts  
✔ Providing business-ready insights  

---

## Business Value

This system helps retail organizations:

- Improve demand forecasting accuracy
- Reduce inventory holding costs
- Avoid stock shortages
- Improve customer satisfaction
- Optimize supply chain decisions

---

## System Workflow

Data Generation → Preprocessing → EDA → Feature Engineering → ML Model → Forecasting → Inventory Optimization → Reporting → Visualization

---

## Project Architecture

Retail-Sales-Forecasting/
│
├── data/ # Raw & processed data
├── src/ # Core Python modules
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── feature_engineering.py
│ ├── model.py
│ ├── inventory.py
│ ├── visualization.py
│ ├── report_generator.py
│
├── notebooks/ # EDA notebook
├── outputs/ # Generated CSV reports
├── images/ # Saved graphs & visuals
├── main.py # Pipeline execution file
├── requirements.txt
├── README.md

---

## Dataset Information

Since real retail data is not publicly available, a **synthetic dataset** is generated with the following features:

| Feature | Description |
|--------|-------------|
| date | Daily transaction date |
| store_id | Store identifier |
| product_id | Product identifier |
| category | Product category |
| sales | Units sold |
| price | Product price |

The dataset simulates:

- Seasonal demand patterns  
- Random fluctuations  
- Trend-based growth  
- Multi-store retail structure  

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Machine Learning Model

- Model Used: **Random Forest Regressor**
- Task: Time-series regression forecasting
- Input Features:
  - Day, Month, Weekday
  - Lag features (lag_1, lag_7, lag_30)
  - Rolling averages (7-day, 30-day)

---

## Inventory Optimization Logic

The system uses statistical formulas:

### Safety Stock

Safety Stock = 1.65 × Standard Deviation of Demand

### Reorder Point

Reorder Point = (Average Demand × Lead Time) + Safety Stock

### Decision Rule
- If current stock < reorder point → 🚨 Reorder triggered

---

## Key Features

✔ Synthetic retail data generation  
✔ Data preprocessing pipeline  
✔ Exploratory Data Analysis (EDA)  
✔ Feature engineering (lags, rolling averages)  
✔ Machine learning forecasting model  
✔ Inventory optimization system  
✔ Reorder alerts generation  
✔ Business reporting system  
✔ Visualization dashboard  

---

## Outputs

The system generates:

### CSV Reports
- `forecast_summary.csv`
- `inventory_report.csv`
- `business_summary.csv`

### Visualizations
- Actual vs Forecast Sales
- Inventory vs Reorder Point
- Reorder Alerts Distribution

---

## Author

Bindu P
