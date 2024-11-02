from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('name')
api_secret = os.getenv('privateKey')

client = EnhancedRESTClient(api_key, api_secret)