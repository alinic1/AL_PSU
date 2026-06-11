import numpy as np
import tensorflow as tf
from tensorflow import keras

model_path = 'najbolji_model.keras'
if not tf.io.gfile.exists(model_path):
    raise FileNotFoundError("Prvo moraš pokrenuti zadatak2.py da se generira model!")

model = keras.models.load_model(model_path)
print("Model uspješno učitan.")

slika_putanja = 'test_znak.jpg' 

try:
    img = keras.preprocessing.image.load_img(
        slika_putanja, 
        target_size=(48, 48)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    # Dodavanje batch dimenzije (jer mreža očekuje oblik [batch_size, visina, širina, kanali])
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predvidena_klasa = np.argmax(predictions, axis=1)[0]
    vjerojatnost = predictions[0][predvidena_klasa]

    print("\n--- REZULTAT KLASIFIKACIJE ---")
    print(f"Predviđena klasa (ID): {predvidena_klasa}")
    print(f"Sigurnost mreže u predikciju: {vjerojatnost * 100:.2f}%")

except Exception as e:
    print(f"Greška pri učitavanju slike: {e}")
    print("Provjeri nalazi li se slika 'test_znak.jpg' u istom direktoriju.")