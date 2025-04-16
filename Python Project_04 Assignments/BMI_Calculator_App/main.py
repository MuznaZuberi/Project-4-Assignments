# =============================== 🏋️‍♀️ BMI Calculator | By Muzna Amir Zubairi ===============================

import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Weight kg: ", min_value=1.0, max_value=200.0)
height = st.number_input("Height m: ", min_value=0.5, max_value=2.5)

bmi = weight / (height ** 2)
category = "Underweight 🥺" if bmi < 18.5 else "Normal weight 👍" if bmi < 24.9 else "Overweight ⚠️" if bmi < 29.9 else "Obese ⚠️"

st.write(f"BMI: {bmi:.2f}")
st.write(f"Category: {category}")

st.markdown("<p style='text-align: right;'>❤️ Built by Muzna Amir Zubairi 💻</p>", unsafe_allow_html=True)
