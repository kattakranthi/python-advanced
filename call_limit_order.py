'''
Limit Order Buy order
The current price of APPL stock is $100. 
Person A places a Buy limit order of APPL stocks of 100 if the price drops to $90.
The limit order executes in market if the price drops to $90.

'''

class Stock:
    def __init__(self, symbol, current_price):
        self.symbol = symbol
        self.current_price = current_price

class Broker:
    def place_limit_buy_order(self, stock, limit_price, quantity):
        if stock.current_price <= limit_price:
            print(f"Placing limit buy order for {quantity} shares of {stock.symbol} at {limit_price}")
            # Add your order execution logic here
        else:
            print(f"Limit price not reached for {stock.symbol}. Current price is {stock.current_price}")

# Example usage
if __name__ == "__main__":
    # Create a stock instance
    apple_stock = Stock(symbol="AAPL", current_price=150.0)

    # Create a broker instance
    my_broker = Broker()

    # Set a limit price and quantity for the buy order
    limit_price = 145.0
    quantity = 10

    # Place a limit buy order
    my_broker.place_limit_buy_order(apple_stock, limit_price, quantity)

'''
Sell Limit Order Example
'''
class Stock:
    def __init__(self, symbol, current_price):
        self.symbol = symbol
        self.current_price = current_price

class Broker:
    def place_limit_sell_order(self, stock, limit_price, quantity):
        if stock.current_price >= limit_price:
            print(f"Placing limit sell order for {quantity} shares of {stock.symbol} at {limit_price}")
            # Add your order execution logic here
        else:
            print(f"Limit price not reached for {stock.symbol}. Current price is {stock.current_price}")

# Example usage
if __name__ == "__main__":
    # Create a stock instance
    apple_stock = Stock(symbol="AAPL", current_price=150.0)

    # Create a broker instance
    my_broker = Broker()

    # Set a limit price and quantity for the sell order
    limit_price = 155.0
    quantity = 5

    # Place a limit sell order
    my_broker.place_limit_sell_order(apple_stock, limit_price, quantity)

import ccxt

exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
})

symbol = 'AAPL'  # Symbol for the stock you want to trade
side = 'buy'
price = 150.50  # Limit price you want to set
amount = 1.0  # Amount of stock you want to buy

order = exchange.create_limit_order(symbol, side, amount, price)
print(order)
