import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('cars_processed.csv')
df = df.drop(['name'], axis=1) # Ime i dalje ne treba

# One-hot encoding kategoričkih varijabli
df_dummy = pd.get_dummies(df, columns=['fuel', 'seller_type', 'transmission', 'owner'])

X = df_dummy.drop('selling_price', axis=1)
y = df_dummy['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_test_pred = model.predict(X_test_scaled)

print("Rezultati s kategoričkim varijablama:")
print(f"MSE Test: {mean_squared_error(y_test, y_test_pred)}")
print(f"R2 Test: {r2_score(y_test, y_test_pred)}")