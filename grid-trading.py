import os
import requests
import logging
from dotenv import load_dotenv
from coinbase.rest import RESTClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

api_key = os.getenv('name')
api_secret = os.getenv('privateKey')

client = RESTClient(api_key, api_secret)

# Bot Settings:
ORDER_AMOUNT = 20
COIN = "BTC"
TRADING_PAIR = f"{COIN}-USD"
UPPER_LIMIT = 0
LOWER_LIMIT = 0
TIMER = 300 

def get_current_price():
    try:
        response = requests.get(f"https://api.coinbase.com/api/v3/brokerage/products")
        response.raise_for_status()
        data = response.json()
        print(data)
        # return float(data['data']['amount'])
    except Exception as e:
        logger.warning(f"Failed to retrieve current price for {TRADING_PAIR}")

def grid_bot():
    while True:
        get_current_price()

if __name__ == "__main__":
    get_current_price()