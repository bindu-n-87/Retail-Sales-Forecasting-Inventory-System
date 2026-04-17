from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.model import train_model, forecast
from src.inventory import calculate_inventory
from src.visualization import plot_results
from src.report_generator import generate_report

# Step 1
df = load_data()

# Step 2
df = preprocess_data(df)

# Step 3
df = create_features(df)

# Step 4
model = train_model(df)

# Step 5
df = forecast(model, df)

# Step 6
df = calculate_inventory(df)

# Step 7
plot_results(df)

# Step 8 then 9 - Generate Reports
generate_report(df)

print("\nALL OUTPUTS GENERATED SUCCESSFULLY")
