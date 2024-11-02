import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../data/sample_data.csv")

# Display basic statistics
print(df.describe())

# Ensure the visualizations directory exists
output_dir = "../visualizations"
os.makedirs(output_dir, exist_ok=True)

# Plot Temperature vs. Emissions
plt.figure(figsize=(8, 5))
plt.scatter(df["Temperature"], df["Emissions"], color="blue", alpha=0.6)
plt.xlabel("Temperature (°C)")
plt.ylabel("Emissions")
plt.title("Temperature vs. Emissions")
plt.savefig(os.path.join(output_dir, "temp_vs_emissions.png"))
plt.show()

# Plot Pressure vs. Emissions
plt.figure(figsize=(8, 5))
plt.scatter(df["Pressure"], df["Emissions"], color="green", alpha=0.6)
plt.xlabel("Pressure (atm)")
plt.ylabel("Emissions")
plt.title("Pressure vs. Emissions")
plt.savefig(os.path.join(output_dir, "pressure_vs_emissions.png"))
plt.show()
