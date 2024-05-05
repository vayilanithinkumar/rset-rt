import numpy as np
import pickle
import streamlit as st

loaded_model= pickle.load(open(http://localhost:8502/diabetes_model.sav','rb'))

def diabetes_prediction(input_data):
    input_data = [10,168,74,0,0,38,0.537,34]
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return 'person is non diabetic'
    else:
        return 'person is diabetic'
    
    
def main():
    st.title('Diabetes Prediction Web app')
    
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure level')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    
    
    diagnosis = " "
    
    if st.button('Diabetes test result'):
        diagnosis_prediction = ([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()
    
    
        
