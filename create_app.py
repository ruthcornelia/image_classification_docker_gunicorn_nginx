from flask import Flask, request
from flasgger import Swagger
from PIL import Image
import numpy as np 
from keras.models import load_model
import tensorflow as tf

print(tf)

model = load_model("model.h5")

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)
    
    @app.route("/predict_digit", methods=["POST"])
    def predict_digit():
      """
      Example endpoint returning a prediction of mnist
      ---
      parameters:
          - name: image
            in: formData
            type: file
            required: true
      responses:
          200:
              description: ok
      """
    
      im = Image.open(request.files['image'])
      im2arr = np.array(im).reshape((1, 28, 28, 1))
      return str(np.argmax(model.predict(im2arr)))
    return app