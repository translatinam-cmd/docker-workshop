import sys  
print(sys.executable)

import pandas as pd

import os
os.makedirs("data", exist_ok=True)

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month']=month
print(df.head())

df.to_parquet(f"data/pipeline_output_{month}.parquet")

print(f"Hello pipeline, month={month}")