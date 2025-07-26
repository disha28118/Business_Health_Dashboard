def detect_anomalies(df):
    anomalies = []
    if 'cost' in df.columns and df['cost'].max() > 100000:
        anomalies.append(" Extremely high cost detected.")
    if 'profit' in df.columns and df['profit'].min() < 0:
        anomalies.append(" Negative profit observed in some records.")
    return anomalies or ["No anomalies detected."]