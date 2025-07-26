def clean_data_with_model(df):
    # Standardize column names
    df = df.rename(columns=lambda c: c.strip().lower().replace(' ', '_'))
    # Remove duplicates
    df = df.drop_duplicates()
    # Fill missing values forward/backward
    df = df.fillna(method='ffill').fillna(method='bfill')
    return df
