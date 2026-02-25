

# API Ingestion & Schema Normalization Framework
## 1. Project Overview

This repository contains a modular Data Engineering framework designed to automate the extraction of unstructured data from external REST API endpoints. The system focuses on **JSON Normalization (Flattening)** and metadata enrichment to prepare raw API responses for downstream Lakehouse integration.

## 2. Technical Stack

* **Language:** Python 3.10+
* **Data Processing:** Pandas (JSON Normalization & Transformation)
* **Network Layer:** Requests (REST API Integration)
* **Monitoring:** Streamlit (Pipeline Orchestration Dashboard)
* **Environment:** Virtual Environment (venv) with Git version control

## 3. Key Engineering Features

* **Automated Ingestion:** Handles secure connections to REST endpoints with comprehensive error handling for network timeouts and HTTP status codes.
* **Hierarchical Flattening:** Programmatically converts deeply nested JSON objects (e.g., nested address and company metadata) into a flat, relational DataFrame structure.
* **Data Lineage & Governance:** Every ingested record is enriched with a `batch_id` and `ingestion_timestamp` to maintain audit trails.
* **Dashboard-as-a-Service:** A built-in Streamlit portal allows users to trigger ingestion manually and audit the "Staging Zone" data quality in real-time.

## 4. Repository Structure

 app.py              # Streamlit Monitoring Dashboard
 app_pipeline.py     # Core ETL & API Ingestion Logic
 requirements.txt    # Project Dependencies
.gitignore          # Environment & Data Exclusion Rules
 staging_zone/       # Local Data Persistence (CSV)


## 5. Deployment Guide

### Prerequisites

Ensure you have Python installed and a virtual environment activated.

pip install -r requirements.txt


### Execution

1. **Launch the Pipeline:** You can run the ingestion logic directly via terminal:
python app_pipeline.py


2. **Start the UI Dashboard:**
For a visual overview and manual control:
streamlit run app.py



## 6. Business Impact

This framework eliminates the manual overhead of parsing complex JSON files. By providing a **Staging-ready CSV**, it serves as a critical entry point for Enterprise Data Lakes (Bronze Layer), ensuring that all incoming data is validated and structured for high-performance analytics.
