import pandas as pd
from tabulate import tabulate
import numpy as np

# Read the CSV file
df = pd.read_csv('heart-disease.csv')

# Select only numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Calculate central tendencies
results = []
for col in numerical_cols:
    mean_val = df[col].mean()
    median_val = df[col].median()
    mode_val = df[col].mode()[0] if not df[col].mode().empty else None
    min_val = df[col].min()
    max_val = df[col].max()
    
    results.append([col, mean_val, median_val, mode_val, min_val, max_val])

# Create table
headers = ['Column', 'Mean', 'Median', 'Mode', 'Min', 'Max']
print(tabulate(results, headers=headers, tablefmt='pipe', floatfmt='.2f'))
