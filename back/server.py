from flask import Flask, request
from flask_cors import CORS, cross_origin
from joblib import dump, load
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = load_model('/Users/rayant/app2/model/med_model.h5')
scaler = load('/Users/rayant/app2/model/scaler.joblib')

@app.route("/", methods=['POST'])
@cross_origin()
def helloWorld():
  input_array = request.get_json().get('inputArray')
  input_array = np.array(input_array).reshape(1, -1)
  input_array = scaler.transform(input_array)
  pred = model.predict(input_array)
  return str(pred[0]), 200

if __name__ == "__main__":
    app.run(port=5000)  # run the server on port 5000