📊 Business Health Dashboard: Anomaly Detection & Recommendations System

A powerful **Streamlit-based web app** that allows businesses to upload messy datasets (CSV or Excel), automatically clean them using a trained machine learning model, detect anomalies, visualize KPIs, and generate actionable recommendations. It also provides a one-click option to export a professional PDF business report.

---

## 🚀 Features

- ✅ **Upload CSV or Excel** files with no restrictions on size or format  
- 🧹 **Auto Data Cleaning** using machine learning models (missing values, formatting, duplication)  
- 📈 **Interactive Dashboard** with visualizations (Date, Region, Profit, Loss, Cost, etc.)  
- 🔍 **Anomaly Detection** to spot unusual business behavior  
- 🧠 **Actionable Recommendations** using rule-based or model-assisted logic  
- 📄 **PDF Report Generation** that includes clean data and business suggestions  

---

## 📁 Project Structure

.
├── app.py
├── business_data.csv
├── requirements.txt
├── README.md
├── outputs/
│ └── reports/
│ └── business_health_report.pdf ← auto-generated
└── utils/
├── file_handler.py ← Loads CSV or Excel
├── cleaner.py ← ML-based data cleaning
├── visualizer.py ← Dashboard plots
├── anomalydetection.py ← Outlier/anomaly detection logic
└── recommendations.py ← Business advice generator

---

## 📦 Installation

### ⚙️ Pre-requisites

- Python 3.8+
- pip (Python package installer)

### 🔧 Setup Instructions

```bash
# Clone the repo or extract the ZIP
cd your_project_directory

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
📤 Export to PDF
Click "Export Report as PDF" in the app to generate a simple, clean business health report containing:

First 20 rows of cleaned data

Anomaly summary

Actionable business recommendations

📁 The report is saved in:

bash
Copy
Edit
outputs/reports/business_health_report.pdf
📊 Sample Dashboard Visuals
Revenue Trends over Time

Profit vs Cost Heatmap by Region

Loss Distribution by Product or Department

Outlier Events with Anomaly Flags

📘 Sample Data Columns
You can upload any file with the following suggested columns:

Date (yyyy-mm-dd format)

Region

Profit

Loss

Cost

📁 Sample File
A sample dataset business_data.csv with 1000+ rows and appropriate columns is included for quick testing.

👨‍💻 Author
Disha Gupta
Streamlit | Python | Data Science

⚖️ License
This project is licensed under the MIT License.