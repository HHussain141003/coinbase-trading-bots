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

def get_current_price():
    try:
        response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=BTC')
        response.raise_for_status()
        data = response.json()
        print(data)
    except Exception as e:
        logger.info("Failed to retrieve current price")

get_current_price()