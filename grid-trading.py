import os
import requests
import logging
from dotenv import load_dotenv
from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

api_key = os.getenv('name')
api_secret = os.getenv('privateKey')

client = EnhancedRESTClient(api_key, api_secret)

# Bot Settings:
ORDER_AMOUNT = 20
COIN = "ETH"
TRADING_PAIR = f"{COIN}-USDC"
UPPER_LIMIT = 0
LOWER_LIMIT = 0
TIMER = 300 

def get_current_price():
    try:
        response = requests.get(f"https://api.exchange.coinbase.com/currencies/{COIN}")
        response.raise_for_status()
        data = response.json()
        print(data)
        # return float(data['data']['amount'])
    except Exception as e:
        logger.warning(f"Failed to retrieve current price for {COIN}")

if __name__ == "__main__":
    get_current_price()