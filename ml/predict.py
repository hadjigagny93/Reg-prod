from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib

def predict_pipeline(features):
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler()),])

    features = features.reshape(1, 4)
    transformed_features = pipeline.fit_transform(features)

    # so load model and make predictions
    model = joblib.load('ml/models/model.pkl')
    prediction = model.predict(transformed_features)
    return prediction[0]



