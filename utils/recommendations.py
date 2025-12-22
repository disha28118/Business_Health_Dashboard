def generate_recommendations(df):
    recs = []
    if 'revenue' in df.columns and df['revenue'].sum() < 100000:
        recs.append(" Increase marketing efforts to boost revenue.")
    if 'loss' in df.columns and df['loss'].mean() > 5000:
        recs.append(" Investigate major sources of loss to reduce them.")
    return recs or [" Business performance is within normal range."]
