import os
import sys
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Custom CSS to make it stylish
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #3d85c6;
        text-align: center;
        padding-bottom: 10px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #3d85c6;
        color: white;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True
)

# Set up the Streamlit app layout
st.markdown('<h1 class="title">🎓 Student Performance Prediction 🧠</h1>', unsafe_allow_html=True)

st.write("""
### Predict student performance based on various factors!
""")

# Sidebar section for inputs
with st.sidebar:
    st.subheader("Input Student Information")
    
    gender = st.radio("Select Gender", ("male", "female"), help="Select the student's gender")  # Changed to radio button
    race_ethnicity = st.selectbox("Select Race/Ethnicity", 
                                  ("group A", "group B", "group C", "group D", "group E"),
                                  help="Select the student's race/ethnicity group")  # Added a help tooltip
    parental_level_of_education = st.selectbox("Parental Level of Education", 
                                               ("some high school", "high school", "associate's degree", 
                                                "some college", "bachelor's degree", "master's degree"),
                                               help="Select the parent's level of education")
    lunch = st.selectbox("Lunch", ("standard", "free/reduced"), help="Select the type of lunch the student gets")
    test_preparation_course = st.selectbox("Test Preparation Course", ("none", "completed"),
                                           help="Select if the student completed the test preparation course")
    
    reading_score = st.slider("Reading Score", 0, 100, 50, help="Input the student's reading score")
    writing_score = st.slider("Writing Score", 0, 100, 50, help="Input the student's writing score")

# Explanation of factors
with st.expander("ℹ️ What do these factors mean?"):
    st.write("""
    - **Gender**: The gender of the student.
    - **Race/Ethnicity**: The racial or ethnic group the student belongs to.
    - **Parental Level of Education**: The highest level of education achieved by the student's parents.
    - **Lunch**: Whether the student receives standard or free/reduced lunch.
    - **Test Preparation Course**: Whether the student has completed a test preparation course.
    - **Reading Score & Writing Score**: The student's scores in reading and writing subjects.
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Button to make predictions with hover effect
if st.button('📊 Predict Performance', help="Click to predict the student's score"):
    with st.spinner('Predicting...'):
        try:
            # Create a custom data instance using the user inputs
            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            # Convert the input data to a dataframe
            pred_df = data.get_data_as_data_frame()
            st.write("### Input Data Summary:")
            st.write(pred_df)

            # Initialize the PredictPipeline
            predict_pipeline = PredictPipeline()

            # Make predictions using the pipeline
            results = predict_pipeline.predict(pred_df)

            # Show the results on the web page
            st.success(f"🎯 The predicted score is: **{results[0]}**")

        except CustomException as ce:
            st.error(f"Prediction failed: {ce}")

        except Exception as e:
            st.error(f"An error occurred: {e}")


# Footer with some styling
st.markdown(
    """
    <div class="footer">
        Made with 💻 by Shobhana | Powered by Streamlit
    </div>
    """, unsafe_allow_html=True
)
