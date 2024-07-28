import streamlit as st
import numpy as np
import joblib

# Load the model and scaler once at startup
model_path = (r'C:\Users\Praveen Shetty\YourProjectDirectory\svm_model.pkl')
scaler_path = (r'C:\Users\Praveen Shetty\YourProjectDirectory\scaler.pkl')
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

st.title("Loan Approval Prediction")

st.write("""
Please enter the following details to predict loan approval:
""")

self_employed = st.text_input("Self Employed (0 or 1)")
income_annum = st.text_input("Income Annum")
loan_amount = st.text_input("Loan Amount")
loan_term = st.text_input("Loan Term")
cibil_score = st.text_input("CIBIL Score")
residential_assets_value = st.text_input("Residential Assets Value")
commercial_assets_value = st.text_input("Commercial Assets Value")
luxury_assets_value = st.text_input("Luxury Assets Value")
bank_asset_value = st.text_input("Bank Asset Value")

if st.button("Predict"):
    try:
        features = np.array([[
            float(self_employed),
            float(income_annum),
            float(loan_amount),
            float(loan_term),
            float(cibil_score),
            float(residential_assets_value),
            float(commercial_assets_value),
            float(luxury_assets_value),
            float(bank_asset_value)
        ]])

        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)
        if prediction[0] == 0:
            st.error('❌ Loan Approval Prediction: Not Approved')
        else:
            st.success('✅ Loan Approval Prediction: Approved')
    except Exception as e:
        st.error(f'Error: {e}')
