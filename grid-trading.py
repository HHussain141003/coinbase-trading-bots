import os
import logging
from dotenv import load_dotenv
from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

api_key = os.getenv('name')
api_secret = os.getenv('privateKey')

client = EnhancedRESTClient(api_key, api_secret)
