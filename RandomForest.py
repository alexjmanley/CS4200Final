import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Importing and formatting data from data set
data = pd.read_csv("data/iran_war_oil_prices_daily_2026.csv")

# Assigning x and y values
x = data[['brent_usd_barrel', 'wti_usd_barrel', 'dubai_usd_barrel', 'strait_hormuz_daily_ships',
	'iran_production_mbpd', 'war_day', 'brent_vs_prewar_pct', 'gas_vs_prewar_pct', 
	'gas_change_from_prewar_dollars']]

y = data['us_gas_avg_gallon']

# assign model and fit
model = RandomForestRegressor(n_estimators=100)
model.fit(x, y)
predictions = model.predict(x)

print(model.feature_importances_)

for index in range(len(predictions)):
	print('Actual: ', y[index], 'Predicted: ', predictions[index])
