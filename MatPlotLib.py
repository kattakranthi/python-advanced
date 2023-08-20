#CandleStick chart for OCLC Data
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# Sample OHLC data
ohlc_data = [
    ('2023-08-16', 150, 160, 140, 155),
    ('2023-08-17', 155, 170, 150, 165),
    ('2023-08-18', 165, 175, 160, 170),
    ('2023-08-19', 170, 180, 165, 175),
    ('2023-08-20', 175, 185, 170, 180)
]

# Convert data to DataFrame
df = pd.DataFrame(ohlc_data, columns=['Date', 'Open', 'High', 'Low', 'Close'])
df['Date'] = pd.to_datetime(df['Date'])

# Set date as index
df.set_index('Date', inplace=True)

# Convert dates to matplotlib format
df['Date'] = mdates.date2num(df.index)

# Create the figure and subplot
fig, ax = plt.subplots()

# Plot candlestick chart
candlestick_ohlc(ax, df.values, width=0.6, colorup='g', colordown='r', alpha=0.8)

# Format x-axis to show dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('OHLC Candlestick Chart')

# Show the plot
plt.tight_layout()
plt.show()

