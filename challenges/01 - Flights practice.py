import pandas as pd
#dir = '../ml-basics-master/challenges/'
data_dir = './data/flights.csv'

df_flights = pd.read_csv(data_dir)
df_flights.head()
print()