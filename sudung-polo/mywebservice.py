import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

flower_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
model = joblib.load('E:/HMUD/smartAPI/models/dtmodel-iris.joblib')

@app.route("/")
def hello_world():
    return "Đây là máy chủ dịch vụ web cung cấp các mô hình trí tuệ nhân tạo"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = data['features']
        prediction = model.predict([features])
        result = {"prediction": int(prediction[0]), "flower_name": flower_names[int(prediction[0])]}
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/checkImage', methods=['POST'])
def checkImage():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No file part"})

        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({"error": "No selected file"})

        img_folder = "images"
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)

        image_path = os.path.join(img_folder, image_file.filename)
        image_file.save(image_path)

        return jsonify({"message": "Image uploaded successfully!", "image_path": image_path})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()
