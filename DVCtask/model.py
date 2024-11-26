from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd

df = pd.read_csv('processed_data.csv')
X = df[['Humidity', 'Wind Speed']]  # Features
y = df['Temperature']  # Target

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
