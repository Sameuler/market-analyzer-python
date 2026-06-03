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
query = "SELECT * FROM historic_prices ORDER BY date_time DESC LIMIT 100;"
df = pd.read_sql(query, connection)

df_sorted=df.sort_values(by="date_time")
st.subheader("Latest Database Market Prices")
st.dataframe(df)

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
