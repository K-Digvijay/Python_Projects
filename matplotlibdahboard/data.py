"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate dummy sales data
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
sales_data = pd.DataFrame({
    'date': dates,
    'sales': np.random.randint(100, 500, size=len(dates))
})

# Generate dummy inventory data
inventory_data = pd.DataFrame({
    'product_id': np.arange(1, 101),
    'stock_level': np.random.randint(50, 300, size=100)
})

# Generate dummy product data
product_data = pd.DataFrame({
    'product_id': np.arange(1, 101),
    'price': np.random.uniform(10, 100, size=100),
    'category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Toys'], size=100)
})

# Generate dummy sales year data
sales_year_data = pd.DataFrame({
    'year': np.arange(2015, 2024),
    'annual_sales': np.random.randint(50000, 150000, size=9)
})

# Generate dummy inventory month data
inventory_month = pd.DataFrame({
    'month': pd.date_range(start='2023-01-01', end='2023-12-01', freq='MS').strftime('%Y-%m'),
    'inventory_level': np.random.randint(2000, 5000, size=12)
})
"""
import numpy as np
import pandas as pd

# Number of products to generate
num_products = 100

# Generate product IDs
product_ids = np.arange(1, num_products + 1)

# Generate random product names
product_names = [f"Product_{i}" for i in product_ids]

# Generate random categories
categories = np.random.choice(['Electronics', 'Clothing', 'Home', 'Toys', 'Sports', 'Beauty'], size=num_products)

# Generate random prices
prices = np.round(np.random.uniform(5.0, 500.0, size=num_products), 2)

# Generate random stock levels
stock_levels = np.random.randint(1, 1000, size=num_products)

# Generate dummy product data as a DataFrame
product_data = pd.DataFrame({
    'product_id': product_ids,
    'product_name': product_names,
    'category': categories,
    'price': prices,
    'stock_level': stock_levels
})

# Display the first few rows of the DataFrame
print(product_data.head())

# Save to a CSV file if needed
product_data.to_csv('dummy_product_data.csv', index=False)
