import streamlit as st
import pandas as pd
import requests
import os
from datetime import datetime

# --- UI CONFIGURATION ---
st.set_page_config(page_title="API Ingestion Portal", layout="wide")

# Custom Professional CSS
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .status-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

st.title(" External API Ingestion Framework")
st.markdown("---")

# Sidebar
st.sidebar.header("Pipeline Control")
st.sidebar.write("Project: API-to-Staging")
st.sidebar.write("Engineer: Srishti Goenka")

# --- API INGESTION LOGIC ---
def fetch_api_data():
    URL = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            # JSON Flattening (Resume Highlight)
            df = pd.json_normalize(data)
            df['ingested_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return df
        return None
    except:
        return None

# Execution Button
if st.sidebar.button("Trigger Ingestion"):
    with st.spinner("Fetching data from API..."):
        df_result = fetch_api_data()
        if df_result is not None:
            # Save to local staging
            os.makedirs("staging_zone", exist_ok=True)
            df_result.to_csv("staging_zone/stg_api_users.csv", index=False)
            st.success("SUCCESS: API Data Ingested and Normalized!")
        else:
            st.error("FAILED: Could not connect to API Source.")

# --- DISPLAY SECTION ---
st.subheader("Staging Area Audit")

if os.path.exists("staging_zone/stg_api_users.csv"):
    df = pd.read_csv("staging_zone/stg_api_users.csv")
    
    # KPI Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Records", len(df))
    c2.metric("Source", "REST API")
    c3.metric("Status", "Operational")

    st.markdown("### Flattened Data Preview")
    # Professional Column selection
    st.dataframe(df[['id', 'name', 'email', 'address.city', 'company.name', 'ingested_at']], use_container_width=True)

    # Search Feature
    search = st.text_input("Search User by Name")
    if search:
        filtered_df = df[df['name'].str.contains(search, case=False)]
        st.write(filtered_df)
else:
    st.info("Click 'Trigger Ingestion' on the sidebar to fetch data from the external API.")

st.markdown("---")
st.caption("DataOps Framework v2.0 | Secured API Endpoint")