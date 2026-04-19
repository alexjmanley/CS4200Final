import pandas as pd
from sklearn.cluster import DBSCAN

# grabbing data set and seeing shape 
dataFile = pd .read_csv('./data/iran_war_oil_prices_daily_2026.csv')
print(dataFile.shape)

# Look at first rows of data
print(dataFile.head())

# Check to see if there is duplications in rows
print(dataFile.duplicated())

# Check to see if there is any null values 
print(dataFile.isnull().sum())

# Maybe lets check for outliers on the us gas average column? 
# need to convert date column to something legible 

dataFile['intdate'] = pd.to_datetime(dataFile['date']).astype('int64')

df = pd.DataFrame(dataFile, columns=['intdate', 'us_gas_avg_gallon'])

clustering = DBSCAN(eps=5, min_samples=3).fit(df)
labels = clustering.labels_

i = 0
print("Index	Cluster 	X	Y")
for row in df.iterrows():
	if labels[i] == -1:
		print(i, '   ', labels[i], '    ', row[1]['intdate'], '   ', row[1]['us_gas_avg_gallon'])
	i = i + 1
