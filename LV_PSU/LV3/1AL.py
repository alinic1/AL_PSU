import pandas as pd

mtcars = pd.read_csv('mtcars.csv')


print("1. Top 5 s najvećim MPG (najmanja potrošnja):")
print(mtcars.sort_values(by='mpg', ascending=False).head(5))

print("\n2. Tri s 8 cilindara i najvećim mpg:")
print(mtcars[mtcars.cyl == 8].sort_values(by='mpg', ascending=False).head(3))

print(f"\n3. Srednja potrošnja (6 cyl): {mtcars[mtcars.cyl == 6].mpg.mean():.2f}")


print(f"4. Srednja potrošnja (4 cyl, 2000-2200 lbs): {mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)].mpg.mean():.2f}")

print("\n5. Broj mjenjača (0=auto, 1=manual):")
print(mtcars['am'].value_counts())

print(f"\n6. Automatik i hp > 100: {len(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)])}")

mtcars['mass_kg'] = mtcars.wt * 1000 * 0.453592
print("\n7. Masa u kg (prvih 5):")
print(mtcars[['car', 'mass_kg']].head())