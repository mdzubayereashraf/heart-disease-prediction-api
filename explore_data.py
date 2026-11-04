import pandas as pd

# Load dataset
df = pd.read_csv("data/heart.csv")

# Display first five rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Target distribution
print("\nTarget Distribution:")
print(df["target"].value_counts())