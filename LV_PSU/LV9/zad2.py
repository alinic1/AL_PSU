import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image_dataset_from_directory
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

train_ds = image_dataset_from_directory(
    directory='gtsrb/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    subset="training",
    seed=123,
    validation_split=0.2,
    image_size=(48, 48)
)

validation_ds = image_dataset_from_directory(
    directory='gtsrb/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    subset="validation",
    seed=123,
    validation_split=0.2,
    image_size=(48, 48)
)

test_ds = image_dataset_from_directory(
    directory='gtsrb/Test',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48),
    shuffle=False
)

train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
validation_ds = validation_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=tf.data.AUTOTUNE)

model = keras.Sequential()

model.add(layers.Rescaling(1./255, input_shape=(48, 48, 3)))

filteri = [32, 64, 128]
for f in filteri:
    model.add(layers.Conv2D(filters=f, kernel_size=(3, 3), strides=1, padding='same', activation='relu'))
    model.add(layers.Conv2D(filters=f, kernel_size=(3, 3), strides=1, padding='valid', activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(layers.Dropout(rate=0.2))

model.add(layers.Flatten())

model.add(layers.Dense(units=512, activation='relu'))
model.add(layers.Dropout(rate=0.5))
model.add(layers.Dense(units=43, activation='softmax'))

model.summary()

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath='najbolji_model.keras',
        save_best_only=True,
        monitor='val_loss',
        mode='min',
        verbose=1
    ),
    keras.callbacks.TensorBoard(
        log_dir='logs/gtsrb_mreza',
        histogram_freq=1
    )
]

EPOCHS = 15
history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=EPOCHS,
    callbacks=callbacks
)

print("\n--- Evaluacija modela na testnim podacima ---")
najbolji_model = keras.models.load_model('najbolji_model.keras')

loss, accuracy = najbolji_model.evaluate(test_ds)
print(f"Točnost na testnom skupu: {accuracy * 100:.2f}%")

y_true = []
for _, labels in test_ds:
    y_true.extend(np.argmax(labels.numpy(), axis=1))

y_pred_probas = najbolji_model.predict(test_ds)
y_pred = np.argmax(y_pred_probas, axis=1)

print("\nMatrica zabune:")
cm = confusion_matrix(y_true, y_pred)
print(cm)

print("\nIzvještaj klasifikacije:")
print(classification_report(y_true, y_pred))

print("\nOtvaram grafički prikaz matrice zabune...")
plt.figure(figsize=(15, 12))

sns.heatmap(cm, annot=False, cmap='Blues', fmt='g')

plt.xlabel('Predviđena klasa')
plt.ylabel('Stvarna klasa')
plt.title('Vizualna matrica zabune (Confusion Matrix) - GTSRB')

plt.show()