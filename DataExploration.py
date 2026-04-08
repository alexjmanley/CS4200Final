import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/iran_war_gas_prices_by_state.csv")

print(df.head())
print(df.describe())
print(df.info())

df["gas_price_mar19_2026"].hist()
plt.title("Gas Prices Distribution (March 2026)")
plt.show()

df.groupby("region")["gas_price_mar19_2026"].mean().plot(kind="bar")
plt.title("Average Gas Price by Region")
plt.show()

df.plot.scatter(x="gas_price_prewar_feb27",
		y="gas_price_mar19_2026")
plt.title("Pre-war vs Post-war Gas Prices")
plt.show()
