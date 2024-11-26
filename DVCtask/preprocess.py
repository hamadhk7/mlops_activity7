import pandas as pd

df = pd.read_csv('raw_data.csv')
df.fillna(method='ffill', inplace=True)
df['Temperature'] = (df['Temperature'] - df['Temperature'].mean()) / df['Temperature'].std()
df.to_csv('processed_data.csv', index=False)
