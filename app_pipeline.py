import requests
import pandas as pd
import os
from datetime import datetime

def run_extraction_service():
    # 1. Configuration & Directory Setup
    STAGING_PATH = "staging_zone"
    os.makedirs(STAGING_PATH, exist_ok=True)
    
    # Remote API Endpoint (Industry Standard Mock API)
    API_SOURCE = "https://jsonplaceholder.typicode.com/users"
    
    print("|--- Initializing API Extraction Service ---|")
    
    try:
        # 2. Secure Data Fetching
        response = requests.get(API_SOURCE, timeout=10)
        response.raise_for_status() # Check for 404/500 errors
        raw_json = response.json()
        print(f"STATUS: Received {len(raw_json)} records from Source.")

        # 3. Data Transformation (The 'Wow' Factor: Flattening)
        # Nested JSON (Address/Company) ko relational columns mein convert karna
        print("STATUS: Executing JSON Normalization...")
        df = pd.json_normalize(raw_json)
        
        # Adding Audit Metadata
        df['ingestion_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df['batch_id'] = f"BATCH-{datetime.now().strftime('%m%d')}"

        # 4. Storage (Landing into Staging)
        file_path = os.path.join(STAGING_PATH, "api_raw_ingested.csv")
        df.to_csv(file_path, index=False)
        
        print(f"SUCCESS: Data persistent at {file_path}")
        return df

    except Exception as e:
        print(f"CRITICAL ERROR: Pipeline failed: {e}")
        return None

if __name__ == "__main__":
    run_extraction_service()