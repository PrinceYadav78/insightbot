from google.adk.agents import Agent
import pandas as pd

class AnalyzerAgent(Agent):
    def run(self, data):
        print("[Analyzer] Analyzing data...")
        df = pd.DataFrame(data)
        df["MA20"] = df["Close"].rolling(window=20).mean()
        df["Volatility"] = df["Close"].rolling(window=20).std()
        df["summary"] = "Price trend analysis complete."
        self.send("Presenter", df.to_dict())