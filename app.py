from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import os
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MODEL_PATH = "C:/Users/New PC/OneDrive/Desktop/Final/Final/Backend/brain_tumor_detector.h5"
model = load_model(MODEL_PATH)

class_names = ["Healthy", "Not Healthy"]

def prepare_image(img_path):
    img = Image.open(img_path).convert('RGB')
    img = img.resize((128, 128))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join("temp", file.filename)
    os.makedirs("temp", exist_ok=True)
    file.save(filepath)

    img_array = prepare_image(filepath)
    predictions = model.predict(img_array)

    predicted_class = class_names[int(predictions[0] > 0.5)]

    os.remove(filepath)

    return jsonify({
        "prediction": predicted_class,
        "confidence": float(predictions[0][0])
    })

if __name__ == '__main__':
    app.run(debug=True)
