import os
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
COIN = "BTC"
TRADING_PAIR = f"{COIN}-USD"
UPPER_BOUND = 0
LOWER_BOUND = 0
GRID_SIZE = 0            
ORDER_SIZE_USD = 0    
TIMER = 0 


def get_current_price():
    try:
        product_info = client.get_product(product_id=TRADING_PAIR)
        current_price = product_info.price
        return current_price
    except Exception as e:
        logger.warning(f"Failed to retrieve current price for {TRADING_PAIR}")
        return None

def grid_bot():
    while True:
        current_price = get_current_price()
        if current_price is None:
            break

        logger.info(f"Current price for {TRADING_PAIR}: {current_price}")

if __name__ == "__main__":
    grid_bot()