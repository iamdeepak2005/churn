# 💼 Customer Churn Prediction System

---

## 🧠 Project Objective

The primary goal of this project is to build a machine learning model that **predicts customer churn** — whether a customer will leave a telecom service or not — using structured data. The model is embedded into an interactive **Streamlit web application**.

---

## 📂 Folder Structure

churn/
│
├── ChurnImplementation.ipynb ← Full EDA, preprocessing, model training
├── WA_Fn-UseC_-Telco-Customer-Churn.csv ← Original dataset
├── pipeline.pkl ← Serialized pipeline (preprocessor + model)
├── model.pkl ← Trained model (Random Forest)
├── preprocessor.pkl ← Serialized preprocessing pipeline
├── app.py ← Streamlit frontend interface
├── README.md ← This file

yaml
Copy
Edit

---

## 📝 Dataset Information

- 📌 **Source**: IBM Watson Telco Customer Churn Dataset  
- 📌 **Type**: Structured (CSV)  
- 📌 **Target**: `Churn` (Yes/No)  
- 📌 **Records**: ~7043  
- 📌 **Features**:
  - Demographics: `gender`, `SeniorCitizen`, `Partner`, `Dependents`
  - Services: `PhoneService`, `InternetService`, `StreamingTV`, etc.
  - Account Info: `tenure`, `Contract`, `PaymentMethod`, `MonthlyCharges`, etc.

---

## ⚙️ Workflow Breakdown

### 🔹 Step 1: Data Cleaning & Transformation

- Handled missing and erroneous entries in `TotalCharges`
- Converted all categorical fields using **OneHotEncoding**
- Applied **StandardScaler** to numerical columns

---

### 🔹 Step 2: Model Building

- Data split into `X_train`, `X_test`, `y_train`, `y_test`
- Multiple algorithms tested:
  - ✅ Random Forest (Best Performance)
  - Logistic Regression
  - Decision Tree

- Best model saved using `joblib` as: `model.pkl`

---

### 🔹 Step 3: Pipeline Integration

- Built a full preprocessing + model pipeline:
  - `ColumnTransformer` for column-wise preprocessing
  - Wrapped with classifier using `Pipeline`
  - Saved complete object to `pipeline.pkl` for inference

---

### 🔹 Step 4: Web Application (Streamlit)

- Built a UI with:
  - Select boxes & sliders for inputs
  - Prediction on button click
  - Clear result: **“Likely to Churn”** or **“Not Likely to Churn”**
- Web app reads from `pipeline.pkl` and applies on user inputs

---

## 🚀 How to Run the Project

### 🧰 Step 1: Clone the Repository
```bash
git clone https://github.com/iamdeepak2005/churn.git
cd churn
🧰 Step 2: Set up a Virtual Environment
bash
Copy
Edit
python -m venv .venv
.\.venv\Scripts\activate        # Windows
# source .venv/bin/activate    # Mac/Linux
🧰 Step 3: Install Required Libraries
Create a file requirements.txt or install manually:

bash
Copy
Edit
pip install streamlit scikit-learn pandas numpy matplotlib seaborn
🧰 Step 4: Launch the Streamlit App
bash
Copy
Edit
streamlit run app.py
🧾 Output Screenshot Example
📸 When you run the app, you’ll see an interactive form with dropdowns, sliders, and a Predict button.

The prediction result will appear as:

✅ Not Likely to Churn
or
⚠️ Likely to Churn

🔮 Future Enhancements
Add user authentication to app

Deploy on cloud (Render / Heroku / AWS EC2)

Show SHAP-based model explanations

Include download option for prediction history

👨‍💻 Author
Name	GitHub
Deepak B O	@iamdeepak2005
