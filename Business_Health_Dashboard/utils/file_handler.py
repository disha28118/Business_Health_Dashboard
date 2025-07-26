import pandas as pd

def load_data(uploaded_file):
    if uploaded_file.name.lower().endswith('.csv'):
        return pd.read_csv(uploaded_file)
    elif uploaded_file.name.lower().endswith(('.xls', '.xlsx')):
        return pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload CSV or Excel.")
