import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")

bright = img + 50

rot = np.rot90(img, -1)

mirror = np.fliplr(img)

small = img[::10, ::10]

h, w, c = img.shape
nova = np.zeros_like(img)

nova[:, w//4:w//2] = img[:, w//4:w//2]

plt.subplot(2,3,1)
plt.imshow(img)
plt.title("Original")

plt.subplot(2,3,2)
plt.imshow(bright)
plt.title("Bright")

plt.subplot(2,3,3)
plt.imshow(rot)
plt.title("Rot")

plt.subplot(2,3,4)
plt.imshow(mirror)
plt.title("Mirror")

plt.subplot(2,3,5)
plt.imshow(small)
plt.title("Small")

plt.subplot(2,3,6)
plt.imshow(nova)
plt.title("Dio slike")

plt.show()