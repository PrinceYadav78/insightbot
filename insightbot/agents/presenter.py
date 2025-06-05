from google.adk.agents import Agent
import pandas as pd

class PresenterAgent(Agent):
    def run(self, data):
        print("[Presenter] Preparing data for UI...")
        df = pd.DataFrame(data)
        df.to_csv("output/latest_insights.csv", index=False)