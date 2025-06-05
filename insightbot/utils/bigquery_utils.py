from google.cloud import bigquery
import pandas as pd

PROJECT_ID = "your-project-id"
DATASET_ID = "insightbot"
TABLE_ID = "market_data"

client = bigquery.Client()

def upload_to_bigquery(df):
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    job = client.load_table_from_dataframe(df, table_ref)
    job.result()

def fetch_latest_analysis():
    query = f"""
        SELECT *
        FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
        ORDER BY Date DESC
        LIMIT 100
    """
    return client.query(query).to_dataframe()
