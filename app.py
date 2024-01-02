import pickle
import streamlit as st
from PIL import Image
import pandas as pd

def show_recommended_crop(nitrogen,phosphorous,potassium,temperature,humidity,ph,rainfall):
    # Función que recomienda el mejor tipo de cultivo para las características del terreno y clima

    parameters = pd.DataFrame([[nitrogen,phosphorous,potassium,temperature,humidity,ph,rainfall]],
                                columns=['N','P','K','temperature','humidity','ph','rainfall'])
    
    parameters = scaler.transform(parameters)

    Y_pred = knn.predict(parameters)
    recommended_crop = Y_pred[0]

    st.write(f'# The type of crop best suited for your soil is: :blue[{recommended_crop}].')

    image = Image.open('crop_images/' + recommended_crop + '.jpg')

    st.image(image)

    return recommended_crop

# Importamos el modelo de machine learning
with open('pickle_objects/knn.pickle', 'rb') as f:
    knn = pickle.load(f)

# Importamos el objeto scaler
with open('pickle_objects/scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)

st.markdown("<h1 style='text-align: center; color: green;'>Crop recommender</h1>", 
            unsafe_allow_html=True)

with st.form('input_parameters'):
    st.write('Insert the parameters related to your soil and climate')
    nitrogen = st.number_input('Nitrogen (kg/ha):')
    phosphorous = st.number_input('Phosphorous (kg/ha):')
    potassium = st.number_input('Potassium (kg/ha):')
    temperature = st.number_input('Temperature (ºC):')
    humidity = st.number_input('Humidity (%):')
    ph = st.number_input('pH:')
    rainfall = st.number_input('Rainfall (mm):')

    if st.form_submit_button("Submit"):
        show_recommended_crop(nitrogen,phosphorous,potassium,temperature,humidity,ph,rainfall)