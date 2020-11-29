from predict import predict_pipeline
import numpy as np

def test_predict_pipeline():
    fake_feature = np.array([1, 1, 1, 1]).reshape(-1, 1)
    fake_prediction = predict_pipeline(fake_feature)
    assert  isinstance(fake_prediction, float)
