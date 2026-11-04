from fastapi import FastAPI
import pandas as pd
import joblib

from pathlib import Path
from app.schemas import HeartDiseaseInput


# Load trained model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "heart_model.joblib"

model = joblib.load(MODEL_PATH)


# Create FastAPI application
app = FastAPI(
    title="Heart Disease Prediction API",
    description="An API for predicting heart disease using Machine Learning.",
    version="1.0.0"
)


# Feature names
FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]


# GET: Health Check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Heart Disease Prediction API is running!"
    }


# GET: API Information
@app.get("/info")
def get_info():
    return {
        "model_type": "Logistic Regression",
        "features": FEATURES,
        "total_features": len(FEATURES)
    }


# POST: Make Prediction
@app.post("/predict")
def predict_heart_disease(data: HeartDiseaseInput):

    input_data = pd.DataFrame(
        [data.model_dump()],
        columns=FEATURES
    )

    prediction = model.predict(input_data)[0]

    return {
        "heart_disease": bool(prediction)
    }