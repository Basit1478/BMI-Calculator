import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m)", min_value=0.1, step=0.01)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        classification = classify_bmi(bmi)
        if classification == "Underweight":
            st.warning(f"Your BMI is {bmi:.2f}. You are underweight. Consider gaining some weight for better health.")
        elif classification == "Normal weight":
            st.success(f"Your BMI is {bmi:.2f}. You have a normal weight. Keep maintaining your healthy lifestyle!")
        elif classification == "Overweight":
            st.warning(f"Your BMI is {bmi:.2f}. You are overweight. Consider a balanced diet and exercise.")
        else:
            st.error(f"Your BMI is {bmi:.2f}. You are obese. It's recommended to consult a healthcare professional.")
    else:
        st.error("Height must be greater than 0")
