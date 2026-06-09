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

dropdown_tickers =["All Tickers"]+list(df_sorted['ticker_symbol'].unique())

selected_ticker = st.selectbox(
    label="Select a stock:",
    options=dropdown_tickers,
    index=0
)
if selected_ticker== "All Tickers":
    chart_df=df_sorted
else:
    chart_df=df[df['ticker_symbol']==selected_ticker]


fig=px.line(
    chart_df,
    x="date_time",
    y="price",
    color="ticker_symbol",
    title=f"Market Prices {selected_ticker}",
    labels={
        "date_time": "Date",
        "price": "Price",
})
st.plotly_chart(fig)

t.sleep(10)
st.rerun()
