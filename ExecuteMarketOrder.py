import alpaca_trade_api as tradeapi

# Alpaca API credentials
APCA_API_KEY_ID = 'your_api_key_id'
APCA_API_SECRET_KEY = 'your_secret_key'
APCA_BASE_URL = 'https://paper-api.alpaca.markets'  

# Initialize the API
api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_BASE_URL, api_version='v2')

# Define the symbol and quantity to trade
symbol = 'AAPL'  
quantity = 1  

# Place a market order to buy
api.submit_order(
    symbol=symbol,
    qty=quantity,
    side='buy',
    type='market',
    time_in_force='gtc'
)

print(f"Bought {quantity} shares of {symbol}.")

// Handle email notifications of success and failure
// Inform to the the client that it is successful
