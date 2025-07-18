import streamlit as st
import joblib
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Churn Prediction App",
    page_icon="📉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title
st.title("📊 Customer Churn Prediction")

# Load pipeline (includes preprocessor + classifier)
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Input Form
with st.form("churn_form"):
    st.subheader("Enter Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
        device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

    with col2:
        tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check", "Mailed check",
                "Bank transfer (automatic)", "Credit card (automatic)"
            ]
        )
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
        total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=500.0)

    # Submit button
    submit = st.form_submit_button("Predict Churn")

    if submit:
        try:
            # Prepare the input data as a single-row DataFrame
            input_data = {
                "gender": gender,
                "SeniorCitizen": senior_citizen,
                "Partner": partner,
                "Dependents": dependents,
                "tenure": tenure,
                "PhoneService": phone_service,
                "MultipleLines": multiple_lines,
                "InternetService": internet_service,
                "OnlineSecurity": online_security,
                "OnlineBackup": online_backup,
                "DeviceProtection": device_protection,
                "TechSupport": tech_support,
                "StreamingTV": streaming_tv,
                "StreamingMovies": streaming_movies,
                "Contract": contract,
                "PaperlessBilling": paperless_billing,
                "PaymentMethod": payment_method,
                "MonthlyCharges": monthly_charges,
                "TotalCharges": total_charges
            }

            df_input = pd.DataFrame([input_data])

            # Predict using the pipeline
            prediction = model.predict(df_input)[0]
            prob = model.predict_proba(df_input)[0][1]

            st.markdown("---")
            if prediction == 1:
                st.error(f"""⚠️ **High Risk**: This customer is likely to churn.  
                📉 _Churn Probability: {prob:.2%}_""")
            else:
                st.success(f"""✅ **Low Risk**: This customer is likely to stay.  
                📈 _Retention Probability: {1 - prob:.2%}_""")

        except Exception as e:
            st.error(f"❌ An error occurred: `{str(e)}`")
