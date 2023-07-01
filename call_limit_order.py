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
