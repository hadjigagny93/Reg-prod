
from flask import Flask, jsonify, make_response, request
from ml.predict import predict_pipeline
import numpy as np 

app = Flask(__name__)


@app.route('/score', methods=['POST'])
def score():
    features = request.json['X']
    features = np.array(features)
    score = predict_pipeline(features)
    return make_response(jsonify({'score': score}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



