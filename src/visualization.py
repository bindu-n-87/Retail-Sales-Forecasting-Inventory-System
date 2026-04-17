import matplotlib.pyplot as plt
import os

# Ensure images folder exists
os.makedirs("images", exist_ok=True)


def save_and_show(plot_name):
    """
    Helper function to save and display plots
    """
    file_path = f"images/{plot_name}.png"
    plt.savefig(file_path)
    plt.show()
    print(f"Saved: {file_path}")


def plot_results(df):

    plt.figure()
    plt.plot(df['date'], df['sales'], label='Actual Sales')
    plt.plot(df['date'], df['forecast'], label='Forecast Sales')
    plt.title("Actual vs Forecast Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    save_and_show("actual_vs_forecast")

    plt.figure()
    plt.plot(df['date'], df['current_stock'], label='Current Stock')
    plt.plot(df['date'], df['reorder_point'], label='Reorder Point')
    plt.title("Inventory vs Reorder Point")
    plt.xlabel("Date")
    plt.ylabel("Stock Level")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    save_and_show("inventory_vs_reorder")

    reorder_counts = df['reorder_flag'].value_counts()

    plt.figure()
    reorder_counts.plot(kind='bar')
    plt.title("Reorder Alerts Distribution")
    plt.xticks(rotation=0)
    plt.tight_layout()

    save_and_show("reorder_distribution")

    print("\nAll visualizations saved inside /images folder")
