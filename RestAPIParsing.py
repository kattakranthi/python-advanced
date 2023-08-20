//Use http jar 
//use json jar 
//use requests jar
import requests
import json 
import requests

# Sample JSON response with exchange rate data
sample_json_response = {
    "base": "USD",
    "date": "2023-08-20",
    "rates": {
        "EUR": 0.85,
        "GBP": 0.73,
        "JPY": 110.15,
        "AUD": 1.37
        # ... more currencies
    }
}

# Parse the sample JSON response
base_currency = sample_json_response["base"]
exchange_date = sample_json_response["date"]
exchange_rates = sample_json_response["rates"]

print(f"Base Currency: {base_currency}")
print(f"Exchange Date: {exchange_date}")
print("Exchange Rates:")
for currency, rate in exchange_rates.items():
    print(f"{currency}: {rate}")



