import pandas as pd
import numpy as np
import random
import string

# Define the number of rows in the sample data
num_rows = 100

# Generate sample data
data = {
    'request_id': range(1, num_rows + 1),
    'initiated_at': pd.date_range(start='2023-01-01', periods=num_rows, freq='H'),
    'updated_at': pd.date_range(start='2023-01-01', periods=num_rows, freq='H') + pd.to_timedelta(np.random.randint(1, 24, num_rows), unit='H'),
    'difference': np.random.randint(1, 1440, num_rows),  # Random difference in minutes
    'type': [random.choice(string.ascii_uppercase) for _ in range(num_rows)]  # Random type
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('sample_data.csv', index=False)
