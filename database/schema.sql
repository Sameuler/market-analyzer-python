CREATE DATABASE IF NOT EXISTS market_prices;
USE market_prices;
CREATE TABLE IF NOT EXISTS historic_prices (
	ID int auto_increment PRIMARY KEY,
    ticker_symbol varchar(5),
    date_time datetime,
    price decimal(16,4)
);



    
    