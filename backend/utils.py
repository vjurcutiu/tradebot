from web3 import Web3
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Debugging: Print the loaded environment variables
print("Loaded INFURA_PROJECT_ID:", os.getenv('INFURA_PROJECT_ID'))

# Infura API endpoint
INFURA_URL = f"https://mainnet.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"

# Debugging: Print the Infura URL
print("Infura URL:", INFURA_URL)

# Initialize Web3 connection
def get_web3():
    """
    Initialize and return a Web3 instance connected to the Infura API.
    """
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))
    
    # Check if the connection is successful
    if web3.is_connected():
        print("Successfully connected to Infura!")
        return web3
    else:
        raise ConnectionError("Failed to connect to Infura. Check your Infura URL or network connection.")

def get_coin_data(coin_id):
    """
    Fetch cryptocurrency data from CoinGecko API and return only specific fields.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract only the required fields
        return {
            "id": data["id"],
            "symbol": data["symbol"],
            "name": data["name"],
            "price_usd": data["market_data"]["current_price"]["usd"],
            "market_cap_usd": data["market_data"]["market_cap"]["usd"],
            "volume_usd": data["market_data"]["total_volume"]["usd"],
            "last_updated": data["last_updated"]
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch coin data: {str(e)}")

# Global Web3 instance
try:
    web3 = get_web3()
except ConnectionError as e:
    print(e)
    web3 = None  # Set web3 to None if the connection fails