import pandas as pd
import numpy as np

dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')
np.random.seed(42)

fuel_consumption = np.random.normal(loc=450, scale=10, size=len(dates))
rpm = np.random.normal(loc=1000, scale=50, size=len(dates))
temperature = np.random.normal(loc=320, scale=5, size=len(dates))

df = pd.DataFrame({ 
    "timestamp": dates,
    "fuel_consumption": fuel_consumption.round(2),
    "rpm": rpm.round(0).astype(int),
    "temperature": temperature.round(2)
    })

df.to_csv("data/simulated_engine_usage.csv", index=False)

print(df.head())
