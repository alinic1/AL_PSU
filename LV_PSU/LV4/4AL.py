import pandas as pd

df = pd.read_csv('cars_processed.csv')

# 1. Broj mjerenja
print(f"1. Broj automobila: {len(df)}")

# 2. Tipovi stupaca
print("2. Tipovi stupaca:")
print(df.dtypes)

# 3. Max i Min cijena
# Napomena: selling_price je logaritam cijene prema opisu
max_car = df.loc[df['selling_price'].idxmax(), 'name']
min_car = df.loc[df['selling_price'].idxmin(), 'name']
print(f"3. Najskuplji: {max_car}, Najjeftiniji: {min_car}")

# 4. Automobili iz 2012.
broj_2012 = len(df[df['year'] == 2012])
print(f"4. Proizvedeno 2012: {broj_2012}")

# 5. Kilometraža
max_km_car = df.loc[df['km_driven'].idxmax(), 'name']
min_km_car = df.loc[df['km_driven'].idxmin(), 'name']
print(f"5. Najviše km: {max_km_car}, Najmanje km: {min_km_car}")

# 6. Najčešći broj sjedala
mode_seats = df['seats'].mode()[0]
print(f"6. Najčešći broj sjedala: {mode_seats}")

# 7. Prosječna kilometraža Diesel vs Petrol
avg_diesel = df[df['fuel'] == 'Diesel']['km_driven'].mean()
avg_petrol = df[df['fuel'] == 'Petrol']['km_driven'].mean()
print(f"7. Prosjek Diesel: {avg_diesel:.2f}, Prosjek Petrol: {avg_petrol:.2f}")