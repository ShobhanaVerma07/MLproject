
# Student Performance Prediction

This repository contains a **Student Performance Prediction** model built to predict a student's academic performance based on their personal and background information. The model is deployed as a web application using **Streamlit**, where users can input details about a student and receive an instant performance prediction.

## Project Overview

The goal of this project is to use **machine learning** to predict student performance based on various factors, such as gender, race/ethnicity, parental education, and test scores. Predicting student performance can help educators and administrators make data-driven decisions to improve education strategies.

The project is developed using a **modular coding** approach, where each functionality—such as data processing, model prediction, and web deployment—has been broken down into distinct modules. This makes the code more organized, reusable, and easier to maintain.

### Main Components:
1. **Data Preprocessing**: Cleaning and transforming the data to make it suitable for machine learning models.
2. **Feature Engineering**: Selecting key features such as gender, race, parental education, lunch type, and test preparation to build the prediction model.
3. **Model Training**: Training a machine learning model to predict a student's overall performance based on the selected features.
4. **Deployment**: Deploying the model using **Streamlit** to create an interactive web application where users can input data and get predictions.

## Features of the Project

- **Custom Data Input**: Allows users to input student information (gender, race/ethnicity, parental education, etc.) through an intuitive interface.
- **Instant Predictions**: After inputting the required data, the app predicts the student’s performance in real-time.
- **Modular Code Design**: The codebase is structured in a modular way, ensuring that each function (e.g., data processing, model loading, predictions) is encapsulated in separate modules for better scalability and maintainability.

### Input Variables:

- **Gender**: Male or Female
- **Race/Ethnicity**: Group A to Group E
- **Parental Level of Education**: The highest level of education completed by the student’s parents
- **Lunch Type**: Whether the student receives standard or free/reduced-price lunch
- **Test Preparation**: Whether the student completed a test preparation course
- **Reading Score**: The student’s reading exam score
- **Writing Score**: The student’s writing exam score

## The Machine Learning Pipeline

The project is divided into two main components: **Data Preparation** and **Model Prediction**.

### 1. Data Preparation
Before making predictions, the data provided by the user is processed in the same way as the training data. This ensures that the input data matches the format expected by the machine learning model:
- **Categorical Features** such as gender and race/ethnicity are encoded using **OneHotEncoding**.
- **Numerical Features** such as reading and writing scores are scaled using **StandardScaler** to ensure all input data is on the same scale.

### 2. Model Prediction
After preprocessing, the data is passed to the machine learning model, which has been trained using **Scikit-learn**. The model predicts the student’s expected performance. The performance can be used to understand how the student is likely to perform based on their input data.

## Model Used

The machine learning model behind this prediction is a **Random Forest Classifier**, chosen because of its ability to handle both categorical and numerical data and its robustness in predictive tasks. The model was trained using historical student performance data, and key features were selected based on their correlation with the output variable (student performance).

The training process involved:
- **Hyperparameter Tuning** to optimize the performance of the Random Forest model.
- **Cross-validation** to ensure the model generalizes well to unseen data.

## How to Run the Project

To run the project locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/<your-username>/student-performance-prediction.git
cd student-performance-prediction
```

### 2. Install the required dependencies:
You can install the necessary libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application:
```bash
streamlit run app.py
```

Once the app is running, you can enter the student’s information in the input fields and click "Predict Performance" to get an instant prediction based on the machine learning model.

## Modular Design

This project uses a **modular approach**, which makes the code easy to manage and scale. Key functionalities are divided into:
- **Data Processing Module**: Handles data preprocessing, feature encoding, and scaling.
- **Prediction Module**: Contains the logic to load the trained model and make predictions based on user inputs.
- **Web Interface**: Built using **Streamlit** to provide a user-friendly interface for data input and result visualization.

