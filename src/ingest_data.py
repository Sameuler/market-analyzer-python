import mysql.connector
import yfinance as yf
import pandas as pd


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter your password: "),
    database="market_prices"
)
cursor = db.cursor()

ticker_symbol = input("Enter ticker symbol: ")
ticker=yf.Ticker(ticker_symbol)
historical_data=ticker.history(period="1d", interval="1m")
pd.set_option('display.max_columns', None)
price=historical_data["Close"].iloc[-1]
time=historical_data.iloc[-1].name
sql_query = "INSERT INTO historic_prices (ticker_symbol, date_time, price) VALUES (%s, %s, %s)"

cursor.execute(sql_query, (ticker_symbol, time, price))
db.commit()
cursor.close()
db.close()