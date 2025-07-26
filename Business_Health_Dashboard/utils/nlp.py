import re

def parse_user_query(query, columns):
    """
    Extracts intent from user query and maps it to available columns.
    Returns a dictionary with type of chart and relevant columns.
    """
    query = query.lower()
    chart_type = "bar"  # Default

    if "scatter" in query:
        chart_type = "scatter"
    elif "line" in query:
        chart_type = "line"
    elif "hist" in query or "distribution" in query:
        chart_type = "histogram"
    elif "pie" in query:
        chart_type = "pie"
    elif "box" in query:
        chart_type = "box"

    # Try to find matching column names in query
    matched_cols = [col for col in columns if col.lower() in query]

    if len(matched_cols) >= 2:
        x_col, y_col = matched_cols[0], matched_cols[1]
    elif len(matched_cols) == 1:
        x_col, y_col = matched_cols[0], None
    else:
        x_col, y_col = None, None

    return {
        "chart_type": chart_type,
        "x": x_col,
        "y": y_col
    }
