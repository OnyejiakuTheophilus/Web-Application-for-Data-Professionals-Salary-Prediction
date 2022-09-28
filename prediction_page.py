import streamlit as st
import pickle
import pandas as pd
import numpy as np


def load_model():
    with open("data science prediction.pki", "rb") as file:
        my_data = pickle.load(file)
    return my_data


my_data = load_model()
model_1_prediction = my_data["model_1"]
model_2_prediction = my_data["model_2"]
model_3_prediction = my_data["model_3"]
model_4_prediction = my_data["model_4"]
model_5_prediction = my_data["model_5"]
my_column = my_data["columns"]


def show_prediction_page():
    st.title("A Data Professional Salary Prediction App by Theophilus Onyejiaku")
    st.image("Data-Science-1.jpg")

    st.write("""Please select your choice so we can predict""")

    experience_level = ["Senior Level", "Mid level", "Entry Level", "Executive"]
    employment_type = ["Full Time", "Part Time", "Contract Type", "Freelance"]
    employee_residence = ['Germany', 'others', 'Great Britain', 'United States',
                          'France', 'India', 'Greece', 'Canada', 'Spain']
    company_location = ['Germany', 'others', 'Great Britain', 'United States',
                        'France', 'India', 'Greece', 'Canada', 'Spain']
    company_size = ['Large', 'Small', 'Medium Size']

    experience = st.selectbox("What is your Experience Level?", experience_level)
    employ_type = st.selectbox("What is the Employment Type?", employment_type)
    residence = st.selectbox("Where do you reside?", employee_residence)
    location = st.selectbox("Where is the Company Location?", company_location)
    size = st.selectbox("What is the Company Size?", company_size)

    my_columns = ['experience_level', 'employment_type', 'employee_residence',
                  'company_location', 'company_size']
    a = np.array([[experience, employ_type, residence, location, size]])
    a = pd.DataFrame(a, columns=my_columns)
    models_selection = ["model 1", "model 2", "model 3", "model 4", "model 5"]
    my_selection = st.selectbox("What model would you like to make this prediction", models_selection)
    if st.button('predict'):
        if my_selection == "model 1":
            prediction = model_1_prediction.predict(a)
            st.subheader(f"The estimated Salary you will earn is ${prediction[0]:.2f}")
        elif my_selection == "model 2":
            prediction = model_2_prediction.predict(a)
            st.subheader(f"The estimated Salary you will earn is ${prediction[0]:.2f}")
        elif my_selection == "model 3":
            prediction = model_3_prediction.predict(a)
            st.subheader(f"The estimated Salary you will earn is ${prediction[0]:.2f}")
        elif my_selection == "model 4":
            prediction = model_4_prediction.predict(a)
            st.subheader(f"The estimated Salary you will earn is ${prediction[0]:.2f}")
        elif my_selection == "model 5":
            prediction = model_5_prediction.predict(a)
            st.subheader(f"The estimated Salary you will earn is ${prediction[0]:.2f}")
    st.image("1eiE.gif")
    st.header('Thank you!')


show_prediction_page()
