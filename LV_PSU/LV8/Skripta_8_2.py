import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'testal.png'

# Ucitaj sliku
img_original = mpimg.imread(filename)
img = color.rgb2gray(img_original)
img = resize(img, (28, 28))

# Prikazi sliku
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')  
plt.show()

# Pripremi sliku - ulaz u mrezu
img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# TODO: ucitaj izgradenu mrezu [cite: 131]
model = models.load_model('best_model.h5')

# TODO: napravi predikciju za ucitanu sliku pomocu mreze [cite: 132]
prediction = model.predict(img)
predicted_class = np.argmax(prediction)

# TODO: ispis rezultat u terminal [cite: 133]
print(f"Predikcija modela za datoteku '{filename}': {predicted_class}")
print(f"Vjerojatnosti po klasama: {prediction}")