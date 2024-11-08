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
        product_info = client.get_product(product_id=TRADING_PAIR)
        current_price = product_info.price
        return current_price
    except Exception as e:
        logger.warning(f"Failed to retrieve current price for {TRADING_PAIR}")

def grid_bot():
    while True:
        get_current_price()

if __name__ == "__main__":
    current_price = get_current_price()
    print(current_price)
