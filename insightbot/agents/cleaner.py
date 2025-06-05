from google.adk.agents import Agent
import pandas as pd
from utils.bigquery_utils import upload_to_bigquery

class CleanerAgent(Agent):
    def run(self, data):
        print("[Cleaner] Cleaning data...")
        df = pd.DataFrame(data)
        df.dropna(inplace=True)
        upload_to_bigquery(df)
        self.send("Analyzer", df.to_dict())