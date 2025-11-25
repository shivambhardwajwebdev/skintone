from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import face_detect
import kMeansImgPy
import allotSkinTone

app = Flask(__name__)
CORS(app)

@app.route('/analyze-skin-tone', methods=['POST'])
def analyze_skin_tone():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400

        file = request.files['image']
        npimg = np.fromfile(file, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        # 1. Detect Face
        try:
            face_extracted = face_detect.detect_face(image)
        except Exception:
            return jsonify({'error': 'No face detected. Try a clearer photo.'}), 400

        # 2. Get Dominant Color
        colorsList = kMeansImgPy.kMeansImage(face_extracted)

        # 3. Get Text Label
        result_label = allotSkinTone.allotSkin(colorsList)

        return jsonify({
            'status': 'success',
            'skin_tone': result_label,
            'rgb': colorsList
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Gunicorn will look for 'app', so we don't need app.run() here for production
