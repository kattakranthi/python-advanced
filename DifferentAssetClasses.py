class Asset:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.price = 0.0

    def set_price(self, price):
        self.price = price

    def get_value(self):
        return self.price

class Stock(Asset):
    def __init__(self, name, symbol, shares):
        super().__init__(name, symbol)
        self.shares = shares

    def get_value(self):
        return self.price * self.shares

class Bond(Asset):
    def __init__(self, name, symbol, face_value, coupon_rate):
        super().__init__(name, symbol)
        self.face_value = face_value
        self.coupon_rate = coupon_rate

    def get_value(self):
        return self.face_value + (self.face_value * self.coupon_rate / 100)

class RealEstate(Asset):
    def __init__(self, name, symbol, property_value):
        super().__init__(name, symbol)
        self.property_value = property_value

    def get_value(self):
        return self.property_value

# Example usage:
if __name__ == "__main__":
    # Create instances of different asset classes
    apple_stock = Stock("Apple Inc.", "AAPL", 100)
    apple_stock.set_price(150.0)

    treasury_bond = Bond("US Treasury Bond", "USTB", 1000, 2.5)
    treasury_bond.set_price(1050.0)

    residential_property = RealEstate("Residential Property", "RE01", 250000)
    residential_property.set_price(275000.0)

    # Calculate the total value of the portfolio
    portfolio_value = apple_stock.get_value() + treasury_bond.get_value() + residential_property.get_value()

    # Print the total portfolio value
    print(f"Total Portfolio Value: ${portfolio_value:.2f}")

import pandas as pd

# Create a DataFrame for Asset Classes
data = {
    "AssetClassID": [1, 2, 3, 4],
    "AssetClassName": ["Equity", "Fixed Income", "Real Estate", "Commodities"],
    "Description": [
        "Ownership shares in a company or corporation.",
        "Debt securities with fixed interest payments.",
        "Investments in physical properties like land or buildings.",
        "Physical goods such as gold, oil, or agricultural products."
    ],
    "RiskLevel": ["High", "Low", "Moderate", "Varied"]
}

asset_class_df = pd.DataFrame(data)

print(asset_class_df)

