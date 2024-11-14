from backtesting.test import EURUSD
import yfinance as yf

output = yf.download("XRP-USD", start="2020-01-03")

print(output)