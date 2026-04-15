import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing and formatting data from data set
df = pd.read_csv("data/iran_war_oil_prices_daily_2026.csv")
df["date"] = pd.to_datetime(df["date"])

# Assigning x and y values
x= np.array(df['date'])
y = np.array(df['us_gas_avg_gallon'])

# simple plot to see line
plt.plot(x, y)
plt.show()
