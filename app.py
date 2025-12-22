import streamlit as st
import pandas as pd
from utils.file_handler import load_data
from utils.cleaner import clean_data_with_model
from utils.visualizer import plot_dashboard, train_and_plot_regression
from utils.anomaly_detection import detect_anomalies
from utils.recommendations import generate_recommendations
from utils.nlp import parse_user_query  # Ensure this is defined
from fpdf import FPDF
import plotly.express as px
import os

st.set_page_config(page_title="Business Health Dashboard", layout="wide")
st.title(" Business Health Dashboard")

uploaded_file = st.file_uploader(" Upload a CSV or Excel File", type=["csv", "xlsx"])

if uploaded_file:
    # Load and Display Raw Data
    df = load_data(uploaded_file)
    st.subheader(" Raw Data Preview")
    st.dataframe(df.head())

    # Clean Data Automatically
    df_clean = clean_data_with_model(df)
    st.subheader(" Cleaned Data Preview")
    st.dataframe(df_clean.head())

    # Visual Insights
    st.subheader(" Business Insights")
    plot_dashboard(df_clean)

    # Regression Analysis
    st.subheader("Regression Analysis")
    target = st.selectbox("Select target column for regression:", df_clean.select_dtypes(include='number').columns)
    if target:
        train_and_plot_regression(df_clean, target)

    # Detect Anomalies and Generate Recommendations
    anomalies = detect_anomalies(df_clean)
    recs = generate_recommendations(df_clean)

    st.subheader(" Anomalies Detected")
    st.dataframe(anomalies)

    st.subheader(" Actionable Recommendations")
    for rec in recs:
        st.write("- ", rec)

    # Export to PDF
    if st.button(" Export Report as PDF"):
        output_dir = "outputs/reports"
        os.makedirs(output_dir, exist_ok=True)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt="Business Health Report", ln=True)

        pdf.cell(0, 10, txt="Cleaned Data (First 20 Rows):", ln=True)
        for row in df_clean.head(20).astype(str).values:
            pdf.cell(0, 5, txt=" | ".join(row), ln=True)

        pdf.ln(5)
        pdf.cell(0, 10, txt="Key Recommendations:", ln=True)
        for rec in recs:
            pdf.multi_cell(0, 5, txt=f"- {rec}")

        report_path = f"{output_dir}/business_health_report.pdf"
        pdf.output(report_path)
        st.success(f"Report saved to `{report_path}`")
else:
    st.info(" Please upload a CSV or Excel file to begin.")
