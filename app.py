from flask import Flask, request, render_template, redirect, url_for
# from keras.models import load_model
# from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import keras
import os

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model
model = keras.models.load_model('vgg16_model.h5')

# Define the class names based on your dataset
class_names = ['Bud Root Dropping', 'Bud Rot', 'CCI_Caterpillars', 'Gray Leaf Spot', 'Stem Bleeding', 'WCLWD_Yellowing']

# Define the path to save uploaded images
UPLOAD_FOLDER = 'uploads'  # Directory where uploaded images are saved
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to preprocess the image
def preprocess_image(image_path):
    image = keras.preprocessing.image.load_img(image_path, target_size=(180, 180))  # Ensure the target size matches the model's input size
    image = keras.preprocessing.image.img_to_array(image)
    image = image / 255.0  # Normalize the image to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    return image

# Define the route for the homepage
@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            filepath = os.path.join('static',app.config['UPLOAD_FOLDER'], file.filename).replace("\\", "/")
            filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], file.filename).replace("\\", "/")
            file.save(filepath)
            
            # Preprocess the image and make predictions
            image = preprocess_image(filepath)
            predictions = model.predict(image)
            predicted_class = np.argmax(predictions[0])
            predicted_label = class_names[predicted_class]
            print(f"Predicted class: {predicted_label}")
            print(f"file: {filepath}")
            
            return render_template('base.html', prediction=predicted_label, image_path=filepath1)
    
    return render_template('index.html')

# Define the route for serving uploaded images
@app.route('/base.html')
@app.route('/uploads/<filename>')
def send_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename))

if __name__ == '__main__':
    app.run(debug=True)