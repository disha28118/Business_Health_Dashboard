from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def train_and_plot_regression(df, target_column):
    numeric_cols = df.select_dtypes(include='number').columns.drop(target_column)
    X = df[numeric_cols]
    y = df[target_column]

    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)

    st.subheader("Regression Model Results")
    st.write("R² Score:", model.score(X, y))

    for col in numeric_cols:
        plt.figure(figsize=(6, 3))
        sns.regplot(x=col, y=target_column, data=df)
        st.pyplot(plt)
