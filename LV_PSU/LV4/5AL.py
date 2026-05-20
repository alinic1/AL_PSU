import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('cars_processed.csv')

# 1.
df_numeric = df.drop(['name', 'fuel', 'seller_type', 'transmission', 'owner'], axis=1)

# Definicija ulaza i izlaza
X = df_numeric.drop('selling_price', axis=1)
y = df_numeric['selling_price']

# 2. Podjela na train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Skaliranje
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 5. Evaluacija
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

print(f"MSE Test: {mean_squared_error(y_test, y_test_pred)}")
print(f"R2 Test: {r2_score(y_test, y_test_pred)}")
