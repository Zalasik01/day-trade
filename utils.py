from binance.client import Client

def create_binance_client(api_key=None, api_secret=None, testnet=True):
    if testnet:
        client = Client(api_key, api_secret)
        client.API_URL = 'https://testnet.binance.vision/api'
    else:
        client = Client(api_key, api_secret)
    return client
