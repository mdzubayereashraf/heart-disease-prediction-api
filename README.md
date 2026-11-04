# ❤️ Heart Disease Prediction API

A Machine Learning-powered REST API that predicts the possibility of heart disease using patient health information.

This project demonstrates an end-to-end Machine Learning deployment workflow using **Scikit-learn, FastAPI, Docker, and Render**.

## 🚀 Live Demo

**Live API:** https://heart-disease-prediction-api-v15y.onrender.com

**API Documentation (Swagger UI):**
https://heart-disease-prediction-api-v15y.onrender.com/docs

**Health Check:**
https://heart-disease-prediction-api-v15y.onrender.com/health

---

## 🎯 Project Objective

The objective of this project is to build and deploy a Machine Learning model that predicts whether a patient may have heart disease based on 13 health-related features.

The main focus is on:

* Machine Learning model development
* REST API development with FastAPI
* Input validation using Pydantic
* Model serialization using Joblib
* Containerization using Docker
* Cloud deployment using Render

## 📊 Dataset

**Dataset:** Heart Disease Dataset

**Source:** Kaggle
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

The dataset contains 13 input features and one target variable.

### Input Features

| Feature | Descrip:
 age	  - Age of the patient
sex	     -  Sex
cp	     -  Chest pain type
trestbps  - Resting blood pressure
chol	 -  Cholesterol level
fbs	     -  Fasting blood sugar
restecg	 -  Resting electrocardiographic results
thalach	 -  Maximum heart rate achieved
exang	 -  Exercise-induced angina
oldpeak	-   ST depression
slope	  - Slope of the ST segment
ca	   -    Number of major vessels
thal	 - Thalassemia

Target Variable:

0 = No Heart Disease
1 = Heart Disease
🧠 Machine Learning Model

Algorithm: Logistic Regression

Model Development Steps
Loaded and explored the dataset.
Separated input features and target variable.
Split the dataset into training and testing sets.
Applied StandardScaler for feature scaling.
Trained a Logistic Regression classifier.
Evaluated the model using:
Accuracy Score
Confusion Matrix
Classification Report
Saved the trained model using Joblib.

The preprocessing and classifier are combined into a Scikit-learn Pipeline to ensure consistent predictions.

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
FastAPI
Pydantic
Uvicorn
Joblib
Docker
Docker Compose
Git & GitHub
Render
📁 Project Structure
heart-disease-prediction-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── model/
│   └── heart_model.joblib
│
├── data/
│
├── train_model.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
⚡ API Endpoints

The API provides three endpoints.

Method	Endpoint	Description
GET	/health	Checks API health
GET	/info	Returns model information
POST	/predict	Predicts heart disease
1. Health Check

Request:

GET /health

Response:

{
  "status": "healthy",
  "message": "Heart Disease Prediction API is running!"
}
2. Model Information

Request:

GET /info

Returns the model type and the list of input features.

3. Heart Disease Prediction

Request:

POST /predict

Example Input:

{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}

Example Response:

{
  "heart_disease": true
}
🐳 Run Locally Using Docker
Prerequisites
Python
Docker Desktop
Git
1. Clone the Repository
git clone https://github.com/mdzubayereashraf/heart-disease-prediction-api.git
2. Navigate to the Project
cd heart-disease-prediction-api
3. Build and Run with Docker Compose
docker compose up --build
4. Open API Documentation

Visit:

http://localhost:8000/docs

You can now test all API endpoints using Swagger UI.

☁️ Deployment

The application is deployed on Render using Docker.

Deployment workflow:

Developed the Machine Learning model.
Built the FastAPI application.
Created a Dockerfile.
Configured Docker Compose.
Pushed the project to GitHub.
Connected the GitHub repository to Render.
Successfully deployed the API.

Deployment Status: Live ✅

⚠️ Disclaimer

This project is developed for educational and demonstration purposes only.

It is not a clinically validated medical diagnostic system. Predictions should not be used for medical decisions.

👨‍💻 Author

Zubayer

Statistics Graduate | Aspiring Data Scientist & Machine Learning Engineer

⭐ If you find this project interesting, feel free to explore the repository!
