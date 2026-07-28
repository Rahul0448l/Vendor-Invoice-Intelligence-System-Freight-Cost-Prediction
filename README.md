# 📦 Vendor Invoice Intelligence Portal

An end-to-end Machine Learning application that predicts freight costs and identifies vendor invoices requiring manual approval. The system combines regression and classification models with an interactive Streamlit dashboard to support finance and supply chain decision-making.

---

## 🚀 Live Demo

->https://rahul0448l-vendor-invoice-intelligence-system-freigh-app-lcncwm.streamlit.app/


---

## 📖 Overview

This project automates two common procurement and finance tasks:

### 🚛 Freight Cost Prediction
Predicts the estimated freight cost from invoice information using a trained Linear Regression model.

### 🧾 Invoice Risk Flagging
Predicts whether an invoice should be flagged for manual approval using a Random Forest classifier.

The application is built with **Python**, **Scikit-learn**, and **Streamlit**.

---

# ✨ Features

- 🚛 Freight Cost Prediction
- 🚨 Invoice Risk Detection
- 📊 Interactive Streamlit Dashboard
- 🤖 Machine Learning Models
- 📈 Real-time Predictions
- 💾 Model Serialization using Joblib
- 📂 SQLite Database Integration

---

# 🛠 Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Linear Regression
- Random Forest Classifier

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly

## Deployment

- Streamlit

## Database

- SQLite

## Model Saving

- Joblib

---

# 📁 Project Structure

```
Vendor-Invoice-Intelligence-System-Freight-Cost-Prediction/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── inventory.db
│
├── freight_cost_prediction/
│   ├── train.py
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   └── models/
│       └── predict_freight_model.pkl
│
├── invoice_flagging/
│   ├── train.py
│   ├── data_preprocessing.py
│   ├── modeling_evaluation.py
│   └── models/
│       ├── predict_flag_invoice.pkl
│       └── scaler.pkl
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
└── README.md
```

---

# 📊 Machine Learning Workflow

## Freight Cost Prediction

- Data Preprocessing
- Feature Engineering
- Linear Regression Training
- Model Evaluation
- Model Serialization
- Real-time Prediction

---

## Invoice Risk Prediction

- Data Cleaning
- Feature Engineering
- Feature Scaling
- Random Forest Training
- Model Evaluation
- Model Serialization
- Risk Prediction

---

# 📈 Model Performance

## Freight Cost Prediction

**Model**

- Linear Regression

Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Invoice Risk Classification

**Model**

- Random Forest Classifier

Performance

| Metric | Score |
|--------|-------|
| Accuracy | **88%** |
| Precision | **94%** |
| Recall | **72%** |
| F1 Score | **81%** |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Rahul0448l/Vendor-Invoice-Intelligence-System-Freight-Cost-Prediction.git
```

## Move to Project Folder

```bash
cd Vendor-Invoice-Intelligence-System-Freight-Cost-Prediction
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit

```bash
streamlit run app.py
```





# 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Machine Learning
- Data Preprocessing
- Feature Engineering
- Regression & Classification
- Model Evaluation
- Model Deployment
- Streamlit
- Git & GitHub
- End-to-End ML Application Development

---

# 👨‍💻 Author

**Rahul Singh Jethi**

- GitHub: https://github.com/Rahul0448l

---

# ⭐ Support

If you found this project useful, please consider giving it a **Star ⭐** on GitHub.
