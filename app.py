import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('model/iris_model.pkl', 'rb'))

# Map prediction numbers to species names
species_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

st.title("Iris Species Predictor")

with st.form('iris_app_form'):
    sl = st.number_input('Enter Sepal Length (cm)')
    sw = st.number_input('Enter Sepal Width (cm)')
    pl = st.number_input('Enter Petal Length (cm)')
    pw = st.number_input('Enter Petal Width (cm)')
    submitted = st.form_submit_button('Predict Species')

if submitted:
    prediction = model.predict([[sl, sw, pl, pw]])
    species_name = species_map[prediction[0]]  # Convert number to species name
    st.success(f'Predicted species: {species_name}')
