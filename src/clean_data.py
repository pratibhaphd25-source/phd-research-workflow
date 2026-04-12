import pandas as pd

# Read the data
df = pd.read_csv('data/sample_data.csv')

# Fill missing numeric values with mean
df['experiment_score'] = df['experiment_score'].fillna(df['experiment_score'].mean())
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())

# Save cleaned data
df.to_csv('data/cleaned_data.csv', index=False)

print("Cleaned data saved to data/cleaned_data.csv")
