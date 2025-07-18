# 📊 Telecom Customer Churn Prediction

This project demonstrates the complete process of building and deploying a machine learning model to predict customer churn in a telecom company.

> ⚠️ Note: This project is for educational and internal demonstration purposes only.

---

## 🛠️ Project Components

Below are the core files used in this implementation:

📁 Project Directory
├── app.py # Streamlit application
├── pipeline.pkl # Fitted ColumnTransformer (preprocessing pipeline)
├── model.pkl # Trained Logistic Regression model
├── preprocessor.pkl # Preprocessing logic (if stored separately)
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Raw dataset
├── ChurnImplementation.ipynb # Jupyter notebook with model training steps
├── README.md # This documentation

markdown
Copy
Edit

---

## 🧠 What this project does:

1. **Data Cleaning & Preprocessing**
   - Handled missing values
   - Categorical columns encoded via `OneHotEncoder`
   - Numerical columns scaled using `StandardScaler`
   - Combined using `ColumnTransformer`

2. **Model Building**
   - Used `LogisticRegression` from `scikit-learn`
   - Trained on preprocessed dataset
   - Serialized pipeline and model using `joblib`

3. **Deployment**
   - Built an interactive frontend using `Streamlit`
   - Inputs taken via sidebar
   - Predictions shown on main page

4. **Execution**
   - Once you run the app, you will get a line like this:
     ```
     your url is: https://tasty-tigers-switch.loca.lt
     ```
   - Visit that URL in your browser
   - ⚠️ Use the "External URL" (shown in terminal output) as your secret password for any optional gated inputs (if implemented)

---

## ▶️ How to Run the App

1. Install required libraries:
   ```bash
   pip install streamlit pandas numpy scikit-learn joblib
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Once it runs, note the following output (example):

csharp
Copy
Edit
Local URL: http://localhost:8501
Network URL: http://192.168.1.3:8501
External URL: http://34.80.9.43:8501
your url is: https://tasty-tigers-switch.loca.lt
Copy the your url into your browser to test the app remotely.

🧪 Sample Inputs
When using the web interface, enter:

gender: Male / Female

tenure: Numeric value (e.g., 5)

contract type: Month-to-month, One year, Two year

monthly charges: e.g., 45.65

etc...

🧩 Author Notes
This project includes obfuscation of certain logic in app.py to deter blind copy-pasting.

Some outputs require decoding or understanding of how external URLs link to frontend routing behavior.

All .pkl files are essential — do not delete or rename unless retraining the pipeline.

📧 Contact
If you're running this demo and have issues, reach out to the project maintainer.

