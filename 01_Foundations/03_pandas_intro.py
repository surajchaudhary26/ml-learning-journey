import pandas as pd
import numpy as np

# Topic: Pandas DataFrames
# Pandas is built ON TOP of NumPy. It gives names to the columns.

# 1. Creating a "Fake" Dataset (Simulation)
# In real life, you would use: df = pd.read_csv("file.csv")
data = {
    'House_Size_SqFt': [1200, 1500, 800, 2000, 1100],
    'Bedrooms': [2, 3, 1, 4, 2],
    'Price_USD': [200000, 350000, 100000, 500000, 220000]
}

# Convert dictionary to DataFrame (The standard Excel-like table)
df = pd.DataFrame(data)

print("--- The Full Dataset ---")
print(df)

# 2. Accessing Data
print("\n--- Just the Prices ---")
print(df['Price_USD'])

# 3. Quick Statistics (The Power of Pandas)
print("\n--- Market Analysis ---")
print(f"Average Price: ${df['Price_USD'].mean()}")
print(f"Max Size: {df['House_Size_SqFt'].max()} SqFt")

# 4. Filtering (Querying the data)
# "Show me only houses with more than 2 bedrooms"
big_houses = df[df['Bedrooms'] > 2]
print("\n--- Big Houses Only (> 2 Beds) ---")
print(big_houses)