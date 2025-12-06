import numpy as np

# Topic: Matrices and Shapes
# In ML, Data is always a Matrix (Rows = Samples, Columns = Features)

# 1. Create a Matrix (2D Array)
# Imagine 3 houses (Rows), with 2 features each (Size, Price)
housing_data = np.array([
    [1200, 200], # House 1
    [1500, 350], # House 2
    [800,  100]  # House 3
])

print("--- Data Shape ---")
# .shape is the most important debug tool in ML
print(f"Shape: {housing_data.shape}")  # Output should be (3, 2)
print(f"Rows (Samples): {housing_data.shape[0]}")
print(f"Cols (Features): {housing_data.shape[1]}")

# 2. Matrix Multiplication
# To make a prediction, we multiply inputs (Data) by weights.
# Rule: Inner numbers must match. (3,2) can be multiplied by (2,1)
weights = np.array([
    [0.1], 
    [0.5]
])

print("\n--- Matrix Multiplication ---")
# We use the '@' symbol for matrix multiplication (Standard in modern Python)
prediction = housing_data @ weights

print(f"Predictions for 3 houses:\n{prediction}")