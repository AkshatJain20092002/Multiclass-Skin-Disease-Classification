from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import urllib.request
import os

app = Flask(__name__)

# Load the first model for skin disease classification
skin_model = load_model('vgg16_monkepox.h5')
skin_class_labels = ['chickenpox', 'measles', 'monkeypox', 'normal']

# Load the second model for skin type classification
type_model = load_model('skin_classification_without.h5')
type_class_labels = ['Acne and Rosacea', 'Eczema', 'Melanoma', 'Psoriasis', 'Chickenpox', 'Measles', 'Monkeypox', 'Normal']

# Image size for preprocessing
image_size = (227, 227)

# Define a function for skin disease classification
def classify_skin_disease(image_path):
    image = load_img(image_path, target_size=image_size)
    img_array = img_to_array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = skin_model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = skin_class_labels[predicted_class_index]
    return predicted_class

# Define a function for skin type classification
def classify_skin_type(image_path):
    image = load_img(image_path, target_size=image_size)
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
    predictions = type_model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = type_class_labels[predicted_class_index]
    return predicted_class

uploads_dir = 'static/uploads'
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/result', methods=['POST'])
def result():
    if 'image' not in request.files:
        return render_template('index.html', message='No file part')

    file = request.files['image']

    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file:
        image_path = 'static/uploads/' + file.filename
        file.save(image_path)
        predicted_skin_disease = classify_skin_disease(image_path)
        return render_template('result.html', image_path=image_path, predicted_skin_disease=predicted_skin_disease)
    
@app.route('/result1', methods=['POST'])
def result1():
    if 'image' not in request.files:
        return render_template('index2.html', message='No file part')

    file = request.files['image']

    if file.filename == '':
        return render_template('index2.html', message='No selected file')

    if file:
        image_path = 'static/uploads/' + file.filename
        file.save(image_path)
        predicted_skin_type = classify_skin_type(image_path)
        return render_template('result1.html', image_path=image_path, predicted_skin_type=predicted_skin_type)

if __name__ == '__main__':
    app.run(debug=True)