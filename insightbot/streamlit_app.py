import streamlit as st
import pandas as pd

st.title("📈 InsightBot – AI Market Analyst")

try:
    df = pd.read_csv("output/latest_insights.csv")
    st.subheader("Latest Market Trends")
    st.line_chart(df.set_index("Date")["Close"])
    st.markdown("### Summary")
    st.write(df["summary"].iloc[-1])
except Exception as e:
    st.error(f"Error loading data: {e}")