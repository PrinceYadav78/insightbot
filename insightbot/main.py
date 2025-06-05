from google.adk.agents import Agent
from agents.data_fetcher import DataFetcherAgent
from agents.cleaner import CleanerAgent
from agents.analyzer import AnalyzerAgent
from agents.presenter import PresenterAgent

system = Agent(name="SystemAgent")

fetcher = DataFetcherAgent(name="Fetcher")
cleaner = CleanerAgent(name="Cleaner")
analyzer = AnalyzerAgent(name="Analyzer")
presenter = PresenterAgent(name="Presenter")

system.sub_agents = [fetcher, cleaner, analyzer, presenter]
system.run_live(parent_context=None)

