import yfinance as yf  # You can use the yfinance library to fetch stock data
import pandas as pd

# Define the stock symbol and the date range for historical data
stock_symbol = "AAPL"  # Replace with the symbol of the stock you want to trade
start_date = "2020-01-01"
end_date = "2021-12-31"

# Fetch historical stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate a short-term and a long-term moving average
short_window = 50
long_window = 200

stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window).mean()
stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window).mean()

# Initialize a variable to track whether we have a position in the stock
have_position = False

# Define a variable to represent the amount of stock to buy
buy_quantity = 100  # Replace with your desired buy quantity

# Iterate through the stock data
for index, row in stock_data.iterrows():
    # Check if a buy signal is generated (short-term MA crosses above long-term MA)
    if row['Short_MA'] > row['Long_MA'] and not have_position:
        # Place a buy order
        print(f"Buy {buy_quantity} shares of {stock_symbol} at {row['Close']:.2f} on {index}")
        have_position = True
    
    
# Close any remaining position at the end of the data
if have_position:
    last_close_price = stock_data.iloc[-1]['Close']
    print(f"Close the position at {last_close_price:.2f}")
    have_position = False

