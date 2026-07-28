import streamlit as st
import pandas as pd

from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide"
)

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------

st.title("📦 Vendor Invoice Intelligence Portal")
st.subheader("AI-Driven Freight Cost Prediction & Invoice Risk Flagging")

st.markdown("""
This internal analytics portal leverages Machine Learning to:

- 📈 Forecast Freight Costs
- 🚨 Detect Risky Vendor Invoices
- ⚡ Improve Finance Operations
""")

st.divider()

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------

st.sidebar.title("🔍 Model Selection")

selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Business Impact

- 📉 Better Cost Forecasting
- 🚨 Reduced Invoice Fraud
- ⏱ Faster Approval Process
""")

# ============================================================
# Freight Cost Prediction
# ============================================================

if selected_model == "Freight Cost Prediction":

    st.header("🚛 Freight Cost Prediction")

    st.write(
        "Enter the invoice amount to estimate the freight cost."
    )

    with st.form("freight_form"):

        dollars = st.number_input(
            "💰 Invoice Dollars",
            min_value=1.0,
            value=18500.0,
            step=100.0
        )

        submit = st.form_submit_button(
            "🎯 Predict Freight Cost"
        )

    if submit:

        input_data = {
            "Dollars": [dollars]
        }

        prediction = predict_freight_cost(input_data)

        freight_cost = prediction["Predicted_Freight"].iloc[0]

        st.success("Prediction Completed Successfully")

        st.metric(
            "Estimated Freight Cost",
            f"${freight_cost:,.2f}"
        )

# ============================================================
# Invoice Flag Prediction
# ============================================================

else:

    st.header("🧾 Invoice Manual Approval Prediction")

    st.write(
        "Predict whether an invoice should be flagged for manual approval."
    )

    with st.form("invoice_form"):

        col1, col2 = st.columns(2)

        with col1:

            invoice_quantity = st.number_input(
                "Invoice Quantity",
                min_value=1,
                value=50
            )

            invoice_dollars = st.number_input(
                "Invoice Dollars",
                min_value=1.0,
                value=352.95
            )

            freight = st.number_input(
                "Freight",
                min_value=0.0,
                value=1.73
            )

        with col2:

            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=1,
                value=162
            )

            total_item_dollars = st.number_input(
                "Total Item Dollars",
                min_value=1.0,
                value=2476.0
            )

        submit = st.form_submit_button(
            "🧠 Evaluate Invoice Risk"
        )

    if submit:

        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        prediction = predict_invoice_flag(input_data)

        flag = prediction["Predicted_Flag"].iloc[0]

        if flag == 1:

            st.error("🚨 Invoice requires MANUAL APPROVAL")

        else:

            st.success("✅ Invoice is SAFE for Auto Approval")