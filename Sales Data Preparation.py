# sales_data_generator.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample sales data
np.random.seed(42)
n = 500

regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Beauty']
start_date = datetime(2023, 1, 1)

data = {
    'Order ID': [f"ORD-{i:04d}" for i in range(1, n+1)],
    'Date': [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(n)],
    'Region': np.random.choice(regions, n),
    'Category': np.random.choice(categories, n),
    'Units Sold': np.random.randint(1, 50, n),
    'Unit Price': np.round(np.random.uniform(10.0, 500.0, n), 2)
}

df = pd.DataFrame(data)
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

# Save as CSV to use in Tableau
df.to_csv('sales_data.csv', index=False)
print("Sample sales data saved as 'sales_data.csv'")
