import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])

plt.plot(x, y, marker='o', color='blue')

plt.title("Primjer")
plt.xlabel("x - os")
plt.ylabel("y - os")

plt.xlim(0, 4)
plt.ylim(0, 4)

plt.show()