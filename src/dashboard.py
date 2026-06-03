import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import time as t

st.title("Market Analyzer")

@st.cache_resource
def get_connection(password):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="market_prices"
    )
db_password= st.text_input("Enter your DB Password: ",type="password")
if not db_password:
    st.warning("Please enter your DB Password")
    st.stop()
try:
    connection = get_connection(db_password)
except Exception as e:
    st.error(f"Failed to connect: {e}")
    st.stop()
query = "SELECT * FROM historic_prices ORDER BY date_time DESC;"
df = pd.read_sql(query, connection)

df_sorted=df.sort_values(by="date_time")

st.subheader("Portfolio Performance Metrics")

unique_tickers =df_sorted['ticker_symbol'].unique()
cols=st.columns(len(unique_tickers))
for col, ticker in zip(cols, unique_tickers):
    ticker_df=df[df['ticker_symbol']==ticker].sort_values(by="date_time")
    if not ticker_df.empty:
        initial_price=ticker_df['price'].iloc[0]
        latest_price=ticker_df['price'].iloc[-1]
        pct_change=(latest_price-initial_price)/initial_price
        col.metric(
            label=ticker,
            value=f"${latest_price:.2f}",
            delta=f"${pct_change:+.2f}"
        )
fig=px.line(
    df,
    x="date_time",
    y="price",
    color="ticker_symbol",
    title="Intraday Prices",
    labels={
        "date_time": "Date",
        "price": "Price",
})
st.plotly_chart(fig)

t.sleep(10)
st.rerun()
