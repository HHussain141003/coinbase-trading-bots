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
COIN = "XRP"
TRADING_PAIR = f"{COIN}-USDC"
GRID_UPPER_BOUND = 0.5557
GRID_LOWER_BOUND = 0.5458
GRID_SIZE = 20            
ORDER_SIZE_USD = 0    
TIMER = 0 

price_interval = (GRID_UPPER_BOUND - GRID_LOWER_BOUND) / GRID_SIZE

def get_current_price():
    try:
        product_info = client.get_product(product_id=TRADING_PAIR)
        current_price = product_info.price
        return current_price
    except Exception as e:
        logger.warning(f"Failed to retrieve current price for {TRADING_PAIR}")
        return None

def place_buy_order():
    order = client.market_order_buy(product_id=TRADING_PAIR, quote_size=ORDER_SIZE_USD)

def grid_bot():
    while True:
        current_price = get_current_price()
        if current_price is None:
            break

        logger.info(f"Current price for {TRADING_PAIR}: {current_price}")

if __name__ == "__main__":
    grid_bot()