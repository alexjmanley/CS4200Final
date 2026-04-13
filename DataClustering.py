import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("data/iran_war_gas_prices_by_state.csv")
df.head()
