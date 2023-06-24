import requests

def search_ticker_symbol(query):
    url = f"https://query1.finance.yahoo.com/v1/finance/search?q={query}&newsCount=0"
    response = requests.get(url)
    data = response.json()

    if 'quotes' in data:
        # Extract the first matching ticker symbol
        first_result = data['quotes'][0]
        symbol = first_result['symbol']
        name = first_result['shortname']
        exchange = first_result['exchange']

        print(f"Symbol: {symbol}")
        print(f"Name: {name}")
        print(f"Exchange: {exchange}")
    else:
        print("No matching ticker symbol found.")

# Example usage
search_query = 'AAPL'  # Search query for Apple Inc.
search_ticker_symbol(search_query)

