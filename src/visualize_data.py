import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Create results folder
os.makedirs("results", exist_ok=True)

# Plot 1: Experiment Score
plt.figure()
df["experiment_score"].plot()
plt.title("Experiment Score")
plt.savefig("results/score_plot.png")

# Plot 2: Temperature vs Humidity
plt.figure()
plt.scatter(df["temperature"], df["humidity"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")
plt.savefig("results/temperature_humidity_plot.png")

print("Plots generated successfully.")