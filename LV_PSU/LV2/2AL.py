import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

mpg = data[:, 0]
hp = data[:, 3]
wt = data[:, 5]
cyl = data[:, 1]

plt.xlabel('Konjske snage (hp)')
plt.ylabel('Potrosnja (mpg)')

plt.scatter(hp, mpg, s=wt*30)
plt.show()

print("Minimalni mpg:", np.min(mpg))
print("Maksimalni mpg:", np.max(mpg))
print("Prosječni mpg:", np.mean(mpg))

mpg_6 = mpg[cyl == 6]

print("Minimalni mpg (6 cilindara):", np.min(mpg_6))
print("Maksimalni mpg (6 cilindara):", np.max(mpg_6))
print("Prosječni mpg (6 cilindara):", np.mean(mpg_6))