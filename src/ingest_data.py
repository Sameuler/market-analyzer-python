import mysql.connector
import yfinance as yf

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter your password: "),
    database="market_prices"
)
cursor = db.cursor()
cursor.close()
db.close()