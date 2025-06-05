from google.adk.agents import Agent
import yfinance as yf
import pandas as pd

class DataFetcherAgent(Agent):
    def run(self):
        print("[DataFetcher] Fetching market data...")
        ticker = yf.Ticker("AAPL")
        hist = ticker.history(period="1mo")
        hist.reset_index(inplace=True)
        self.send("Cleaner", hist.to_dict())