import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)

dir = "data"
os.makedirs(dir, exist_ok=True)

file_path = os.path.join(dir , "sample_data.csv")

df.to_csv(file_path)
