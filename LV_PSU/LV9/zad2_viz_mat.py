import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image_dataset_from_directory
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

test_ds = image_dataset_from_directory(
    directory='gtsrb/Test',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48),
    shuffle=False
)

print("Učitavam ")
najbolji_model = keras.models.load_model('najbolji_model.keras')

print("Računam ")
y_true = []
for _, labels in test_ds:
    y_true.extend(np.argmax(labels.numpy(), axis=1))

y_pred_probas = najbolji_model.predict(test_ds)
y_pred = np.argmax(y_pred_probas, axis=1)

cm = confusion_matrix(y_true, y_pred)

print("Otvaram prozor s grafom")
plt.figure(figsize=(15, 12))
sns.heatmap(cm, annot=False, cmap='Blues', fmt='g')
plt.xlabel('Predviđena klasa')
plt.ylabel('Stvarna klasa')
plt.title('Vizualna matrica zabune (Confusion Matrix) - GTSRB')

plt.show()