from flask import Flask, jsonify, request
from deepface import DeepFace
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

def save_image(data):
    try:
        img_data = base64.b64decode(data)
        image = Image.open(BytesIO(img_data))
        image.save("image.jpg")
        return True
    except Exception as e:
        return False

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json['data']
        result = save_image(data)
        if result:
            demography = DeepFace.analyze("image.jpg")
            return jsonify(demography)
        else:
            return jsonify({"error": "Something went wrong."}), 400
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Face could not be detected. Please try a different image."}), 400


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001)