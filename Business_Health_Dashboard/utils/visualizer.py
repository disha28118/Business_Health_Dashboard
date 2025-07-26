import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_dashboard(df):
    # Ensure date column is datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    if 'revenue' in df.columns and 'date' in df.columns:
        st.subheader("Revenue Over Time")
        fig = px.line(df, x='date', y='revenue', title="Revenue Trend")
        st.plotly_chart(fig, use_container_width=True)

    if 'sales' in df.columns and 'region' in df.columns:
        st.subheader("Sales by Region")
        fig = px.bar(df, x='region', y='sales', title="Sales by Region", color='region')
        st.plotly_chart(fig, use_container_width=True)

    metrics = {}
    for col in ['profit', 'loss', 'cost']:
        if col in df.columns:
            metrics[col.capitalize()] = df[col].sum()
    if metrics:
        st.subheader("Aggregate Metrics")
        for k,v in metrics.items():
            st.metric(k, f"₹{v:,.2f}")
from sklearn.linear_model import LinearRegression
import numpy as np

def train_and_plot_regression(df, target_col):
    numeric_cols = df.select_dtypes(include='number').columns
    features = [col for col in numeric_cols if col != target_col]

    for feature in features:
        X = df[[feature]].dropna()
        y = df[target_col].loc[X.index]
        if len(X) > 1:
            model = LinearRegression()
            model.fit(X, y)
            y_pred = model.predict(X)

            st.write(f"### Regression: {target_col} vs {feature}")
            fig = px.scatter(df, x=feature, y=target_col, title=f"{target_col} vs {feature}")
            fig.add_scatter(x=X[feature], y=y_pred, mode='lines', name='Regression Line')
            st.plotly_chart(fig)
