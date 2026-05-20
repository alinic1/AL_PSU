import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 1. MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa
plt.figure(figsize=(10, 3))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.show()

# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)

# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()
model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(100, activation='relu'),   # 1. skriveni sloj (100 neurona)
    layers.Dense(50, activation='relu'),    # 2. skriveni sloj (50 neurona)
    layers.Dense(10, activation='softmax')  # Izlazni sloj (10 neurona)
])
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# TODO: provedi treniranje mreze pomocu .fit()
history = model.fit(x_train_s, y_train_s, 
                    epochs=10, 
                    batch_size=32, 
                    validation_split=0.1)

# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
score_train = model.evaluate(x_train_s, y_train_s, verbose=0)
score_test = model.evaluate(x_test_s, y_test_s, verbose=0)

print(f"\nTocnost na skupu za ucenje: {score_train[1]:.4f}")
print(f"Tocnost na skupu za testiranje: {score_test[1]:.4f}")

# TODO: Prikazite matricu zabune na skupu podataka za testiranje
predictions = model.predict(x_test_s)
predictions_labels = np.argmax(predictions, axis=1)

cm = confusion_matrix(y_test, predictions_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title("Matrica zabune (Testni skup)")
plt.show()

# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala
misclassified_idx = np.where(predictions_labels != y_test)[0]

plt.figure(figsize=(12, 5))
for i, idx in enumerate(misclassified_idx[:5]):
    plt.subplot(1, 5, i+1)
    # Vraćamo oblik u 28x28 za prikaz
    plt.imshow(x_test[idx], cmap='gray')
    plt.title(f"Stvarno: {y_test[idx]}\nPred.: {predictions_labels[idx]}")
    plt.axis('off')
plt.tight_layout()
plt.show()