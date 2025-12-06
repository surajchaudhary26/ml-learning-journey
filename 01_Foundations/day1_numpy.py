import numpy as np

# Day 1: Machine Learning Foundations
# The Dot Product: Calculating "Similarity" between two vectors

# 1. Define two vectors 
# Scenario: [Price, Weight, QualityScore]
product_a = np.array([10, 20, 5])
product_b = np.array([10, 25, 4])

# 2. Calculate Dot Product 
# Calculation: (10*10) + (20*25) + (5*4) = 620
result = np.dot(product_a, product_b)

print(f"The Dot Product result is: {result}")